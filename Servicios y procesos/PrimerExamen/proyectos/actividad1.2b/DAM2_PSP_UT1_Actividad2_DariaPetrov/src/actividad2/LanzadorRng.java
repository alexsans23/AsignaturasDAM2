package actividad2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class LanzadorRng {

    /**
     * Metodo que llama a un proceso hijo para pasarle las entradas del usuario por teclado
     * para generar enteros aleatorios por cada caracter en la entrada
     * @param input Input del usuario como String pasado al proceso hijo en una llamada
     */

    private void lanzarRng(String input){
        ProcessBuilder pb;
        Process process;

        String classname= "actividad2.GeneradorAleatorio"; //Nombre del .class y su paquete
        String currentPath = System.getProperty("user.dir"); //Coge el directorio de trabajo del proyecto
        String classpath = currentPath + "/out/production/Actividad2NumerosAleatorios"; //Dirección relativa desde el directorio de trabajo

        try {
            pb = new ProcessBuilder("java", "-cp", classpath, classname, input); //Comando a ejecutar por el interprete de comandos

            process = pb.start();
            //process.waitFor();
            BufferedReader auxReader = new BufferedReader(new InputStreamReader(process.getInputStream())); //Recogemos el output del proceso hijo para no precisar de un fichero auxiliar
            String linea;

            while ((linea = auxReader.readLine()) != null) System.out.println(linea);
            auxReader.close();

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        LanzadorRng rngLauncher = new LanzadorRng();

        Scanner scannerUser = new Scanner(System.in);
        String inputUser;

        do {
            System.out.println("Introduce una cadena");
            inputUser = scannerUser.nextLine();

            //Evaluamos el input del usuario
            if (!inputUser.equalsIgnoreCase("fin")) {
                rngLauncher.lanzarRng(inputUser);
            }
        } while (!inputUser.equalsIgnoreCase("fin")); //condicion de salida = String fin

        scannerUser.close();

    }

}
