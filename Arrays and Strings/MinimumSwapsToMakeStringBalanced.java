class Solution {
    public int minSwaps(String s) {
        int max = 0, extra = 0;
        for(char c: s.toCharArray()){
            if(c==']') extra++;
            else extra--;
            max = extra>max?extra:max;
        }
        return (max+1)/2;
    }
}