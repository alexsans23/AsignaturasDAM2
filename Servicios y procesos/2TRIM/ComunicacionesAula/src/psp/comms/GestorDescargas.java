package psp.comms;

import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;

public class GestorDescargas {

    public void descargarArchivo(String url_descargar, String nombreFichero){
        System.out.println("descargando: "+ url_descargar);

        try {
            URL url = new URL(url_descargar);
            InputStream is = url.openStream();
            InputStreamReader reader= new InputStreamReader(is);
            BufferedReader bReader = new BufferedReader(new InputStreamReader(is));
            FileWriter escritorFichero = new FileWriter(nombreFichero);

            String linea;
            while((linea = bReader.readLine()) != null){
                escritorFichero.write(linea + "\n");
            }

            escritorFichero.close();
            bReader.close();
            is.close(); //para buenas practicas esto se meteria en el finally(inicializando fuera )


        } catch (MalformedURLException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) {
        GestorDescargas gd = new GestorDescargas();
        String url = "http://www.bbc.com/robots.txt";
        gd.descargarArchivo(url, "Descarga.txt");
    }

}
