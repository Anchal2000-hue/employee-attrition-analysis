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
st.caption("Prepared by Anchal Tiwari | B.Tech CSE 2026")
