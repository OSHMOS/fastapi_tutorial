# fastapi_tutorial

## 설치 순서
1. 가상환경 생성 - python3 -m venv venv
2. 가상환경 실행 - source venv/bin/activate
3. FastAPI 설치 - pip install fastapi

## FastAPI는 자체 서버가 없다!
### uvicorn 설치하기
- pip install uvicorn

### uvicorn 실행하기
- uvicorn [파일_이름]:app --reload

## httpie
### 개발한 api 간단하게 확인하기
1. httpie 설치하기
    - pip install httpie

2. httpie 실행하기 (uvicorn 실행하고나서)
    - http localhost:8000
    - http :8000

## type hint
    - 내가 원하는 데이터의 자료형을 정할 수 있다.
    - 경로 매개변수에 직접 정하기 보다는 함수 매개변수에다가 설정하는 것이 좋다.

## FastAPI의 몇 안되는 단점, 순서 문제!
    - 경로 동작이 앤드포인트 순서에 따라 수행된다. 이 점을 숙지하자!

## 쿼리 매개변수
### 쿼리 매개변수 기본값 정하기
    - 함수 매개변수에다가 = 기본값 붙이면 된다.
    - 기본값을 선택적으로 주고 싶다면 = None을 붙이면 된다.

### 쿼리 매개변수 논리형
    - TRUE, True, true, 1, on, yes 모두 true로 표시된다.(FastAPI는 굉장히 똑똑하다.)

### 쿼리 매개변수 문자열 열거형
    - 열거형의 기본값을 적을 경우 하드 코딩하는 것보다 직접 작성해주는 것이 좋다.