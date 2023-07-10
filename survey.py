# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display

path = r"C:\Users\slopezgu\OneDrive - Capgemini\Desktop\Survey\responses.csv"
df = pd.read_csv(path, encoding='latin-1', on_bad_lines='skip', engine = 'python', delimiter=",")

pathinfo = r"C:\Users\slopezgu\OneDrive - Capgemini\Desktop\Survey\columns.csv"
info = pd.read_csv(pathinfo, encoding='latin-1', on_bad_lines='skip', engine = 'python', delimiter=",")

column_types = df.dtypes
info = pd.merge(column_types.rename('type'), info, left_index=True, right_on='short')

nulls = pd.DataFrame(df[df.columns[df.isnull().any()]].isnull().sum())
nulls['Percentage'] = df[df.columns[df.isnull().any()]].isnull().sum() / df.shape[0]
nulls = nulls.rename(columns={0: 'nulls'})

# Vemos que en muchos campos existe un único nulo. Comprobamos si es el mismo
operanull = df[df['Opera'].isnull()]
heightnull = df[df['Height'].isnull()]

# There is not a significative ammount of nulls in any field, and they do not seem to reflect any especific trend, so we keep moving
# Let´s check the distribution.

for column in df.columns:
    display(pd.crosstab(index=df[column], columns="% observations", normalize="columns"))

print(df.columns.tolist())

music_col = ['Music', 'Slow songs or fast songs', 'Dance', 'Folk', 'Country',
       'Classical music', 'Musical', 'Pop', 'Rock', 'Metal or Hardrock', 'Punk', 'Hiphop, Rap', 'Reggae, Ska', 'Swing, Jazz', 'Rock n roll', 'Alternative', 'Latino', 'Techno, Trance', 'Opera' ]
movies_col = ['Movies', 'Horror', 'Thriller', 'Comedy', 'Romantic', 'Sci-fi', 'War', 'Fantasy/Fairy tales', 'Animated', 'Documentary', 'Western', 'Action']
hobbies_col = ['History', 'Psychology', 'Politics', 'Mathematics', 'Physics', 'Internet', 'PC', 'Economy Management', 'Biology', 'Chemistry', 'Reading', 'Geography', 'Foreign languages', 'Medicine', 'Law', 'Cars', 'Art exhibitions', 'Religion', 'Countryside, outdoors', 'Dancing', 'Musical instruments', 'Writing', 'Passive sport', 'Active sport', 'Gardening', 'Celebrities', 'Shopping', 'Science and technology', 'Theatre', 'Fun with friends', 'Adrenaline sports', 'Pets']
phobias_col = ['Flying', 'Storm', 'Darkness', 'Heights', 'Spiders', 'Snakes', 'Rats', 'Ageing', 'Dangerous dogs', 'Fear of public speaking']
health_col = ['Smoking', 'Alcohol', 'Healthy eating']
personality_col = ['Daily events', 'Prioritising workload', 'Writing notes', 'Workaholism', 'Thinking ahead', 'Final judgement', 'Reliability', 'Keeping promises', 'Loss of interest', 'Friends versus money', 'Funniness', 'Fake', 'Criminal damage', 'Decision making', 'Elections', 'Self-criticism', 'Judgment calls', 'Hypochondria', 'Empathy', 'Eating to survive', 'Giving', 'Compassion to animals', 'Borrowed stuff', 'Loneliness', 'Cheating in school', 'Health', 'Changing the past', 'God', 'Dreams', 'Charity', 'Number of friends', 'Punctuality', 'Lying', 'Waiting', 'New environment', 'Mood swings', 'Appearence and gestures', 'Socializing', 'Achievements', 'Responding to a serious letter', 'Children', 'Assertiveness', 'Getting angry', 'Knowing the right people', 'Public speaking', 'Unpopularity', 'Life struggles', 'Happiness in life', 'Energy levels', 'Small - big dogs', 'Personality', 'Finding lost valuables', 'Getting up', 'Interests or hobbies', "Parents' advice", 'Questionnaires or polls', 'Internet usage', 'Finances']
personality_col1 = ['Criminal damage', 'Decision making', 'Elections', 'Self-criticism', 'Judgment calls', 'Hypochondria', 'Empathy', 'Eating to survive', 'Giving', 'Compassion to animals', 'Borrowed stuff', 'Loneliness']
personality_col2 = ['Daily events', 'Prioritising workload', 'Writing notes', 'Workaholism', 'Thinking ahead', 'Final judgement', 'Reliability', 'Keeping promises', 'Loss of interest', 'Friends versus money', 'Funniness', 'Fake']
personality_col3 = ['Cheating in school', 'Health', 'Changing the past', 'God', 'Dreams', 'Charity', 'Number of friends', 'Punctuality', 'Lying', 'Waiting', 'New environment', 'Mood swings']
personality_col4 = ['Appearence and gestures', 'Socializing', 'Achievements', 'Responding to a serious letter', 'Children', 'Assertiveness', 'Getting angry', 'Knowing the right people', 'Public speaking', 'Unpopularity', 'Life struggles', 'Happiness in life']
personality_col5 = ['Energy levels', 'Small - big dogs', 'Personality', 'Finding lost valuables', 'Getting up', 'Interests or hobbies', "Parents' advice", 'Questionnaires or polls', 'Internet usage']

spending_col = ['Finances', 'Shopping centres', 'Branded clothing', 'Entertainment spending', 'Spending on looks', 'Spending on gadgets', 'Spending on healthy eating']
demo_col = ['Age', 'Height', 'Weight', 'Number of siblings', 'Gender', 'Left - right handed', 'Education', 'Only child', 'Village - town', 'House - block of flats']
list_by_topics = [music_col, movies_col, hobbies_col, phobias_col, health_col, personality_col, demo_col]

#Let´s check the distribution

df['Smoking'] = pd.Categorical(df[('Smoking')])
df['Alcohol'] = pd.Categorical(df[('Alcohol')])

sns.countplot(x= 'Smoking',data=df)
sns.countplot(x= 'Alcohol',data=df)

plt.show()
df['Smoking'].replace(['never smoked', 'tried smoking', 'former smoker', 'current smoker'],
                        [0, 1, 2, 3], inplace=True)
df['Alcohol'].replace(['never', 'social drinker', 'drink a lot'],
                        [0, 1, 2], inplace=True)
df['Smoking'] = pd.to_numeric(df[('Smoking')])
df['Alcohol'] = pd.to_numeric(df[('Alcohol')])


music_hist = df[music_col].hist(bins=30, sharey=True, figsize=(10, 10))
hobbies_hist = df[hobbies_col].hist(bins=30, sharey=True, figsize=(10, 10))
phobias_hist = df[phobias_col].hist(bins=30, sharey=True, figsize=(10, 10))
health_hist = df[health_col].hist(bins=30, sharey=True, figsize=(10, 10))
#personality_hist = df[personality_col].hist(bins=30, sharey=True, figsize=(10, 10))
personality_hist1 = df[personality_col1].hist(bins=30, sharey=True, figsize=(10, 10))
personality_hist2 = df[personality_col2].hist(bins=30, sharey=True, figsize=(10, 10))
personality_hist3 = df[personality_col3].hist(bins=30, sharey=True, figsize=(10, 10))
personality_hist4 = df[personality_col4].hist(bins=30, sharey=True, figsize=(10, 10))
personality_hist5 = df[personality_col5].hist(bins=30, sharey=True, figsize=(10, 10))
spending_hist = df[spending_col].hist(bins=30, sharey=True, figsize=(10, 10))
demo_hist = df[demo_col].hist(bins=30, sharey=True, figsize=(10, 10))

# Convertimos variables categoricas a numéricas

   
#df['Left - right handed'] = pd.Categorical(df['Left - right handed'])
#df_data['SBP'] = pd.to_numeric(df_data['SBP'], errors='coerce')
#df_data['NRS_pain'] = df_data['NRS_pain'].astype('Int32')
