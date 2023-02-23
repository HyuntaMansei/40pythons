import googletrans
from os import linesep

translator = googletrans.Translator()

read_file_path = 'english.txt'

with open(read_file_path, 'r') as f:
    readlines = f.readlines()

for line in readlines:
    #긴 문장은 번역이 안 됨.
    result1 = translator.translate(line, dest='ko')
    print(result1.text)




