import pandas as pd

df = pd.read_csv('movie_dataset.csv', header=0, sep=',')
df.rename(columns={'Runtime (Minutes)':'Runtime_Minutes', 'Revenue (Millions)':'Revenue_Millions'}, inplace=True)
df  = df[['Title', 'Genre', 'Director', 'Actors', 'Year', 'Rating', 'Revenue_Millions']]
df = df.dropna()
df.reset_index(drop=True)

#1. The Highest rated moview
print(df[df['Rating']==df['Rating'].max()].Title)

#2. Average Revenue
print(df['Revenue_Millions'].mean())

#3. Average Revenue from 2015 to 2017
df_rng = df[df['Year'] >= 2015]
df_rng = df_rng[df_rng['Year'] < 2017]
df_rng
print(df_rng['Revenue_Millions'].mean())

#4. Number of movies released in 2016
print(df[df['Year']==2016]['Year'].count())

#5. Number of movies directed by Christopher Nolan
print(df[df['Director']=='Christopher Nolan']['Director'].count())

#6. Number of movies with rating of at least 8.0
df[df['Rating'] >= 8]['Rating'].count()

#7. Median rating of movies directed by Christopher Nolan
df[df['Director']=='Christopher Nolan']['Rating'].median()

#8. Year with the highest average rating
grouped = df.groupby('Year')
yr_avg_rtngs = grouped['Year'].mean()
yr_avg_rtngs.max()

#10. The Most commmon actor in all the movies
actors = []
for actrs in df['Actors']:
    actors = actors + actrs.split(",")
actors

actors_df = pd.DataFrame({'actors':actors})#.str.strip()#.tolist() 
actors_df['actors'] = actors_df['actors'].str.strip() 
grp = actors_df.groupby('actors') ##.tolist()#.str.strip()
counts = grp['actors'].count()
counts.sort_values()

