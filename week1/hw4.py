w = int(input())
x = int(input())
y = int(input())
z = int(input())
nums = []
nums.append(w)
nums.append(x)
nums.append(y)
nums.append(z)
nums.sort()
for i in range(0, 4):
    print(nums[i], end=' ')
