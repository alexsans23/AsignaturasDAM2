package reto2;

import org.w3c.dom.*;
import javax.xml.parsers.*;
import java.io.File;

public class LeerXMLConDOM {
    public static void main(String[] args) {
        try {
            File xmlFile = new File("libros.xml");
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.parse(xmlFile);

            NodeList libros = doc.getElementsByTagName("libro");
            for (int i = 0; i < libros.getLength(); i++) {
                Element libro = (Element) libros.item(i);
                String titulo = libro.getElementsByTagName("titulo").item(0).getTextContent();
                String autor = libro.getElementsByTagName("autor").item(0).getTextContent();
                String anio = libro.getElementsByTagName("anio").item(0).getTextContent();

                System.out.println(titulo + " - " + autor + " (" + anio + ")");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
