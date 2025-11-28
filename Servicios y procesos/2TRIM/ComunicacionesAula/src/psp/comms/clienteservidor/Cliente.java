package psp.comms.clienteservidor;

import java.io.DataInputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.sql.SQLOutput;

public class Cliente {
    public static void main(String[] args) {
        InetAddress direccion;
        Socket servidor = null;
        int PUERTO = 5000;

        System.out.println("soy un cliente e intento coenctarme");

        try {
            direccion= InetAddress.getLocalHost();
            servidor = new Socket(direccion, PUERTO);

            System.out.println("conexion realizada con éxito");

            DataInputStream datos =new DataInputStream(servidor.getInputStream());
            System.out.println(datos.readUTF());




        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }finally {
            try {
                servidor.close();
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }


    }
}
