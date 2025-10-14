package properties;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Properties;

public class PropertiesTest {

	public static void main(String[] args) {
		
		Properties props = new Properties();
		
		props.setProperty("usuario", "alex");
		props.setProperty("contrasenia", "1234");
		props.setProperty("idioma", "es");
		
		try (FileOutputStream fos = new FileOutputStream("fichero.properties")) {
			
			props.store(fos, "fichero.properties");
			System.out.println("creado el fichero.properites");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		try(FileOutputStream fosXML = new FileOutputStream("fichero.xml")){
			
			props.storeToXML(fosXML, "fichero.xml");
			System.out.println("creado el fichero.xml");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		Properties propsRecuperado = new Properties();
		try (FileInputStream fis = new FileInputStream ("fichero.properties")){
			propsRecuperado.load(fis);
			System.out.println("esto es lo que he recuperado del .properties anteriiormente creado:"
					+ propsRecuperado);
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		

	}

}
