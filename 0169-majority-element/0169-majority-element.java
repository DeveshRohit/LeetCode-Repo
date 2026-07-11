class Solution {
    public int majorityElement(int[] nums) {
        for(int i=0; i<nums.length; i++)
        {
            int c = 1, num = nums[i];
            for(int j=i+1; j<nums.length; j++)
            {
                if(nums[j] == num)
                    c++;
            }
            if(c > nums.length/2) {
                return num;
            }
        }
        return -1;
    }
}