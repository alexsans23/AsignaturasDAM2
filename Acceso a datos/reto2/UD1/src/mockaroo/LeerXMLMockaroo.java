package mockaroo;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;
import java.io.FileInputStream;
import java.util.List;

public class LeerXMLMockaroo {
    public static void main(String[] args) throws Exception {
        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);
        xstream.alias("persona", Persona.class);
        xstream.alias("personas", List.class);
        xstream.alias("direccion", Direccion.class);
        xstream.alias("telefono", Telefono.class);

        FileInputStream fis = new FileInputStream("personas.xml");
        List<Persona> personas = (List<Persona>) xstream.fromXML(fis);
        personas.forEach(System.out::println);
    }
}
