package pruebasJson;

import com.thoughtworks.xstream.*; 
import com.thoughtworks.xstream.io.json.JettisonMappedXmlDriver; 
import com.thoughtworks.xstream.security.AnyTypePermission;
import java.nio.file.*;

public class PruebaLibroJettison {
    public static void main(String[] args) throws Exception {
        String json=Files.readString(Path.of("libro_xs.json"));
        XStream xs=new XStream(new JettisonMappedXmlDriver()); 
        xs.addPermission(AnyTypePermission.ANY); 
        xs.alias("libro", Libro.class);
        System.out.println("jettison → "+(Libro) xs.fromXML(json));
    }
}
