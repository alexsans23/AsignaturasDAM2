package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class GuardaListaLibros {
    public static void main(String[] args) {
        List<Libro> lista = new ArrayList<>();
        lista.add(new Libro("El bestiario de Axlin", "Laura Gallego", 2011));
        lista.add(new Libro("Harry Potter", "J.K Rawling", 2004));
        lista.add(new Libro("Fundamentos de Java", "Diego Ceran", 2022));

        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);
        xstream.alias("libro", Libro.class);
        xstream.alias("libros", List.class);

        try (FileOutputStream fos = new FileOutputStream("libros.xml")) {
            xstream.toXML(lista, fos);
            System.out.println("Lista guardada en libros.xml");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
