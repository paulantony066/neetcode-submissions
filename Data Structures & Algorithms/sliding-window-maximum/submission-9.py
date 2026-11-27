class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        result = []

        # Initialize first window
        for i in range(k):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        result.append(max(freq))

        # Slide window
        for i in range(k, len(nums)):
            # Remove outgoing element
            left = nums[i-k]
            freq[left] -= 1

            if freq[left] == 0:
                del freq[left]

            # Add incoming element
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            result.append(max(freq))

        return result