🔑 **PRT(Peer Review Template)**

작성자: 현동철

리뷰어: 이현동

- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    > - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    > - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 퀘스트 문제 요구조건 등을 지칭
    >    - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부

    - [x] CAM을 얻기 위한 기본 모델의 구성과 학습이 정상 진행되었는가?
        - node.ipynb 내에 존재  
        - Resnet50 선택, pooling='avg' 적용, Dense(softmax) 추가  
          ![image](https://github.com/DevHDL/aiffel-dch/assets/163500244/de132286-df56-46f4-925c-a5560d8f0666)  

    - [x] 분류 근거를 설명 가능한 Class Activation Map을 얻을 수 있는가?
        - quest.ipynb에 다음과 같이 존재
          ![image](https://github.com/DevHDL/aiffel-dch/assets/163500244/449e4120-d1ff-4675-9f6a-847cf782e5c2)

    - [x] 인식 결과의 시각화 및 성능 분석을 적절히 수행했는가?
         - quest.ipynb에 다음과 같이 존재
         - no_grad / grad 및 각 threshold에 따른 결과가 같이 첨부가 되어있음
           ![image](https://github.com/DevHDL/aiffel-dch/assets/163500244/9cbd199e-59a3-487e-a04f-a7f118b88d47)


- [ ]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
    > - [ ]  모델 선정 이유
    > - [ ]  Metrics 선정 이유
    > - [ ]  Loss 선정 이유

    - [ ] 코드 주석이 좀 더 잘 기록되어 있으면 좋을 것 같습니다.  
    - [x] 외에 실험 기록을 위한 Markdown은 잘 기록하셨습니다.
          ![image](https://github.com/DevHDL/aiffel-dch/assets/163500244/10554d45-c4ff-4ace-abe5-777e9b02c820)


- [x]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
    > - [ ]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
    > - [ ]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
    > - [ ]  각 실험을 시각화하여 비교하였나요?
    > - [ ]  모든 실험 결과가 기록되었나요?
    
    - [x] 1번에 적은 것과 같이 항목을 수행함.
    - [x] Grad-CAM의 문제 지적  
          ![image](https://github.com/DevHDL/aiffel-dch/assets/163500244/a4c992df-d238-45d4-933e-4f6408e8f3c4)


- [x]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    ![image](https://github.com/DevHDL/aiffel-dch/assets/163500244/87681aab-c1f7-45e7-adcf-1fd0100f4850)  
 
    - [x]  배운 점
    - [x]  아쉬운 점
    - [x]  느낀 점
    - [x]  어려웠던 점

---

**리뷰어 회고**  
- 실험결과 중 저 역시 grad-cAM에서 동일한 문제가 발생했습니다.
- grad-CAM++라는 해결방법을 제시해 주셔서 감사합니다. 저 역시 한 번 실습해보겠습니다.
