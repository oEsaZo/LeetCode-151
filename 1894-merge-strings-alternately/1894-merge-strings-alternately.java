class Solution {
    public String mergeAlternately(String word1, String word2) {
        char[] a1 = word1.toCharArray();
        char[] a2 = word2.toCharArray();
        StringBuilder sb = new StringBuilder();
        int i = 0;
        int j = 0;
        int m = word1.length();
        int n = word2.length();
        while (i < m || j < n){
            if (i < m) sb.append(word1.charAt(i++));        
            if (j < n) sb.append(word2.charAt(j++));    
        }
        return sb.toString();
    }
}