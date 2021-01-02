# !/bin/python3

def k_length_rotation(s: str):
    for n in range(len(s)):
        s_k = s[n:] + s[:n]
        yield s_k


def longest_palindrome(s: str):
    N = len(s)
    max_pal_length = 0
    print("#" * 10)
    for i in range(N - 1):
        if N - i <= max_pal_length:
            break
        for j in reversed(range(i + 1, N + 1)):
            print(i, j)
            sub = s[i:j]
            if len(sub) <= max_pal_length:
                break
            if sub == sub[::-1]:
                max_pal_length = len(sub)
                print("max", max_pal_length)
                break
    return max_pal_length


def circular_palindromes(s):
    result = []

    for s_k in k_length_rotation(s):
        result.append(longest_palindrome(s_k))

    return result


if __name__ == '__main__':
    s = "aaaaabbbbaaaa"

    result = circular_palindromes(s)

    print('\n'.join(map(str, result)))
