![api2](https://user-images.githubusercontent.com/93903157/177038718-f2af1fb2-81c0-49f1-9279-4ca4e06a32f8.gif)

# 코드 스테이츠 Section3 Project

# 서울시 초미세먼지 예측 시스템 개발
## Project Target
- 서울시 기상데이터를 이용해 ML 모델링 하고  API 서비스를 개발하여 배포

## Trained Datasets
· 서울시 열린데이터 광장
   - 수집기간 : 2021.06 ~ 2022.06

## Process
![image](https://user-images.githubusercontent.com/93903157/177038400-caafaa0f-c019-46e0-86b3-8dbf130db46d.png)

## Result
결정계수R2 : 0.44
## Discussion
· 1차원적인 모델링으로 모델의 성능이 낮게 나타남 
· API 서비스에는 성공했으나 Heroku를 사용한 배포에는 실패
· 예측에 필요한 다른 대기질을 측정하는 과정에서 미세먼지, 초미세먼지의 측정도 이루어지기 때문에 예측의 의미가 많이 퇴색됨



