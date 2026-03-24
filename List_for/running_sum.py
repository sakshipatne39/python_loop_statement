l2 = list (range(1,100))

previousvalue = 0

print('for loop start')
for l2value in l2:
    curerentadd  = previousvalue + l2value
    previousvalue = curerentadd 
    print(f"previous value = {previousvalue}, current value = {l2value}, current add = {curerentadd}")
    print()

print('end loop')
