import sys
import random


def user_input():
    sys.stdout.buffer.write(b'minimum number?\n')
    sys.stdout.flush()
    min = sys.stdin.buffer.readline().decode()

    sys.stdout.buffer.write(b'maximum number?\n')
    sys.stdout.flush()
    max = sys.stdin.buffer.readline().decode()

    return (min, max)


def main():
    sys.stdout.buffer.write(b'Guess the number game\nYou can guess the number with your range of min-max\n')

    min, max = user_input()

    if int(max) < int(min):
        sys.stdout.buffer.write(b'minimum number is bigger than maximum number\n')

    random_num = random.randint(int(min), int(max))
    while 1:
        sys.stdout.buffer.write(b'guess the number?\n')
        sys.stdout.flush()
        num = sys.stdin.buffer.readline().decode()

        if int(num) == random_num:
            sys.exit("collect")
        elif int(num) < random_num:
            sys.stdout.buffer.write(b'up\n')
        else:
            sys.stdout.buffer.write(b'down\n')


if __name__ == "__main__":
    main()
