# 버스 도착정보 서비스 웹앱

서울시 공공API를 기반으로 특정 정류장의 버스 도착정보를 조회하고 웹에서 시각적으로 표시해주는 Flask 웹 애플리케이션입니다.



## 주요 기능

* 버스 정류장 번호로 실시간 도착정보 조회
* TinyDB에 저장된 정류장 이름/번호를 선택할 수 있는 드롭다운 제공
* 버스 종류에 따라 다른 이미지로 구분 (파랑/초록/빨강/노랑/회색)



## 실행 환경

* Python 3.8 이상
* Flask 웹 프레임워크

### 필수 패키지 설치

```bash
pip install flask requests tinydb
```


## 디렉토리 구조

```
bus_info_service/
├── bus_info.py                        # 메인 실행 파일
├── config.py                          # API 키를 포함한 설정 파일
├── stations.json                      # TinyDB 저장소 (정류장 목록)
├── templates/
│   └── index.html                     # 결과 출력용 HTML 템플릿
├── businformation_static/
│   └── static/
│       ├── bus_blue@400.png          # 파랑 버스 이미지
│       ├── bus_red@400.png           # 빨강 버스 이미지
│       ├── bus_green@400.png         # 초록 버스 이미지
│       ├── bus_yellow@400.png        # 노랑 버스 이미지
│       └── bus_gray@400.png          # 기타 회색 이미지
└── README.md
```



## 사용 방법

1. `config.py` 파일에 API 키 등록:

```python
SERVICE_KEY = "발급받은_서울시_버스_API_키"
```

2. 정류장 목록은 `stations.json`에 다음 형식으로 저장되어 있어야 합니다:

```json
[
    {"stop_nm": "강남역", "stop_no": "12345"},
    {"stop_nm": "서울역", "stop_no": "10010"}
]
```

3. 실행:

```bash
python bus_info.py
```

4. 브라우저에서 `http://localhost:5000` 접속 후 정류장을 선택해 조회


## 주의사항

* 실제 서비스 키는 공공데이터포털([data.go.kr](https://data.go.kr/))에서 신청 필요
* TinyDB 파일이 없으면 실행 오류가 발생할 수 있으므로 사전 생성 필요
* HTML 템플릿 및 static 경로는 Flask 기준에 맞게 유지



## 라이선스

MIT License
