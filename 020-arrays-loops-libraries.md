# Session 2: Arrays, Loops, Libraries

##  Arrays and Loops

Arrays (arrays.py)
- your crew's names
- Working with individual members of array
- Storing cream per person in an array
- Sync your repo, and check it out online

Loops (loops.py)
- print the names of your crew, then names and amount of cream
- using in vs traditional for loop
- How much cream: we want to generate data we can work with
- Time for Your Google: Python Random Number
- Loop through and create {} with name, amount of cream

Associative Arrays
-  Being able to sort


## Libraries (libraries-excel.py)

Explore the library, play around a little bit with individual cells

Loops through to create spreadsheet given the data you made
- Try a Conditional formatting, play with colors 

Create a chart, such as a line chart?

One Excel file with all the data, for pandas lessons

One Excel per Kitty pirate (because they are such divas)

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()

https://xlsxwriter.readthedocs.io/tutorial01.html



## Homework

- Play with conditional formatting?