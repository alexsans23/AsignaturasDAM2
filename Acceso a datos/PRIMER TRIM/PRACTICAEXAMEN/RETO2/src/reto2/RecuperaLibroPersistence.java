package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;
import com.thoughtworks.xstream.persistence.FilePersistenceStrategy;
import com.thoughtworks.xstream.persistence.PersistenceStrategy;
import reto2.Libro;

import java.io.File;

public class RecuperaLibroPersistence {
    public static void main(String[] args) {
        // 1️⃣ Crear XStream y dar permisos
        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);

        // 2️⃣ Configurar aliases (idénticos a los usados al guardar)
        xstream.alias("libro", Libro.class);
        xstream.aliasField("titulo-libro", Libro.class, "titulo");
        xstream.aliasField("autor-libro", Libro.class, "autor");
        xstream.aliasField("anio-publicacion", Libro.class, "anio");

        // 3️⃣ Crear estrategia de persistencia
        File directorio = new File("persistencia");
        PersistenceStrategy strategy = new FilePersistenceStrategy(directorio, xstream);

        // 4️⃣ Recuperar el primer objeto (o todos los objetos de la carpeta)
        Libro libroRecuperado = strategy.read(); // lee un objeto
        System.out.println("Libro recuperado:");
        System.out.println(libroRecuperado);
    }
}
