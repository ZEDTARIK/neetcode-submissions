class Solution {
    public int search(int[] nums, int target) {
         index = Arrays.binarySearch(nums, target);
        return index > 0 ? index : -1;

    }
}
