# 🔥 빅데이터로 분석한 대한민국 산불 발생 현황

## 📌 프로젝트 소개
본 프로젝트는 공공 데이터를 활용하여 산불 발생의 주요 원인과 특징을 분석하고, 실시간 뉴스를 통해 최신 정보를 확인하는 프로젝트입니다

## 🕵️ 분석 가설 및 증명 결과

### 1. [계절] 봄철(3~5월)에 산불이 가장 많이 발생하는가? (Yes!)
- **증명 방법**: 10년 평균 데이터를 기반으로 계절별 발생 건수 비교
- **분석 결과**: 봄철 평균 발생 건수가 약 300건 이상으로, 여름/가을 대비 6~7배 높은 수치를 기록함

### 2. [요일] 사람이 많은 주말에 산불이 더 자주 발생하는가? (Yes!)
- **증명 방법**: 월~일 요일별 산불 발생 추이 분석.
- **분석 결과**: 평일 평균 대비 토요일과 일요일의 발생 건수가 약 20~30% 상승하는 '주말 집중 현상' 확인

### 3. [인구] 인구 밀집 지역일수록 산불이 많이 발생하는가? (NO!)
- **증명 방법**: 시도별 주민등록 인구수와 산불 발생 건수의 상관관계 분석
- **분석 결과**: 
    - **경기도**: 인구가 가장 많으며 산불 발생 건수도 전국 1위로 가설과 일치
    - **강원/경북**: 인구는 적으나 산림 면적이 넓어 인구 대비 발생 건수가 매우 높게 나타남
- 
## 🛠 사용 기술
- **Language**: Python
- **Library**: Pandas, Matplotlib, Seaborn, BeautifulSoup
- **Data**: 산림청 산불 발생 공공 데이터 (1997-2024)

## 🛠 핵심 데이터 처리 로직 설명
-특정 항목을 제외하거나 포함해야 할 때, 여러 번의 if 조건 대신 isin()을 사용하여 코드의 가독성을 높였습니다
-merge()를 활용해 서로 다른 출처의 데이터를 하나로 합쳐 새로운 인사이트(상관계수)를 도출하기 위해 사용했습니다
-데이터 정제(Preprocessing)의 중요성 : merge를 하기 전, 데이터의 불일치 문제를 해결하기 위해 이름 통일(Mapping) 과정을 거쳤습니다

## 📊 주요 시각화 결과
<img width="1200" height="600" alt="계절별" src="https://github.com/user-attachments/assets/07dacbe3-59a5-4845-95f1-f7f29870af08" />
<img width="1200" height="600" alt="요일별" src="https://github.com/user-attachments/assets/56f4aa4e-8b0b-4f99-a271-0e335a9af18c" />
<img width="972" height="538" alt="인구수" src="https://github.com/user-attachments/assets/40ae76e0-48fc-4077-aaf6-1ddd5891db93" />

## 참고 링크
[javascript:treeDownList("C_12,MT_ZTITLE,2")](https://kosis.kr/statHtml/statHtml.do?orgId=136&tblId=TX_13625_A002&conn_path=I2)
