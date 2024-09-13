# aiffel

아이펠 8기 학습자료

| 프로젝트             | 목표                                    | 결과 정리    |
| -------------------- | -------------------------------------- | ------------------- |
| ====================== | **딥러닝 (CV, NLP 기초)** | ====================== |
| **카메라 스티커앱 만들기** | 사람 얼굴 감지<br>얼굴의 눈,코,입 등 위치 detection 하기 | <br>Computer Vision의 Object detection 맛 보기 (아래 라이브러리 이용)<br>opencv로 이미지 처리<br>dlib object detection 모델<br><br>**코드**:<br>https://github.com/hyeonDD/aiffel/blob/main/08_study/my_camera.ipynb |
| **인물사진을 만들어 보자** | 사진에서 사람과 배경을 segmentation 하기 | CNN 신경망과 친해지기<br>(YOLO 모델도 겸사겸사 한번보기)<br>YOLO 모델은 object detection을 one-stage로 해결한 모델<br><br>Computer Vision의 semantic segmentation task 맛 보기<br>pixellib로 사람과 배경 segmentation하기<br><br>**코드**:<br>https://github.com/hyeonDD/aiffel/blob/main/09_study/segementation.ipynb |
| **네이버 영화 리뷰 감정 분류** | 자연어 처리로 감정을 분류 | 1. RNN, LSTM 신경망 공부하기<br>2. NLP 처리과정의 순서 공부하기 (ex: 단어 사전 만들기, tokenizer 등)<br><br>NLP binary classification<br>konlpy의 Mecab 토크나이저 사용<br><br>**데이터셋**:<br>https://github.com/e9t/nsmc<br>**코드**:<br>https://github.com/hyeonDD/aiffel/blob/main/11_study/quest/naver_movie_analysis.ipynb |
| **뉴스 기사 요약해보기** | 자연어 처리로 문장 요약하기 | RNN, LSTM 신경망과 친해지기<br><br>Summa summarize로 요약해보기 (라이브러리)<br><br>**데이터셋** (아래 코드로 다운가능):<br>`import urllib.request`<br>`urllib.request.urlretrieve("https://raw.githubusercontent.com/sunnysai12345/News_Summary/master/news_summary_more.csv", filename="news_summary_more.csv")`<br>`data = pd.read_csv('news_summary_more.csv', encoding='iso-8859-1')`<br><br>**코드**:<br>https://github.com/hyeonDD/aiffel/blob/main/11_study/quest2/my_news_summarize.ipynb |
| **한국어 챗봇 만들기** | Transformer 모델을 직접 만들기 | 1. Transformer 모델 공부<br>참고자료 (transformer\_리뷰.pdf)<br><br>**데이터셋**:<br>https://github.com/songys/Chatbot_data/blob/master/ChatbotData.csv<br>**코드**:<br>https://github.com/hyeonDD/aiffel/blob/main/14_study/quest/korean_chatbot.ipynb |
| ====================== | **딥러닝 (CV 심화)** | ====================== |
| **ResNet모델 직접만들기** | 모델이 복잡해 질 수록 (layer가 많을 수록) 모델이 좀더 좋은 성능을 내지 못한 점을 개선한 것을 이해하기 | Computer Vision에서 많이 사용되는 백본 모델 만들어보기<br><br>**ResNet 논문**:<br>https://arxiv.org/pdf/1512.03385<br>**논문 구현**:<br>https://github.com/KaimingHe/deep-residual-networks<br>**코드**:<br>https://github.com/hyeonDD/aiffel/blob/main/17_resnet_ablation_study/quest.ipynb |
| **CV분야의 데이터 증강해보기** | 데이터 수집은 가장 비용이 많이 듬<br><br>data augmentation을 통해 기존 수집된 데이터를 최대한 활용해보기 | Computer Vision에서 사용해볼 수 있는 data augmentation 해보기<br>CutMix<br>MixUp<br><br>**코드**:<br>https://github.com/hyeonDD/aiffel/blob/main/18_data_augmentation/quest_colab.ipynb |
| **Class Activation Map 만들기** | 모델이 (보통 CNN계열) 무엇을 보고 있는지를 정성적으로 확인해보기 | **코드**:<br>https://github.com/hyeonDD/aiffel/blob/main/19_class_activation_map/quest.ipynb |
| **직접 만들어보는 OCR** | OCR task의 흐름 파악하기 | **코드**:<br>https://github.com/hyeonDD/aiffel/blob/main/20_ocr/quest.ipynb |
| ====================== | **읽은 논문들** | ====================== |
| **Gaussian Splatting for Real-Time Radiance Field Rendering** | 2D 이미지에서 3D 이미지로 변환할 수 있음 | **논문**:<br>https://arxiv.org/pdf/2308.04079 |
| **Yolact - You Only Look At Coefficients** | 프로젝트 중 사람과 배경을 나누는 YOLO 모델의 semantic segmentation과 비슷하게 Instance segmentation 작업도 거의 실시간 처리가 되도록 만든 모델 | **논문**:<br>https://arxiv.org/pdf/1904.02689 |
| **(VIT) An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale** | LLM의 엄청난 성공 (GPT, BERT 등)의 사례를 보며 Transformer 모델의 매커니즘을 Computer Vision에도 적용한 모델 | **논문**:<br>https://arxiv.org/pdf/2010.11929 |
| **(CLIP) Learning Transferable Visual Models From Natural Language Supervision** | OpenAI에서 만든 VIT 모델<br>텍스트(자연어)와 이미지를 같이 학습 시킨 모델 | **논문**:<br>https://arxiv.org/pdf/2103.00020<br>**텍스트로 이미지 검색하는 코드**:<br>https://github.com/hyeonDD/clip-elasticsearch-kibana |
