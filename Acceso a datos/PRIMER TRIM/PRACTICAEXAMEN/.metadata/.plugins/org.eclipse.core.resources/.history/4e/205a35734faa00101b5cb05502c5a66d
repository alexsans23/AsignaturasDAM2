package pruebasJson;


import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.json.JettisonMappedXmlDriver;


import java.nio.file.Files;
import java.nio.file.Paths;


public class ReadWithJettison {
public static void main(String[] args) throws Exception {
byte[] bytes = Files.readAllBytes(Paths.get("libro.json"));
String json = new String(bytes, java.nio.charset.StandardCharsets.UTF_8);


XStream xstream = new XStream(new JettisonMappedXmlDriver());
XStream.setupDefaultSecurity(xstream);
xstream.allowTypesByWildcard(new String[] {"pruebasJson.*"});
xstream.setMode(XStream.NO_REFERENCES);


// Con Jettison podemos usar fromXML para parsear JSON -> objeto
Libro libro = (Libro) xstream.fromXML(json);
System.out.println("Objeto regenerado con Jettison: " + libro);
}
}