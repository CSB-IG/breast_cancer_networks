/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import fileOperations.*;
import jsc.*;
//import java.io.*;
import java.util.*;
import java.text.DecimalFormat;
import java.lang.Object;
import jsc.correlation.SpearmanCorrelation;
import jsc.datastructures.PairedData;
import jsc.regression.PearsonCorrelation;
import jsc.tests.H1;
import java.awt.*;
import java.awt.event.*;
import java.applet.*;
import java.io.File;
import java.io.File;
import java.io.FilenameFilter;

/**
 *
 * @author jespinal
 */
public class Metoditos {

    /**
     * Este metodo genera Criminal-like networks entre el promedio de la
     * expresion de genes de personas sanas (61 muestras), las cuales su
     * desviacipon standard es menor a la des- viacion promedio (13586 genes).
     * Este promedio va a ser el vector de comparacion contra los 13586 genes de
     * los 1130 enfermos. ponemos valores de umbral en cada red para cortar y
     * ver si hay match con las redes de aracnel.
     */
    public static double GeneraRed() {
        String[] gen = new String[13586];
        double[] sano = new double[gen.length];
        double promSano;
        double varSano;
        double[] prom = new double[1130];
        double[] var = new double[prom.length];
        String[] muestras = new String[prom.length];
        double[][] enf = new double[gen.length][prom.length];
        DecimalFormat d = new DecimalFormat("0.00000000000");
        FileToRead entry = new FileToRead("1191DataSets/AffysAVGsanoVSenf_13587.txt");
        /*
         Lleno el arreglo con el nombre de los enfermos
         */
//        entry.nextString();
        entry.nextString();
        for (int i = 0; i < prom.length; ++i) {
            muestras[i] = entry.nextString();
        }
        System.out.println(muestras[prom.length - 1]);
        for (int i = 0; i < gen.length; ++i) {
//            entry.nextInt();//ordinal del gen
            gen[i] = entry.nextString();
            sano[i] = entry.nextDouble();
            for (int j = 0; j < prom.length; ++j) {
                enf[i][j] = entry.nextDouble() - sano[i];
            }
        }
        System.out.println("acabe el llenado de las casillas");

        /*
         * lleno la varianza y el promedio
         */
        promSano = entry.nextDouble();
        for (int i = 0; i < prom.length; ++i) {
            prom[i] = entry.nextDouble() - promSano;
        }
        entry.nextLine();
        varSano = entry.nextDouble();
        for (int i = 0; i < prom.length; ++i) {
            var[i] = entry.nextDouble() - varSano;
        }
        entry.close();
        System.out.println("acabe promedio y varianza");
        /*
         * comparo la resta del promedio de los sanos con 
         * una muestra de enfermos. Si correlacionan, 
         * lo escribo en archivo de texto o si no,
         * hago la matriz
         */

        for (int thr = 100; thr >= 14; thr--) {
            System.out.println("ahora vamos con umbral = " + thr + "*********************");
//        double thr = 50.0;
            for (int n = 0; n < prom.length; ++n) {
                System.out.println("ahora vamos haciendo el archivo sif número" + n);
                FileToWrite fw = new FileToWrite("1191DataSets/sifs/" + thr + "/" + muestras[n] + "__" + ".sif");
                int tope = 0;
                for (int i = tope; i < gen.length; ++i) {
                    for (int j = i + 1; j < gen.length; ++j) {
                        double corr = ((enf[i][n] * enf[j][n]) - (prom[n] * prom[n])) / var[n];
                        if (corr > thr || corr < -thr) {
                            fw.writeLine(gen[i] + "\t" + d.format(corr) + "\t" + gen[j]);
                        }
                    }
                    tope++;
                }
                fw.close();
            }
        }//este es de los meses (n)
        return 0;
    }

    /**
     * Metodo para crear un archivo que contenga gen gen interaccion. Archivo
     * con los genes de cluster proliferativo contra todos los genes (22283)
     * corridos con aracne Agarro los adj's, los corto de las 17 primeras lineas
     * y la fila de resultados, la hago 3 columnas con el gen1, el gen2 y su
     * MI-value
     */
    public static void CortaAdj(String path, String name, int p) {
        /*
         Primero leemos todos los archivos de la carpeta
         */
        FilenameFilter filter = (File dir, String fileName) -> fileName.endsWith("adj");

        File f = new File(path);
        String[] fileList = f.list(filter);
        FileToWrite fw = new FileToWrite("AllNets/autofagia_" + name + "_ADJ_output_" + p +".txt");
        for (int i = 0; i < fileList.length; i++) {
            System.out.println(fileList[i]);

            FileToRead fr = new FileToRead(path + fileList[i]);
            for (int j = 0; j < 17; ++j) {
                fr.nextLine();
            }
            if (fr.hasNext()) {
                String GenBlanco = new String(fr.nextString());
                while (fr.hasNext()) {
                    fw.writeString(GenBlanco + "\t");
                    fw.writeString(fr.nextString() + "\t");
                    fw.writeString(fr.nextString() + "\n");
                }
            }
            fr.close();
        }
        fw.close();
    }

    /**
     * Crea Archivos dentro de un directorio.
     */
    public static void MakeFile() {
        for (int i = 1; i <= 100; ++i) {
            File e = new File("FilePath/" + i + "/");
            e.mkdir();
        }
    }
    
    public static void RNAseq(){
        String[] geneName = new String[20533];
        int[] rawcount = new int[geneName.length];
        double[] medianNorm = new double[geneName.length];
        double[] RPKM = new double[geneName.length];
        FileToWrite rawFile= new FileToWrite("rawCount.dat");
        
        for(int i = 0; i < 10; ++i){
        FileToRead fr = new FileToRead("/gene.quantification.txt");
        rawFile.writeString(fr.nextString() + "\t");
        rawFile.writeString(fr.nextString() + "\n");
        
        }
    }

    /**
     * Genera archivos sif reducidos con un
     * umbral de informacion mutua
     * determinado por el usuario. Esta chido, usa 
     * los valores de MI de aracneles.
     * @param path EL path del archivo
     * @param name nombre del archivo
     * @param thr umbral de informaccion mutua
     * @param output el archivo de salida
     */
    public static void MIthreshold(String path, String name,  String output, double thr){
    FileToRead fr = new FileToRead(path + name );
    FileToWrite fw = new FileToWrite(output);
    ArrayList<String> geneSource = new ArrayList<String>();
    ArrayList<String> geneTarget = new ArrayList<String>();
    ArrayList MI = new ArrayList();
        while(fr.hasNext()){
            geneSource.add(fr.nextString());
            geneTarget.add(fr.nextString());
            MI.add(fr.nextDouble());
        }
        
        for(int i = 0; i < MI.size(); ++i){
            double entero = Double.parseDouble(MI.get(i).toString());

            if(entero > thr){
                fw.writeString(geneSource.get(i) + "\t");
                fw.writeString(geneTarget.get(i) + "\t");
                fw.writeString(entero + "\n");
            }
        }
        fr.close();
        fw.close();
}


    
    public static void AffyToGene(String fInput, String fOutput ){
        FileToRead fr = new FileToRead(fInput);
        //21307 con pareja de gene symbol
        ArrayList<String> geneSource = new ArrayList<String>();
    ArrayList<String> geneTarget = new ArrayList<String>();
    ArrayList MI = new ArrayList();
        while(fr.hasNext()){
            geneSource.add(fr.nextString());
            geneTarget.add(fr.nextString());
            MI.add(fr.nextDouble());
        }
        ArrayList<String> affy = new ArrayList<String>();
    ArrayList<String> gs = new ArrayList<String>();
        FileToRead AG = new FileToRead("AffyGene.txt");
        AG.nextLine();
        while (AG.hasNext()){
            affy.add(AG.nextString());
            gs.add(AG.nextString());
        }
        
        for(int j = 0; j < affy.size(); ++j){
            for(int i = 0; i < geneSource.size(); ++i){
                if(affy.get(j).toString().equals(geneSource.get(i).toString())){
                    geneSource.set(i, gs.get(j).toString());
                }
            }
            for(int i = 0; i < geneTarget.size(); ++i){
                if(affy.get(j).toString().equals(geneTarget.get(i).toString())){
                    geneTarget.set(i, gs.get(j).toString());
                }
            }
        }
        FileToWrite fw = new FileToWrite(fOutput);
        for(int i = 0; i < MI.size(); ++i){
            fw.writeString(geneSource.get(i).toString() + "\t");
            fw.writeString(geneTarget.get(i).toString() + "\t");
            fw.writeString(MI.get(i).toString() + "\n");
        }
        fr.close();
        AG.close();
        fw.close();
        System.out.println("Escribí " + fOutput);
    }
    
   
    public static void HistFreqGO(){
        FileToRead fr = new FileToRead("GeneSym/ThresholdMI/6/cp_e80_mi6_bf_p2.bgo");
        ArrayList<String> TotGenes = new ArrayList();
        ArrayList<Integer> freq = new ArrayList();
        
        for(int i = 0; i < 14; ++i){
            fr.nextLine();
        }
        String temp = new String();
        while(temp.equals("No")==false){   
        temp = fr.nextString();
        TotGenes.add(temp);
        }
        
        for(int i = 0; i < 4; ++i){
            fr.nextLine();
        }
        
        while(fr.hasNext()){
             String genes = new String(fr.nextLine() + "");
             StringTokenizer st = new StringTokenizer(genes);
             for(int i = 0 ; i < 7; ++i){
                st.nextToken();
             }
             String s = new String(st.nextToken());
             System.out.print(s + "\t");
            while(s.contains("\t")==true){
//                 System.out.print(st.nextToken()+"\t");
                 s = st.nextToken().c;
            }
            System.out.println();
       
        st.nextToken("|");
        

        while(st.nextToken().contains(genes))
//        System.out.println(st.nextToken());
//        String s2 = new String(st.nextToken());
        
        while(st.hasMoreTokens()){
            System.out.print(st.nextToken()+ "\t");
        }
        System.out.println("\n");
        }
        
        fr.close();
    }
    
}
