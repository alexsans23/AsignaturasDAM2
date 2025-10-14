package pruebasJson;

import com.google.gson.*; 
import java.nio.file.*;

public class LeerJSONGson {
    public static void main(String[] args) throws Exception {
        String json = Files.readString(Path.of("libro_xs.json"));
        System.out.println("JSON leído: " + json);

        Gson g = new GsonBuilder().setPrettyPrinting().create();

        JsonElement root = JsonParser.parseString(json);
        JsonObject rootObj = root.getAsJsonObject();

        JsonElement libroElem = rootObj.has("libro") ? rootObj.get("libro") : rootObj;

        Libro l = g.fromJson(libroElem, Libro.class);
        System.out.println("gson → " + l);
        Files.writeString(Path.of("libro_gson.json"), g.toJson(l));
    }
}
