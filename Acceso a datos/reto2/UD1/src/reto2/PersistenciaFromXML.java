package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;

import java.io.FileReader;

public class PersistenciaFromXML {
    public static void main(String[] args) {
        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);
        xstream.alias("libro", Libro.class);

        try (FileReader fr = new FileReader("libro.xml")) {
            Libro libro = (Libro) xstream.fromXML(fr);
            System.out.println("Libro recuperado:\n" + libro);
        } catch (Exception e) {
            System.err.println("Error al leer el archivo: " + e.getMessage());
        }
    }
}
