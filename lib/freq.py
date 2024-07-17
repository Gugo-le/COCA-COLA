import pandas as pd
from collections import Counter

# CSV 파일 로드
coca_df = pd.read_csv('assets/files/COCA.csv')
tokens_df = pd.read_csv('assets/files/COCA_tokens.csv')


# 단어와 빈도를 딕셔너리로 변환
word_freq = dict(zip(tokens_df['Token'], tokens_df['Count']))

top_words = Counter(word_freq).most_common(10)
print("\n빈도 높은 단어 상위 10개:")
for word, freq in top_words:
    print(f"{word}: {freq}")