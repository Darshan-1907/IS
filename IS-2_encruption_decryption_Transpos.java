import java.util.Scanner;

public class TranspositionCipher {
    
    // Encrypt the plaintext using the transposition cipher technique
    public static String encrypt(String text, int key) {
        // Create a matrix with 'key' columns
        char[][] matrix = new char[(int) Math.ceil(text.length() / (double) key)][key];
        
        // Fill the matrix with the text
        int k = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < key; j++) {
                if (k < text.length()) {
                    matrix[i][j] = text.charAt(k++);
                } else {
                    matrix[i][j] = 'X'; // Filling with 'X' if there's any empty space
                }
            }
        }
        
        // Read the matrix column by column to form the ciphertext
        StringBuilder ciphertext = new StringBuilder();
        for (int j = 0; j < key; j++) {
            for (int i = 0; i < matrix.length; i++) {
                ciphertext.append(matrix[i][j]);
            }
        }
        
        return ciphertext.toString();
    }
    
    // Decrypt the ciphertext using the transposition cipher technique
    public static String decrypt(String ciphertext, int key) {
        // Calculate the number of rows
        int numRows = (int) Math.ceil(ciphertext.length() / (double) key);
        char[][] matrix = new char[numRows][key];
        
        // Fill the matrix column by column with the ciphertext
        int k = 0;
        for (int j = 0; j < key; j++) {
            for (int i = 0; i < numRows; i++) {
                if (k < ciphertext.length()) {
                    matrix[i][j] = ciphertext.charAt(k++);
                }
            }
        }
        
        // Read the matrix row by row to get the decrypted text
        StringBuilder decryptedText = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < key; j++) {
                if (matrix[i][j] != 'X') {
                    decryptedText.append(matrix[i][j]);
                }
            }
        }
        
        return decryptedText.toString();
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input message and key
        System.out.print("Enter the message: ");
        String message = scanner.nextLine();
        System.out.print("Enter the key (number of columns): ");
        int key = scanner.nextInt();
        
        // Encryption
        String encrypted = encrypt(message, key);
        System.out.println("Encrypted Message: " + encrypted);
        
        // Decryption
        String decrypted = decrypt(encrypted, key);
        System.out.println("Decrypted Message: " + decrypted);
        
        scanner.close();
    }
}
