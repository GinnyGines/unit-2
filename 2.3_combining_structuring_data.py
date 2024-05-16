#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Data-Transformation:-Combining-and-Structuring-Data" data-toc-modified-id="Data-Transformation:-Combining-and-Structuring-Data-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Data Transformation: Combining and Structuring Data</a></span><ul class="toc-item"><li><span><a href="#Combining-Data" data-toc-modified-id="Combining-Data-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Combining Data</a></span><ul class="toc-item"><li><span><a href="#concat" data-toc-modified-id="concat-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span><code>concat</code></a></span><ul class="toc-item"><li><span><a href="#axis=0" data-toc-modified-id="axis=0-1.1.1.1"><span class="toc-item-num">1.1.1.1&nbsp;&nbsp;</span><code>axis=0</code></a></span></li><li><span><a href="#axis=1" data-toc-modified-id="axis=1-1.1.1.2"><span class="toc-item-num">1.1.1.2&nbsp;&nbsp;</span><code>axis=1</code></a></span></li><li><span><a href="#join=&quot;inner&quot;" data-toc-modified-id="join=&quot;inner&quot;-1.1.1.3"><span class="toc-item-num">1.1.1.3&nbsp;&nbsp;</span><code>join="inner"</code></a></span></li></ul></li><li><span><a href="#merge" data-toc-modified-id="merge-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span><code>merge</code></a></span></li><li><span><a href="#join" data-toc-modified-id="join-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span><code>join</code></a></span></li><li><span><a href="#Summary" data-toc-modified-id="Summary-1.1.4"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Summary</a></span></li><li><span><a href="#💡-Check-for-understanding" data-toc-modified-id="💡-Check-for-understanding-1.1.5"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>💡 Check for understanding</a></span></li></ul></li><li><span><a href="#Structuring-Data-with-Pivot,-Stack/Unstack,-and-Melt" data-toc-modified-id="Structuring-Data-with-Pivot,-Stack/Unstack,-and-Melt-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Structuring Data with Pivot, Stack/Unstack, and Melt</a></span><ul class="toc-item"><li><span><a href="#Pivot" data-toc-modified-id="Pivot-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Pivot</a></span></li><li><span><a href="#Stack-and-Unstack" data-toc-modified-id="Stack-and-Unstack-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Stack and Unstack</a></span></li><li><span><a href="#Melt" data-toc-modified-id="Melt-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Melt</a></span></li><li><span><a href="#Summary" data-toc-modified-id="Summary-1.2.4"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Summary</a></span></li><li><span><a href="#💡-Check-for-understanding" data-toc-modified-id="💡-Check-for-understanding-1.2.5"><span class="toc-item-num">1.2.5&nbsp;&nbsp;</span>💡 Check for understanding</a></span></li></ul></li></ul></li></ul></div>

# # Data Transformation: Combining and Structuring Data

# ## Combining Data
# 
# When working with data, you often encounter situations where you need to combine or merge multiple datasets to gain more insights or perform further analysis.
# 
# Pandas provides functions for [combining different data sets](http://pandas.pydata.org/pandas-docs/stable/merging.html) based on [relational algebra](https://en.wikipedia.org/wiki/Relational_algebra): `join`, `merge` and `concat`.

# In[ ]:


import pandas as pd

# DataFrame 1: Sales information
df_sales = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Product': ['A', 'B', 'C', 'D'],
    'Quantity_Sold': [100, 200, 150, 120]
})

# DataFrame 2: Revenue information
df_revenue = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-05'],
    'Revenue': [1000, 1500, 1200, 800]
})

# DataFrame 3: Costs information
df_costs = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Costs': [500, 700, 600, 400]
})

# DataFrame 1: Sales information next 4 months
df_sales_2 = pd.DataFrame({
    'Date': ['2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08'],
    'Product': ['A', 'B', 'C', 'D'],
    'Quantity_Sold': [100, 200, 150, 120]
})


# ### `concat`
# 
# - `concat` is usually used when you want to combine two or more DataFrames vertically or horizontally.
# - It is commonly used when you have data split across multiple files or sources and want to stack them together to create a larger dataset.
# - Vertical concatenation is used when you want to add more rows to an existing DataFrame.
# - Horizontal concatenation is used when you want to add more columns to an existing DataFrame.
# - Example: combining monthly or yearly sales data: Suppose you have sales data for a retail store split across multiple files, where each file contains sales data for a specific month or year. You can use concat to vertically stack these DataFrames and create a single DataFrame containing the complete sales data for all months or years.

# `pd.concat` is used to concatenate multiple DataFrames.
# - The `axis` parameter determines the axis along which the DataFrames will be stacked. `axis=0` (the default) stacks the DataFrames vertically (along rows), while `axis=1` stacks them horizontally (along columns).

# #### `axis=0`

# In[ ]:


# Concatenate the sales, and sales_2 vertically (along rows)
pd.concat([df_sales, df_sales_2], axis=0)


# In[ ]:


# Concatenate the sales, revenue, and costs DataFrames vertically (along rows)
pd.concat([df_sales, df_revenue, df_costs], axis=0)


# #### `axis=1`

# In[ ]:


# Concatenate the sales, revenue, and costs DataFrames horizontally (along columns)
pd.concat([df_sales, df_revenue, df_costs], axis=1) # by default is outer, takes the union


# #### `join="inner"`

# - `Join` Parameter:
#     - The `join` parameter is used to specify how to handle the overlapping columns during concatenation.
#     - By default (`join='outer'`), all columns from all DataFrames are included in the result, and missing values are filled with NaN.
#     - If `join='inner'`, only the overlapping columns are included in the result, and non-overlapping columns are excluded.
# 

# In[ ]:


pd.concat([df_sales, df_revenue, df_costs], axis=0, join="inner")


# ### `merge`

# Merge is used to combine DataFrames based on a common column. By default, `merge` performs an *inner join*, where only the matching rows between the DataFrames are included in the result.

# In[ ]:


df_revenue.Date


# In[ ]:


# Merge the sales and revenue DataFrames on the 'Date' column (inner join)
# Only rows with a common value in the 'Date' column, present in both DataFrames, are included in the merged result.
pd.merge(df_sales, df_revenue, on='Date')


# If you want to perform an outer join, where all rows from both DataFrames are included, you can use `how='outer'`.

# In[ ]:


# Merge the sales and revenue DataFrames on the 'Date' column (outer join)
pd.merge(df_sales, df_revenue, on='Date', how='outer')


# If you want to include all rows from the left DataFrame and only the matching rows from the right DataFrame, you can use `how='left'`.

# In[ ]:


# Merge the sales and revenue DataFrames on the 'Date' column (left join)
pd.merge(df_sales, df_revenue, on='Date', how='left')


# Similarly, if you want to include all rows from the right DataFrame and only the matching rows from the left DataFrame, you can use `how='right'`.

# In[ ]:


# Merge the sales and revenue DataFrames on the 'Date' column (right join)
pd.merge(df_sales, df_revenue, on='Date', how='right')


# In these examples, we had the same column ('Date') in both DataFrames, but this is not always the case. To perform such joins, we use the `left_on` and `right_on` parameters.

# `df1.merge(df2, left_on='col_1', right_on='col_2', how='inner')`

# ### `join`

# `join()` works similarly to `merge()`. It is also used to combine DataFrames. However, there are some differences between the two:
# 
# 1. **Method of Combination:**
#    - `join()`: Combines DataFrames **based on their indexes**. It uses the index as the key to align the rows.
#    - `merge()`: Combines DataFrames **based on the values in specified columns**. It can use one or more columns as the keys to align the rows.
# 
# 2. **Default Behavior:**
#    - `join()`: By default, performs a left join, keeping all rows from the left DataFrame and filling missing values with NaN from the right DataFrame.
#    - `merge()`: By default, performs an inner join, keeping only the rows with matching values in both DataFrames.
# 
# 

# First, we set the 'Date' column as the index for all three DataFrames, as follows:

# In[ ]:


df_sales.set_index('Date', inplace=True)
df_revenue.set_index('Date', inplace=True)
df_costs.set_index('Date', inplace=True)


# Next, we use the `join()` method on `df_sales` to merge it with `df_revenue` and `df_costs`. By default, `join()` uses the 'Date' column as the key to merge the DataFrames.
# 
# The resulting df_combined DataFrame will contain all rows from df_sales along with corresponding revenue and costs information, where available. If there is no data for a specific date in either df_revenue or df_costs, the corresponding values will be filled with NaN.

# In[ ]:


# By default is a Left Join: Keep all rows from the left DataFrame and fill missing values with NaN from the right DataFrame.

df_sales.join([df_revenue, df_costs])


# In[ ]:


# Inner Join: Only include rows with matching 'Date' values in both DataFrames.
df_sales.join([df_revenue, df_costs], how='inner')


# In[ ]:


# Outer Join: Include all rows from both DataFrames and fill missing values with NaN where data is not available.
df_sales.join([df_revenue, df_costs],how='outer')


# ### Summary
# 
# - `concat` is used to combine two or more DataFrames vertically or horizontally. It's often used when data is split across multiple files and you want to create a larger dataset.
#   - Vertical concatenation adds more rows to a DataFrame.
#   - Horizontal concatenation adds more columns to a DataFrame.
#   - `pd.concat` is used with the `axis` parameter determining the axis along which the DataFrames will be stacked (`axis=0` for rows and `axis=1` for columns).
#   - The `join` parameter determines how to handle overlapping columns during concatenation. `join='outer'` includes all columns and fills missing values with NaN, while `join='inner'` includes only overlapping columns.
# - `merge` is used to combine DataFrames based on a common column.
#   - By default, `merge` performs an inner join, including only the matching rows between the DataFrames.
#   - `how='outer'` performs an outer join, including all rows from both DataFrames.
#   - `how='left'` performs a left join, including all rows from the left DataFrame and only matching rows from the right.
#   - `how='right'` performs a right join, including all rows from the right DataFrame and only matching rows from the left.
#   - If the columns to join on don't have the same name, `left_on` and `right_on` parameters are used.
# - `join` is used to combine DataFrames based on their indexes.
#   - By default, `join` performs a left join.
#   - The DataFrame's index can be set using `set_index` and then `join` can be used to merge on this index.
#   - Different types of joins (inner, outer) can be performed using the `how` parameter in the `join` function.

# ### 💡 Check for understanding

# In[7]:


import pandas as pd

# Dataset 1: Student information
df_students = pd.DataFrame({
    'StudentID': ['S1', 'S2', 'S3', 'S4'],
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Major': ['Physics', 'Mathematics', 'Chemistry', 'Biology']
})

# Create df_students_2 DataFrame
df_students_2 = pd.DataFrame({
    'StudentID': ['S5', 'S6'],
    'Name': ['Eve', 'Frank'],
    'Major': ['English', 'Computer Science']
})

# Dataset 2: Course enrollment information
df_courses = pd.DataFrame({
    'StudentID': ['S1', 'S2', 'S3', 'S5'],
    'Course': ['Physics 101', 'Mathematics 101', 'Chemistry 101', 'Biology 101']
})

# Dataset 3: Student grades
df_grades = pd.DataFrame({
    'StudentID': ['S1', 'S3', 'S4', 'S6'],
    'Grade': ['A', 'B', 'A', 'C']
})


# 1. Create a new DataFrame that contains the information from both `df_students` and `df_students_2`.
# 
# 2. Merge `df_students` and `df_courses` on the 'StudentID' column. Try all four types of merges (inner, outer, left, and right) and observe the differences.
# 
# 3. Set 'StudentID' as the index for `df_students`, `df_courses`, and `df_grades`. Then use `df_students.join` to combine all three datasets. Try different types of joins (inner, outer) and observe the differences.

# ## Structuring Data with Pivot, Stack/Unstack, and Melt

# These methods are useful for restructuring, aggregating, and reshaping data to better analyze and visualize it.

# ### Pivot

# - Pivot is used to create a new derived table from another one.
# - Allows us to reshape a DataFrame based on column values.
# - Converts unique values from one column into multiple columns.

# In[6]:


# Your answer goes here

1.
#Create a new DataFrame that contains the information from both df_students and df_students_2.
import pandas as pd
# Dataset 1: Student information
df_students = pd.DataFrame({
    'StudentID': ['S1', 'S2', 'S3', 'S4'],
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Major': ['Physics', 'Mathematics', 'Chemistry', 'Biology']
})
# Create df_students_2 DataFrame
df_students_2 = pd.DataFrame({
    'StudentID': ['S5', 'S6'],
    'Name': ['Eve', 'Frank'],
    'Major': ['English', 'Computer Science']
})
# Dataset 2: Course enrollment information
df_courses = pd.DataFrame({
    'StudentID': ['S1', 'S2', 'S3', 'S5'],
    'Course': ['Physics 101', 'Mathematics 101', 'Chemistry 101', 'Biology 101']
})
# Dataset 3: Student grades
df_grades = pd.DataFrame({
    'StudentID': ['S1', 'S3', 'S4', 'S6'],
    'Grade': ['A', 'B', 'A', 'C']
})
display(df_students, df_students_2, df_courses, df_grades)


# In[8]:


#Merge df_students and df_courses on the 'StudentID' column.
#Try all four types of merges (inner, outer, left, and right) and observe the differences.
print("Merge on StudentID:")
display(pd.merge(df_students, df_courses, on= "StudentID"))
print("inner Merge on StudentID:")
display(pd.merge(df_students, df_courses, on= "StudentID", how="inner"))
print("outer Merge on StudentID:")
display(pd.merge(df_students, df_courses, on= "StudentID", how="outer"))
print("left Merge on StudentID:")
display(pd.merge(df_students, df_courses, on= "StudentID", how="left"))
print("right Merge on StudentID:")
display(pd.merge(df_students, df_courses, on= "StudentID", how="right"))


# In[9]:


3.
import pandas as pd
# Dataset 1: Student information
df_students = pd.DataFrame({
    'StudentID': ['S1', 'S2', 'S3', 'S4'],
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Major': ['Physics', 'Mathematics', 'Chemistry', 'Biology']
})
# Create df_students_2 DataFrame
df_students_2 = pd.DataFrame({
    'StudentID': ['S5', 'S6'],
    'Name': ['Eve', 'Frank'],
    'Major': ['English', 'Computer Science']
})
# Dataset 2: Course enrollment information
df_courses = pd.DataFrame({
    'StudentID': ['S1', 'S2', 'S3', 'S5'],
    'Course': ['Physics 101', 'Mathematics 101', 'Chemistry 101', 'Biology 101']
})
# Dataset 3: Student grades
df_grades = pd.DataFrame({
    'StudentID': ['S1', 'S3', 'S4', 'S6'],
    'Grade': ['A', 'B', 'A', 'C']
})
#Set 'StudentID' as the index for df_students, df_courses, and df_grades.
df_st = df_students.set_index("StudentID", inplace=True)
df_co = df_courses.set_index("StudentID", inplace=True)
df_gr = df_grades.set_index("StudentID", inplace=True)
#Then use df_students.join to combine all three datasets. Try different types of joins (inner, outer) and observe the differences.
inner_join = df_students.join([df_courses, df_grades], how="inner")
outer_join = df_students.join([df_courses, df_grades], how="outer")
display(inner_join, outer_join)
display(join)


# ![](https://github.com/data-bootcamp-v4/lessons/blob/main/img/pivot.png?raw=true)

# In[ ]:





# In[20]:


import pandas as pd

# Load Chipotle dataset from an online source
url = 'https://raw.githubusercontent.com/data-bootcamp-v4/data/main/worldstats.csv'
df = pd.read_csv(url)


# In[19]:


df.head()


# In[23]:


# Pivot the DataFrame to see the GDP based on the country and year
df.pivot(index='country', columns='year', values=['Population'])


# In[16]:


pivot_df = df.pivot_table(index='country', columns='year', values['Population']


# ### Stack and Unstack

# In pandas, `stack()` and `unstack()` are two methods used to transform data between "wide" and "long" formats in a DataFrame.
# 
# - `stack()`: This method "stacks" the data, converting the **columns into rows**, and results in a multi-level index. It is useful when you have a DataFrame with multiple columns representing similar data, and you want to combine them into a single column.
# 
# - `unstack()`: This method does the opposite of `stack()`. It "unstacks" the data, converting the **index back into columns**, and results in a more "wide" format. It is useful when you have a DataFrame with multi-level index and you want to separate the levels into separate columns.
# 

# ![](https://github.com/data-bootcamp-v4/lessons/blob/main/img/stack.png?raw=true)

# In[ ]:


# Create a multi-index DataFrame using set_index with 'country' and 'year' as the index columns
df_multiindex = df.set_index(['country', 'year'])
df_multiindex


# In[ ]:


# Stack the DataFrame to convert columns into rows and create a Series
stacked_data = df_multiindex.stack()
stacked_data


# In[ ]:


# Unstack the Series back into a DataFrame with the 'year' level as columns
unstacked_data = stacked_data.unstack('year')

unstacked_data.head()


# ### Melt

# The `melt()` function in pandas is used to transform a DataFrame from a **wide format to a long format**, which is often more suitable for certain data analysis tasks. In the wide format, each row represents a unique observation, and each column represents a different variable. However, in the long format, multiple rows may represent the same observation, and a new column is introduced to distinguish between the different variables.

# ![](https://github.com/data-bootcamp-v4/lessons/blob/main/img/melt.png?raw=true)

# In[ ]:


# Melt the DataFrame, keeping 'country' and 'year' as identifier variables, and 'Population' and 'GDP' as value variables
melted_data = pd.melt(df, id_vars=['country', 'year'], value_vars=['Population', 'GDP'], var_name='Indicator', value_name='Value')
melted_data.head()


# ### Summary

# - `pivot` is used to create a new derived table from an existing one by reshaping a DataFrame based on column values and converting unique values from one column into multiple columns.
# - `stack` and `unstack` are used to transform data between "wide" and "long" formats.
#   - `stack` converts columns into rows, leading to a multi-level index. It's useful when multiple columns represent similar data that you want to combine into a single column.
#   - `unstack` does the opposite of `stack`, converting the index back into columns and leading to a more "wide" format. It's useful when a DataFrame has a multi-level index that you want to separate into different columns.
# - `melt` transforms a DataFrame from a wide format to a long format. It's useful for certain data analysis tasks where each row represents a unique observation in the wide format, but in the long format, multiple rows represent the same observation, and a new column is introduced to distinguish between different variables.

# ### 💡 Check for understanding

# You are given a DataFrame with sales data for a company. The DataFrame contains information about the sales of various products in different regions. Create a summary of the total sales for each product in each region.
# 
# 
# Dataset:
# 
# ```python
# import pandas as pd
# 
# data = {
#     'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
#     'Region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East', 'East'],
#     'Sales': [100, 150, 200, 120, 180, 240, 80, 110, 160]
# }
# 
# df = pd.DataFrame(data)
# ```
# 
# Expected output:
# 
# ```python
# Region   East  North  South
# 
# Product                    
# 
# A          80    100    120
# 
# B         110    150    180
# 
# C         160    200    240
# ```

# In[28]:


# Your code here

import pandas as pd

data = {
    'Product': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
    'Region': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East', 'East'],
    'Sales': [100, 150, 200, 120, 180, 240, 80, 110, 160]
}

df = pd.DataFrame(data)


# In[25]:


display(df)


# In[29]:


# Pivot table to summarize total sales for each product in each region
df.pivot_table(values='Sales', index='Product', columns='Region', aggfunc='sum')


# In[ ]:





# In[27]:




