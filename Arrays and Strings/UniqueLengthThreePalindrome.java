class Solution {
    public int countPalindromicSubsequence(String s) {
        int count = 0;
        char[] str = s.toCharArray();
        HashSet<Character> chars = new HashSet<>();
        for(Character c: str){
            chars.add(c);
        }

        for(Character c: chars){
            int first = s.indexOf(c);
            int last = s.lastIndexOf(c);
            HashSet<Character> subchars = new HashSet<>();
            for (int i = first+1;i<last;i++){
                subchars.add(s.charAt(i));
            }
            count+=subchars.size();
        }
        return count;
    }
}