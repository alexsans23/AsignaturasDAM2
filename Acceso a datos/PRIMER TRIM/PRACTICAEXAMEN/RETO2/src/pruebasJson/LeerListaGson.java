package pruebasJson;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class LeerListaGson {
    public static void main(String[] args) throws Exception {
        // 1) Leer el fichero gson.json
        byte[] bytes = Files.readAllBytes(Paths.get("gson.json"));
        String jsonLeido = new String(bytes, java.nio.charset.StandardCharsets.UTF_8);

        // 2) Deserializar a List<Libro> usando TypeToken para conservar genéricos
        Gson gson = new Gson();
        Type tipoLista = new TypeToken<List<Libro>>() {}.getType();
        List<Libro> listaRecuperada = gson.fromJson(jsonLeido, tipoLista);

        // 3) Imprimir la lista recuperada por pantalla
        System.out.println("Lista recuperada desde gson.json:");
        for (Libro l : listaRecuperada) {
            System.out.println(l);
        }
    }
}
