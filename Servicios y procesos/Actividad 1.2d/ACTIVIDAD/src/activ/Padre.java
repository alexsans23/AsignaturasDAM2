package activ;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Padre {
public static void main(String[] args) throws IOException {
Scanner sc = new Scanner(System.in);

    while (true) {
        System.out.print("> ");
        String line = sc.nextLine();

        // Finalizar cuando el usuario escriba "fin"
        if (line.equalsIgnoreCase("fin")) {
            break;
        }

        // Lista para almacenar los procesos hijos
        List<Process> children = new ArrayList<>();

        // Para cada carácter, lanzar un proceso hijo
        for (char c : line.toCharArray()) {
            // Ruta al ejecutable java y classpath actual (automático)
            String javaBin = System.getProperty("java.home") + File.separator + "bin" + File.separator + "java";
            String classpath = System.getProperty("java.class.path");
            String className = "RandomGenerator"; // nombre exacto de la clase hija

            ProcessBuilder pb = new ProcessBuilder(javaBin, "-cp", classpath, className);
            pb.redirectErrorStream(true);

            Process p = pb.start();
            children.add(p);
        }

        // Leer la salida de todos los procesos y mostrarla seguida
        StringBuilder sb = new StringBuilder();
        for (Process p : children) {
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()))) {
                String output = reader.readLine();
                if (output != null) {
                    sb.append(output);
                }
            }
        }

        System.out.println(sb.toString());
    }

    sc.close();
    System.out.println("Programa finalizado.");
}


}