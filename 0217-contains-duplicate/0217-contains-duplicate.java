import java.util.HashSet;
import java.util.stream.Stream;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        return Arrays.stream(nums).distinct().count() < nums.length;
    }
}