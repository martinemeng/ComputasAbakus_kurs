n = 10  # Total number of lines for the pyramid

for i in range(n):
    # Print leading spaces
    print(" " * (n - i - 1), end="")
    # Print '#' characters with spaces in between
    print("# " * (i + 1))