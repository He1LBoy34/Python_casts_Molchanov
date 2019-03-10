# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass

def calc(m):
    # 1000 : 10 = m : x
    try:
        m = int(m)
    except:
        m = 0
    return 10 * m / 1000

print(calc(1000))

def calc2(m):
    # 1000 : 10 = m : x
    try:
        m = int(m)
    except  Exception:
        print('Something went wrong')
    else:
        return 10 * m / 1000
    finally:
        print('Hello')  # этот блок выполняется в любом случае

print(calc2(1000))