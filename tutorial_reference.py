# tutorial code
print("tutorial code")


def reverse(n):
    # to point first item
    start_index = 0
    end_index = len(n) - 1

    while end_index > start_index:
        # swapping the items
        n[start_index], n[end_index] = n[end_index], n[start_index]
        start_index += 1
        end_index -= 1


if __name__ == "__main__":

    n = [-1, 3, -5, 8, 9, 7, 2]
    print(f"before reversing:- {n}")
    reverse(n)
    print(f"after reversing:- {n}")
