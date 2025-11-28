package psp.comms.clienteservidor;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Servidor {
    public static void main(String[] args) {
        ServerSocket servidor = null;
        Socket cliente = null;
        int numCliente= 0;
        int PUERTO = 5000;

        try {
            servidor = new ServerSocket(PUERTO);

            System.out.println("soy el servidor  y empiezo a escuchar peticiones por el puerto"+ PUERTO);

            do{
                cliente = servidor.accept();
                numCliente++;
                System.out.println("Llega el cliente "+ numCliente);

                DataOutputStream os = new DataOutputStream(cliente.getOutputStream());
                os.writeUTF("usted es mi cliente: " +numCliente);

                cliente.close();
                System.out.println("se ha cerrado la conexio ncon el cleinte : "+ numCliente);


            }while (true);


        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }


}
