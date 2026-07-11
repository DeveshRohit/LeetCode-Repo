class Solution {
    public int removeElement(int[] nums, int val) {
        int k=0;
        for(int i=0; i<nums.length; i++) {
            if(nums[i] == val) {
                for(int j=nums.length-1; j>i; j--)
                {
                    if(nums[j] != val)
                    {
                        nums[i] = nums[j];
                        nums[j] = val;
                        k++;
                        break;
                    }
                }
            }
            else
                k++;
        }
        return k;
    }
}