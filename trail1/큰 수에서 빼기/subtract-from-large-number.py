inp = input()
nums = inp.split()

a = int(nums[0])
b = int(nums[1])

if a > b:
    print(a - b)

if b >= a:
    print(b - a)