#!/bin/python3

import collections

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    if not note or not magazine or len(magazine) < len(note) or set(magazine) < set(note):
        print("No")
        return
    m = collections.Counter(magazine)
    n = collections.Counter(note)

    for word in n:
        if n[word] > m[word]:
            # print(word, n[word], m[word])
            print("No")
            return

    print("Yes")


if __name__ == '__main__':

    magazine = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg".split()
    note = "elo lxkvg bg mwz clm w".split()

    checkMagazine(magazine, note)
