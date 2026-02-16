def analyze_text(text):
    # 1. Normalize text: lowercase and remove punctuation
    punctuation = '.,!?:;"()'
    cleaned = text.lower()
    for p in punctuation:
        cleaned = cleaned.replace(p, "")

    words = cleaned.split()

    # 2. Count occurrences
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # 3. Unique word count
    unique_count = len(word_counts)

    # 4. Words appearing more than once
    repeated_words = sorted([w for w, c in word_counts.items() if c > 1])

    # 5. Palindrome words
    palindromes = sorted([w for w in word_counts if w == w[::-1]])

    # 6. Return results
    return {
        "unique_count": unique_count,
        "repeated_words": repeated_words,
        "palindromes": palindromes
    }
