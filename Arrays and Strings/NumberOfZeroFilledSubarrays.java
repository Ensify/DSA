class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long c=0;
        int a=1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                c+=a;
                a++;
            }
            else a=1;
        }
        return c;
    }
}