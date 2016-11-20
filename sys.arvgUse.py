import sys

def readfile(filename):
    f = readfile(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
            print(line)
            f.close()
        if len(sys.argv) < 2:
            print("No action!")
            sys.exit()
        if sys.argv[1].startswith('--'):
            if option == 'version':
                print("Version 1.4")
            elif option == 'help':
                print("'...'")
            else:
                print("Unknow option.")
                sys.exit()
        else:
            for filename in sys.argv[1:]:
                readfile(filename)
