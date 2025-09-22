string = input()
target_unicode = int(input())

counter = 0

for char in string:
    unicode_value = ord(char)
    # Convert both to lowercase for case-insensitive comparison
    if chr(unicode_value).lower() == chr(target_unicode).lower():
        counter += 1
print(counter)