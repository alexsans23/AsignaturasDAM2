package ejercicios;

import java.io.*;
import java.nio.charset.StandardCharsets;
// Para manejar bien las tildes y ñ
import java.util.ArrayList;

public class CSVTest {

    public static void main(String[] args) {

        // 1️⃣ Crear una colección (ArrayList) de perros
        ArrayList<Perro> perros = new ArrayList<>();
        perros.add(new Perro("Toby", 3, 12.5, "Beagle"));
        perros.add(new Perro("Luna", 5, 8.2, "Caniche"));
        perros.add(new Perro("Rocky", 2, 25.7, "Pastor Alemán"));
        perros.add(new Perro("Niña", 4, 10.1, "Chihuahua"));
        perros.add(new Perro("Max, el travieso", 1, 7.4, "Bulldog Francés"));

        // 2️⃣ Guardar la lista en un archivo CSV
        try (
            // Usamos UTF-8 para soportar acentos y eñes correctamente
            PrintWriter pw = new PrintWriter(
                    new OutputStreamWriter(
                            new FileOutputStream("perros.csv"), 
                            StandardCharsets.UTF_8
                    )
            )
        ) {
            // Escribimos la cabecera (encabezado de columnas)
            pw.println("nombre;edad;peso;raza");

            // Escribimos cada perro en una línea del CSV
            for (Perro p : perros) {
                // Reemplazamos las comas con otro símbolo si las hay (para no romper el formato CSV)
                String nombreLimpio = p.getNombre().replace(",", " ");
                String razaLimpia = p.getRaza().replace(",", " ");
                pw.println(nombreLimpio + ";" + p.getEdad() + ";" + p.getPeso() + ";" + razaLimpia);
            }

            System.out.println("✅ Archivo perros.csv guardado correctamente.");

        } catch (IOException e) {
            e.printStackTrace();
        }
        

        // 3️⃣ Leer los perros desde el archivo CSV
        ArrayList<Perro> perrosLeidos = new ArrayList<>();

        try (
            BufferedReader br = new BufferedReader(
                    new InputStreamReader(
                            new FileInputStream("perros.csv"), 
                            StandardCharsets.UTF_8
                    )
            )
        ) {
            String linea = br.readLine(); // Leemos la primera línea (cabecera) y la descartamos

            while ((linea = br.readLine()) != null) { // Leemos línea a línea
                String[] partes = linea.split(";"); // Dividimos los campos por ";"

                // Convertimos los valores de texto a los tipos adecuados
                String nombre = partes[0];
                int edad = Integer.parseInt(partes[1]);
                double peso = Double.parseDouble(partes[2]);
                String raza = partes[3];

                // Creamos un nuevo objeto Perro y lo añadimos a la lista
                Perro p = new Perro(nombre, edad, peso, raza);
                perrosLeidos.add(p);
            }

            System.out.println("✅ Perros leídos desde el archivo:");
            for (Perro p : perrosLeidos) {
                System.out.println(p);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
