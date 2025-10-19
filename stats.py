def get_num_words(content):
    return len(content.split())


def get_freq_chars(content):
    num_chars = {}
    for ch in content:
        lower_ch = ch.lower()
        if lower_ch in num_chars:
            num_chars[lower_ch] += 1
        else:
            num_chars[lower_ch] = 1
    return num_chars


def sort_chars(chars_freq):
    chars_count = []
    for ch, count in chars_freq.items():
        chars_count.append({"char": ch, "num": count})
    chars_count.sort(reverse=True, key=lambda x: x["num"])
    return chars_count
