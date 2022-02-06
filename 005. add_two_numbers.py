# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# works with array
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         # l1_reversed_int = 0
#         # l2_reversed_int = 0
#         max_len = max(len(l1), len(l2))
#         output_array = []
#         latest_carry = 0
#         for i in range(0, max_len):

#             if i > (len(l1) - 1):
#                 output_array += [(l2[i] + latest_carry) % 10]
#                 if l2[i] + latest_carry < 10:
#                     latest_carry = 0
#                 else:
#                     if i == max_len - 1:
#                         output_array += [1]


#             elif i > (len(l2) - 1):
#                 output_array += [(l1[i] + latest_carry) % 10]
#                 if l1[i] + latest_carry < 10:
#                     latest_carry = 0
#                 else:
#                     if i == max_len - 1:
#                         output_array += [1]

#             else:
#                 output_array += [(l1[i] + l2[i] + latest_carry) % 10]

#                 if (l1[i] + l2[i] + latest_carry) >= 10:
#                     latest_carry = 1
#                 else:
#                     latest_carry = 0
#         return output_array


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next

print(Solution().addTwoNumbers([1,2,3],[3,2,1]))
print(Solution().addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
print(Solution().addTwoNumbers([0],[0]))
