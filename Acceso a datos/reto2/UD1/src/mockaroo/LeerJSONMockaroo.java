package mockaroo;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class LeerJSONMockaroo {
    public static void main(String[] args) throws Exception {
        String json = Files.readString(Path.of("personas.json"));
        Gson gson = new Gson();

        List<Persona> personas = gson.fromJson(json, new TypeToken<List<Persona>>(){}.getType());
        personas.forEach(System.out::println);
    }
}
