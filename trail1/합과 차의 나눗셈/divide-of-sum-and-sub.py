inp = input()
nums = inp.split()

a = int(nums[0])
b = int(nums[1])

result = (a + b) / (a - b)

print(f'{result:.2f}')