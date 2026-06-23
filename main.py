import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/netflix_titles.csv")

countries = df["country"].dropna().str.split(",").explode()

top_countries = countries.value_counts().head(10)

print(top_countries)

plt.figure(figsize=(10,5))

top_countries.plot(kind="bar")

plt.title("Top 10 Countries on Netflix")

plt.xlabel("Country")

plt.ylabel("Number of Shows")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top10_countries.png", dpi=300, bbox_inches="tight")

plt.show()

movie_tv = df["type"].value_counts()

plt.figure(figsize=(6,6))

movie_tv.plot(kind="pie", autopct="%1.1f%%")

plt.title("Movies vs TV Shows")

plt.ylabel("")

plt.savefig("movies_vs_tv.png", dpi=300, bbox_inches="tight")

plt.show()

year_data = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(12,5))

year_data.plot(kind="line")

plt.title("Netflix Content by Release Year")

plt.xlabel("Year")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig("release_year_trend.png", dpi=300, bbox_inches="tight")

plt.show()

rating_data = df["rating"].dropna().value_counts().head(10)

plt.figure(figsize=(10,5))

rating_data.plot(kind="bar")

plt.title("Top 10 Ratings")

plt.xlabel("Rating")

plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top_ratings.png", dpi=300, bbox_inches="tight")

plt.show()





