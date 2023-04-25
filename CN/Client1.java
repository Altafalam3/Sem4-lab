import java.io.*;
import java.net.*;

public class Client1 {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("localhost", 8888);
        System.out.println("Connected to server.");

        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
        String userInput;
        while ((userInput = stdIn.readLine()) != null) {
            // Split the user input into two numbers
            String[] numbers = userInput.split(" ");
            int num1 = Integer.parseInt(numbers[0]);
            int num2 = Integer.parseInt(numbers[1]);

            // Send the two numbers to the server
            out.println(num1 + " " + num2);

            // Receive the sum from the server and print it
            String sum = in.readLine();
            System.out.println("Sum of " + num1 + " and " + num2 + " is " + sum);
        }

        out.close();
        in.close();
        stdIn.close();
        socket.close();
        System.out.println("Disconnected from server.");
    }
}
