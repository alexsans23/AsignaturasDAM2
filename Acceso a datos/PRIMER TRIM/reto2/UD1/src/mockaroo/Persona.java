package mockaroo;

import java.util.List;

public class Persona {
    private int id;
    private String nombre;
    private String email;
    private Direccion direccion;
    private List<Telefono> telefonos;

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public Direccion getDireccion() { return direccion; }
    public void setDireccion(Direccion direccion) { this.direccion = direccion; }

    public List<Telefono> getTelefonos() { return telefonos; }
    public void setTelefonos(List<Telefono> telefonos) { this.telefonos = telefonos; }

    @Override
    public String toString() {
        return nombre + " (" + email + "), " + direccion + ", " + telefonos;
    }
}
