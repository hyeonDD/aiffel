🔑 **PRT(Peer Review Template)**


코더: 현동철


리뷰어: 윤소정

- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부
        1. Text recognition을 위해 특화된 데이터셋 구성이 체계적으로 진행되었다.<br>![image](https://github.com/hyeonDD/aiffel/assets/104029654/4245d040-f6cd-43f2-85a4-6037b15085e3)<br>
          ![image](https://github.com/hyeonDD/aiffel/assets/104029654/937b0c12-5b02-4a8f-a3eb-12dfc7c46543)<br>![image](https://github.com/hyeonDD/aiffel/assets/104029654/b27ce250-bd18-4ebd-af54-95dacba9884d)<br>
        2. CRNN 기반의 recognition 모델의 학습이 정상적으로 진행되었다.	학습결과 loss가 안정적으로 감소하고 대부분의 문자인식 추론 결과가 정확하다.<br> ![image](https://github.com/hyeonDD/aiffel/assets/104029654/47950a16-edea-42d8-84f2-ffe5fa1c0406)<br>![image](https://github.com/hyeonDD/aiffel/assets/104029654/c8ddcf1c-08b6-4bfb-8a79-7c3a1daa997d)

        3. keras-ocr detector와 CRNN recognizer를 엮어 원본 이미지 입력으로부터 text가 출력되는 OCR이 End-to-End로 구성되었다.	샘플 이미지를 원본으로 받아 OCR 수행 결과를 리턴하는 1개의 함수가 만들어졌다.<br> ![image](https://github.com/hyeonDD/aiffel/assets/104029654/38e7ccf8-74cf-4a3f-a249-f98d154042cb)<br>![image](https://github.com/hyeonDD/aiffel/assets/104029654/4e6c13fa-410d-4b87-b5ba-f55b483db41c)<br>![image](https://github.com/hyeonDD/aiffel/assets/104029654/2b42c7ca-09ab-431d-9190-e7c1072b9d85)

 
- [X]  **2. 핵심적이거나 복잡하고 이해하기 어려운 부분에 작성된 설명을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭에 doc string/annotation/markdown이 달려 있는지 확인
    - 해당 코드가 무슨 기능을 하는지, 왜 그렇게 짜여진건지, 작동 메커니즘이 뭔지 기술.
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - ![image](https://github.com/hyeonDD/aiffel/assets/104029654/903b8aaa-d497-4e5f-9de2-62b9abf030bf)
        - 해당 코드가 무슨 기능을 하는지 왜 그렇게 짜여진 것인지 등을 서술하였습니다.
        
- [ ]  **3.** 에러가 난 부분을 디버깅하여 “문제를 해결한 기록”을 남겼나요? 또는
   “새로운 시도 및 추가 실험”을 해봤나요? ****
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인 또는
    - 문제에서 요구하는 조건에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - ![image](https://github.com/hyeonDD/aiffel/assets/104029654/ba4c8f75-513d-4265-a105-90ea69f40940)
        - ![image](https://github.com/hyeonDD/aiffel/assets/104029654/cd54e65f-0b0b-46b5-ad69-84cb08b9132a)
        - 정말 다양한 텍스트를 가져와서 실험하셨습니다. 그리고 실험을 통 문제점도 파악하셨습니다.


        
- [X]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    - [X]  배운 점
    - [X]  아쉬운 점
    - [X]  느낀 점
    - [X]  어려운점
    - ![image](https://github.com/hyeonDD/aiffel/assets/104029654/1bb0f655-4105-4158-bbc4-43d2b2838190)
    - 네 회고가 상세히 잘 적혀있습니다.


- [X]  **5. 코드가 간결하고 효율적인가요?**
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 모듈화(함수화) 했는지
        - 잘 작성되었다고 생각되는 부분을 근거로 첨부합니다.
        - ![image](https://github.com/hyeonDD/aiffel/assets/104029654/a13e3c78-17b9-4a33-9b21-1ff1c869b39e)

        - 정말 간결하게 keras ocr 의 recognizer를 활용해 간단하게 텍스트를 받아내셨습니다.
        - ![image](https://github.com/hyeonDD/aiffel/assets/104029654/86b92b93-c7e5-43b8-8400-d4f4e9f049fc)
        - keras ocr을 이용한 탐지하는 함수도 간단히 만드셨습니다.

-----------------------------------------------------------------------------------------------
리뷰어 느낀점:
다양한 실험을 하시면서 다양한 문제점을 찾아내신 점이 인상깊었습니다. 또한 이미지 속 텍스트를 찾는것이라고만 생각을 해서 예시 이미지로 뉴스와 많은 텍스트를 가져오신 부분에서 제가 생각지 못한 부분을 깨달을 수 있는 부분이었습니다. 또한 이 텍스트들과 뉴스이미지를 통해 찾은 문제점들 중 중간에 선이 들어가면 사람은 그 선을 넘지 않고 밑으로 내려가서 읽는데 AI는 그렇지 않고 줄대로 읽는다는 점 또한 생각지 못한 점이었습니다. 그 문제점을 알게되자 정말 어떻게 풀어가야할지 저도 궁금해지네요. 많은 생각을 할 수 있게 만드는 프로젝트였습니다. 감사합니다.
