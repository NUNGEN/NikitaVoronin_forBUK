def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count_without_spaces = len(text.replace(" ", ""))
    longest_word = max(words, key=len)
    
    return word_count, char_count_without_spaces, longest_word

text = "Codingggg  makes our life way better for..."
word_count, char_count_without_spaces, longest_word = analyze_text(text)

print(f"Words: {word_count}")
print(f"Characters without spaces: {char_count_without_spaces}")
print(f"Longest word: \"{longest_word}\"")
