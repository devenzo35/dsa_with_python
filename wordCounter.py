# word counter


text = "a text which has six words            "
text.strip()  # * strip() does not mutate the variable (text)
stripText = (
    text.strip()
)  # * assigning to a new variable is the correcto way of using it
splitText = stripText.split(" ")
print(splitText)


def wordCounter():
    count = 0
    for _, elem in enumerate(splitText):
        if len(elem) >= 1:
            count += 1

    return count


print(wordCounter())
