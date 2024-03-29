# 🌊Seesea-Start🌊
이화여자대학교 캡스톤 창업 디자인프로젝트 스타트 8팀 어푸어푸입니다.

![캡스톤포스xjjj (3)](https://user-images.githubusercontent.com/93649914/206694303-2c104433-4bfc-454d-ba81-7884197cded6.png)


## :trophy: 캡스톤디자인경진대회 창업 아이디어 부문 동상 수상 :trophy:

## 프로젝트 소개
드론을 이용한 실시간 영상 인식과 수상 구조

## 프로젝트 목적
통계청의 자료에 의하면 사고로 인한 사망자 수 3위는 익사 사고로 인한 것이라고 합니다. 익사 사고의 대부분은 여름철인 7, 8월에 발생하고 5세 이하, 노인층과 같은 취약 계층에서 많이 일어나는 것으로 나타납니다. 현재는 이를 해결하기 위해 인력을 추가배치 중입니다. 그러나 단지 안전요원의 수를 채우기 위해서 충분한 자격이 없는 사람들을 고용하기 때문에 실질적으로 익사 문제를 해결할 수는 없습니다. 이를 위해 드론을 이용하여 해수욕장의 모습을 촬영하고, 촬영한 영상을 실시간으로 분석한 후, 구조가 필요한 상황이 발생하면 안전요원에게 알림이 가도록 하는 서비스를 만들고자 합니다.

## 프로젝트 기술
#### 1) 관리해야 하는 해수욕장의 면적에 따라 드론들을 최적의 위치에 배치
사각지대가 발생하지 않도록 여러 대의 드론을 사각지대가 없게, 최소한의 수로 배치해주는 기술 구현(1월 중 예정)

#### 2) YOLO v5를 이용하여 실시간 영상 분석
드론으로부터 실시간으로 영상을 받아와서 분석, YOLO v5 커스텀 후 정확도 테스트
이를 위해 데이터를 수집하고 있고, 익사 기준이 중요하기 때문에 여러 논문을 참고하고 있음.
관련 논문 링크 : https://ieeexplore.ieee.org/document/1269750

깃허브 : https://github.com/Ahpuh-Ahpuh/Seesea-Start/tree/main/YOLOv5

#### 3) Depth Estimation을 이용하여 드론과 위험상황에 처한 사람 거리 분석
Depth Estimation(깊이 추정) 방식 중에서도 단안카메라를 이용한 Mono Depth Estimation을 통해 거리를 계산

깃허브 : https://github.com/Ahpuh-Ahpuh/Seesea-Start/tree/main/MonoDepthEstimation

#### 4) 이중 PI 제어로 드론 위치 고정
바람이 심한 바닷가 특성상 드론이 제자리를 고정할 수 있도록 이중 PI제어를 이용

깃허브 : https://github.com/Ahpuh-Ahpuh/Seesea-Start/tree/main/tello_PID

#### 5) 프로토타입
FIGMA 링크 : https://www.figma.com/file/S0zZ8bRSJRIrufWTuJL4po/Untitled?node-id=0%3A1&t=DBGMDXkFiHG7ne17-1

UI 영상 : https://github.com/Ahpuh-Ahpuh/Seesea-Start/blob/main/UI%20%EC%98%81%EC%83%81.mp4

#### 6) 시연 영상
시연 영상 링크 :  https://youtu.be/7B0MAAZR1q4 

#### 7) 제품설명서
<img width="1000" alt="제품설명서001" src="https://user-images.githubusercontent.com/112617546/206697649-2abe3a4f-c60b-416f-9a82-efe946bf6d39.png">

