/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import aguaspkg.Metoditos;
import java.io.File;
import java.io.FilenameFilter;
import fileOperations.*;
import java.io.File;
/**
 *
 * @author jespinal
 */



public class main {

    
    
    /**
     * @param args the command line arguments
     */
    
    
    
    public static void main(String[] args) {
//        String name = new String("sanos");
//        int p = 20;
//        String pathSanos10 = new String("apoptosis/" + name + p + "/");
//        Metoditos.CortaAdj( pathSanos10, name, p); 
//        String name2 = new String("enfermos");
//        String pathEnf10 = new String("autofagia/" + name2 + p + "/");
//        Metoditos.CortaAdj( pathEnf10, name2, p);
//        int i = 20;
//        for(int i = 20; i <=40; i+=20){
//            String pathSanos = new String("clusterproliferativo/" + name + i + "/");
//        Metoditos.CortaAdj( pathSanos, name, i); 
//        if(i >= 60){
//        String pathEnf = new String("autofagia/" + name2 + i + "/");
//        Metoditos.CortaAdj( pathEnf, name2, i);
//        }
//        } 
        
//        String path= new String("GeneSym/");
////        Metoditos.MIthreshold(path, name2, .4);
////        
////        String path = new String("AllNets/");
//        String sn = new String("sanos");
//        String en = new String("enfermos");
//        String p53 = new String("p53");
//        String cp = new String("clusterproliferativo");
//        String af = new String("autofagia");
//        String ap = new String("apoptosis");
////        int p = 10;
//        int thr = 7;
//        double tr = 0.7;
//        for(int p = 20; p <= 100; p+=20){
//        Metoditos.MIthreshold(path, 
//                p53 +"_" + sn + "_ADJ_output_" + p + "_genesym.txt",
//                path + "ThresholdMI/" +thr  + "/" + p53 +"_" + sn + "_ADJ_output_" + p + "_genesym.txt", 
//                tr);
//        
//         Metoditos.MIthreshold(path, 
//               ap +"_" + sn + "_ADJ_output_" + p + "_genesym.txt",
//                path + "ThresholdMI/" +thr  + "/" + ap +"_" + sn + "_ADJ_output_" + p + "_genesym.txt", 
//                tr);
//         
//          Metoditos.MIthreshold(path, 
//                af +"_" + sn + "_ADJ_output_" + p + "_genesym.txt",
//                path + "ThresholdMI/" +thr  + "/" + af +"_" + sn + "_ADJ_output_" + p + "_genesym.txt", 
//                tr);
//          
//           Metoditos.MIthreshold(path, 
//                cp +"_" + sn + "_ADJ_output_" + p + "_genesym.txt",
//                path + "ThresholdMI/" +thr  + "/" + cp +"_" + sn + "_ADJ_output_" + p + "_genesym.txt", 
//                tr);
//      }
//        
//       double a = Metoditos.GeneraRed();
        
        Metoditos.HistFreqGO();

    }

}
