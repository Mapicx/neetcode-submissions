class Solution {
public:
    bool isPalindrome(string s) {
        if(s.size() == 0) return true;
        if(s.size() == 1) return true;
        string palindrome_check;
        for(int i = 0; i < s.size(); i++)
        {
            if (isalnum(s[i])) 
            {
                palindrome_check.push_back(tolower(s[i]));
            }
        }

        int left = 0;
        int right = palindrome_check.size() - 1;

        while(left < right)
        {
            if(palindrome_check[left] != palindrome_check[right])
            {
                return false;
            }
            right--;
            left++;
            
        }
        return true;
    }
};
