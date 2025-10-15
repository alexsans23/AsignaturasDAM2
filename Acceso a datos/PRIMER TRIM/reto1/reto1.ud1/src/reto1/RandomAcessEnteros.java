package reto1;

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;




public class RandomAcessEnteros {
    private static final String nombrefichero = "datos.bin";
    private static final long numero = 20L; // ponemos un numero de prueba
    private static final long BYTES_LONG = 8; // un long ocupa 8 bits

    public static void main(String[] args) {
        long[] numeros = new long[(int) numero];

        File f = new File(nombrefichero);
        if (f.exists()) {
            try (DataInputStream dis = new DataInputStream(new FileInputStream(f))) {
                for (int i = 0; i < numero; i++) {
                    if (dis.available() >= BYTES_LONG) {
                        numeros[i] = dis.readLong();
                    } else {
                        numeros[i] = 0;
                    }
                }
                System.out.println("Leído desde binario existente.");
            } catch (IOException e) {
                System.out.println("Error leyendo inicial: " + e.getMessage());
                Arrays.fill(numeros, 0);
            }
        } else {
            Arrays.fill(numeros, 0);
            try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(f))) {
                for (int i = 0; i < numero; i++) {
                    dos.writeLong(numeros[i]);
                }
                System.out.println("Archivo creado con " + numero + " ceros.");
            } catch (IOException e) {
                System.out.println("Error creando archivo: " + e.getMessage());
                return;
            }
        }

        try (RandomAccessFile raf = new RandomAccessFile(f, "rwd");
             Scanner sc = new Scanner(System.in)) {

            while (true) {
                mostrar(numeros);
                System.out.print("Posición a modificar [0-" + (numero - 1) + "] (negativo para salir): ");
                
                int pos;
                try {
                    pos = Integer.parseInt(sc.nextLine().trim());
                } catch (NumberFormatException e) {
                    System.out.println("Número no válido.");
                    continue;
                }
                
                if (pos < 0) {
                    System.out.println("Fin.");
                    break;
                }
                if (pos >= numero) {
                    System.out.println("Fuera de rango.");
                    continue;
                }
                

                System.out.print("Nuevo valor (long) para pos " + pos + ": ");
                long valor;
                try {
                    valor = Long.parseLong(sc.nextLine().trim());
                } catch (NumberFormatException e) {
                    System.out.println("Número no válido.");
                    continue;
                }

                // Actualizamos array en memoria
                numeros[pos] = valor;

                // Actualizamos en archivo
                try {
                    long offset = pos * BYTES_LONG;
                    raf.seek(offset);// Nos movemos a este sitio
                    raf.writeLong(valor); // Escribimos el nuevo valor
                    System.out.println("Actualizado en disco (offset " + offset + ").");
                } catch (IOException e) {
                    System.out.println("Error escribiendo en disco: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.out.println("Error con RandomAccessFile: " + e.getMessage());
        }
    }

    private static void mostrar(long[] numeros) {
        System.out.print("Array: [");
        for (int i = 0; i < numeros.length; i++) {
            System.out.print(numeros[i]);
            if (i < numeros.length - 1) System.out.print(", ");
        }
        System.out.println("]");
    }
}
