package tarea;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

public class Main{

	public static void main(String[] args) {
		List<Pokemon> pokedex = new ArrayList<>();
		
		Pokemon p1 = new Pokemon("Eve", "Fuego", 28);
		Pokemon p2 = new Pokemon("Bulbassur", "Tierra", 42);
		Pokemon p3 = new Pokemon("Eve", "Fuego", 28);
		
		pokedex.add(p1);
		pokedex.add(p2);
		
		for (Pokemon p : pokedex) {
			p.mostrarInfo();
		}
			 
		 pokedex.sort(null);
		 
		 for (Pokemon p : pokedex) {
				p.mostrarInfo();
			}
		 
		 System.out.println("\n//////////////// HashSet:\n");
		 Set<Pokemon> pokedex2= new HashSet<>();
		 
		 pokedex2.add(p1);		 
		 pokedex2.add(p2);
		 pokedex2.add(p3);
		 
		 for (Pokemon p : pokedex2) {
			 p.mostrarInfo();
		 }
		 
		 System.out.println("\n/////////////////HashMap:\n");
		 
		 Map<String, Pokemon> pokedex3 = new HashMap<>();
		 

		 for (Pokemon p : pokedex) {
			 pokedex3.put(p.getNombre(), p);
		 }
		 
		 Pokemon buscado = pokedex3.get("Eve");
		 
		 System.out.println("He encontrado esto: ");
		 buscado.mostrarInfo();
		 
		
		
		

	}
	
	
	

}
