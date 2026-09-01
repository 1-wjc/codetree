inp = input()
nums = inp.split()

a = int(nums[0])
b = int(nums[1])
c = int(nums[2])

total = a + b + c
mean = total / 3

print(total)
print(int(mean))
print(int(total - mean))