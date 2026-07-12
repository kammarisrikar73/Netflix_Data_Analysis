import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.title("Netflix Data Analysis")
st.write("This is a netflix analysis dashboard here you observe the stats of the movies and tv shows in netflix dataset")
df = pd.read_csv("Data/cleaned_netflix.csv")
df.head()
df.info()
df.describe(include="all")
df.shape
df.columns
df.isnull().sum()
df.fillna("unknown",inplace=True)
df.drop_duplicates(inplace=True)
df["date_added"] = pd.to_datetime(df["date_added"],errors="coerce")
df.to_csv("cleaned_netflix.csv",index=False)
df["type"].value_counts().plot(kind="bar",color="green")
if st.button("click here to see the count of movies and tv shows"):
    plt.title("count of movies and tv shows")
    plt.xlabel("type")
    plt.ylabel("count")
    plt.legend(["movies","tv shows"])
    plt.savefig("netflix_analysis1.png")
    plt.show()
if st.button("click here to see the top 10 countries with most content"):
    country_counts = (df["country"].
                    dropna().str.split(",").value_counts().head(10))
    country_counts.plot(kind="bar",color="orange")
    plt.title("Top 10 countries with most content")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.savefig("netflix_analysis2.png")
    plt.show()
if st.button("click here to see the most releasing year"):
    df["release_year"].value_counts().sort_index().plot(kind="bar",color="orange")
    plt.title("most releasing year")
    plt.xlabel("release year")
    plt.ylabel("count")
    plt.legend(["count"])
    plt.savefig("netflix_analysis3.png")
    plt.show()
if st.button("click here to see the count of movies and tv shows released per year"):
    sns.barplot(data=df,y="release_year",hue="type")
    plt.title("most releasing year")
    plt.xlabel("release year")
    plt.ylabel("count")
    plt.legend(["count"])
    plt.savefig("netflix_analysis3.png")
    plt.show()
if st.button("click here to see the count of movies and tv shows by release year"):
    sns.barplot(data=df,y="release_year",hue="type")
    plt.title("count of movies and tv shows by release year")
    plt.xlabel("movies and tv shows")
    plt.ylabel("release year")
    plt.show()
    plt.savefig("netflix_analysis4.png")