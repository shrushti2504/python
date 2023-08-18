sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]
output = []
counts = {}
for word_trees in sentences:
    words = word_trees.split()
    output.append(words)
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word]=1
output2 = {word:count for word,count in counts.items()}

print(output)
print(output2)

