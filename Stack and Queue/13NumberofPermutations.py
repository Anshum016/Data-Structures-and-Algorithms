def is_valid(num):
    str_num = str(num)
    perms = []

    # Generate all permutations manually
    def permute(s, chosen):
        if not s:
            perms.append(int(chosen))
        else:
            for i in range(len(s)):
                permute(s[:i] + s[i+1:], chosen + s[i])

    permute(str_num, "")

    # Check if all permutations are >= num
    return all(p >= num for p in perms)

def count_valid_numbers(n):
    count = 0
    for num in range(1, n + 1):
        if is_valid(num):
            count += 1
    return count

n = int(input("Enter n: "))
print("Count:", count_valid_numbers(n))
