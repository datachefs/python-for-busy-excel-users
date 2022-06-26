# pandas

Like working with spreadsheets/tables of data

voyage = pd.read_excel(“pirates.xlsx”)
voyage.head()
voyage.info()

voyage = pd.read_csv(“pirates.csv”)
voyage


## Outputting data to a file
tags.to_csv(dir + r'Tags.csv', index=False)




Every row has label, aka index. Looks like a column of data, but in fact labels for the row
- By default number like Excel, but can be  name 

.loc lets you select rows and columns using their labels. For example, to get the data in the row labeled 1 and column labeled Name.  Slicing using .iloc works similarly to .loc, except that .iloc uses the positions of rows and columns rather than labels—e.g.,  dogs.iloc[0:3, 0:2]

voyage.loc[1, 'Name']
But we rarely use loc: mostly pulling either all data or rows of data based on criteria

Shorthand for voyage.loc[:, ['Name', 'Count']]
- voyage[['Name', 'Count']]


Filtering 

Get a Series with the Year data
voyage['Year']

is_2020 = []
for value in voyage['Year']:
    is_2020.append(value == 2020)
    
Filtering has a shorthand. This computes the same table as the snippet above
without using .loc
voyage[voyage['Year'] == 2020]

When you have a long expression, you can wrap it in parentheses, then add
line breaks to make it more readable.
(voyage[voyage['Year'] == 2020]
 .sort_values('Count', ascending=False)
 .head(7) # take the first seven rows
)


Filter: keep only rows with 'Luna' in the Name column.
Filter: keep only rows with 'F' in the Sex column.
Slice: keep the Count and Year columns.
Now, it’s a matter of translating each step into code.

luna = voyage[voyage['Name'] == 'Luna'] # [1]
luna = luna[luna['Sex'] == 'F']     # [2]
luna = luna[['Count', 'Year']]      # [3]
luna

Using .query is similar to using .loc with a boolean series. query() has more
restrictions on what kinds of filtering you can do but can be convenient as a
shorthand. 
siri = (voyage.query('Name == "Siri"')
        .query('Sex == "F"'))
px.line(siri, x='Year', y='Count', width=350, height=250)



## Cleaning up Data

From when you read in the file:
```
voyage = pd.read_excel(“pirates.xlsx”, usecols=[’Name’, ‘Cream’])
pastries = pd.read_csv('2012_pastries.csv', parse_dates=['Purchase Date'])

nation_template.fillna('', inplace=True)
google_analytics.rename(columns={'Campaign':'Google Tracking Code'}, inplace=True)

data_map = pd.merge( data_columns, nation, on="Client Field", how="left")
```




Series versus data frames
the whole weird thing of being billed on numpy
design for the Finance world by a geek in Finance.



With bigger data sets, redefining as types really matters

