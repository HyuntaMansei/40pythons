import googletrans
from os import linesep

translator = googletrans.Translator()

read_file_path = 'english.txt'
write_file_path = 'korean.txt'

with open(read_file_path, 'r') as f:
    readlines = f.readlines()

for line in readlines:
    text = translator.translate(line, dest='ko')
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(text.text + '\n')
        print(text.text)