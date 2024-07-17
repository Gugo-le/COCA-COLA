# 파일 경로
file_path = 'assets/files/COCAsample_single_file.txt'
target_word = 'mind'  # 추출하고자 하는 특정 단어

# 파일 열기
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 특정 단어가 포함된 예문 추출 및 출력
print(f"텍스트 파일 '{file_path}'에서 '{target_word}'가 포함된 예문:")
found_any = False  # 검색된 예문이 하나라도 있는지 여부를 저장하는 변수

for line in lines:
    if target_word.lower() in line.lower():  # 대소문자 구분 없이 검색
        print(line.strip())  # 검색된 줄을 출력
        found_any = True

if not found_any:
    print(f"'{target_word}'를 포함하는 예문이 없습니다.")