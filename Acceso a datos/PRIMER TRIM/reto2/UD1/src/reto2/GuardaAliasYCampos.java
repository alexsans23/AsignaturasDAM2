package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;

import java.io.FileWriter;
import java.io.IOException;

public class GuardaAliasYCampos {
    public static void main(String[] args) {
        Libro libro = new Libro("Java Avanzado", "Francisco", 2025);

        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);

        xstream.alias("libro", Libro.class);
        xstream.aliasField("tituloLibro", Libro.class, "titulo"); 
        xstream.aliasField("anioPublicacion", Libro.class, "anio"); 

        String xml = xstream.toXML(libro);
        System.out.println("XML con alias y aliasField:\n" + xml);

        try (FileWriter fw = new FileWriter("libro_alias.xml")) {
            fw.write(xml);
            System.out.println("Guardado en libro_alias.xml");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
