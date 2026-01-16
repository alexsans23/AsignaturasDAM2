package mockaroo;

public class Direccion {
    private String calle;
    private String ciudad;
    private String pais;

    public String getCalle() { return calle; }
    public void setCalle(String calle) { this.calle = calle; }

    public String getCiudad() { return ciudad; }
    public void setCiudad(String ciudad) { this.ciudad = ciudad; }

    public String getPais() { return pais; }
    public void setPais(String pais) { this.pais = pais; }

    @Override
    public String toString() {
        return calle + ", " + ciudad + ", " + pais;
    }
}
