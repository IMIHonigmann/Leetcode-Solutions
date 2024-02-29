import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> newHashSet = new HashSet<>();

        for(int i=0; i<nums.length; i++) {
            if(newHashSet.contains(nums[i])) {
                return true;
            }
            newHashSet.add(nums[i]);
        }
        return false;
    }
}