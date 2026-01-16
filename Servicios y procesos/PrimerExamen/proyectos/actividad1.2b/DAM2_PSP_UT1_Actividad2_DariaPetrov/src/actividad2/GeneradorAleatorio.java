package actividad2;

import java.util.Random;

public class GeneradorAleatorio {

    /**
     * Metodo que genera un número aleatorio por cada caracter en cada argumento recibido
     * @param input trata cada argumento individual como String para devolver un numero por cada caracter
     * @return Devuelve una serie de enteros convertidos a String
     */

    public String generar(String[] input){
        Random rng = new Random();
        String aux = ""; //String vacía inicializada

        for (String s : input) {
            for (char c : s.toCharArray()) {
                aux += (rng.nextInt(10)); //Concatena el número aleatorio generado, en un rango excluyendo el tope, a la String auxiliar
            }
        }
        return aux; //Devuelve la String
    }

    public static void main(String[] args) {
        GeneradorAleatorio rngGen = new GeneradorAleatorio();

        String prueba = rngGen.generar(args);
        System.out.println(prueba); // Syso capturado por el proceso padre mediante un InputStream

    }

}
