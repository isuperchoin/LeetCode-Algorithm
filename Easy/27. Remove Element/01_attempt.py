class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        #nums 리스트를 순회한다
        #각 원소를 val과 비교한다
        #만약 val과 다르다면 맨 앞 원소로 밀고 카운트를 올린다
        #만약 같다면 '_'로 치환한다
        #최종적으로 카운트 리턴

        pointer = 0
        count = 0

        for i in nums:
            if i != val:
                nums[pointer] = i
                pointer += 1
                count += 1
            else: nums[nums.index(i)] = '_'

        return count


        