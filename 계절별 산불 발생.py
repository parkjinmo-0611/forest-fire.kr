import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df_season = pd.read_csv('계절별_산불발생_현황(97-24).csv', encoding='cp949')
except:
    df_season = pd.read_csv('계절별_산불발생_현황(97-24).csv', encoding='utf-8')

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False 

df_season_avg = df_season[(df_season['기간별'] == '10년평균') & (df_season['계절별'] != '합계')].copy()

df_season_final = df_season_avg[['계절별', '2022', '2023', '2024']]
df_plot = df_season_final.melt(id_vars='계절별', var_name='연도', value_name='발생건수')

plt.figure(figsize=(12, 6))
sns.barplot(data=df_plot, x='계절별', y='발생건수', hue='연도', palette='autumn')

plt.title('계절별 산불 발생 현황 (10년 평균, 2022-2024)', fontsize=15)
plt.xlabel('계절')
plt.ylabel('평균 발생 건수(건)')
plt.grid(axis='y', alpha=0.3)

plt.show()

#print("--- 데이터 표 ---")
#print(df_season_final)
