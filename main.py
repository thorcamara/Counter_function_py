from time import sleep

def counter(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Count from \033[4;31m{i}\033[m until \033[4;32m{f}\033[m in \033[4;33m{p}\033[m')
    sleep(2.5)

    if i < f:
        count = i
        while count <= f:
            print(f'\033[4;34m{count}\033[m ', end='', flush=True)
            sleep(0.5)
            count += p
        print('\033[4;31mEND!\033[m')
    else:
        count = i
        while count >= f:
            print(f'\033[4;34m{count}\033[m ', end='', flush=True)
            sleep(0.5)
            count -= p
        print('\033[4;31mEND!\033[m')


# Main Program
counter(1, 10, 1)
counter(10, 0, 2)
print('-=' * 20)
print('Now it is your turn to personalize the counter!')
start = int(input('Start:'))
end = int(input('End: '))
pace = int(input('Pace: '))
counter(start, end, pace)
