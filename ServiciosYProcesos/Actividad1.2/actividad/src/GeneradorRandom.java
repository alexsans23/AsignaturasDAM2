import java.util.Random;

public class RandomGenerator {
    public static void main(String[] args) {
        Random rnd = new Random();
        int number = rnd.nextInt(10); // número natural entre 0 y 9 inclusive
        System.out.println(number);
        // salimos con código 0 por defecto
    }
}
