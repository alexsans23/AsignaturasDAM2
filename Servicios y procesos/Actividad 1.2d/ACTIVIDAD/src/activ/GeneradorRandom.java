package activ;

import java.util.Random;

public class GeneradorRandom {
public static void main(String[] args) {
Random rand = new Random();
int num = rand.nextInt(10);
System.out.print(num);
}
}
