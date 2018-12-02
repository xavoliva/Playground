

exampleList = ["elvis", "restful", "fluster", "lives", "whatever", "some", "other", "veils", "elvis"]

def charge_List(word_List):
    word_dict = {}
    for word in word_List:
        word_dict[word] = "".join(sorted(word))

    return word_dict

def find_Anagrams(word, word_dict):

    if word in word_dict:
        sortedWord = "".join(sorted(word))
        resultList = []

        for key in word_dict:
            if word_dict[key] == sortedWord:
                resultList.append(key)

        resultList.remove(word)
        return resultList


    else:
        return []


def main():


    word_dict = charge_List(exampleList)
    print("List successfully charged")
    print("Type enter key to finish program.")
    print("")
    input_Word = "..."

    while True:
        
        input_Word = input("Enter word: ")
        if not input_Word:
            break
        print(input_Word)
        print(find_Anagrams(input_Word, word_dict))
    

if __name__ == "__main__":
    main()
