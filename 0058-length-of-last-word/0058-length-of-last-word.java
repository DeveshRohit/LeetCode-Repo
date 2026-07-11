class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        String w[]=s.split(" ");
        return w[w.length-1].length();
    }
}