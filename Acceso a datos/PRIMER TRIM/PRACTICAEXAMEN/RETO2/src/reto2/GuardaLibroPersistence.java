package reto2;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;
import com.thoughtworks.xstream.security.AnyTypePermission;
import com.thoughtworks.xstream.persistence.FilePersistenceStrategy;
import com.thoughtworks.xstream.persistence.PersistenceStrategy;
import reto2.Libro;

import java.io.File;

public class GuardaLibroPersistence {
    public static void main(String[] args) {
        // 1️⃣ Crear XStream y dar permisos
        XStream xstream = new XStream(new DomDriver());
        xstream.addPermission(AnyTypePermission.ANY);

        // 2️⃣ Configurar aliases (como antes)
        xstream.alias("libro", Libro.class);
        xstream.aliasField("titulo-libro", Libro.class, "titulo");
        xstream.aliasField("autor-libro", Libro.class, "autor");
        xstream.aliasField("anio-publicacion", Libro.class, "anio");

        // 3️⃣ Crear objeto Libro
        Libro libro = new Libro("El Principito", "Antoine de Saint-Exupéry", 1943);

        // 4️⃣ Crear estrategia de persistencia: cada objeto será un fichero en la carpeta "persistencia"
        File directorio = new File("persistencia");
        directorio.mkdir(); // crea la carpeta si no existe

        PersistenceStrategy strategy = new FilePersistenceStrategy(directorio, xstream);

        // 5️⃣ Guardar objeto en fichero
        strategy.write(libro);
        System.out.println("Libro guardado en carpeta persistencia usando PersistenceStrategy");
    }
}
