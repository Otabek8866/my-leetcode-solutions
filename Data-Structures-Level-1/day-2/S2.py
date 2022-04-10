class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Slution 1
        # for i in range(len(nums2)):
        #     nums1[m+i] = nums2[i]
        # nums1.sort()

        # Slution 1
        nums1[m:] = []
        i = 0
        j = 0
        while j < n and i < m + j:
            if nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                print("len:", len(nums1))
                j += 1
                i += 1
            else:
                i += 1
        nums1.extend(nums2[j:])
