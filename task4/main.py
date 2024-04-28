def load_stop_words(filename):
    with open(filename, 'r') as f:
        stop_list = f.read().split()
    return stop_list


def rename_text(text: str, stop_list: list):
    words = text.split()
    result = []
    for word in words:
        result.append(word)
        for stop_word in stop_list:

            new_word = word.lower().replace(stop_word, '*' * len(stop_word))
            if '*' in new_word:
                result.append(new_word)
                result.remove(word)

    return ' '.join(result)


stop_list = load_stop_words('stop_words.txt')
with open('text.txt', 'r') as file:
    text = file.read()
    result_text = rename_text(text, stop_list)
    print(f"Итоговый текст после цензуры:\n{result_text}")
