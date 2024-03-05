increment_i = False
for i in range(0, 10):
    if increment_i:
        increment_i = False
    else:
        if i == 4:
            increment_i = True
    print("Current i:", i)