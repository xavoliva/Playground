def nr_elements_in_common(a, b):
    return len(set(a) & set(b))


if __name__ == "__main__":
    a = [13, 27, 35, 40, 49, 55, 59]
    b = [17, 35, 39, 40, 55, 58, 60]

    nr = nr_elements_in_common(a, b)
    print(nr)
