'''
647. Palindromic Substrings Medium

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        total_count = 0
        # Loop through each  character
        for i, c in enumerate(s):
            total_count+=self.count_padlindrome(i,i, s)
            total_count+=self.count_padlindrome(i,i+1, s)
            
        return total_count
            
    # Starts at specific location 
    # Counts outward on number of padlindromes
    def count_padlindrome(self, left, right, s):
        count = 0
        while(left>= 0 and right < len(s) and s[left] == s[right]):
            left-=1
            right+=1
            count+=1
        return count
