package Model2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class ModeloAlumnosJDBC implements IModeloAlumnos {

	private static String cadenaConexion =  "jdbc:mysql://localhost:3306/instituto";
	private static String user = "dam2";
	private static String pass = "asdf.1234";
	
	public ModeloAlumnosJDBC() {
		
	}

	@Override
	public List<String> getAll() {
	    List<String> alumnos = new ArrayList<>(); 
	    String sql = "SELECT dni, nombre, apellidos, cp FROM alumnos";  
	    try (Connection con = DriverManager.getConnection(cadenaConexion, user, pass)) {
	        PreparedStatement stmt = con.prepareStatement(sql);
	        ResultSet rs = stmt.executeQuery();
	        while (rs.next()) {
	            Alumno alumno = new Alumno();
	            alumno.setDNI(rs.getString("dni"));
	            alumno.setNombre(rs.getString("nombre"));
	            alumno.setApellidos(rs.getString("apellidos"));
	            alumno.setCP(rs.getString("cp"));
	            alumnos.add(alumno.toString());
	        }
	    } catch (SQLException e) {
	        System.err.println("Error al obtener todos los alumnos: " + e.getMessage());
	    }
	    return alumnos;  
	}

	@Override
	public Alumno getAlumnoPorDNI(String DNI) {
		Alumno alumno = new Alumno();
		
		try(Connection con = DriverManager.getConnection(cadenaConexion, user, pass)) {	
			PreparedStatement stmt = con.prepareStatement("SELECT dni, nombre, apellidos, cp FROM alumnos WHERE dni = ?");
			stmt.setString(1, DNI);
			ResultSet datos = stmt.executeQuery();
			if (datos.next()) { 
			    alumno.setDNI(datos.getString("dni"));
			    alumno.setNombre(datos.getString("nombre"));
			    alumno.setApellidos(datos.getString("apellidos"));
			    alumno.setCP(datos.getString("cp"));
			    return alumno;
			}
		}catch(SQLException e){
			e.printStackTrace();
		}
		
		return null;
	}

	@Override
	public boolean modificarAlumno(Alumno alumno) {
	    String sql = "UPDATE Alumnos SET nombre = ?, apellidos = ?, cp = ? WHERE dni = ?"; 

	    try (Connection con = DriverManager.getConnection(cadenaConexion, user, pass)) {
	        PreparedStatement stmt = con.prepareStatement(sql);
	        
	        stmt.setString(1, alumno.getNombre()); 
	        stmt.setString(2, alumno.getApellidos());
	        stmt.setString(3, alumno.getCP());
	        stmt.setString(4, alumno.getDNI());

	        int actualizada = stmt.executeUpdate();

	        return actualizada > 0;

	    } catch (SQLException e) {
	        e.printStackTrace();
	    }

	    return false;
	}


	@Override
	public boolean eliminarAlumno(String DNI) {
		try(Connection con = DriverManager.getConnection(cadenaConexion, user, pass)) {	
			PreparedStatement stmt = con.prepareStatement("delete from Alumnos where dni = '" + DNI + "';");
			
			int eliminada = stmt.executeUpdate();
	        
		      
		    return eliminada > 0;
		        
			
		}catch(SQLException e){
			e.printStackTrace();
		}
		
		return false;
	}

	@Override
	public boolean crear(Alumno alumno) {
	    try(Connection con = DriverManager.getConnection(cadenaConexion, user, pass)) {    
	        PreparedStatement stmt = con.prepareStatement("INSERT INTO alumnos(dni, nombre, apellidos, cp) VALUES(?, ?, ?, ?)");
	        stmt.setString(1, alumno.getDNI()); 
	        stmt.setString(2, alumno.getNombre());
	        stmt.setString(3, alumno.getApellidos());
	        stmt.setString(4, alumno.getCP());
	    
	        int insertada = stmt.executeUpdate();
	        
	        return insertada > 0; 
	        
	    } catch(SQLException e) {
	        System.err.println("Error al crear el alumno: " + e.getMessage());
	    }
	    
	    return false;
	}

	
	

}
