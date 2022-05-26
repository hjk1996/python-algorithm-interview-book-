'''
로그를 재정렬하라 기준은 다음과 같다.

1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.
'''

def reorder_log_files(logs: list[str]) -> list[str]:
    letters, digits = [], []

    # 리스트 속 로그 순회
    for log in logs:
        # 식별자 거르고 맨 처음 단어가 숫자면 digts에 넣고
        if log.split()[1].isdigit():
            digits.append(log)
        # 아니면 문자니까 letters에 넣음
        else:
            letters.append(log)
    
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

if __name__ == "__main__":
    print(reorder_log_files(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
