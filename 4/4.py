import qrcode
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_name = 'qr_list.txt'

with open(file_name, 'rt', encoding='UTF-8') as f:
    code_list = f.readlines()

for code in code_list:
    code = code.strip()
    print(code)
    qr = qrcode.make(code)
    save_path = 'qr_list\\' + code + '.png'
    qr.save(save_path)
