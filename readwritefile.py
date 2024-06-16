# to open file and close automatically
with open('readwrite', 'r') as reader:
    content = reader.readlines()
    #print(content)
    reversed(content)
    with open('readwrite', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
