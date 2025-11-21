package reto1;

import java.io.Serializable;

public class Perro implements Serializable {

	private String nombre;
    private String raza;
    private int edad;

    public Perro(String nombre, String raza, int edad) {
		this.nombre = nombre;
		this.raza = raza;
		this.edad = edad;
	}


	public String getNombre() {
		return nombre;
	}


	public String getRaza() {
		return raza;
	}


	 public int getEdad() {
		return edad;
	}


	@Override
		public String toString() {
			return "nombre=" + nombre + ", raza=" + raza + ", edad=" + edad;
		}


}
