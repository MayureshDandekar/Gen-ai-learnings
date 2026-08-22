def capitalize_words(text):
    string = []
    for i in text.split(" "):
        string.append(i.capitalize())
    return " ".join(string)

c_string = capitalize_words("mayuresh is gettin better in coding")
print(c_string)                                                                    


def reverse_string(text):
    # return text[::-1]
    word= text.split(" ")
    word.reverse()
    return " ".join(word) 

r_string = reverse_string("mayuresh is gettin better in coding")
print(r_string)


def word_count(text):
    words = text.split(" ")
    return f"The number of words in text is {len(words)}"

count = word_count("mayuresh is gettin better in coding")
print(count)