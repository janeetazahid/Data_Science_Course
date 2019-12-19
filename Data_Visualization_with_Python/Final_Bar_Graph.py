
import matplotlib as mp1
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
df_survey=pd.read_csv(r"Topic_Survey_Assignment.csv")
df_survey.rename(columns={'Unnamed: 0':'Topic'},inplace=True)
df_survey.sort_values(['Very interested'],axis=0,ascending=False,inplace=True)
df_survey['Very interested']=df_survey['Very interested']/2233
df_survey['Very interested']=df_survey['Very interested']*100
df_survey['Somewhat interested']=df_survey['Somewhat interested']/2233
df_survey['Somewhat interested']=df_survey['Somewhat interested']*100
df_survey['Not interested']=df_survey['Not interested']/2233
df_survey['Not interested']=df_survey['Not interested']*100
df_survey
#df_survey.round({"Very interested": 2, "Somewhat interested": 2, "Not interested": 3})
ax = df_survey.plot(kind='bar', figsize=(20, 8),width=0.8,color=['#5cb85c','#5bc0de','#d9534f'])
ax.set_title('Precentage of Repondents Interest In Data Science Areas',fontsize=16)
for i in ax.patches:
   ax.text(i.get_x()+0.06,i.get_height()+0.01,str(round((i.get_height()),2)),fontsize=14)
ax.set_xticklabels(['Data Analysis/Statistics','Machine Learning','Data Visualization','Big Data(Spark/Hadoop)','Deep Learning','Data Journalism'],fontsize=14,rotation=90)
ax.set_yticks([])
ax.legend(prop=dict(size=14))
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')