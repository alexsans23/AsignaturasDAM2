package pruebasJson;

import com.google.gson.Gson;

import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;

public class CrearListaGson {
    public static void main(String[] args) throws Exception {
        // 1) Crear lista de libros
        List<Libro> lista = new ArrayList<>();
        lista.add(new Libro("Cien años de soledad", "Gabriel García Márquez", 1967));
        lista.add(new Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605));
        lista.add(new Libro("La sombra del viento", "Carlos Ruiz Zafón", 2001));

        // 2) Serializar la lista con Gson y guardar en gson.json
        Gson gson = new Gson();
        String json = gson.toJson(lista);

        try (FileWriter fw = new FileWriter("gson.json")) {
            fw.write(json);
        }

        System.out.println("Lista serializada y guardada en gson.json");
    }
}
