class Solution {
public:
    bool isValid(string s) {
        stack<char> check_text; bool checking = false;
        int size_text = s.size();
        for (int i = 0; i <= size_text; i++)
        {
            check_text.push(s[i]);
        }
        char left[3] = {'(', '[', '{'}; char right[3] = {')', ']', '}'};
        
        return checking;
    }
};