import sys


def main():
    if bool(sys.argv[1]):
        name = input('Enter your name: ')
    else:
        name = sys.argv[1]
    print("Hello,",name+'!')


if __name__ == "__main__":
    main()