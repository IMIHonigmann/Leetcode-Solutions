import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        // Initialize and fill a frequency Table for all values
        HashMap<Integer, Integer> frequencyTable = new HashMap<>();

        for(int i=0 ; i < nums.length ; i++) {

            if(frequencyTable.containsKey(nums[i])) {
                int newValue = frequencyTable.get(nums[i]) + 1;
                frequencyTable.put(nums[i], newValue);
            }
            else {
                frequencyTable.put(nums[i], 1);
            }
        }

        //Takes the value with the highest frequency, deletes it from the hashmap and then it does it again depending on the amount k
        int[] finalArray = new int[k];
        for(int i=0; i<k; i++)
        {
            int lastBiggestValue = 0;
            int correspondingKey = -1;
            for(Map.Entry<Integer,Integer> entry : frequencyTable.entrySet()) {
                if(entry.getValue() > lastBiggestValue) {
                    lastBiggestValue = entry.getValue();
                    correspondingKey = entry.getKey();
                }
            }
            finalArray[i] = correspondingKey;
            frequencyTable.remove(correspondingKey);
        }
        
        return finalArray;
    }
}