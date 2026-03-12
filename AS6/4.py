def word_frequency(text):
    words = text.split()
    freq = {}
    for w in words:
        w = w.lower()
        freq[w] = freq.get(w, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    top5 = dict(sorted_items[:5])
    total = len(words)
    proportion = sum(top5.values()) / total * 100

    print("Top 5:", top5)
    print("Total number of words:", total)
    print(f"Proportion of 5 most common words: {sum(top5.values())} / {total} = {proportion:.2f}%")

# Example usage
text = "the world is mine the world is out the world"
word_frequency(text)
