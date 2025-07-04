#zameencom-property-data-By-Kaggle.csv
import pandas as pd

#  Read csv file to DataFrame
#  Reference: https://pandas.pydata.org/docs/dev/reference/api/pandas.read_csv.html
#  Note below, date formatting - In Pandas, DateTime is a data type that represents a single point in time. It is especially useful when dealing with time-series data like stock prices, weather records, economic indicators etc.
df = pd.read_csv('Week2/zameencom-property-data-By-Kaggle-short.csv',delimiter=";",parse_dates=["date_added"], date_format={'date_added': '%d-%m-%Y'})

print(df)

print("df - data types" , df.dtypes)

print("df.info():   " , df.info() )

# display the last three rows
print('Last three Rows:')
print(df.tail(3))

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

#Summary of Statistics of DataFrame using describe() method.
print("Summary of Statistics of DataFrame using describe() method", df.describe())

#Counting the rows and columns in DataFrame using shape(). It returns the no. of rows and columns enclosed in a tuple.
print("Counting the rows and columns in DataFrame using shape() : " ,df.shape)
print()



# access the Name column
agency = df['agency']
print("access the Name column: df : ")
print(agency)
print()

"""
0            Real Biz International
1                       Khan Estate
2                   Shahum Estate 2
3                               NaN
4                               NaN
                   ...
144    Harum Real Estate & Builders
145                     Almo Estate
146              Gateway Properties
147             Chughtai Associates
148             Chughtai Associates
"""

# access multiple columns
agency_agent = df[['agency','agent']]
print("access multiple columns: df : ")
print(agency_agent)
print()


""""                           agency                    agent
0          Real Biz International               Usama Khan
1                     Khan Estate         mohsinkhan and B
2                 Shahum Estate 2  Babar Hameed, Raja Omar
3                             NaN                      NaN
4                             NaN                      NaN
..                            ...                      ...
144  Harum Real Estate & Builders                Rashid Ch
145                   Almo Estate              ALMO Estate
146            Gateway Properties           Muhammad Faraz
147           Chughtai Associates         Mehboob Chughtai
148           Chughtai Associates         Mehboob Chughtai"""




"""There are four primary ways to select rows with .loc. These include:
Selecting a single row
Selecting multiple rows
Selecting a slice of rows
Conditional row selection"""

# Case 1 : using .loc - default case - starts here
# Reference: https://www.datacamp.com/tutorial/loc-vs-iloc
# 
"""
Syntax               df.loc[row_indexer, column_indexer]              df.iloc[row_indexer, column_indexer]
Indexing Method      Label-based                                      Position-based indexing
Used for Reference   Row and column labels (names)                    Numerical indices of rows and columns (starting from 0)
"""
#Selecting a single row using .loc
second_row = df.loc[1]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df.loc[[1, 3]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df.loc[1:5]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()


#Conditional selection of rows using .loc
second_row4 = df.loc[df['agency'] == 'Sukhera Estate & Builders']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df.loc[:5,'agency']
print("#Selecting a single column using .loc")
print(second_row5)
print()

#Selecting multiple columns using .loc
second_row6 = df.loc[:1,['agency','agent']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df.loc[:1,'location':'agency']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df.loc[df['agency'] == 'Sukhera Estate & Builders','location':'agency']
print("#Combined row and column selection using .loc")
print(second_row8)
print()
# Case 1 : using .loc - default case - ends here


print("# Case 2 : using .loc with index_col - starts here")
# Case 2 : using .loc with index_col - starts here
# Second cycle - with index_col as property_id
# Why Second cycle - Note Index - , index_col='property_id'
df_index_col = pd.read_csv('Week2/zameencom-property-data-By-Kaggle-short.csv',delimiter=";",parse_dates=[14], date_format={'date_added': '%d-%m-%Y'} , index_col='property_id')

print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())
# Second cycle - with index_col as property_id

#Selecting a single row using .loc
second_row = df_index_col.loc[482892]
print("#Selecting a single row using .loc")
print(second_row)
print()

#Selecting multiple rows using .loc
second_row2 = df_index_col.loc[[482892, 555962]]
print("#Selecting multiple rows using .loc")
print(second_row2)
print()

#Selecting a slice of rows using .loc
second_row3 = df_index_col.loc[482892:686990]
print("#Selecting a slice of rows using .loc")
print(second_row3)
print()

#Conditional selection of rows using .loc
second_row4 = df_index_col.loc[df_index_col['agency'] == 'Gateway Properties']
print("#Conditional selection of rows using .loc")
print(second_row4)
print()

#Selecting a single column using .loc
second_row5 = df_index_col.loc[:686990,'agency']
print("#Selecting a single column using .loc")
print(second_row5)
print()


#Selecting multiple columns using .loc
second_row6 = df_index_col.loc[:686990,['agency','agent']]
print("#Selecting multiple columns using .loc")
print(second_row6)
print()

#Selecting a slice of columns using .loc
second_row7 = df_index_col.loc[:686990,'location':'agency']
print("#Selecting a slice of columns using .loc")
print(second_row7)
print()

#Combined row and column selection using .loc
second_row8 = df_index_col.loc[df_index_col['agency'] == 'Gateway Properties','location':'agency']
print("#Combined row and column selection using .loc")
print(second_row8)
print()

# Case 2 : using .loc with index_col  -  ends here


print("# Case 3 : Using .iloc - starts here")
# Case 3 : Using .iloc - starts here
"""Using .iloc: Selection by Integer Position
.iloc selects by position instead of label. This is the standard syntax of using .iloc: df.iloc[row_indexer, column_indexer]. There are two special things to look out for:

Counting starting at 0: The first row and column have the index 0, the second one index 1, etc.
Exclusivity of range end value: When using a slice, the row or column specified behind the colon is not included in the selection."""

#Selecting a single row using .iloc
second_row = df_index_col.iloc[0]
print("#Selecting a single row using .iloc")
print(second_row)
print()

#Selecting multiple rows using .iloc
second_row2 = df_index_col.iloc[[1, 3,5]]
print("#Selecting multiple rows using .iloc")
print(second_row2)
print()

#Selecting a slice of rows using .iloc
second_row3 = df_index_col.iloc[2:5]
print("#Selecting a slice of rows using .iloc")
print(second_row3)
print()

#Selecting a single column using .iloc
second_row5 = df_index_col.iloc[:,2]
print("#Selecting a single column using .iloc")
print(second_row5)
print()

#Selecting multiple columns using .iloc
second_row6 = df_index_col.iloc[:,[2,4]]
print("#Selecting multiple columns using .iloc")
print(second_row6)
print()

#Selecting a slice of columns using .iloc
second_row7 = df_index_col.iloc[:,2:4]
print("#Selecting a slice of columns using .iloc")
print(second_row7)
print()

#Combined row and column selection using .iloc
second_row8 = df_index_col.iloc[[1, 3,5],2:4]
print("#Combined row and column selection using .iloc")
print(second_row8)
print()

# Case 3 : Using .iloc - ends here

# Next Run 
print("Next Run")

""""Pandas DataFrame Manipulation
DataFrame manipulation in Pandas involves editing and modifying existing DataFrames. Some common DataFrame manipulation operations are:

Adding rows/columns
Removing rows/columns
Renaming rows/columns"""

#Add a New Row to a Pandas DataFrame
# add a new row
# Copy array from list and add to DataFrame
# 3477952;82;"https://www.zameen.com/Property/lahore_model_town_6_kanal_excellent_house_for_sale_in_model_town-347795-8-12.html";"House2";2200000002;"Model Town2";"Lahore2";"Punjab2";312.483868658082;742.325685501099;02;"6 Kanal2";"For Sale2";02;"07-17-2019";"Real Biz International2";"Usama Khan2"
print("------")
df.loc[len(df.index)] = [3477952,82,"https://www.zameen.com/Property/lahore_model_town_6_kanal_excellent_house_for_sale_in_model_town-347795-8-12.html","House2",2200000002,"Model Town2","Lahore2","Punjab2",312.483868658082,742.325685501099,2,"6 Kanal2","For Sale2",2,"07-17-2019","Real Biz International2","Usama Khan2"] 
print("Modified DataFrame - add a new row:")
print(df)
print()


#Remove Rows/Columns from a Pandas DataFrame


# delete row with index 1
df.drop(1, axis=0, inplace=True)
# delete row with index 1
df.drop(index=2, inplace=True)
# delete rows with index 3 and 5
df.drop([3, 5], axis=0, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame - Remove Rows:")
print(df)



# delete age column
df.drop('page_url', axis=1, inplace=True)
# delete marital status column
df.drop(columns='property_type', inplace=True)
# delete height and profession columns
df.drop(['location', 'city'], axis=1, inplace=True)
# display the modified DataFrame after deleting rows
print("Modified DataFrame -  delete page_url ,property_type , location , city , column :")
print(df)


#Rename Labels in a DataFrame
# rename column 'Name' to 'First_Name'
df.rename(columns= {'province_name': 'province_nameChanged'}, inplace=True)
# rename columns 'Age' and 'City'
df.rename(mapper= {'bedrooms': 'bedrooms_Changed', 'date_added':'date_added_Changed'}, axis=1, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame  - Rename Labels :")
print(df)


#Example: Rename Row Labels
# rename column one index label
df.rename(index={0: 7}, inplace=True)
# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)
# display the DataFrame after renaming column
print("Modified DataFrame - Rename Row - 0  >>> 7 , 1 >>> 10 , 2 >>> 100  Labels:")
print(df)



#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.

# select the rows where the age is greater than 25
selected_rows = df.query('agency == \'Gateway Properties\' or price > 11000000')

print(selected_rows.to_string())
print(len(selected_rows))



# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='price')
print(sorted_df.to_string(index=False))

#Sort Pandas DataFrame by Multiple Columns

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['price', 'location_id'])

print("Sorting by 'price' (ascending) and then by 'location_id' (ascending):\n")
print(df1.to_string(index=False))


"""
Reference: https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/
Explanation: This code creates a DataFrame from a dictionary with three columns (Weight, Name, Age), structures it into a tabular format using pd.DataFrame() and converts it into a fully visible string representation with df.to_string().

Syntax
DataFrame.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep=’NaN’, formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal=’.’, line_width=None)


Parameters:

buf: Buffer to write the output string to (e.g., a file). Defaults to None, which means the output is returned as a string.
columns: Specifies a subset of columns to include in the output. If None, all columns are printed.
col_space: Defines the minimum width of each column.
header: Whether to print column names. Can also accept a list of column name aliases.
index: Whether to include index labels. Default is True.
na_rep: String representation for missing values (NaN). Default is ‘NaN’.
formatters: Dictionary or list of functions to apply to columns for formatting their output.
float_format: Formatter function to apply specifically to floating-point numbers.
sparsify: Controls hierarchical index formatting. If False, prints every multi-index key at each row.
index_names: Whether to print index names. Default is True.
justify: Alignment of column headers (‘left’, ‘right’, ‘center’, ‘justify’ or ‘justify-all’).
max_rows: Maximum number of rows to display. If exceeded, truncates output.
max_cols: Maximum number of columns to display. If exceeded, truncates output.
show_dimensions: If True, displays the shape (rows x columns) of the DataFrame.
decimal: Specifies the character for decimal separation (e.g., ‘,’ for European formatting).
line_width: Defines the maximum character width of a row before wrapping text."""



#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

# group the DataFrame by the location_id column and
# calculate the sum of price for each category
grouped = df.groupby('location_id')['price'].sum()

print(grouped.to_string())
print("grouped :" , len(grouped))


""""Pandas Data Cleaning
Data cleaning means fixing and organizing messy data. Pandas offers a wide range of tools and functions to help us clean and preprocess our data effectively.
"""
# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)


# filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)



# create a list named data
data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()

#Pandas Reshape
#In Pandas, reshaping data refers to the process of converting a DataFrame from one format to another for better data visualization and analysis.
#Pandas provides multiple methods like pivot(), pivot_table(), stack(), unstack() and melt() to reshape data. We can choose the method based on our analysis requirement.


# to be continued....