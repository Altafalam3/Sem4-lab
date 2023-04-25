import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8888);
        System.out.println("Server started. Listening on port 8888.");

        while (true) {
            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected.");

            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                System.out.println("Client says: " + inputLine);
                out.println("Server received: " + inputLine);
            }

            out.close();
            in.close();
            clientSocket.close();
            System.out.println("Client disconnected.");
        }
    }
}
