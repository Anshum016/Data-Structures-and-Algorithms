  
def calculate_common(a, b, c):
    i, j, k = 0, 0, 0  # Initialize pointers
    last_common = None  # To avoid duplicate common elements
    common_elements = []  # List to store common elements

    # Traverse all three arrays
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] == c[k]:  # If all three elements are equal
            if a[i] != last_common:  # Avoid duplicates
                common_elements.append(a[i])
                last_common = a[i]
            # Move all pointers forward
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:  # Move pointer i if A[i] is the smallest
            i += 1
        elif b[j] < c[k]:  # Move pointer j if B[j] is the smallest
            j += 1
        else:  # Move pointer k if C[k] is the smallest
            k += 1

    return common_elements

# Test the function
a = [1, 5, 10, 20, 30]
b = [5, 13, 15, 20]
c = [5, 20]

print("Our Answer is", calculate_common(a, b, c))
