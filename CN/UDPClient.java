import java.io.*;
import java.net.*;

public class UDPClient {
    public static void main(String[] args) throws IOException {
        DatagramSocket socket = new DatagramSocket();
        InetAddress serverAddress = InetAddress.getByName("localhost");
        int serverPort = 8888;

        BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            // Read in two numbers from the user
            System.out.print("Enter two numbers (separated by a space): ");
            String userInput = stdIn.readLine();
            String[] numbers = userInput.split(" ");
            int num1 = Integer.parseInt(numbers[0]);
            int num2 = Integer.parseInt(numbers[1]);

            // Convert the two numbers to bytes
            byte[] buffer = (num1 + " " + num2).getBytes();

            // Create a datagram packet to send to the server
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length, serverAddress, serverPort);

            // Send the packet to the server
            socket.send(packet);

            // Receive the sum from the server
            byte[] receiveBuffer = new byte[1024];
            DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
            socket.receive(receivePacket);

            // Convert the sum to a string and print it
            String sum = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Sum of " + num1 + " and " + num2 + " is " + sum);
        }
    }
}
