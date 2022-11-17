# Interview Question #1
#
# The problem is that we want to reverse a T[] array in O(N) linear time complexity
# and we want the algorithm to be in-place as well - so no additional memory can be used!
#
# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

print("my code")


def array_reverse(array):
    iteration_length = int(len(T) / 2)
    for i in range(iteration_length):
        T[i], T[-(i + 1)] = T[-(i + 1)], T[i]


T = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"before reversing:-{T}")
array_reverse(T)
print(f"after reversing:-{T}")



