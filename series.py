#Series

nums = input('Enter the numbers: ')
sub_s = int(input('Enter the length of outputs: '))

for i in range((len(nums) - sub_s) + 1):
    if i + (sub_s - 1) < len(nums):
        print (nums[i : (i + sub_s)])