# -*- coding: utf-8 -*-
from konlpy.tag import Mecab

"""
mecab.tagset
{'EC': '연결 어미', 'EF': '종결 어미', 'EP': '선어말어미', 'ETM': '관형형 전성 어미', 'ETN': '명사형 전성 어미', 'IC': '감탄사',
 'JC': '접속 조사', 'JKB': '부사격 조사', 'JKC': '보격 조사', 'JKG': '관형격 조사', 'JKO': '목적격 조사', 'JKQ': '인용격 조사',
'JKS': '주격 조사', 'JKV': '호격 조사', 'JX': '보조사', 'MAG': '일반 부사', 'MAJ': '접속 부사', 'MM': '관형사', 'NNB': '의존 명사', 
'NNBC': '단위를 나타내는 명사', 'NNG': '일반 명사', 'NNP': '고유 명사', 'NP': '대명사', 'NR': '수사', 'SC': '구분자 , · / :', 
'SE': '줄임표 …', 'SF': '마침표, 물음표, 느낌표', 'SH': '한자', 'SL': '외국어', 'SN': '숫자', 'SSC': '닫는 괄호 ), ]', 
'SSO': '여는 괄호 (, [', 'SY': '기타 기호', 'VA': '형용사', 'VCN': '부정 지정사', 'VCP': '긍정 지정사', 'VV': '동사', 
'VX': '보조 용언', 'XPN': '체언 접두사', 'XR': '어근', 'XSA': '형용사 파생 접미사', 'XSN': '명사파생 접미사', 'XSV': '동사 파생 접미사'}

조사: 'JC': '접속 조사', 'JKB': '부사격 조사', 'JKC': '보격 조사', 'JKG': '관형격 조사', 'JKO': '목적격 조사', 'JKQ': '인용격 조사',
'JKS': '주격 조사', 'JKV': '호격 조사', 'JX': '보조사'

어미: 'EC': '연결 어미', 'EF': '종결 어미', 'EP': '선어말어미', 'ETM': '관형형 전성 어미', 'ETN': '명사형 전성 어미'

"""

mecab = Mecab()

josa_tag = {'JC': '접속 조사', 'JKB': '부사격 조사', 'JKC': '보격 조사', 'JKG': '관형격 조사', 'JKO': '목적격 조사', 'JKQ': '인용격 조사', 'JKS': '주격 조사', 'JKV': '호격 조사', 'JX': '보조사'}
eomi_tag = {'EC': '연결 어미', 'EF': '종결 어미', 'EP': '선어말어미', 'ETM': '관형형 전성 어미', 'ETN': '명사형 전성 어미'}
myungsa_tag = {'NNB': '의존 명사', 'NNBC': '단위를 나타내는 명사', 'NNG': '일반 명사', 'NNP': '고유 명사', 'NP': '대명사'}
josa_keys = josa_tag.keys()
eomi_keys = eomi_tag.keys()
myungsa_keys = myungsa_tag.keys()
josa = []
eomi = []
jeobmisa_keys = ['하다', '한다', '했다', '되다', '된다', '됐다', '시키다', '시킨다', '시켰다']

f_path = '/home/hanjeong/source/datamining/kt_all_utf8.txt'
#f_path = '/home/hanjeong/source/datamining/ko_wiki_utf8.txt'
#f_path = '/home/hanjeong/source/datamining/gtlee_utf8.txt'
#f_path = '/home/hanjeong/source/datamining/ratings.txt'

f = open(f_path , mode='rt', encoding='utf-8')

lines = f.readlines()

for line in lines:
    result = mecab.pos(line)
    for r in result:
        if r[1] in josa_keys:
            josa.append(r)
            continue
        if r[1] in eomi_keys:
            eomi.append(r)

josa_set = set(josa)
eomi_set = set(eomi)

print("1. 조사/어미 목록 추출")
print("<조사>")
print(josa_set)
print("<어미>")
print(eomi_set)

word = input("2. 분석하고 싶은 어절을 입력하세요: ")

find = 0

for key, value in josa_set:
    idx = word.find(key)
    if idx != -1:
        if idx == 0:
            if len(word) == len(key):
                print(word+'/head')
                find = 1
        else:
            if len(word[idx:]) == len(key):
                print(word[0:idx], end='')
                print('/head +', end='')
                print(word[idx:], end='')
                print("/tail_Josa-"+value)
                find = 1
        

for key, value in eomi_set:
    idx = word.find(key)
    if idx != -1:
        if idx == 0:
            if len(word) == len(key):
                print(word+'/head')
                find = 1
        else:
            if len(word[idx:]) == len(key):
                print(word[0:idx], end='')
                print('/head +', end='')
                print(word[idx:], end='')
                print("/tail_Eomi-"+value)
                find = 1

for j in jeobmisa_keys:
    idx = word.find(j)
    if idx != -1:
        if idx == 0:
            print(word+'/head')
            find = 1
        else:
            if mecab.pos(word[0:idx])[0][1] in myungsa_keys:
                print(word[0:idx], end='')
                print('/head +', end='')
                print(word[idx:], end='')
                print("/tail_suffix")
                find = 1

if find == 0:
    print(word+'/head')


f.close()
