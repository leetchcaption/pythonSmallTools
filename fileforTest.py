# !/usr/bin/python

import os


def main():
    def dirList(path):
        fileList = os.listdir(path)
        fpath = os.getcwd()
        allfile = []
        for filename in fileList:
            filepath = os.path.join(fpath, filename)
            if os.path.isdir(filepath):
                dirList(filepath)
            allfile.append(filepath)
        return allfile

    list = dirList('D:/workspace/python/')
    print(list)

    filename = input("please input fileName:")
    try:
        fop = open(filename)
    except IOError:
        print("NameError")
    except NameError:
        print("内部出错!")
    # finally:
    #     if fop:
    #         fop.close()
    #     else:
    #         pass
    finally:
        try:
            fop.close()
        except NameError:
            pass
            print("fop not found!")


if __name__ == '__main__':
    main()
