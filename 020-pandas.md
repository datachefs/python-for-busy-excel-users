




# pandas

Every row has label, aka index
- By default number like Excel, but can be  name 


faster pandas:
https://gitlab.com/cheevahagadog/talks-demos-n-such/-/blob/master/PyGotham2019/PyGotham-updated.ipynb

https://www.kaggle.com/code/ceshine/1000x-faster-data-manipulation/notebook


https://pandastutor.com/index.html
- Build sessions around this

[Intro to Data Science](http://www.textbook.ds100.org/ch/06/pandas_subsetting.html)
- For explainations

https://github.com/aschneiderman/my-little-pandas-cookbook


[Effective Pandas](https://youtu.be/UURvPeczxJI)

My [old cookbook](https://nbviewer.org/github/aschneiderman/cookbook-notes/blob/master/cookbook/Pandas_4_Excel_Users.ipynb)


https://pandas.pydata.org/docs/user_guide/cookbook.html

https://www.samlau.me



https://datacarpentry.org/python-ecology-lesson/

http://pandas.pydata.org/pandas-docs/stable/

https://docs.bokeh.org/en/latest/


The row labels have a special name. We call them the index of a dataframe. even though the index looks like a column of data, the index really represents row labels, not data. 
.loc lets you select rows and columns using their labels. For example, to get the data in the row labeled 1 and column labeled Name
#        The first argument is the row label
#        ↓
baby.loc[1, 'Name']

# Shorthand for baby.loc[:, ['Name', 'Count']]
baby[['Name', 'Count']]


Slicing using .iloc works similarly to .loc, except that .iloc uses the positions of rows and columns rather than labels

To get the first three rows and first two columns by position, use .iloc:

dogs.iloc[0:3, 0:2]

grooming	food_cost
breed		
Labrador Retriever	weekly	466.0
German Shepherd	weekly	466.0
BeaTo get the first three rows and first two columns by position, use .iloc:

dogs.iloc[0:3, 0:2]

The same operation using .loc requires you to use the dataframe labels:

dogs.loc['Labrador Retriever':'Beagle', 'grooming':'food_cost']

Filtering 

# Get a Series with the Year data
baby['Year']

is_2020 = []
for value in baby['Year']:
    is_2020.append(value == 2020)
    
# Filtering has a shorthand. This computes the same table as the snippet above
# without using .loc
baby[baby['Year'] == 2020]

# When you have a long expression, you can wrap it in parentheses, then add
# line breaks to make it more readable.
(baby[baby['Year'] == 2020]
 .sort_values('Count', ascending=False)
 .head(7) # take the first seven rows
)


Filter: keep only rows with 'Luna' in the Name column.
Filter: keep only rows with 'F' in the Sex column.
Slice: keep the Count and Year columns.
Now, it’s a matter of translating each step into code.

luna = baby[baby['Name'] == 'Luna'] # [1]
luna = luna[luna['Sex'] == 'F']     # [2]
luna = luna[['Count', 'Year']]      # [3]
luna

# Using .query is similar to using .loc with a boolean series. query() has more
# restrictions on what kinds of filtering you can do but can be convenient as a
# shorthand. 
siri = (baby.query('Name == "Siri"')
        .query('Sex == "F"'))
px.line(siri, x='Year', y='Count', width=350, height=250)


homework:
use slashdot:  what do you think?
do some more googling
