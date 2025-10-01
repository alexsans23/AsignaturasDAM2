package primeraTareaPropia;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class HolaProceso {
    public static void main(String[] args) {

        // 1) Detectar sistema operativo
        String os = System.getProperty("os.name").toLowerCase();
        System.out.println("Sistema operativo detectado: " + os);

        // 2) Preparar el comando adecuado para la shell del SO
        
        List<String> comando;
        if (os.contains("win")) {
            comando = Arrays.asList("cmd", "/c", "echo Hola desde el proceso hijo");
        } else {
            comando = Arrays.asList("sh", "-c", "echo Hola desde el proceso hijo");
        }
        System.out.println("Comando que vamos a ejecutar: " + comando);

        // 3) Crear ProcessBuilder y arrancar el proceso
        ProcessBuilder pb = new ProcessBuilder(comando);
        pb.redirectErrorStream(true); // mezcla stderr en stdout
        Process proceso = null;
        try {
            System.out.println("Arrancando el proceso...");
            proceso = pb.start();
        } catch (Exception e) {
            System.err.println("Error al iniciar el proceso: " + e.getMessage());
            e.printStackTrace();
            return;
        }

        // 4) Leer la salida del proceso (stdout)
        try (InputStream is = proceso.getInputStream();
             InputStreamReader isr = new InputStreamReader(is);
             BufferedReader br = new BufferedReader(isr)) {

            String linea;
            System.out.println("Salida del proceso:");
            while ((linea = br.readLine()) != null) {
                System.out.println("  > " + linea);
            }
        } catch (IOException ioe) {
            System.err.println("Error leyendo la salida del proceso: " + ioe.getMessage());
        }

        // 5) Esperar a que el proceso termine y mostrar código de salida
        try {
            int codigoSalida = proceso.waitFor();
            System.out.println("Código de salida del proceso: " + codigoSalida);
        } catch (InterruptedException ie) {
            System.err.println("Se interrumpió la espera del proceso: " + ie.getMessage());
        }
    }
}
