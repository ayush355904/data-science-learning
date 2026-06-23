import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/netflix_titles.csv")

# clean country data
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