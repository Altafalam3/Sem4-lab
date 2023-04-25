import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException {
        // create a socket and connect to the server on port 8888
        Socket socket = new Socket("localhost", 8888);
        System.out.println("Connected to server.");

        // create input and output streams for the socket
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

        // read input from user and send to the server
        BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
        String userInput;
        while ((userInput = stdIn.readLine()) != null) {
            out.println(userInput);
            System.out.println("Server says: " + in.readLine());
        }

        // close the connection
        out.close();
        in.close();
        stdIn.close();
        socket.close();
        System.out.println("Disconnected from server.");
    }
}

