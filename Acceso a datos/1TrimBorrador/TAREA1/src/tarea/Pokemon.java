package tarea;

import java.util.Objects;

public class Pokemon implements Comparable<Pokemon>{

	private String nombre;
	private String tipo;
	private int peso;

	public Pokemon(String nombre, String tipo, int peso) {
		this.nombre = nombre;
		this.tipo = tipo;
		this.peso = peso;
	}

    public String getNombre() {
        return nombre;
    }

    public String getTipo() {
        return tipo;
    }

    public int getPeso() {
        return peso;
    }
    
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public void setPeso(int peso) {
		this.peso = peso;
	}

	
	public void mostrarInfo() {
		System.out.println("Nombre: "+ nombre+ ", tipo: "+ tipo + " y peso: " + peso + ".");
	}
	
	@Override
    public int compareTo(Pokemon otro) {
        return this.nombre.compareToIgnoreCase(otro.nombre);
    }

	@Override
	public int hashCode() {
		return Objects.hash(nombre, peso, tipo);
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString();
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Pokemon other = (Pokemon) obj;
		return Objects.equals(nombre, other.nombre) && peso == other.peso && Objects.equals(tipo, other.tipo);
	}

	
}
