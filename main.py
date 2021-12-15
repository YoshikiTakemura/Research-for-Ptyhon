print('Processing...\n')
for i in range(2,100000):
    for j in range(2,i):
        if i % j == 0:
            break
print('Processing completed\n')