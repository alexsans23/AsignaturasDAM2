package bbdd;

import java.util.List;

public class Prueba {
    public static void main(String[] args) {
        try {
            BD_Alumnos dao = new BD_Alumnos();

            // --- CREATE ---
            int id1 = dao.insertar(new Alumno("ana", "lópez", "ana@example.com"));
            int id2 = dao.insertar(new Alumno("bruno", "díaz", "bruno@example.com"));
            System.out.println("Insertados con id: " + id1 + " y " + id2);

            // --- READ ALL ---
            System.out.println("\n---- Alumnos antes de actualizar ----");
            List<Alumno> alumnos = dao.listarTodos();
            for (Alumno a : alumnos) System.out.println(a);

            // --- UPDATE parcial (solo email) ---
            int tocadas = dao.actualizarEmail(id2, "bruno.nuevo@example.com");
            System.out.println("\nFilas actualizadas (email): " + tocadas);

            // --- UPDATE completo ---
            Alumno aModificar = dao.buscarPorId(id1);
            if (aModificar != null) {
                aModificar.setNombre("Ana María");
                aModificar.setApellido("López Pérez");
                aModificar.setEmail("ana.nuevo@example.com");
                int filas = dao.actualizarAlumno(aModificar);
                System.out.println("Filas actualizadas (completo): " + filas);
            }

            // --- READ individual ---
            Alumno buscado = dao.buscarPorId(id1);
            System.out.println("\nAlumno buscado por ID " + id1 + ": " + buscado);

            // --- DELETE ---
            int borradas = dao.borrarPorId(id1);
            System.out.println("\nFilas borradas: " + borradas);

            // --- READ ALL final ---
            System.out.println("\n---- Alumnos finales en la tabla ----");
            alumnos = dao.listarTodos();
            for (Alumno a : alumnos) System.out.println(a);

            System.out.println("\nPrueba CRUD terminada OK.");

        } catch (Exception e) {
            System.err.println("Error en la prueba:");
            e.printStackTrace();
        }
    }
}
