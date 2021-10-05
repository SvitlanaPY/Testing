def nitro_salt(m):
    # print(10 * m / 1000)
    try:
        m = int(m)
    except:
        m = 0
    return int(10 * m / 1000)

# print(nitro_salt(1500))
