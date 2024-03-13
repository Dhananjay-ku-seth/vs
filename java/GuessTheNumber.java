import java.util.Scanner;
import java.util.Random;

public class GuessTheNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        int lowerBound = 1;
        int upperBound = 100;
        int maxAttempts = 7; // Decreased number of attempts
        
        boolean playAgain = true;
        int totalAttempts = 0;
        int roundsWon = 0;

        while (playAgain) {
            int targetNumber = random.nextInt(upperBound - lowerBound + 1) + lowerBound;
            int attempts = 0;
            
            System.out.println("Guess the number between " + lowerBound + " and " + upperBound + ".");
            
            while (attempts < maxAttempts) {
                System.out.print("Enter your guess: ");
                int userGuess = scanner.nextInt();
                attempts++;
                
                if (userGuess < targetNumber) {
                    System.out.println("Too low! Try again.");
                } else if (userGuess > targetNumber) {
                    System.out.println("Too high! Try again.");
                } else {
                    System.out.println("Congratulations! You've guessed the number " + targetNumber + " correctly in " + attempts + " attempts.");
                    totalAttempts += attempts;
                    roundsWon++;
                    break;
                }
            }
            
            if (attempts == maxAttempts) {
                System.out.println("Sorry, you've reached the maximum number of attempts. The correct number was: " + targetNumber);
            }
            
            System.out.print("Do you want to play again? (yes/no): ");
            String playChoice = scanner.next();
            playAgain = playChoice.equalsIgnoreCase("yes");
        }
        
        scanner.close();
        
        System.out.println("Game Over! Total rounds played: " + roundsWon + ", Rounds won: " + roundsWon + ", Average attempts per round: " + (totalAttempts / (double) roundsWon));
    }
}
