height = int(input("Enter the number of rows you want on your holiday tree: "))
spaces = height - 1
hashes = height - spaces
count = 0

if height != 0:
    while count < height:
        print(" " * spaces, "#" * hashes)
        spaces -= 1
        hashes += 2
        count += 1

spaces = height - 1
hashes = height - spaces
print(" " * spaces, "#" * hashes)
print()
print("Happy Holidays!")