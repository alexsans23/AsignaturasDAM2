import java.util.concurrent.ThreadLocalRandom;

public class GeneradorRandom {
    public static void main(String[] args) {
        int min = 0;
        int max = 9;
        if (args.length >= 2) {
            try {
                min = Integer.parseInt(args[0]);
                max = Integer.parseInt(args[1]);
            } catch (NumberFormatException e) {
            }
        }
        int n = ThreadLocalRandom.current().nextInt(min, max + 1);
        System.out.println(n);
    }
}