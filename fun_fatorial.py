def fatorial(num: int, show: bool = False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c != 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
        f *= c
    print(f)

print('-'*30)
fatorial(5, show=False)