package tarea;

import com.thoughtworks.xstream.XStream;

public class Main {
    public static void main(String[] args) {
        XStream xstream = new XStream();
        String xml = xstream.toXML("Hola XStream!");
        System.out.println(xml);
    }
}
