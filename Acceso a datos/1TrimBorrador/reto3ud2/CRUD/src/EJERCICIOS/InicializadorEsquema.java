package EJERCICIOS;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class InicializadorEsquema {

    private static final String URL =
        "jdbc:mysql://localhost:3306/adat1?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true";
    private static final String USUARIO = "dam2";
    private static final String CLAVE   = "asdf.1234";

    private static final String SQL_CREAR_ALUMNOS =
        "CREATE TABLE IF NOT EXISTS alumnos ("
      + "id INT AUTO_INCREMENT PRIMARY KEY,"
      + "nombre VARCHAR(80) NOT NULL,"
      + "apellido VARCHAR(80),"
      + "email VARCHAR(120),"
      + "fecha_registro DATE DEFAULT CURRENT_DATE"
      + ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci";

    private static final String SQL_CREAR_MATRICULAS =
        "CREATE TABLE IF NOT EXISTS matriculas ("
      + "id INT AUTO_INCREMENT PRIMARY KEY,"
      + "alumno_id INT NOT NULL,"
      + "curso VARCHAR(120) NOT NULL,"
      + "fecha_matricula DATE NOT NULL,"
      + "observaciones VARCHAR(255),"
      + "CONSTRAINT fk_matricula_alumno FOREIGN KEY (alumno_id)"
      + " REFERENCES alumnos(id) ON DELETE CASCADE ON UPDATE CASCADE"
      + ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci";

    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver"); // carga el driver (seguro)
            try (Connection conexion = DriverManager.getConnection(URL, USUARIO, CLAVE)) {

                try (PreparedStatement ps1 = conexion.prepareStatement(SQL_CREAR_ALUMNOS)) {
                    ps1.executeUpdate();
                }

                try (PreparedStatement ps2 = conexion.prepareStatement(SQL_CREAR_MATRICULAS)) {
                    ps2.executeUpdate();
                }

                System.out.println("Tablas 'alumnos' y 'matriculas' creadas correctamente (si no existían).");
            }
        } catch (Exception e) {
            System.err.println("Error al crear las tablas:");
            e.printStackTrace();
        }
    }
}
