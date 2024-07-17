import pandas as pd

# CSV 파일 로드
coca_df = pd.read_csv('assets/files/COCA.csv')
tokens_df = pd.read_csv('assets/files/COCA_tokens.csv')

# 데이터 확인
print(coca_df.head())
print(tokens_df.head())