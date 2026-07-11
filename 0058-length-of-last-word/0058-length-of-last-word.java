class Solution {
    public int lengthOfLastWord(String s) {
        String w="";
        s = s.trim();
        for(int i=s.length()-1; i>=0; i--)
        {
            char ch = s.charAt(i);
            if(ch == ' ')
                break;
            w = ch + w;
        }
        return w.length();
    }
}