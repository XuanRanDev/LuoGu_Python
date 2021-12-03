if __name__ == '__main__':
    E = 250
    data = input().split()
    d = int(data[0])
    day = int(data[1])
    ans = 0

    for i in range(d, d + day):
        if 1 <= i % 7 <= 5:
            ans = ans + E


    print(ans)
