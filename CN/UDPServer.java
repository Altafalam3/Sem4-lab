import java.io.*;
import java.net.*;

public class UDPServer {
    public static void main(String[] args) throws IOException {
        DatagramSocket socket = new DatagramSocket(8888);
        System.out.println("Server started. Listening on port 8888.");

        while (true) {
            // Receive the datagram packet from the client
            byte[] buffer = new byte[1024];
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            socket.receive(packet);

            // Convert the received bytes to two numbers
            String inputLine = new String(packet.getData(), 0, packet.getLength());
            String[] numbers = inputLine.split(" ");
            int num1 = Integer.parseInt(numbers[0]);
            int num2 = Integer.parseInt(numbers[1]);

            // Compute the sum of the two numbers
            int sum = num1 + num2;

            // Convert the sum to bytes
            byte[] sumBytes = ("" + sum).getBytes();

            // Send the sum back to the client
            DatagramPacket sumPacket = new DatagramPacket(sumBytes, sumBytes.length, packet.getAddress(), packet.getPort());
            socket.send(sumPacket);
        }
    }
}
