class Solution {
    public int search(int[] nums, int target) {
        int l=0, u=nums.length-1, mid=(u+l)/2;
        // boolean flag=false;
        while(u>=l) {
            mid = (u+l)/2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] > target)
                u = mid-1;
            else if(nums[mid] < target)
                l = mid+1;
        }
        return -1;
    }
}