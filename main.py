import pandas as pd
df = pd.read_csv("data/netflix_titles.csv")
print(df.head())
print(df.columns)
print(df.shape)
print(df.info())
movies = df [df['type'] == "Movie"]
print("Movies:",len(movies))
shows = df[df["type"] == "TV Show"]

print("TV Shows:", len(shows))
print(df["country"].value_counts().head())
import matplotlib.pyplot as plt

df["type"].value_counts().plot(kind="bar")

plt.title("Movies vs TV Shows")

plt.xlabel("Type")

plt.ylabel("Count")

plt.show()