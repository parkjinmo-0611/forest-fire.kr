import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False 

try:
    df_pop_raw = pd.read_csv('시도별_주민등록_인구현황(09-24).csv', encoding='cp949')
    df_fire_raw = pd.read_csv('시도별_산불발생_현황(01-24).csv', encoding='cp949')
except:
    df_pop_raw = pd.read_csv('시도별_주민등록_인구현황(09-24).csv', encoding='utf-8')
    df_fire_raw = pd.read_csv('시도별_산불발생_현황(01-24).csv', encoding='utf-8')

df_pop = df_pop_raw.iloc[2:].copy()
df_pop = df_pop[['시·도별(1)', '2024']]
df_pop.columns = ['지역', '인구수']
df_pop['인구수'] = pd.to_numeric(df_pop['인구수'])

df_fire = df_fire_raw.iloc[3:].copy()
df_fire = df_fire[['시도별(1)', '2024.2']]
df_fire.columns = ['지역', '산불건수']
df_fire['산불건수'] = pd.to_numeric(df_fire['산불건수'])

name_mapping = {
    '서울특별시': '서울', '부산광역시': '부산', '대구광역시': '대구', '인천광역시': '인천',
    '광주광역시': '광주', '대전광역시': '대전', '울산광역시': '울산', '세종특별자치시': '세종',
    '경기도': '경기', '강원특별자치도': '강원', '충청북도': '충북', '충청남도': '충남',
    '전라북도': '전북', '전라남도': '전남', '경상북도': '경북', '경상남도': '경남',
    '제주특별자치도': '제주'
}
df_fire['지역'] = df_fire['지역'].replace(name_mapping)

df_merged = pd.merge(df_pop, df_fire, on='지역')

plt.figure(figsize=(12, 8))
sns.regplot(data=df_merged, x='인구수', y='산불건수', scatter_kws={'s':100}, line_kws={'color':'red'})

for i in range(df_merged.shape[0]):
    plt.text(df_merged.인구수[i], df_merged.산불건수[i], df_merged.지역[i], 
             fontsize=11, fontweight='bold', va='bottom')

plt.title('시도별 인구수와 산불 발생의 상관관계 (10년 평균)', fontsize=15)
plt.xlabel('인구수 (명)')
plt.ylabel('산불 발생 건수 (건)')
plt.grid(True, alpha=0.3)
plt.show()
