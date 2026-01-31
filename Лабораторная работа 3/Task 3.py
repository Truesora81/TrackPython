def count_letters(text: str) -> dict:
    letters_count = {}

    for ch in text.lower():
        if ch.isalpha():
            letters_count[ch] = letters_count.get(ch, 0) + 1

    return letters_count

def calculate_frequency(letters_count: dict) -> dict:
    total_letters = sum(letters_count.values())
    if total_letters == 0: 
        return letters_count

    frequencies = {}
    for letter, count in letters_count.items():
        frequencies[letter] = count / total_letters

    return frequencies

if __name__ == "__main__":

    main_str = """
      У лукоморья дуб зелёный;
      Златая цепь на дубе том:
      И днём и ночью кот учёный
      Всё ходит по цепи кругом;
      Идёт направо — песнь заводит,
      Налево — сказку говорит.
      Там чудеса: там леший бродит,
      Русалка на ветвях сидит;
      Там на неведомых дорожках
      Следы невиданных зверей;
      Избушка там на курьих ножках
      Стоит без окон, без дверей;
      Там лес и дол видений полны;
      Там о заре прихлынут волны
      На брег песчаный и пустой,
      И тридцать витязей прекрасных
      Чредой из вод выходят ясных,
      И с ними дядька их морской;
      Там королевич мимоходом
      Пленяет грозного царя;
      Там в облаках перед народом
      Через леса, через моря
      Колдун несёт богатыря;
      В темнице там царевна тужит,
      А бурый волк ей верно служит;
      Там ступа с Бабою Ягой
      Идёт, бредёт сама собой,
      Там царь Кащей над златом чахнет;
      Там русский дух… там Русью пахнет!
      И там я был, и мёд я пил;
      У моря видел дуб зелёный;
      Под ним сидел, и кот учёный
      Свои мне сказки говорил.
      """

    counts = count_letters(main_str)
    freqs = calculate_frequency(counts)

    for letter, freq in sorted(freqs.items()): 
        print(f"{letter}: {round(freq, 2)}")
