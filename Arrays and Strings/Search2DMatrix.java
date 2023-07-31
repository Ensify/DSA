class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int R = matrix.length, C = matrix[0].length;
        int l = 0, r = R*C -1,mid;
        while(l<=r){
            mid = (l+r)/2;
            if(matrix[mid/C][mid%C]<target) l = mid+1;
            else if(matrix[mid/C][mid%C]>target) r = mid-1;
            else return true;
        }
        return false;
    }
}