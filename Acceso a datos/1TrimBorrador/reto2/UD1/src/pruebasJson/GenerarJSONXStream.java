package pruebasJson;

import com.thoughtworks.xstream.*; 
import com.thoughtworks.xstream.io.json.JsonHierarchicalStreamDriver; 
import com.thoughtworks.xstream.security.AnyTypePermission;
import java.nio.file.*;

public class GenerarJSONXStream {
    public static void main(String[] args) throws Exception {
        Libro l=new Libro("el principito","antoine",1943);
        XStream xs=new XStream(new JsonHierarchicalStreamDriver());
        xs.addPermission(AnyTypePermission.ANY);
        xs.alias("libro", Libro.class);
        String json=xs.toXML(l);
        Files.writeString(Path.of("libro_xs.json"), json);
        System.out.println(json);
    }
}
