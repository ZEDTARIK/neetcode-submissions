class Solution {
    public int search(int[] nums, int target) {
        index index = Arrays.binarySearch(nums, target);
        return index > 0 ? index : -1;

    }
}
