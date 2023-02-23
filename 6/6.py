import itertools
import zipfile

def unzip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len):
        to_attempt = itertools.product(passwd_string, repeat=len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd=passwd.encode())
                print(f"pass is {passwd}")
                return 1
            except:
                pass

passwd_string = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

zFile = zipfile.ZipFile('credential.zip')
# try:
#     result = zFile.extractall(pwd='88'.encode())
#     print(result)
# except:
#     print("Failed")



min_len = 1
max_len = 3

unzip_result = unzip(passwd_string, min_len, max_len, zFile)

if unzip_result == 1:
    print("Pass Solved")
else:
    print("Failed to Solve")
