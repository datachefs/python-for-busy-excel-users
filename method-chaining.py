You can also use query:

df.assign(sp_int = df.Speed.str.replace(' ms', '').astype(int)).query('sp_int < 1000')


Can turn this:
new_df = (
  df
  .loc[ df.Speed.apply(lambda x: int(x.replace(' ms', '')) < 1000) ]
  .assign(sp_int = df. Speed.apply(lambda x: int(x.replace(' ms', ''))))
  ...
)

Into this:

df_mc = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0).assign(point_ratio=df['point'] / 100).drop(columns='state').sort_values('age').head(3)
df_mc_break = pd.read_csv(
    'data/src/sample_pandas_normal.csv',
    index_col=0
).assign(
    point_ratio=df['point'] / 100
).drop(
    columns='state'
).sort_values(
    'age'
).head(
    3
)



# Clean up the `world_rank` 
def clean_world_rank(input_df):
    df = input_df.copy()
    df.world_rank = df.world_rank.str.split('-').str[0].str.split('='
).str[0]
    return df
    
# Assign the common years of `shanghai_df` and `times_df` to 
`common_years`    
common_years = set(shanghai_df.year) & set(times_df.year) 
# Print `common_years`
print(common_years)
# Filter years
def filter_year(input_df, years):
    df = input_df.copy()
    return df.query('year in {}'.format(list(years)))
# Clean `times_df` and `shanghai_df`
cleaned_times_df = (times_df.loc[:, common_columns]
                            .pipe(filter_year, common_years)
                            .pipe(clean_world_rank)
                            .assign(name='times'))
cleaned_shanghai_df = (shanghai_df.loc[:, common_columns]
                                  .pipe(filter_year, common_years)
                                  .pipe(clean_world_rank)
                                  .assign(name='shanghai'))



# Compose `ranking_df` with `cleaned_times_df` and 
`cleaned_shanghai_df`
ranking_df = pd.concat([cleaned_times_df, cleaned_shanghai_df])
# Calculate the percentage of missing data
missing_data = 100 * pd.isnull(ranking_df.total_score).sum() / len
(ranking_df)
# Drop the `total_score` column of `ranking_df`
ranking_df = ranking_df.drop('total_score', axis=1)



(pd.read_csv('data.csv')
   .fillna(...)
   .query('some_condition')
   .assign(new_column = df.cut(...))
   .pivot_table(...)
   .rename(...)
)
Method Chaining has always been available in Pandas, but support for chaining has increased through the addition of new “chain-able” methods. For example, query(), assign(), pivot_table(), and in particular pipe() for allowing user-defined methods in method chaining.

According to Titanic Data Dictionary, passengers departed from Southampton should have Embarked with value S . Let’s query that using the Pandas query() function.
res = (
  pd.read_csv('data/train.csv')
    .pipe(replace_age_na, pclass_age_map)
    .query('Embarked == "S"')
)
res.head()

3. Convert ages to groups of age ranges: ≤12, Teen (≤ 18), Adult (≤ 60) and Older (>60)
We did this with a custom function in the Pandas pipe function article. Alternatively, we can use Pandas built-in function assign() to add new columns to a DataFrame. Let’s go ahead withassign().
bins=[0, 13, 19, 61, sys.maxsize]
labels=['<12', 'Teen', 'Adult', 'Older']
res = (
  pd.read_csv('data/train.csv')
    .pipe(replace_age_na, pclass_age_map)
    .query('Embarked == "S"')
    .assign(ageGroup = lambda df: pd.cut(df['Age'], bins=bins, labels=labels))
)


Create a pivot table to display the survival rate for different age groups and Pclass
A pivot table allows us to insights into our data. Let’s figure out the survival rate with it.
bins=[0, 13, 19, 61, sys.maxsize]
labels=['<12', 'Teen', 'Adult', 'Older']
(
  pd.read_csv('data/train.csv')
    .pipe(replace_age_na, pclass_age_map)
    .query('Embarked == "S"')
    .assign(ageGroup = lambda df: pd.cut(df['Age'], bins=bins, labels=labels))
    .pivot_table(
        values='Survived', 
        columns='Pclass', 
        index='ageGroup', 
        aggfunc='mean')
)

(ramen['Stars']
     .replace('Unrated', None)
     .dropna()
     .astype('float64')
     .head())
     
     

do

(pd.read_csv('data.csv')
   .fillna(...)
   .query('some_condition')
   .assign(new_column = df.cut(...))
   .pivot_table(...)
   .rename(...)
)









We can see the wealthier passengers in the higher classes tend to be older, which makes sense. We’ll use these average age values to impute based on Pclass for Age.
pclass_age_map = {
  1: 37,
  2: 29,
  3: 24,
}
def replace_age_na(x_df, fill_map):
    cond=x_df['Age'].isna()
    res=x_df.loc[cond,'Pclass'].map(fill_map)
    x_df.loc[cond,'Age']=res
    return x_df
x_df['Age'].isna() selects the Age column and detects the missing values. Then, x_df.loc[cond, 'Pclass'] is used to access Pclass values conditionally and call Pandas map() for substituting each value with another value. Finally, x_df.loc[cond, 'Age']=res conditionally replace all missing Age values with res.
Running the following code
res = (
  pd.read_csv('data/train.csv')
    .pipe(replace_age_na, pclass_age_map)
)
res.head()
All missing ages should be replaced based on Pclass for Age




Let’s start by checking out missing values. We can use seaborn to create a simple heatmap to see where are missing values
sns.heatmap(df.isnull(), 
            yticklabels=False, 
            cbar=False, 
            cmap='viridis')
