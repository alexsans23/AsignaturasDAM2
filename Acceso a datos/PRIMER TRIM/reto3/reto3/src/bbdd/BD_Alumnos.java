package bbdd;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class BD_Alumnos {

    private static final String URL =
        "jdbc:mysql://localhost:3306/adat1?useSSL=false&serverTimezone=UTC&allowPublicKeyRetrieval=true";
    private static final String USUARIO = "dam2";
    private static final String CLAVE   = "asdf.1234";

    // ---------------- CREATE ----------------
    public int insertar(Alumno a) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        String sql = "INSERT INTO alumnos (nombre, apellido, email) VALUES (?,?,?)";

        try (Connection cn = DriverManager.getConnection(URL, USUARIO, CLAVE);
             PreparedStatement ps = cn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {

            ps.setString(1, a.getNombre());
            ps.setString(2, a.getApellido());
            ps.setString(3, a.getEmail());
            ps.executeUpdate();

            try (ResultSet rs = ps.getGeneratedKeys()) {
                if (rs.next()) {
                    int id = rs.getInt(1);
                    a.setId(id);
                    return id;
                }
            }
            throw new SQLException("no se obtuvo id generado");
        }
    }

    // ---------------- READ ALL ----------------
    public List<Alumno> listarTodos() throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        String sql = "SELECT id, nombre, apellido, email, fecha_registro FROM alumnos ORDER BY id";

        List<Alumno> lista = new ArrayList<>();

        try (Connection cn = DriverManager.getConnection(URL, USUARIO, CLAVE);
             PreparedStatement ps = cn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {

            while (rs.next()) {
                Alumno a = new Alumno(
                    rs.getString("nombre"),
                    rs.getString("apellido"),
                    rs.getString("email")
                );
                a.setId(rs.getInt("id"));

                Date fr = rs.getDate("fecha_registro");
                if (fr != null) a.setFechaRegistro(fr.toLocalDate());

                lista.add(a);
            }
        }
        return lista;
    }

    // ---------------- READ by ID ----------------
    public Alumno buscarPorId(int id) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        String sql = "SELECT id, nombre, apellido, email, fecha_registro FROM alumnos WHERE id=?";

        try (Connection cn = DriverManager.getConnection(URL, USUARIO, CLAVE);
             PreparedStatement ps = cn.prepareStatement(sql)) {

            ps.setInt(1, id);

            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    Alumno a = new Alumno(
                        rs.getString("nombre"),
                        rs.getString("apellido"),
                        rs.getString("email")
                    );
                    a.setId(rs.getInt("id"));
                    Date fr = rs.getDate("fecha_registro");
                    if (fr != null) a.setFechaRegistro(fr.toLocalDate());
                    return a;
                }
            }
        }
        return null; // si no existe
    }

    // ---------------- UPDATE parcial ----------------
    public int actualizarEmail(int id, String nuevoEmail) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        String sql = "UPDATE alumnos SET email=? WHERE id=?";

        try (Connection cn = DriverManager.getConnection(URL, USUARIO, CLAVE);
             PreparedStatement ps = cn.prepareStatement(sql)) {

            ps.setString(1, nuevoEmail);
            ps.setInt(2, id);

            return ps.executeUpdate();
        }
    }

    // ---------------- UPDATE completo ----------------
    public int actualizarAlumno(Alumno a) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        String sql = "UPDATE alumnos SET nombre=?, apellido=?, email=? WHERE id=?";

        try (Connection cn = DriverManager.getConnection(URL, USUARIO, CLAVE);
             PreparedStatement ps = cn.prepareStatement(sql)) {

            ps.setString(1, a.getNombre());
            ps.setString(2, a.getApellido());
            ps.setString(3, a.getEmail());
            ps.setInt(4, a.getId());

            return ps.executeUpdate();
        }
    }

    // ---------------- DELETE ----------------
    public int borrarPorId(int id) throws Exception {
        Class.forName("com.mysql.cj.jdbc.Driver");
        String sql = "DELETE FROM alumnos WHERE id=?";

        try (Connection cn = DriverManager.getConnection(URL, USUARIO, CLAVE);
             PreparedStatement ps = cn.prepareStatement(sql)) {

            ps.setInt(1, id);
            return ps.executeUpdate();
        }
    }
}
