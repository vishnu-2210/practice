def is_shadow_sentence(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()

    if len(words1) != len(words2):
        return False

    for w1, w2 in zip(words1, words2):
        if len(w1) != len(w2):
            return False
        if set(w1) & set(w2):
            return False

    return True

print(is_shadow_sentence("they are round", "fold two times"))
print(is_shadow_sentence("his friends", "our company"))
