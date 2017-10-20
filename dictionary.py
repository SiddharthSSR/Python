def count(string):
    counts = {}

    for char in string:
        if char in counts:
            print(char)
            break
        else:
            counts[char] = 1
    print('Done')
count('ABCDEFAB')
