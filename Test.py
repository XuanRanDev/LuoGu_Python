if __name__ == '__main__':
    i = 20207
    mp = []
    mp.append(int(i / 10000))
    mp.append(int(i / 1000) % 10)
    mp.append(int(i / 100) % 10)
    mp.append(int(i / 10) % 10)
    mp.append(i % 10)
    print(mp)
    print(mp[0] * 100 + mp[1] * 10 + mp[2])
    print(mp[1] * 100 + mp[2] * 10 + mp[3])
    print(mp[2] * 100 + mp[3] * 10 + mp[4])

    # print(int(i / 1000) % 10)
