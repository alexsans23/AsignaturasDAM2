package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;
import reto2.Libro;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;

public class RecuperaLibrosPersonalizado {
    public static void main(String[] args) {
        // 1️⃣ Crear XStream con permisos
        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);

        // 2️⃣ Configurar mismos aliases que al guardar
        xstream.alias("libro", Libro.class);
        xstream.aliasField("titulo-libro", Libro.class, "titulo");
        xstream.aliasField("autor-libro", Libro.class, "autor");
        xstream.useAttributeFor(Libro.class, "anio");
        xstream.alias("biblioteca", ArrayList.class);

        // 3️⃣ Leer XML desde fichero
        try (FileInputStream fis = new FileInputStream("biblioteca_personalizado.xml")) {
            ArrayList<Libro> biblioteca = (ArrayList<Libro>) xstream.fromXML(fis);

            System.out.println("Libros recuperados:");
            for (Libro libro : biblioteca) {
                System.out.println(libro);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
