class Solution {
    public int compress(char[] chars) {
        int i = 0,res =0;
        while(i<chars.length){
            int c = 1;
            while (i+c<chars.length && chars[i+c]==chars[i]) c++;
            chars[res++] = chars[i];
            if(c>1){
                for (char ch:Integer.toString(c).toCharArray()) chars[res++]=ch;
            }
            i+=c;
        }
        return res;
    }
}