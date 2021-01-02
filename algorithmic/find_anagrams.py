example_list = ["elvis", "restful", "fluster", "lives",
                "whatever", "some", "other", "veils", "elvis"]


def charge_list(word_List):
    """
    Charge list into a dictionary, where keys are words in lowercase
    and values are the words sorted alphabetically
    """
    word_dict = {}
    for word in word_List:
        word_dict[word.lower()] = "".join(sorted(word)).lower()

    return word_dict


def find_anagrams(word, word_dict):
    """
    Find all keys (words) with the same value
    """

    if word in word_dict:
        sorted_word = "".join(sorted(word))
        result_list = []

        for key in word_dict:
            if word_dict[key] == sorted_word:
                result_list.append(key)

        # remove actual word, since it is not considered anagram of himself
        result_list.remove(word)
        return result_list

    return []


def main():

    word_dict = charge_list(example_list)
    print("List successfully charged")
    print("Type enter key to finish program.")
    print("")
    input_word = "..."

    while True:
        input_word = input("Enter word: ").lower()
        if not input_word:
            break
        print(find_anagrams(input_word, word_dict))


if __name__ == "__main__":
    main()
