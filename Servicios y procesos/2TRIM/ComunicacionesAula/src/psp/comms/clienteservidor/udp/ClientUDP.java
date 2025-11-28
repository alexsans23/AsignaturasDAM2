package psp.comms.clienteservidor.udp;


import java.io.IOException;
import java.net.*;

public class ClientUDP {
    public static void main(String[] args) {
        int PUERTO = 6789;
        int BUFFER_SIZE = 1000;
        System.out.println("soy el cleinte y voy a enviar un datagrama");
        String mensaje = " Hola soy un cleinte UDP";


        try (DatagramSocket socketUDP = new DatagramSocket()) {
            byte[] men = mensaje.getBytes();
            InetAddress hostServidor = InetAddress.getByName("localhost");

            DatagramPacket peticion = new DatagramPacket(men, men.length, hostServidor, PUERTO);
            socketUDP.send(peticion);

            byte[] bufer = new byte[BUFFER_SIZE];

            DatagramPacket respuesta = new DatagramPacket(bufer, BUFFER_SIZE);
            socketUDP.receive(respuesta);

            System.out.println("respuesta:" + new String (respuesta.getData()).trim());

        } catch (SocketException e) {
            throw new RuntimeException(e);
        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }
}
