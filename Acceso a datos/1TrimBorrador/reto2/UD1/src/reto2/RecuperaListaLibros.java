package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;

import java.io.File;
import java.io.FileInputStream;
import java.util.List;

public class RecuperaListaLibros {
    public static void main(String[] args) {
        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);
        xstream.alias("libro", Libro.class);
        xstream.alias("libros", List.class);

        File f = new File("libros.xml");
        if (!f.exists()) {
            System.err.println("No se encuentra libros.xml. ");
            return;
        }

        try (FileInputStream fis = new FileInputStream(f)) {
            List<Libro> lista = (List<Libro>) xstream.fromXML(fis);
            for (Libro libro : lista) {
                System.out.println(libro);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
