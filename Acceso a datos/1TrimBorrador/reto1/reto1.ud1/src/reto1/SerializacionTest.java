package reto1;

import java.io.*;
import java.util.ArrayList;


public class SerializacionTest {
    public static void main(String[] args) {

    	ArrayList<Libro> lista = new ArrayList<>();
        lista.add(new Libro("El principito", "Antoine de Saint-Exupéry", 1943));
        lista.add(new Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605));
        lista.add(new Libro("La sombra del viento", "Carlos Ruiz Zafón", 2001));

        File bin = new File("libros.bin");

       
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(bin))) {
            oos.writeObject(lista);
            System.out.println("Serializado OK: " + bin.getAbsolutePath() + " (" + bin.length() + " bytes)");
        } catch (IOException e) {
            System.out.println("Error guardando binario: " + e.getMessage());
        }

        
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(bin))) {
            Object obj = ois.readObject();
            if (obj instanceof ArrayList) {
                ArrayList<?> leida = (ArrayList<?>) obj;
                System.out.println("Leído desde binario:");
                for (Object o : leida) {
                    System.out.println(" - " + o);
                }
            }
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("Error leyendo binario: " + e.getMessage());
        }
    }
}
