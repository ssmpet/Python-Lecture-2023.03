# 파일의 단어 개수 세기
import re, string, sys

# sys.argv[0] - WordCount, sys.argv[1] - filename
if len(sys.argv) != 2:
    print("사용법: WordCount filename")
    sys.exit(-1)


with open(sys.argv[1]) as file:
    contents = file.read()
clean_content = re.sub('['+string.punctuation+']', '', contents).replace('\n', ' ').lower().strip()
words = clean_content.split()

print(f'총 단어는 {len(words):,d}개 이고, 고유 단어는 {len(set(words)):,d}개 입니다.')

words_dic = {}
for word in words:
    if word in words_dic.keys() : 
        words_dic[word] += 1
    else:
        words_dic[word] = 1

sort_words = sorted(words_dic.items(), key=lambda x: x[1], reverse=True)
print('사용 빈도가 높은 단어 TOP 10')
for word, count in sort_words[:10]:    
    print(f'\t{word}\t{count:,d}')

