# RandyPy

RandyPy는 파이썬에서 다양한 유형의 랜덤 데이터를 생성하는 유틸리티 라이브러리입니다. 이 라이브러리는 자연수, 실수, 문자열, 이름, 비밀번호, 이메일 주소, UUID, 날짜, 색상 등을 랜덤하게 생성할 수 있는 편리한 기능을 제공합니다.

## 주요 기능

- 범위 내의 랜덤한 자연수 및 실수 생성
- 무작위로 하나 선택
- 무작위로 순서 섞기
- 지정된 길이의 랜덤한 문자열 생성
- 랜덤한 이름(이름, 성) 생성
- 지정된 규칙에 따른 랜덤한 비밀번호 생성
- 지정된 도메인의 랜덤한 이메일 주소 생성
- 랜덤한 UUID 생성
- 지정된 날짜 범위 내의 랜덤한 날짜 생성
- 랜덤한 RGB 색상 값 생성

## 설치

RandyPy는 pip를 통해 설치할 수 있습니다:

```
!pip install randypy
```

## 사용 예시

```python
import randypy

# 0과 1 사이의 실수 생성
randy_percentage = randypy.percentage()  # 0.0과 1.0 사이의 실수 생성 (0.0 <= x < 1.0)

# 자연수 생성
randy_int = randypy.randyint(1, 100)  # 1부터 100 사이의 랜덤한 정수 (1 <= x <= 100)

# 실수 생성
randy_float = randypy.randyfloat(0.0, 1.0)  # 0.0부터 1.0 사이의 랜덤한 실수 (0.0 <= x <= 1.0)

# 무작위로 하나 선택
randy_choice = randypy.choice(['apple', 'banana', 'cherry'])  # 매개변수로 받은 문자열, 튜플, range, 리스트에서 무작위로 하나 선택

# 무작위로 순서 섞기
randy_shuffle = randypy.shuffle(['apple', 'banana', 'cherry'])  # 매개변수로 받은 리스트 순서를 무작위로 섞음

# 문자열 생성
randy_str = randypy.str(10)  # 길이 10의 랜덤한 문자열

# 이름 생성
randy_name = randypy.name()  # 랜덤한 이름 생성

# 이메일 주소 생성
randy_email = randypy.email(domain="example.com")  # example.com 도메인의 랜덤한 이메일 주소

# 비밀번호 생성
randy_password = randypy.password(length=12, include_digits=True, include_special_chars=True)  # 길이 12, 숫자와 특수문자 포함하는 랜덤한 비밀번호

# UUID 생성
randy_UUID = randypy.UUID()  # 랜덤한 UUID

# 날짜 생성
randy_date = randypy.date("2024-01-01", "2024-12-31")  # 2024년 1월 1일부터 12월 31일 사이의 랜덤한 날짜

# 색상 생성
randy_color = randypy.color()  # (128, 45, 212) 형식의 랜덤한 RGB 색상 값
```

RandyPy는 파이썬 프로젝트에서 테스트 데이터 생성, 무작위 샘플링, 데이터 익명화 등 다양한 상황에서 유용하게 사용될 수 있습니다.
