
# a = [1,1,2,5,5]
#my first solution , number of unique items ber korte parsilam
# i =0
# c =0
# for i in range(len(a)):
#
#         if a[i] in a[i+1:]:
#
#             c = c+1
#
# print(c)
# print(a)
#eita bujchi , eitai dekhbo ,,
# def remove_duplicates(nums):
#     index = 0
#
#     while index < len(nums):
#         num = nums[index]
#         if num in nums[:index]:  # Check if the current element is already encountered
#             nums.pop(index)
#         else:
#             index += 1
#
#
# # Example usage:
# nums = [1, 1, 2, 3,3,4,5,5]
# remove_duplicates(nums)
# print(nums)

#using count method

# def remove_duplicates(nums):
#     index = 0
#
#     while index < len(nums):
#         num = nums[index]
#         if nums.count(num) > 1:
#             nums.remove(num)
#         else:
#             index += 1
#
#
# # Example usage:
# nums = [1, 1, 2, 2, 2, 3]
# remove_duplicates(nums)
# print(nums)

#using a second list

# def remove_duplicates(nums):
#     unique_digits = []
#     index = 0
#
#     while index < len(nums):
#         num = nums[index]
#         if num not in unique_digits:
#             unique_digits.append(num)
#             index += 1
#         else:
#             nums.pop(index)
#
#
# # Example usage:
# nums = [1, 1, 2, 2, 2, 3]
# remove_duplicates(nums)
# print(nums)

#using set
# def count_unique_digits_set(nums):
#     unique_digits_set = set(nums)
#     return len(unique_digits_set), set(nums)
#
# # Example usage:
# nums = [1, 1, 2, 3, 3, 4, 5, 5]
# result_set = count_unique_digits_set(nums)
# print(result_set)
