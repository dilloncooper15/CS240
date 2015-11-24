
def open_file():
    with open('random.txt', 'r') as inputfile:
        # .splitlines() gets rid of '\n'
        var = inputfile.read().splitlines()
        print(var)


def write_file():
    with open('random.txt', 'w') as outputfile:
        outputfile.write('hi there\n')
        print(outputfile)

if __name__ == '__main__':
    write_file()
    open_file()
