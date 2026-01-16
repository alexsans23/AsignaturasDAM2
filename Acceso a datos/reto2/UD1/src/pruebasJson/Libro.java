package pruebasJson;

public class Libro implements java.io.Serializable {
    private String titulo; 
    private String autor; 
    private int anio;
    public Libro(){
    } 
    public Libro(String t,String a,int y)
    {titulo=t;
    autor=a;
    anio=y;
    }
    public String getTitulo()
    {return titulo;
    } 
    public void setTitulo(String v){
    	titulo=v;
    	}
    
    public String getAutor(){
    	return autor;
    	} public void setAutor(String v){
    		autor=v;
    		}
    public int getAnio()
    {return anio;
    } 
    public void setAnio(int v){
    	anio=v;
    	}
    public String toString(){
    	return "libro{titulo='"+titulo+"', autor='"+autor+"', anio="+anio+"}";
    	}
}
