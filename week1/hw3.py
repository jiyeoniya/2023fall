x = int(input())
y = int(input())
z = int(input())
nums = []
nums.append(x)
nums.append(y)
nums.append(z)
nums.sort()
for i in range(0, 3):
    print(nums[i], end=' ')
