package Controller2;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;

import javax.swing.DefaultListModel;
import javax.swing.JFrame;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

import Model2.Alumno;
import Model2.IModeloAlumnos;
import UI2.VentanaAlumnos;

public class ControladorGestionAlumnos  implements ActionListener, ListSelectionListener {

	private IModeloAlumnos model;
	private VentanaAlumnos view;

	public ControladorGestionAlumnos(IModeloAlumnos model, VentanaAlumnos view) {
		 this.model = model;
        this.view = view;
        anadirListeners(this);
        
        this.view.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.view.pack();
        this.view.setLocationRelativeTo(null);
        this.view.setVisible(true);
	}

	private void anadirListeners(ControladorGestionAlumnos controladorGestionAlumnos) {
		view.btnCargarTodos.addActionListener(controladorGestionAlumnos);
        view.btnCrear.addActionListener(controladorGestionAlumnos);
        view.btnModificar.addActionListener(controladorGestionAlumnos);
        view.btnEliminar.addActionListener(controladorGestionAlumnos);  
        
        view.jListaAlumnos.addListSelectionListener(controladorGestionAlumnos);
	}
	
	

	@Override
	public void actionPerformed(ActionEvent event) {
	   	 String actionCommand = event.getActionCommand();
	
	     System.out.println("estoy en actionPerformed con la opcion "+actionCommand);
	
	     switch (actionCommand) {
	        case "Cargar Todos":
	        	 System.out.println("Cargando todos los alumnos...");
	            List<String> alumnos = model.getAll();
	            DefaultListModel<String> modelo = new DefaultListModel<>();
	            for (String alumno : alumnos) {
	                modelo.addElement(alumno);
	            }
	            view.jListaAlumnos.setModel(modelo); 

	        case "Crear Nuevo":
	        	System.out.println("Creando alumno...");
	            Alumno nuevoAlumno = new Alumno();
	            
	            nuevoAlumno.setDNI(view.textFieldDNI.getText());
	            nuevoAlumno.setNombre(view.textFieldNombre.getText());
	            nuevoAlumno.setApellidos(view.textFieldApellidos.getText());
	            nuevoAlumno.setCP(view.textFieldCP.getText());
	            boolean creado = model.crear(nuevoAlumno); 
	            if (creado) {
	            	limpiarCampos();
	                System.out.println("Alumno creado exitosamente.");
	            } else {
	                System.out.println("Error.");
	            }
	            break;

	        case "Modificar":
	            Alumno alumnoModificar = new Alumno();
	            alumnoModificar.setDNI(view.textFieldDNI.getText());
	            alumnoModificar.setNombre(view.textFieldNombre.getText());
	            alumnoModificar.setApellidos(view.textFieldApellidos.getText());
	            alumnoModificar.setCP(view.textFieldCP.getText());
	            boolean modificado = model.modificarAlumno(alumnoModificar);
	            if (modificado) {
	            	limpiarCampos();
	                System.out.println("Alumno modificado.");
	            } else {
	                System.out.println("Error al modificar el alumno.");
	            }
	            break;

	        case "Eliminar":
	            String dniEliminar = view.textFieldDNI.getText();
	            boolean eliminado = model.eliminarAlumno(dniEliminar);
	            if (eliminado) {
	            	limpiarCampos();
	                System.out.println("Alumno eliminado.");
	            } else {
	                System.out.println("Error al eliminar el alumno.");
	            }
	            break;
	    }
	     
		
	}

	@Override
	public void valueChanged(ListSelectionEvent e) {
		// TODO implementar el pinchar de una lista
	    System.out.println("estoy en valueChanged");
		if (!e.getValueIsAdjusting()) {//This line prevents double events

			int indice = view.jListaAlumnos.getSelectedIndex();
	        
	        if (indice != -1) { 
	            String dniSeleccionado = view.jListaAlumnos.getSelectedValue(); 

	            Alumno alumnoSeleccionado = model.getAlumnoPorDNI(dniSeleccionado);

	            cargarAlumno(alumnoSeleccionado);
	        }

	    }

		
	
	}

	private void limpiarCampos() {
		view.textFieldDNI.setText("");
        view.textFieldNombre.setText("");
        view.textFieldApellidos.setText("");
        view.textFieldCP.setText("");
		
	}
	
	private void cargarAlumno(Alumno alumno) {
        if (alumno == null) {
        	limpiarCampos();
        }

        view.textFieldDNI.setText(alumno.getDNI());
        view.textFieldNombre.setText(alumno.getNombre());
        view.textFieldApellidos.setText(alumno.getApellidos());
        view.textFieldCP.setText(alumno.getCP());
    }

}
