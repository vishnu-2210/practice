def duplicate_letters(sentence):
    for word in sentence.split():
        if len(set(word)) != len(word):
            return True
    return False

print(duplicate_letters("hello world"))
print(duplicate_letters("cat dog pig"))
