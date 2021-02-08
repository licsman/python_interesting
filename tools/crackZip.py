import zipfile


def extractFile(file, password):
    try:
        file.extractall(pwd=password.encode("ascii"))
        return True
    except:
        return False


def main():
    file = zipfile.ZipFile("D:\star.zip")  # 破解文件名
    head = ['m', 'M', 'h', 'H', '1', 'i', 'I', 'j', 'J']
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
    for pos1 in head:
        for pos2 in head:
            password = pos1+pos2+'w'
            result = extractFile(file, password)
            if result:
                print("successful password", password)
                with open('password.txt', 'a') as file_handle:
                    file_handle.write("{}\n".format(password))
                return
            else:
                continue

if __name__ == "__main__":
    main()