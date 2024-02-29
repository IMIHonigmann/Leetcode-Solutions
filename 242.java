import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> letterCounter = new HashMap<>();
        HashMap<Character, Integer> letterCounterT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (letterCounter.containsKey(s.charAt(i))) {
                int counter = letterCounter.get(s.charAt(i)) + 1;
                letterCounter.put(s.charAt(i), counter);
            } else {
                letterCounter.put(s.charAt(i), 1);
            }

        }

        for (int i = 0; i < t.length(); i++) {
            if (letterCounterT.containsKey(t.charAt(i))) {
                int counter = letterCounterT.get(t.charAt(i)) + 1;
                letterCounterT.put(t.charAt(i), counter);
            } else {
                letterCounterT.put(t.charAt(i), 1);
            }

        }

        // System.out.println(letterCounter);
        // System.out.println(letterCounterT);

        if (letterCounter.equals(letterCounterT)) {
            return true;
        } else {
            return false;
        }
    }
}