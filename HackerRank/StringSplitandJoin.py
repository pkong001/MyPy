
def split_and_join(line):
    # Step 1: Split the string into words (mimicking `split(" ")`)
    words = []
    current_word = ""
    for char in line:
        if char == " ":  # Detect spaces
            if current_word:  # If there's a word collected, add it
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:  # Add the last word if there is one
        words.append(current_word)

    # Step 2: Join the words with a hyphen (mimicking `"-".join(words)`)
    result = ""
    for i, word in enumerate(words):
        if i > 0:  # Add a hyphen before subsequent words
            result += "-"
        result += word

    return result

if __name__ == '__main__':
    line = "this is a string"
    #result = split_and_join(line)
    result = "-".join(line.split(" "))
    print(result)