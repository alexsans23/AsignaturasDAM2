package pasoBasico;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

/*
Ver que sistema operativo es (por curiosidad)
Crear un programa Java HolaProceso que:
Lance un proceso hijo en Windows que ejecute cmd /c echo Hola desde el proceso hijo.
Lea la salida del proceso y la muestre en la consola.
Muestre el código de salida del proceso.
 */
public class HolaProceso {
    public static void main(String[] args) {
        String os = System.getProperty("os.name").toLowerCase();
        System.out.println("Sistema operativo detectado: " + os);

        // 1) Definimos el comando para Windows
        // "cmd" es la consola de Windows, "/c" le dice que ejecute el comando que sigue y termine.
        List<String> comando = Arrays.asList("cmd", "/c", "echo Hola desde el proceso hijo");

        ProcessBuilder pb = new ProcessBuilder(comando);
        pb.redirectErrorStream(true);
        Process proceso;
        try{
            System.out.println("Arrancando el proceso...");
            proceso = pb.start();
        } catch (IOException e) {
            System.err.println("No se pudo iniciar el proceso: " + e.getMessage());
            return;
        }

// 4) Leemos la salida del proceso línea a línea
        try (InputStream is = proceso.getInputStream();
             InputStreamReader isr = new InputStreamReader(is);
             BufferedReader br = new BufferedReader(isr)) {

            System.out.println("Salida del proceso:");
            String linea;
            while ((linea = br.readLine()) != null) {
                System.out.println("  > " + linea);
            }
        } catch (IOException ioe) {
            System.err.println("Error leyendo la salida: " + ioe.getMessage());
        }

        // 5) Esperamos a que termine y mostramos el código de salida
        try {
            int codigo = proceso.waitFor(); // espera hasta que el proceso termine
            System.out.println("Código de salida: " + codigo);
        } catch (InterruptedException ie) {
            System.err.println("Esperar proceso interrumpido: " + ie.getMessage());
        }
    }
}