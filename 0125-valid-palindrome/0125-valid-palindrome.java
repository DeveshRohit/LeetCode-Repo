class Solution {
    public boolean isPalindrome(String s) {
        boolean flag = true;
        s = s.toLowerCase();
        for(int i=0, j=s.length()-1; i<=j;)
        {
            if(Character.isLetterOrDigit(s.charAt(i)) && Character.isLetterOrDigit(s.charAt(j))) {
                if(s.charAt(i) != s.charAt(j)) {
                    flag = false;
                    break;
                }
                i++;
                j--;
            }
            else if(!Character.isLetterOrDigit(s.charAt(i)))
                i++;
            else if(!Character.isLetterOrDigit(s.charAt(j)))
                j--;
        }
        return flag;
    }
}