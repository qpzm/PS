def encode(x):
    if not(x):
        return '1'
    else:
        cur, cnt = '', 0
        result = ''
        for letter in x:
            if cur == letter:
                cnt += 1
            else:
                result += f'{cur}{cnt}'
                cur, cnt = letter, 1
        result += f'{cur}{cnt}'
        return result[1:]


def decode(x):
    result = ''
    for i in range(len(x) // 2):
        letter, cnt = x[2 * i], int(x[2 * i + 1])
        result += cnt * letter
    return(result)


def main():
    mode, data = input().split()
    if mode == 'E':
        print(encode(data))
    else:
        print(decode(data))


if __name__ == '__main__':
    main()
