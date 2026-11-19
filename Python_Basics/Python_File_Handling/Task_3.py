#Count how many times each word appears in a file
print("\nCounting how many times each word appears in an opened file.")
file = open("data.txt", "r")
text = file.read()
words = text.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1
print(count)
file.close()


