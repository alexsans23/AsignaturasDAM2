package psp.procesos.sumas;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.PreparedStatement;

public class Sumador {
    public int sumar(int n1, int n2, int proceso) {

        int resultado = 0;
        for(int i= n1; i<= n2 ; i++){
            resultado += i;
        }

        System.out.println("Ejecutado por el proceso:" + proceso);
        System.out.println("El resultado de " + n1 + " y " + n2 +" es "+ resultado);

        return resultado;
    }

    public int sumar2(int n1, int n2,int proceso, String filename) {

        int resultado = 0;
        for(int i= n1; i<= n2 ; i++){
            resultado += i;
        }
        try {
            BufferedWriter bw= new BufferedWriter(new FileWriter(filename));
            System.out.println("Ejecutado por el proceso:" + proceso + "\n");
            System.out.println("El resultado de " + n1 + " y " + n2 +" es "+ resultado);
            bw.flush();
            bw.close();

        } catch (IOException e) {
            throw new RuntimeException(e);
        }


        return resultado;
    }



    public static void main(String[] args) {

        int n1 = Integer.parseInt(args[0]);
        int n2 = Integer.parseInt(args[1]);
        int proceso = Integer.parseInt(args[2]);
        String filename =args[2];
        Sumador sumador = new Sumador();

       // sumador.sumar(n1,n2,proceso);
        sumador.sumar2(n1,n2,proceso,filename);

    }

}
