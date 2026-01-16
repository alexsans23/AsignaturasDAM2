package reto2;

import org.w3c.dom.*;
import javax.xml.parsers.*;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;

public class GenerarXMLConDOM {
    public static void main(String[] args) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document doc = builder.newDocument();

            Element root = doc.createElement("libros");
            doc.appendChild(root);

            Element libro = doc.createElement("libro");

            Element titulo = doc.createElement("titulo");
            titulo.setTextContent("El Principito");
            libro.appendChild(titulo);

            Element autor = doc.createElement("autor");
            autor.setTextContent("Antoine de Saint-Exupéry");
            libro.appendChild(autor);

            Element anio = doc.createElement("anio");
            anio.setTextContent("1943");
            libro.appendChild(anio);

            root.appendChild(libro);

            Transformer transformer = TransformerFactory.newInstance().newTransformer();
            transformer.setOutputProperty(OutputKeys.INDENT, "yes");
            transformer.transform(new DOMSource(doc), new StreamResult(new File("libros.xml")));

            System.out.println("XML generado correctamente.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
