nums = [50, 60, 70, 80, 90, 100]

nums.append(110)
print(nums) # Imprime: [50, 60, 70, 80, 90, 100, 110]

nums.insert(1, 55)
print(nums) # Imprime: [50, 55, 60, 70, 80, 90, 100, 110]

nums.remove(80)
print(nums) # Imprime: [50, 55, 60, 70, 90, 100]

nums = nums[::-1]
nums.sort(reverse=True)
nums
print(nums) # Imprime: [50, 55, 60, 70, 90, 100]