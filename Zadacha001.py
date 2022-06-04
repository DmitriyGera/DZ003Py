nums = [3, 1, 2, 3, 4, 6, 1, 7]
def get_up2(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up2(nums))