package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;

import java.io.File;
import java.io.FileReader;

public class RecuperaLibro {
    public static void main(String[] args) {
        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);
        xstream.alias("libro", Libro.class);

        File f = new File("libro.xml");
        if (!f.exists()) {
            System.err.println("No se encuentra libro.xml — ejecuta GuardaLibro primero.");
            return;
        }

        try (FileReader fr = new FileReader(f)) {
            Object obj = xstream.fromXML(fr);
            if (obj instanceof Libro) {
                Libro libro = (Libro) obj;
                System.out.println("Objeto recuperado: " + libro);
            } else {
                System.out.println("El XML no contiene un objeto Libro (clase: " + obj.getClass() + ")");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
