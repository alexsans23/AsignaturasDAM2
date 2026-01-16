package ejercicios;

import java.io.*;
import java.util.ArrayList;

public class SerializacionTest {

    public static void main(String[] args) {

        // 1️⃣ Crear una lista de perros
        ArrayList<Perro> perros = new ArrayList<>();
        perros.add(new Perro("Toby", 3, 12.5, "Beagle"));
        perros.add(new Perro("Luna", 5, 8.2, "Caniche"));
        perros.add(new Perro("Rocky", 2, 25.7, "Pastor Alemán"));

        // 2️⃣ Guardar la lista en un fichero binario (.dat)
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("perros.dat"))) {
            oos.writeObject(perros); // serializamos toda la lista
            System.out.println("✅ Lista de perros serializada correctamente en perros.dat");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 3️⃣ Recuperar la lista desde el fichero
        ArrayList<Perro> perrosRecuperados = new ArrayList<>();
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("perros.dat"))) {
            perrosRecuperados = (ArrayList<Perro>) ois.readObject(); // casteamos al tipo original
            System.out.println("✅ Lista de perros recuperada desde perros.dat:");
            for (Perro p : perrosRecuperados) {
                System.out.println(p);
            }
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
