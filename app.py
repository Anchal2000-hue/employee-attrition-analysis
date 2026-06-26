import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Employee Attrition Analysis", page_icon="📊", layout="wide")
st.title("📊 Employee Attrition Analysis Dashboard")
st.markdown("**IBM HR Analytics Dataset | By Anchal Tiwari**")
st.markdown("---")

df = pd.read_csv("data/WA_Fn-UseC_-HR-Employee-Attrition.csv")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Employees", "1,470")
col2.metric("Employees Left", "237")
col3.metric("Attrition Rate", "16.12%")
col4.metric("Avg Salary Gap", "Rs.2,045")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Attrition by Department")
    dept = df.groupby("Department")["Attrition"].apply(lambda x: (x=="Yes").sum() / len(x) * 100).reset_index()
    dept.columns = ["Department", "AttritionRate"]
    fig, ax = plt.subplots()
    sns.barplot(data=dept, x="Department", y="AttritionRate", hue="Department", legend=False, palette="Blues_d", ax=ax)
    ax.set_ylabel("Attrition Rate (%)")
    st.pyplot(fig)

with col2:
    st.subheader("Overtime Impact")
    ot = df.groupby("OverTime")["Attrition"].apply(lambda x: (x=="Yes").sum() / len(x) * 100).reset_index()
    ot.columns = ["OverTime", "AttritionRate"]
    fig, ax = plt.subplots()
    sns.barplot(data=ot, x="OverTime", y="AttritionRate", hue="OverTime", legend=False, palette="Reds", ax=ax)
    ax.set_ylabel("Attrition Rate (%)")
    st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Age Distribution by Attrition")
    fig, ax = plt.subplots()
    sns.histplot(data=df, x="Age", hue="Attrition", bins=20, kde=True, palette=["steelblue","tomato"], ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Monthly Income vs Attrition")
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="Attrition", y="MonthlyIncome", hue="Attrition", legend=False, palette=["steelblue","tomato"], ax=ax)
    st.pyplot(fig)

st.markdown("---")
st.subheader("Key Insights")
st.markdown("""
- **Sales department** has the highest attrition at **20.63%**
- Employees working **overtime are 3x more likely** to leave (30.53% vs 10.44%)
- Departed employees earned **Rs.2,045 less** per month on average
- Employees aged **25-35** show the highest attrition rates
""")
st.caption("Prepared by Anchal Tiwari | B.Tech CSE 2026 | anchal.tiwari.dev@gmail.com")
