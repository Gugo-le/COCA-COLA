import pandas as pd
from collections import Counter

# CSV 파일 로드
coca_df = pd.read_csv('assets/files/COCA.csv')
tokens_df = pd.read_csv('assets/files/COCA_tokens.csv')

# 단어 빈도 계산
word_freq = Counter(tokens_df['word'])

# 상위 10개 단어 출력
print(word_freq.most_common(10))