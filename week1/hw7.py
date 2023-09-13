nums = list(map(int, input().split(',')))
# for循环
renums1 = []
for i in nums[::-1]:
    renums1.append(i)
print(renums1)
# while循环
renums2 = []
i = len(nums) - 1
while i >= 0:
    renums2.append(nums[i])
    i -= 1
print(renums2)