package psp.comms;

import java.net.InetAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.Arrays;
import java.util.Enumeration;

public class HostInfo {
    public static void main(String[] args) {
        try {
            InetAddress localHost = InetAddress.getLocalHost();
            System.out.println("nombre del localHost: "+ localHost.getHostName());
            System.out.println("direccion ip local: "+ localHost.getHostAddress());
        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        }
        try {
            InetAddress google = InetAddress.getByName("www.google.com");
            System.out.println("nombre del host remoto: "+ google.getHostName());
            System.out.println("direccion ip remota: "+ google.getHostAddress());
        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        }
        try {
            Enumeration<NetworkInterface> interfaces= NetworkInterface.getNetworkInterfaces();

            while(interfaces.hasMoreElements()){
                NetworkInterface ni = interfaces.nextElement();

                if(!ni.isLoopback() && ni.isUp() && !ni.getInterfaceAddresses().isEmpty()){

                    System.out.println("Nombre de la interfaz: "+ ni.getName());
                    System.out.println("Interfaz activa :"+ ni.isUp());

                    byte[] MACbytes = ni.getHardwareAddress();
                    StringBuilder sb = new StringBuilder();
                    for (int i = 0; i < MACbytes.length; i++) {
                        sb.append(String.format("%02X", MACbytes[i]));
                        if(i<MACbytes.length -1){
                            sb.append(":");
                        }
                    }

                    System.out.println("MAC Adress: " +sb);
                    //System.out.println("MAC: "+ Arrays.toString(ni.getHardwareAddress()));




                    Enumeration<InetAddress> direcciones = ni.getInetAddresses();
                    while(direcciones.hasMoreElements()){
                        InetAddress ip = direcciones.nextElement();
                        System.out.println("direccion ip: "+ ip.getHostAddress());

                    }
                }



            }
        } catch (SocketException e) {
            throw new RuntimeException(e);
        }
    }
}
