import re

def is_valid_email(email):
    """
    이메일 주소가 유효한지 확인하는 함수.
    이메일 주소의 형식을 정규 표현식을 통해 검증함.
    """
    # 이메일 주소의 패턴을 정의
    # 패턴 설명:
    # - ^: 문자열의 시작
    # - [a-zA-Z0-9_.+-]+: 알파벳 대소문자, 숫자, 밑줄, 점, 더하기, 빼기가 1회 이상 반복
    # - @: '@' 문자
    # - [a-zA-Z0-9-]+: 도메인 이름의 일부로 알파벳 대소문자, 숫자, 빼기가 1회 이상 반복
    # - \.: 도메인 이름의 일부로 점(.) 문자
    # - [a-zA-Z]{2,}$: 도메인 이름의 마지막 부분으로 알파벳 대소문자가 2자 이상 반복, 문자열의 끝
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    
    # 이메일 주소가 패턴과 일치하는지 확인
    return re.match(pattern, email) is not None

# 테스트할 이메일 주소 샘플
sample_emails = [
    "test@example.com",         # 올바른 이메일 주소
    "user.name@domain.co.kr",   # 올바른 이메일 주소
    "user_name123@domain.org",  # 올바른 이메일 주소
    "username@sub.domain.com",  # 올바른 이메일 주소
    "user-name@domain.com",     # 올바른 이메일 주소
    "invalid-email@",           # 잘못된 이메일 주소 (도메인 없음)
    "@no-local-part.com",       # 잘못된 이메일 주소 (로컬 파트 없음)
    "username@.com",            # 잘못된 이메일 주소 (도메인 없음)
    "username@domain",          # 잘못된 이메일 주소 (최상위 도메인 없음)
    "username@domain.c",        # 잘못된 이메일 주소 (최상위 도메인 너무 짧음)
]

# 각 이메일 주소를 검증하고 결과를 출력
for email in sample_emails:
    if is_valid_email(email):
        print(f"{email} -> 유효한 이메일 주소입니다.")
    else:
        print(f"{email} -> 유효하지 않은 이메일 주소입니다.")
