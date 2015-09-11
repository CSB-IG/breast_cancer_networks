import pandas as pd
import json

def read_gen_ontology():
    df = pd.read_csv(filepath_or_buffer="gen_ontology.csv")
    return df

def read_ft():
    ft = set([])
    with open("TFs.txt", "r") as f:
        for line in f.readlines():
            ft.add(line.strip("\n"))
    return ft

def read_ft_im():
    df = pd.read_csv(filepath_or_buffer="regulon_2WsC_cy40.sif", sep='\t')
    return df

def read_firma_molecular():
    df = pd.read_csv(filepath_or_buffer="ms_k_sorted.csv")
    return df

def read_genes_no_diferenciados():
    df = pd.read_csv(filepath_or_buffer="etc_k_sorted.csv")
    return df

def clean_nodes_links(nodes, links):
    indexes = set([link["source"] for link in links])
    indexes = indexes.union(set([link["target"] for link in links]))
    n_nodes = []
    n_links = []
    other_index = {}
    for n_index, index in enumerate(indexes):
        other_index[index] = n_index
        n_nodes.append(nodes[index])

    for values in links:
        r = {}
        try:
            s = {"source": other_index[values["source"]]}
        except KeyError:
            s = {"source": values["source"]}

        try:
            t = {"target": other_index[values["target"]]}
        except KeyError:
            s = {"target": values["target"]}

        r.update(s)
        r.update(t)
        r["value"] = values["value"]
        n_links.append(r)

    return n_nodes, n_links

def compress(data):
    compress_data = {}
    for value in data:
        key = value["source"]+value["target"]
        if key in compress_data:
            compress_data[key]["value"] += abs(value["value"])
        else:
            #compress_data[key] = value.copy()
            compress_data[key] = {"source": value["source"], "target": value["target"], "value": value["value"]}
    return compress_data.values()

def join(left, right):
    from collections import defaultdict

    #join_data = defaultdict(dict)
    #for data in (left, right):
    #    for elem in data:
    #        join_data[elem["source"]].setdefault("value", 0)
    #        last_value = join_data[elem["source"]]["value"]
    #        join_data[elem["source"]].update(elem)
    #        join_data[elem["source"]]["value"] = last_value + elem["value"]
    #return join_data.values()

    join_data = []
    right_values = {right_value["source"]: right_value for right_value in right}
    for left_value in left:
        try:
            right_value = right_values[left_value["source"]]
            join_data.append({
                "source": left_value["target"], 
                "target": right_value["target"], 
                "value": left_value["value"]+right_value["value"]})
        except KeyError:
            join_data.append({
                "source": left_value["target"], 
                "target": 0, 
                "value": left_value["value"]})
    return join_data

def get_linked(links, length=0, lower_limit=0, upper_limit=0):
    import networkx as nx
    import random
    G = nx.DiGraph()

    edges = [(link["source"], link["target"], link["value"]) for link in links]
    G.add_weighted_edges_from(edges)

    def only_paths_of_size(paths):
        return [edges for edges in list(paths.values()) if len(edges) >= length]

    uv_key = set([])
    results = []
    for link in links:
        print("SOURCE", link["source"])
        shorted = nx.shortest_path(G, source=link["source"])
        paths = only_paths_of_size(shorted)
        for edges in paths:
            print("PATH", edges)
            vertices = list(zip(edges, edges[1:]))
            last_u, last_v = vertices[-1]
            if lower_limit <= G[last_u][last_v]["weight"] <= upper_limit:
                for u, v in vertices:
                    key = "{}{}".format(u,v)
                    if not key in uv_key:
                        uv_key.add(key)
                        results.append({
                            "source": u, 
                            "target": v, 
                            "value": G[u][v]["weight"]})
            
    return results
        

def ontology_graph(name, search_space_ontology, node_index):
    data = []
    for gene, ontologies in search_space_ontology.items():
        for key_ontology in ontologies[name]:
            for term in ontology_term[key_ontology]:
                data.append({"source": node_index[gene], "target": node_index[term], "value": 1})
    return data

def firma_molecular_graph(fm, gnd, ft_im):
    data = []
    fm_set = set(fm["name"])
    gnd_set = set(gnd["name"])
    for i, row in ft_im.iterrows():
        if row["blanco"] in fm_set:
            target = "Firma Molecular"
        elif row["blanco"] in gnd_set:
            target = "Genes no diferenciados"
        else:
            continue

        data.append({
            "source": node_index[row["ft"]], 
            "target": node_index[target], 
            "value": row["im"]})
    return data


if __name__ == '__main__':
    df = read_gen_ontology()
    ft = read_ft()
    df = df.drop_duplicates(subset="genesym")
    fm = read_firma_molecular()
    gnd = read_genes_no_diferenciados()
    ft_im = read_ft_im()

    gene_ont = ["Gene Ontology Biological Process", "Gene Ontology Cellular Component", "Gene Ontology Molecular Function"]
    gene_ont_abbrv = {"Gene Ontology Biological Process": "gbp", "Gene Ontology Cellular Component": "gcc", "Gene Ontology Molecular Function": "gmf"}
    df_ft = df[df["genesym"].isin(ft)]
    ontology_term = {}
    gene_ontology = {}
    ontology_term_list = set([])
    columns = ["genesym"] + gene_ont
    ontology_gene = {}
    ontologies = {}
    for i, row in df_ft[columns].iterrows():
        #print(row["genesym"])
        for ontology in gene_ont:
            #print(column)
            for go in row[ontology].split("///"):
                go_terms = go.split("//")
                go_id = go_terms.pop(0)
                key = go_id.strip()
                ontology_term.setdefault(key, [])
                ontologies.setdefault(ontology, set([]))
                ontology_gene.setdefault(key, [])
                gene_ontology.setdefault(row["genesym"], dict(zip(gene_ont, [[], [], []])))
                ontologies[ontology].add(key)
                gene_ontology[row["genesym"]][ontology].append(key)
                ontology_gene[key].append(row["genesym"])
                for go_term in go_terms[0:1]:
                    #print(go_term)
                    term = go_term.strip()
                    ontology_term[key].append(gene_ont_abbrv[ontology]+":"+term)                    
                    ontology_term_list.add(gene_ont_abbrv[ontology]+":"+term)

    fm_gnd_set = set(list(fm["name"]) + list(gnd["name"]))
    gene_set = set([])
    
    for gene, ontologies in gene_ontology.items():
        gene_set.add(gene)

    search_space_ontology = {}
    for gene in gene_set.intersection(fm_gnd_set):
        search_space_ontology[gene] = gene_ontology[gene]

    node_index = {}
    nodes = ["NO TARGET"] + list(ft) + list(ontology_term_list) + list(fm["name"]) + list(gnd["name"]) + ["Firma Molecular", "Genes no diferenciados"]
    for i, term in enumerate(nodes):
        if not term in node_index:
            node_index[term] = i
        #else:
        #    print("DUP", term)

    links = []
    pipeline = [        
        compress(ontology_graph("Gene Ontology Cellular Component", search_space_ontology, node_index)),
        compress(ontology_graph("Gene Ontology Biological Process", search_space_ontology, node_index)),
        #compress(ontology_graph("Gene Ontology Molecular Function", search_space_ontology, node_index)),
        compress(firma_molecular_graph(fm, gnd, ft_im))
    ]
    for v in pipeline[0]:
        links.append(v)
    
    for p1, p2 in zip(pipeline, pipeline[1:]):
        for v in join(p1, p2):
            links.append(v)

    paths = get_linked(links, length=len(pipeline)+1, lower_limit=100, upper_limit=200)
    n_nodes, n_links = clean_nodes_links(nodes, paths)
    result = {"nodes": [{"name": node} for node in n_nodes],
            "links": n_links}

    with open("results.json", "w") as f:
        f.write(json.dumps(result))
