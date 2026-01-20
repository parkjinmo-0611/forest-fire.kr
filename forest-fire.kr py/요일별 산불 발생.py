import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False 

try:
    df_day = pd.read_csv('요일별_산불발생_현황(97-24).csv', encoding='cp949')
except:
    df_day = pd.read_csv('요일별_산불발생_현황(97-24).csv', encoding='utf-8')

df_day_avg = df_day[(df_day['기간별'] == '10년평균') & 
                    (~df_day['요일별'].isin(['합계', '공휴일']))].copy()

weekday_order = ['월', '화', '수', '목', '금', '토', '일']
df_day_avg['요일별'] = pd.Categorical(df_day_avg['요일별'], categories=weekday_order, ordered=True)
df_day_avg = df_day_avg.sort_values('요일별')

df_day_plot = df_day_avg.melt(id_vars=['기간별', '요일별'], 
                              value_vars=['2022', '2023', '2024'], 
                              var_name='연도', value_name='발생건수')

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_day_plot, x='요일별', y='발생건수', hue='연도', marker='o', linewidth=2)

plt.title('요일별 산불 발생 추이 (10년 평균 기준, 2022-2024)', fontsize=15)
plt.xlabel('요일')
plt.ylabel('평균 발생 건수(건)')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

print("--- 요일별 10년 평균 데이터 확인 ---")
print(df_day_avg[['요일별', '2022', '2023', '2024']])
