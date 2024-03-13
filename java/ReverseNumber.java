import java.util.Scanner;

public class ReverseNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input number from user
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        // Reverse the number using a for loop
        int reverse = 0;
        for (int i = number; i != 0; i /= 10) {
            int digit = i % 10;
            reverse = reverse * 10 + digit;
        }

        // Display the reverse of the number
        System.out.println("Reverse of the number: " + reverse);

        scanner.close();
    }
}
