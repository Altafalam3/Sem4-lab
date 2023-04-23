import pandas as pd
import numpy as np

data = {
    'ISBN': ['978-1400079179', '978-0374533557', '978-0440241164', '978-0307277673', '978-0441013593', '978-0553382563', '978-0345453747', '978-0345538376', '978-0307278731', '978-0802144656'],
    'Title': ['The Kite Runner', 'The Brief Wondrous Life of Oscar Wao', 'The Da Vinci Code', 'The Road', 'Old Man’s War', 'The Devil in the White City', 'The Hitchhiker’s Guide to the Galaxy', 'Ready Player One', 'The Secret Life of Bees', 'The Book Thief'],
    'Author': ['Khaled Hosseini', 'Junot Diaz', 'Dan Brown', 'Cormac McCarthy', 'John Scalzi', 'Erik Larson', 'Douglas Adams', 'Ernest Cline', 'Sue Monk Kidd', 'Markus Zusak'],
    'Publication': ['Metro Publication', 'Riverhead Books', 'Anchor', 'Vintage', 'Tor Books', 'Vintage', 'Del Rey Books', 'Broadway Books', 'Penguin Books', 'Picador'],
    'Year Published': [2003, 2007, 2003, 2006, 2005, 2003, 1979, 2011, 2002, 2005],
    'Price': [15.00, 16.00, 8.99, 16.00, 7.99, 9.99, 7.99, 14.00, 10.00, 12.00],
    'Copies sold in first edition': [40000, 30000, 100000, 50000, 20000, 10000, 5000, 20000, 40000, 30000],
    'Copies sold in second edition': [30000, 20000, 50000, 40000, 15000, 8000, 3000, 15000, 25000, 20000],
    'Copies sold in third edition': [20000, 15000, 30000, 20000, 10000, 5000, 1000, 8000, 15000, 10000]
}

df = pd.DataFrame(data)

#To display the number of rows and columns in dataframe:
print(df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

#To give the descriptive statistics of the created dataset:
print(df.describe())

#describe copies sold in second edition
print(df['Copies sold in second edition'].describe())

#To display distinct publication names for the dataset:return array
print(df['Publication'].unique())

#To display the book title and author names published by “Metro Publication”:
print(df.loc[df['Publication'] == 'Metro Publication', ['Title', 'Author']])

#To rename columns “Copies sold in first edition”, “Copies sold in second edition” and “Copies sold in third edition”to FE, SE and TE respectively:
df = df.rename(columns={'Copies sold in first edition': 'FE', 'Copies sold in second edition': 'SE', 'Copies sold in third edition': 'TE'})
print(df.columns)

# To add a column “Average sale” to your dataframe derived as (average of FE, SE and TE) * Price:
df['Average sale'] = ((df['FE'] + df['SE'] + df['TE']) / 3) * df['Price']
print(df.head())

# To display the details of books grouped by author:
grouped_data = df.groupby('Author').agg({'Title': 'unique', 'Publication': 'unique', 'Price': 'mean', 'FE': 'sum', 'SE': 'sum', 'TE': 'sum', 'Average sale': 'mean'})
print(grouped_data)

# For each group obtained in above query display maximum value of Average sale:
max_sale = grouped_data['Average sale'].max()
print("Maximum value of Average sale:", max_sale)

# Reshape your dataframe such that rows will show ‘Author’, column will show “Publication” and values will be ‘Title’ of book
pivot_data = pd.pivot_table(df, values='Title', index=['Author'], columns=['Publication'], aggfunc=lambda x: ', '.join(x))
print(pivot_data)