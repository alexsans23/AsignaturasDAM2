package Controller2;

import Model2.IModeloAlumnos;
import Model2.ModeloAlumnosJDBC;
import UI2.VentanaAlumnos;

public class GestionAlumnos {

	public static void main(String[] args) {
		 try {
        	VentanaAlumnos view = new VentanaAlumnos();
        	IModeloAlumnos model = new ModeloAlumnosJDBC();
        	ControladorGestionAlumnos controller = new ControladorGestionAlumnos(model, view);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
