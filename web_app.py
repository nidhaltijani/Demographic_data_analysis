import streamlit as st 
import pandas as pd 
import time
import matplotlib.pyplot as plt
st.title('Demographic data analysis')
df=pd.read_csv('adult.data.csv')
st.markdown('Our demographic dataset')
st.write(df.head())
average_age_men = df[df['sex']=='Male']['age'].mean()
col1,col2,col3=st.columns(3,)
with col1 :
    st.metric('average age of men',average_age_men)
percentage_bachelors = ((df[df['education']=='Bachelors']['education'].count())/len(df))*100
with col2 :
    st.metric('Percentage of people with Bachelors degree',percentage_bachelors)
#start
# What country has the highest percentage of people that earn >50K?
highest_earning_country = df[df['salary']=='>50K'].groupby('native-country').agg({'native-country':'count'})
total=df.groupby('native-country')['salary'].count()
#print(highest_earning_country)
percent=((highest_earning_country['native-country']/total)*100)
percent=percent.sort_values(ascending=False)
with col3:
    st.metric('testing',23)
my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.05)
     my_bar.progress(percent_complete + 1)

#st.balloons()
st.bar_chart(percent.sort_values(ascending=False)[:20])
fig , ax=plt.subplots()
ax.barh(y=percent[:10].index,width=percent[:10])
st.pyplot(fig)

#end