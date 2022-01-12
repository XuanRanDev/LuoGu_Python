if __name__ == '__main__':
    n = int(input())
    num = 0
    for i in range(10000, 30000 + 1):
        mp = [int(i / 10000), int(i / 1000) % 10, int(i / 100) % 10, int(i / 10) % 10, i % 10]
        m1 = mp[0] * 100 + mp[1] * 10 + mp[2]
        m2 = mp[1] * 100 + mp[2] * 10 + mp[3]
        m3 = mp[2] * 100 + mp[3] * 10 + mp[4]
        # print(m1,m2,m3)
        if m1 % n == 0 and m2 % n == 0 and m3 % n == 0:
            print(i)
            num += 1

    if num == 0:
        print("No")
