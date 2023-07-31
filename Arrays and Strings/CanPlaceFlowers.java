class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int max=0;
        if(flowerbed.length==1){
            if(flowerbed[0]==1){
                return n<1;
            }
            else{
                return n<=1;
            }
        }
        for(int i=0;i<flowerbed.length;i++){
            if(i==0){
                if(flowerbed[i]==0 && flowerbed[i+1]==0) {
                    flowerbed[i]=1;max++;
                }
            }
            else if(i==flowerbed.length-1){
                if(flowerbed[i]==0 && flowerbed[i-1]==0) {
                    flowerbed[i]=1;max++;
                }
            }
            else{
                if(flowerbed[i]==0 && flowerbed[i-1]==0 && flowerbed[i+1]==0) {flowerbed[i]=1;max++;}
            }
        }
        if(max<n) return false;
        return true;
    }
}