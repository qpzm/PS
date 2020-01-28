def main():
    size = int(input())
    evens = [num for num in range(1, size + 1) if num % 2 == 0]
    odds = [num for num in range(1, size + 1) if num % 2 != 0]

    if size % 6 == 2:
        odds[0:2] = [3, 1]
        odds.append(odds.pop(2))
    elif size % 6 == 3:
        del odds[0:2]
        odds += [1, 3]
        evens.append(evens.pop(0))

    for x in evens + odds:
        print(x)


if __name__ == "__main__":
    main()
