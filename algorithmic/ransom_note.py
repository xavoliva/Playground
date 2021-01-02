import collections


def check_magazine(magazine, note):
    if not note or not magazine:
        return False

    if len(magazine) < len(note) or set(magazine) < set(note):
        return False

    m = collections.Counter(magazine)
    n = collections.Counter(note)

    for word in n:
        if n[word] > m[word]:
            return False

    return True


if __name__ == '__main__':

    magazine = "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg"\
        .split()
    note = "elo lxkvg bg mwz clm w".split()

    result = check_magazine(magazine, note)

    print(result)
