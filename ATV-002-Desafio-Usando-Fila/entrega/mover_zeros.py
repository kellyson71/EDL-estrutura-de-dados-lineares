from collections import deque


def mover_zeros(nums):
    fila = deque()
    zeros = 0

    for n in nums:
        if n == 0:
            zeros += 1
        else:
            fila.append(n)

    i = 0
    while fila:
        nums[i] = fila.popleft()
        i += 1

    while zeros > 0:
        nums[i] = 0
        i += 1
        zeros -= 1


if __name__ == "__main__":
    for nums in ([0, 1, 0, 3, 12], [0], [1, 2, 3], [0, 0, 0], []):
        print(nums, end=" -> ")
        mover_zeros(nums)
        print(nums)
