package pruebasJson;


import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.json.JsonHierarchicalStreamDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;

import java.io.FileWriter;
import java.io.IOException;


public class PruebaXStreamJSON {
public static void main(String[] args) throws IOException {
Libro libro = new Libro("Cien años de soledad", "Gabriel García Márquez", 1967);


// Configurar XStream para JSON
XStream xstream = new XStream(new JsonHierarchicalStreamDriver());

xstream.addPermission(AnyTypePermission.ANY);

// Genera "JSON" (con este driver XStream usa toXML para producir JSON)
String json = xstream.toXML(libro);


// Guarda en fichero de texto plano
try (FileWriter fw = new FileWriter("libro.json")) {
fw.write(json);
}


System.out.println("JSON guardado en libro.json:\n" + json);
}
}