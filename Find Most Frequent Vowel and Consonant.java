// 3541. Find Most Frequent Vowel and Consonant

// You are given a string s consisting of lowercase English letters ('a' to 'z').

// Your task is to:

// Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
// Find the consonant (all other letters excluding vowels) with the maximum frequency.
// Return the sum of the two frequencies.

// Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

// The frequency of a letter x is the number of times it occurs in the string.
 

// Example 1:

// Input: s = "successes"

// Output: 6

// Explanation:

// The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
// The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
// The output is 2 + 4 = 6.
// Example 2:

// Input: s = "aeiaeia"

// Output: 3

// Explanation:

// The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
// There are no consonants in s. Hence, maximum consonant frequency = 0.
// The output is 3 + 0 = 3.

// Code: Java 
import java.util.*;

class Solution {

    public int maxFreqSum(String s) {
        HashMap<Character, Integer> hm = new HashMap<>();

        // Count frequencies of each character
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            hm.put(ch, hm.getOrDefault(ch, 0) + 1);
        }

        int maxVowelCount = 0;
        int maxConsonantCount = 0;

        // Iterate over map entries
        for (Map.Entry<Character, Integer> e : hm.entrySet()) {
            char ch = e.getKey();
            int freq = e.getValue();

            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                maxVowelCount = Math.max(maxVowelCount, freq);
            } else {
                maxConsonantCount = Math.max(maxConsonantCount, freq);
            }
        }

        return maxVowelCount + maxConsonantCount;
    }

    // (Optimized)
    public int maxFreqSum1(String s) {
        int[] freq = new int[26]; // frequency of each lowercase letter

        // Count frequencies
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch >= 'a' && ch <= 'z') { // ensure lowercase
                freq[ch - 'a']++;
            }
        }

        int maxVowelCount = 0;
        int maxConsonantCount = 0;

        // Check vowels and consonants
        for (int i = 0; i < 26; i++) {
            int count = freq[i];
            if (count == 0) continue;

            char ch = (char) (i + 'a');

            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                maxVowelCount = Math.max(maxVowelCount, count);
            } else {
                maxConsonantCount = Math.max(maxConsonantCount, count);
            }
        }

        return maxVowelCount + maxConsonantCount;
    }
}