package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;

import java.io.FileWriter;
import java.io.IOException;

public class PersistenciaToXML {
    public static void main(String[] args) {
        Libro libro = new Libro("Cien años de soledad", "Gabriel García Márquez", 1967);

        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);
        xstream.alias("libro", Libro.class);

        String xml = xstream.toXML(libro);

        try (FileWriter fw = new FileWriter("/home/alumno/Documentos/libro.xml")) {
            fw.write(xml);
            System.out.println("Libro guardado en archivo libro.xml.");
        } catch (IOException e) {
            System.err.println("Error al guardar el archivo: " + e.getMessage());
        }
    }
}

