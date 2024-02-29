class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] resultArray = new int[nums.length];
        int prefixProduct = 1;
        int suffixProduct = 1;

        resultArray[0] = 1;
        resultArray[nums.length-1] = 1;

        for(int i=1;i<nums.length; i++) {
                resultArray[i] = prefixProduct * nums[i-1];
                prefixProduct *= nums[i-1];
        }

        for(int i=nums.length-2;i>=0;i--) {
                resultArray[i] *= suffixProduct * nums[i+1];
                suffixProduct *= nums[i+1];
        }

        return resultArray;
    }
}