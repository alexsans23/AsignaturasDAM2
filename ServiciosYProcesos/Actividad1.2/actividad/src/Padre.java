import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public class Padre {
    public static void main(String[] args) throws Exception {
        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
        String line;
        System.out.print("> ");
        while ((line = stdin.readLine()) != null) {
            if (line.equals("fin")) break;



            List<Process> processes = new ArrayList<>();
            List<BufferedReader> outputs = new ArrayList<>();


            for (char c : line.toCharArray()) {
                ProcessBuilder pb = new ProcessBuilder("java", "-cp", "bin", "GeneradorRandom");
                pb.redirectErrorStream(true);
                Process p = pb.start();
                processes.add(p);
                outputs.add(new BufferedReader(new InputStreamReader(p.getInputStream())));
            }


            StringBuilder result = new StringBuilder();
            for (int i = 0; i < processes.size(); i++) {
                Process p = processes.get(i);
                BufferedReader r = outputs.get(i);
                String num = r.readLine();
                p.waitFor();
                if (num != null) result.append(num.trim());
            }


            System.out.println(result.toString());
            System.out.print("> ");
        }
        System.out.println("Terminando.");
    }
}