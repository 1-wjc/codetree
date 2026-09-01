inp = input()
nums = inp.split()

h = int(nums[0])
w = int(nums[1])

b = (10000 * w) / (h ** 2)

print(int(b))

if b >= 25:
    print("Obesity")