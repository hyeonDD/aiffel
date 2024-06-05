🔑 **PRT(Peer Review Template)**
> Reviewer : 이현동  

- [x] **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
  > - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
  > - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 퀘스트 문제 요구조건 등을 지칭
  >   - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부

  1. 아웃포커싱 효과가 적용된 인물모드 사진과 동물 사진, 배경전환 크로마키사진을 각각 1장 이상 성공적으로 제작
     ![image](https://github.com/DevHDL/aiffel-hyeondd/assets/163500244/3ffbde45-56e3-4fd6-8ce3-5ae0b354684c) ![image](https://github.com/DevHDL/aiffel-hyeondd/assets/163500244/b27605b7-c1e4-4532-8e60-646f7cf53b13) ![image](https://github.com/DevHDL/aiffel-hyeondd/assets/163500244/0efcab10-c03c-44c9-96d6-23112800f0fb)

  2. 인물사진에서 발생한 문제점을 정확히 지적한 사진을 제출  
    ![image](https://github.com/DevHDL/aiffel-hyeondd/assets/163500244/8cc2d825-9614-4bff-8c9c-4a2fd37e2e23) ![image](https://github.com/DevHDL/aiffel-hyeondd/assets/163500244/f44bcbac-d903-4135-aac0-fda4310fda83)

  3. semantic segmentation mask의 오류를 보완할 수 있는 좋은 솔루션을 이유와 함께 제시
    > 이미지 회전을 통한 잘못된 분류 없애기(실습)  
    
    ![image](https://github.com/DevHDL/aiffel-hyeondd/assets/163500244/6fbe45d4-a1a0-4157-9715-ffd18df67a8a)

- [x] **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
  > - [ ] 모델 선정 이유
  > - [ ] Metrics 선정 이유
  > - [ ] Loss 선정 이유
  
  ![image](https://github.com/DevHDL/aiffel-hyeondd/assets/163500244/d028b77f-78bd-40ba-a967-e2ca68bde27c)

  - [x] 각 내용에 대해 markdown으로 주제 및 설명, 주석으로 코드 해설 등을 잘 작성
  
- [ ] **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
  > - [ ] 데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
  > - [ ] 하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
  > - [ ] 각 실험을 시각화하여 비교하였나요?
  > - [ ] 모든 실험 결과가 기록되었나요?

  - [x] 루브릭 기준의 내용은 모두 수행 완료

- [x] **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
![image](https://github.com/DevHDL/aiffel-hyeondd/assets/163500244/ccf6e17e-e245-4963-9c0f-107d18d4d8f3)
  - [x] 배운 점
  - [x] 아쉬운 점
  - [x] 느낀 점
  - [x] 어려웠던 점

---

**리뷰어 회고**  
- 이미지 회전을 이용해서 이미지 내에 존재하는 잘못된 분류를 해결한 방법이 인상적이었습니다.
- cv2.reisze의 interpolation 옵션에 대해 새로 알아갑니다.
