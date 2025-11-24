package psp.procesos;

import java.io.*;
import java.util.*;

public class Actividad1 {
    static Scanner sc = new Scanner(System.in);
    static boolean isWindows;
    static {
        String os = System.getProperty("os.name");
        if (os == null) {
            isWindows = false;
        } else {
            isWindows = os.toLowerCase().contains("win");
        }
    }

    public static void main(String[] args) throws Exception {
        System.out.println("Actividad 1.1 - Creacion y ejecucion de procesos");
        if (isWindows) {
            System.out.println("SO detectado: Windows");
        } else {
            System.out.println("SO detectado: Linux");
        }
        boolean salir = false;
        while (!salir) {
            System.out.println();
            System.out.println("a) Ping");
            System.out.println("b) Listar archivos a fichero");
            System.out.println("c) Listar procesos y cerrar por PID");
            System.out.println("d) Abrir navegador con URL");
            System.out.println("q) Salir");
            System.out.print("Opcion: ");
            String opcion = sc.nextLine();
            switch (opcion) {
                case "a":
                    opcionPing();
                    break;
                case "b":
                    opcionListarAArchivo();
                    break;
                case "c":
                    opcionListarYCerrarProceso();
                    break;
                case "d":
                    opcionAbrirNavegador();
                    break;
                case "q":
                    System.out.println("Saliendo...");
                    salir = true;
                    break;
                default:
                    System.out.println("Opcion no valida");
                    break;
            }
        }
    }

    static void opcionPing() throws Exception {
        System.out.print("Destino: ");
        String destino = sc.nextLine();
        if (destino.equals("")) {
            System.out.println("Cancelado");
            return;
        }
        List<String> cmd;
        if (isWindows) {
            cmd = Arrays.asList("ping", "-n", "4", destino);
        } else {
            cmd = Arrays.asList("ping", "-c", "4", destino);
        }
        ejecutarYMostrarSalida(cmd);
    }

    static void opcionListarAArchivo() throws Exception {
        System.out.print("Ruta fichero salida: ");
        String ruta = sc.nextLine();
        if (ruta.equals("")) {
            System.out.println("Cancelado");
            return;
        }
        List<String> cmd;
        if (isWindows) {
            cmd = Arrays.asList("cmd", "/c", "dir");
        } else {
            cmd = Arrays.asList("ls", "-la");
        }
        File salida = new File(ruta);
        ProcessBuilder pb = new ProcessBuilder(cmd);
        pb.redirectErrorStream(true);
        File parent = salida.getAbsoluteFile().getParentFile();
        if (parent != null && !parent.exists()) {
            parent.mkdirs();
        }
        pb.redirectOutput(salida);
        Process p = pb.start();
        int code = p.waitFor();
        System.out.println("Proceso finalizado con codigo: " + code);
        if (code == 0) {
            System.out.println("Fichero creado: " + salida.getAbsolutePath());
        }
    }

    static void opcionListarYCerrarProceso() throws Exception {
        List<String> cmdList;
        if (isWindows) {
            cmdList = Arrays.asList("tasklist");
        } else {
            cmdList = Arrays.asList("ps", "-e", "-o", "pid,uid,comm");
        }
        ejecutarYMostrarSalida(cmdList);
        System.out.print("PID a terminar (vacío para cancelar): ");
        String pid = sc.nextLine();
        if (pid.equals("")) {
            System.out.println("Cancelado");
            return;
        }
        List<String> cmdKill;
        if (isWindows) {
            cmdKill = Arrays.asList("taskkill", "/PID", pid, "/F");
        } else {
            cmdKill = Arrays.asList("kill", "-9", pid);
        }
        ejecutarYMostrarSalida(cmdKill);
    }

    static void opcionAbrirNavegador() throws Exception {
        System.out.print("URL: ");
        String url = sc.nextLine();
        if (url.equals("")) {
            System.out.println("Cancelado");
            return;
        }
        List<String> cmd;
        if (isWindows) {
            cmd = Arrays.asList("cmd", "/c", "start", "", url);
        } else {
            cmd = Arrays.asList("xdg-open", url);
        }
        ProcessBuilder pb = new ProcessBuilder(cmd);
        pb.redirectErrorStream(true);
        pb.start();
        System.out.println("Comando lanzado.");
    }

    static void ejecutarYMostrarSalida(List<String> comando) throws Exception {
        ProcessBuilder pb = new ProcessBuilder(comando);
        pb.redirectErrorStream(true);
        Process p = pb.start();
        BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String linea;
        while ((linea = r.readLine()) != null) {
            System.out.println(linea);
        }
        int code = p.waitFor();
        System.out.println("Codigo de salida: " + code);
    }
}
