import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        HashMap<Integer, Integer> valueIndexMap = new HashMap<>();
        for (int iteratedNumber : nums) {
            if (valueIndexMap.containsKey(target - iteratedNumber)) {
                return new int[] { valueIndexMap.get(target - iteratedNumber), i };
            }
            valueIndexMap.put(iteratedNumber, i);
            i++;
        }
        return new int[0];
    }
}