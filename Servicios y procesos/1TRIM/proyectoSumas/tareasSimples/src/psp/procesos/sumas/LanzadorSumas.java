package psp.procesos.sumas;

import org.w3c.dom.ls.LSOutput;

public class LanzadorSumas {

    private void lanzarSuma(Integer n1, Integer n2, Integer proceso){
        ProcessBuilder pb;
        Process process;
        String classname= "psp.procesos.sumas.Sumador";
        //String classpath ="/home/alumno/Asignaturas/git/Serviciosyprocesos/out/production/tareasSimples";
        String currentPath = System.getProperty("user.dir");
        String classpath = currentPath+ "/out/production/tareasSimples";
        try{
            pb = new ProcessBuilder("java", "-cp", classpath, classname, n1.toString(), n2.toString(), proceso.toString());
            pb.inheritIO();
            process = pb.start();
            process.waitFor();
        }catch ( Exception e){
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        LanzadorSumas ls= new LanzadorSumas();
        ls.lanzarSuma(200,30000,1);
        ls.lanzarSuma(23,31,2);
        ls.lanzarSuma(2,3,3);
        ls.lanzarSuma(223,3234,4);
        ls.lanzarSuma(21,43,5);

    }
}
