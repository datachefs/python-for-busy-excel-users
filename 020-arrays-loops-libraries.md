# Session 2: Arrays, Loops, Libraries

##  Arrays and Loops
 We won't do a lot directly with arrays; mostly we will use pandas, which is kind of like a spreadsheet. But…

Basics of an array, a.k.a. list
- Cream per month, for 6 months
- Working with individual members of array
- append,

Loops
- Loops through and display, plus print total
- Store and print your crew's names: sort()
- using in vs traditional for loop:  len(),  for x in range(0, the length of the array)
- Sync your repo, and check it out online

Dictionaries, a.k.a. Associative Arrays
- Storing cream per person in an array
- print the names of your crew, then names and amount of cream


## Using Google
- How much cream: we want to generate data we can work with
- Time for Your Google: Python Random Number
- Loop through and create {} with name, amount of cream


## Methods and Modules

Methods (methods.py)
- why methods
- put into method as is
- my approach: tiny little baby steps: make a very small change, re-run it, make another small change: catch errors right away, less overwhelming (use comments to draft a short plan, then fill out actual code)
- new version: given list of names, return array of cream consumption per month for 5 months
- Sync your repo!
- New version: given list of names, items and categories, number of months, return: Month, name, category, what, amount

Sample code from a different example:
def my_function(x):
  return 5 * x

print(my_function(3))

def my_function(country = "Norway"):



## Libraries (libraries-excel.py)

Install the library

import xlsxwriter

Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write( 3, 5, "Hi There")

expenses = [
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
row = 0
col = 0

for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()

If We Have Time: Create One  Excel spreadsheet per Pirate

https://xlsxwriter.readthedocs.io/tutorial01.html


## Homework Ideas
- Play with Creating Your Own Methods, Read more at WC3
- Create a chart, such as a line chart?
- One Excel per Kitty pirate (because they are such divas)
- Play with conditional formatting?
- One Excel file with all the data, for pandas lessons