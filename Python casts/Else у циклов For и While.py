# else clause

for i in range(5):
    if i == 2:
        print(i)
        break
else:
    print('The end')


Flag = False
for i in range(7):
    if i == 6:
        Flag = True
        break

if Flag:
    print('Six was found')