def hanoi(rings, source, auxiliary, target):
    if rings == 1:
        print('>>>  Move ring 1 from rod {} to rod {}.'.format(source, target))
        return
 
    hanoi(rings - 1, source, target, auxiliary)
    print('>>>  Move ring {} from rod {} to rod {}.'.format(rings, source, target))
    hanoi(rings - 1, auxiliary, source, target)
 
rings = int(input('Enter number of rings: '))
hanoi(rings, 'X', 'Y', 'Z')
print("\n")
print("So for {} rings puzzle has {} moves \n".format(rings,(pow(2,rings)-1)))





####OUTPUT


#  python prg2.py
# Enter number of rings: 3
# >>>  Move ring 1 from rod X to rod Z.
# >>>  Move ring 2 from rod X to rod Y.
# >>>  Move ring 1 from rod Z to rod Y.
# >>>  Move ring 3 from rod X to rod Z.
# >>>  Move ring 1 from rod Y to rod X.
# >>>  Move ring 2 from rod Y to rod Z.
# >>>  Move ring 1 from rod X to rod Z.


# So for 3 rings puzzle has 7 moves