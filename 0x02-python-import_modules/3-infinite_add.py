#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0

    if len(sys.argv) > 1:
        for index in range(1, len(sys.argv)):
            result += int(sys.argv[index])
    print('{:d}'.format(result))
