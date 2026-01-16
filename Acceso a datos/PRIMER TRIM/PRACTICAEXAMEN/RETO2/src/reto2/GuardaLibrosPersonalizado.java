package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;
import reto2.Libro;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;

public class GuardaLibrosPersonalizado {
    public static void main(String[] args) {
        // 1️⃣ Crear XStream con permisos
        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);

        // 2️⃣ Configurar aliases para clase y campos
        xstream.alias("libro", Libro.class);
        xstream.aliasField("titulo-libro", Libro.class, "titulo");
        xstream.aliasField("autor-libro", Libro.class, "autor");
        xstream.useAttributeFor(Libro.class, "anio"); // anio como atributo

        // Alias para la colección
        xstream.alias("biblioteca", ArrayList.class);

        // 3️⃣ Crear colección de libros
        ArrayList<Libro> biblioteca = new ArrayList<>();
        biblioteca.add(new Libro("1984", "George Orwell", 1949));
        biblioteca.add(new Libro("El Principito", "Antoine de Saint-Exupéry", 1943));
        biblioteca.add(new Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967));

        // 4️⃣ Guardar XML en fichero
        try (FileOutputStream fos = new FileOutputStream("biblioteca_personalizado.xml")) {
            xstream.toXML(biblioteca, fos);
            System.out.println("XML guardado correctamente en biblioteca_personalizado.xml");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
