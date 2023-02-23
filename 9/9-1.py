import googletrans

# translator = googletrans.Translator()

translator = googletrans.Translator()

str1 = "Be happy"
str2 = "무척 피곤하네요"

result_1 = translator.translate(str1, dest='ko', src='auto')
result_2 = translator.translate(str2, dest='en', src='auto')

print(result_1.text)
print(result_2.text)
