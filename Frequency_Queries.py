def x(nums,k):
    left = 0
    right = 0
    maxi = 1
    current_zero_count = 0
    while right < len(nums) :
        if nums[right] == 0:
            current_zero_count += 1
        while current_zero_count > k:
            if nums[left] == 0:
                current_zero_count -= 1
            left += 1
        maxi = max(maxi,right - left +1)
        right += 1
    return maxi


if __name__ == "__main__":
    print(x([1,1,1,0,0,0,1,1,1,1,0],2))