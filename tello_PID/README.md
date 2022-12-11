## ✏️ 개발환경  
![image](https://user-images.githubusercontent.com/79096808/206724639-6901c502-36c3-4588-bddb-0b4b45670430.png)
![image](https://user-images.githubusercontent.com/79096808/206724701-dce3e7e9-e482-4480-93a7-656e9e804032.png)

### 파이참과 파이썬을 이용하여 드론 제어 코드 작성



### 파이참 설치 링크
https://www.jetbrains.com/ko-kr/pycharm/download/#section=mac



## 🌙 실행 방법

### 텔로 노트북 연결

1) 드론 전원 작동
2) 노트북 와이파이 -> 텔로 연결
3) 코드 실행



## 텔로 모듈 import

1) 파일 -> 프로젝트 설정
2) 파이썬 인터프리터 -> 생성한 폴더
3) 아래의 + 버튼 클릭
4) djitellopy 검색 후, 해당 모듈 install Package 버튼으로 설치
(numpy, opencv-python가 함께 설치 됨)


##PID 제어 원리
* P 제어 (비례값 이용)

![image](https://user-images.githubusercontent.com/79096808/206883844-54cb63d7-3a2c-43e0-967b-f593bd75387f.png)

* I 제어 (적분값 이용)

![image](https://user-images.githubusercontent.com/79096808/206883851-b9cd4e53-ca6c-4240-9954-08dfbbce8306.png)

* D 제어 (미분값 이용)

![image](https://user-images.githubusercontent.com/79096808/206883854-49740411-311e-42f6-baf3-a60091a78398.png)

=> PID 제어

![image](https://user-images.githubusercontent.com/79096808/206883862-98de668d-d610-4c93-af12-87bba71a0747.png)
 

## 이중 PI 제어 구조도
![image](https://user-images.githubusercontent.com/79096808/206730347-9c158e4d-4cf8-402c-af59-23d84e5c943a.png)

