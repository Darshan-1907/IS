public class XORString {
    public static void main(String[] args) {
        // Input string
        String input = "Hello World";
        
        // Convert each character and apply XOR with 127
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < input.length(); i++) {
            // Get the character at the current index
            char ch = input.charAt(i);
            
            // XOR the character with 127 and cast back to char
            char xorChar = (char) (ch ^ 127);
            
            // Append the XORed character to the result
            result.append(xorChar);
        }
        
        // Display the result
        System.out.println("Original String: " + input);
        System.out.println("XORed with 127: " + result.toString());
    }
}
