import numpy as np
import pandas as pd

chipo = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv')
# print(chipo.describe())
# print(chipo.head())
# 1-----Getting & Knowing Your Data----
# Step 4. See the first 10 entries
# print(chipo.head(10))

#  Step 5. What is the number of observations in the dataset?
# print(len(chipo.index))

#  Step 6. What is the number of columns in the dataset?
#  Step 7. Print the name of all the columns.
# print(chipo.columns.values)

#  Step 8. How is the dataset indexed?
#  Step 9. Which was the most ordered item?
# items = chipo[['item_name', 'quantity']].groupby
# print(items.sort_values(['quantity'], ascending = False))

# 2---- Filtering & Sorting------
# Step 4. How many products cost more than $10.00?
# clean = lambda s: s.strip('$')
# chipo['item_price']= chipo['item_price'].apply(clean).apply(np.float64)
# morethanten = chipo.loc[chipo['item_price'] > 10.0]
# print(morethanten)

# Step 5. What is the price of each item?
# print a data frame with only two columns item_name and item_price
# prices = chipo.drop(['order_id', 'quantity', 'choice_description'], axis=1)
# print(prices)

# Step 6. Sort by the name of the item
# sprices = chipo.sort_values('item_name')
# print(sprices)

# Step 7. What was the quantity of the most expensive item ordered?
# mostexp = chipo.sort_values(by = 'item_price', ascending=False).head()
# print(mostexp)

# Step 8. How many times were a Veggie Salad Bowl ordered?
# vbawl = chipo[chipo.item_name == 'Veggie Salad Bowl'] = chipo['quantity'].sum(axis=0)
# print(vbawl)

# Step 9. How many times people orderd more than one Canned Soda?
# canned = chipo[chipo.item_name == 'Canned Soda']['quantity'] == 1
# print(canned)

# 3. ---------------Grouping-----------------
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|')
# print(users.head())
# Step 4. Discover what is the mean age per occupation
# mean_age = users.groupby(['age']).mean()
# print(mean_age)

# Step 5. Discover the Male ratio per occupation and sort it from the most to the least
# genders = users.groupby("occupation")["gender"].value_counts(normalize=True)*100
# print(genders.head())
# ratio = 

# Step 6. For each occupation, calculate the minimum and maximum ages
# min_max_age = users.groupby('occupation').age.agg([min, max])
# print(min_max_age)

# Step 7. For each combination of occupation and gender, calculate the mean age
# ocup_gender = users.groupby(['occupation', 'gender'])
# for i in ocup_gender:
#     result = ocup_gender.age.mean()
#     print(result) 

# Step 8. For each occupation present the percentage of women and men
users1 = users.groupby('occupation')
percentage = users1.groupby('')
# women = users[users.gender] == 'F'
# man = users[users.gender] == 'M'
print(users1)


# 4. -------------------Merge------------------------
# Step 2. Create the 3 DataFrames based on the followin raw data

raw_data_1 = {
'subject_id': ['1', '2', '3', '4', '5'],
'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
raw_data_2 = {
'subject_id': ['4', '5', '6', '7', '8'],
'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
raw_data_3 = {
'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
# Step 3. Assign each to a variable called data1, data2, data3
# Step 4. Join the two dataframes along rows and assign all_data
# Step 5. Join the two dataframes along columns and assing to all_data_col
# Step 6. Print data3

#5.----------------------Deleting-------------------------
# Step 4. Create columns for the dataset
# 1. sepal_length (in cm)
# 2. sepal_width (in cm)
# 3. petal_length (in cm)
# 4. petal_width (in cm)
# 5. class
# Step 5. Is there any missing value in the dataframe?
# Step 6. Lets set the values of the rows 10 to 29 of the column 'petal_length' to NaN
# Step 7. Good, now lets substitute the NaN values to 1.0
# Step 8. Now let's delete the column class









# petal_length, and petal_width
