import re
from sklearn.feature_extraction.text import TfidfVectorizer

f_train = open("ratings_train.txt", 'r', encoding="utf-8")
f_test = open("ratings_test.txt", 'r', encoding="utf-8")
f_bigram = open("./bigram.txt", 'w', encoding="utf-8")
f_doc_vec_train = open("./document_vector_train.txt", 'w', encoding="utf-8")
f_doc_vec_test = open("./document_vector_test.txt", 'w', encoding="utf-8")

bi_arr = []

def slice_document(text): # 텍스트를 알맞은 형식으로 분리해주는 함수
    join_text = ' '.join(text.split()[1:])
    print(join_text)

    if len(join_text) > 1:
        return join_text[:-2], join_text[-1]
    else:

        return '', join_text[0]

def ngram(s, num): # n_gram 해주는 함수
    res = s[0:num]
    slen = len(s)-num+1
    for i in range(1,slen):
        res = res + ' ' + s[i:i+num]

    return res

def text_tokenizer(text): # 텍스트를 알맞게 토큰화해주는 함수
    if (text != ''):
        e = re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}', flags=re.IGNORECASE) # 이메일
        #email_arr = e.findall(text)
        non_email_text = e.sub(' ', text)

        r = re.compile("[^ 가-힣]+") # 한글 이외의 모든 문자열
        etc_arr = r.findall(non_email_text)
        korean_str = r.sub(' ', text)

        s = re.compile("[\s]+") # 공백
        #blank_arr = s.findall((korean_str))
        non_blank_text = s.sub("_", korean_str)

        if non_blank_text[0] != '_' and non_blank_text[len(non_blank_text) - 1] != '_':
            non_blank_text = '_' + non_blank_text + '_'
        elif non_blank_text[0] != '_':
            non_blank_text = '_' + non_blank_text
        elif (non_blank_text[len(non_blank_text) - 1] != '_'):
            non_blank_text = non_blank_text + '_'

        bi_text = ngram(non_blank_text, 2)

        return bi_text
    else:
        return ''


def vectorize_document(doc_arr): # 문서벡터를 구성하는 함수
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(doc_arr)
    X.todok()

    return X


# main
line = f_train.readline() # 첫번째 줄 제외

while line:
    line = f_train.readline()

    # document slicing
    doc_str, label = slice_document(line)

    # bigram
    bi_text = text_tokenizer(doc_str)
    f_bigram.write(bi_text + '\n')

    bi_arr.append(bi_text)

    # document vectorize
    vec_dict = vectorize_document(bi_arr)
    #print(vec_dict)


# text = "음lhj00@naver.com hihihi qqq!~ 안녕안녕ㅋㅋabc!우왓 헉 李dl이얏호~ rosy@naver.com악ㅋㅋㅋ웩ㅋㅋ       응? 어" # 안녕안녕이랑 우왓 분리돼야 함
# # 아스키 문자열 및 한글 이외의 문자열 분리
# e = re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}', flags = re.IGNORECASE)


f_train.close()
f_bigram.close()
