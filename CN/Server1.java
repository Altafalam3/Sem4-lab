import java.io.*;
import java.net.*;

public class Server1 {
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
                // Split the input line into two numbers
                String[] numbers = inputLine.split(" ");
                int num1 = Integer.parseInt(numbers[0]);
                int num2 = Integer.parseInt(numbers[1]);
                // Compute the sum and send it back to the client
                int sum = num1 + num2;
                out.println(sum);
            }

            out.close();
            in.close();
            clientSocket.close();
            System.out.println("Client disconnected.");
        }
    }
}
