def foo(text, result):
    with open(text, 'r') as f:
        file = f.read()

        words = file.split()
        print(words)
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        max_count = max(word_count, key=word_count.get)

    with open(result, 'w') as f:
        f.write(f"Самое часто повторяемо слово {max_count}, оно повторяется {word_count[max_count]} раз(а)")


foo("text.txt", "result.txt")