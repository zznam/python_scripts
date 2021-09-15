import numpy as np
import pandas as pd


# Create and populate a 3x4 NumPy array.
my_data = np.random.randint(1, 101, size=(3,4))
# Create a Python list that holds the names of the two columns.
my_column_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']


df = pd.DataFrame(data=my_data, columns=my_column_names)
print(df)
print("\nSecond row of the Eleanor column: %d\n" % df['Eleanor'][1])

# Create a new column named Janet.
df["Janet"] = df["Tahani"] + df["Jason"]

# Print the enhanced DataFrame
print(df)





# Create a reference by assigning my_dataframe to a new variable.
print("Experiment with a reference:")
reference_to_df = df

# Print the starting value of a particular cell.
print("  Starting value of df: %d" % df['Jason'][1])
print("  Starting value of reference_to_df: %d\n" % reference_to_df['Jason'][1])

# Modify a cell in df.
df.at[1, 'Jason'] = df['Jason'][1] + 5
print("  Updated df: %d" % df['Jason'][1])
print("  Updated reference_to_df: %d\n\n" % reference_to_df['Jason'][1])

# Create a true copy of my_dataframe
print("Experiment with a true copy:")
copy_of_my_dataframe = df.copy()

# Print the starting value of a particular cell.
print("  Starting value of my_dataframe: %d" % df['Eleanor'][1])
print("  Starting value of copy_of_my_dataframe: %d\n" % copy_of_my_dataframe['Eleanor'][1])

# Modify a cell in df.
df.at[1, 'Eleanor'] = df['Eleanor'][1] + 3
print("  Updated my_dataframe: %d" % df['Eleanor'][1])
print("  copy_of_my_dataframe does not get updated: %d" % copy_of_my_dataframe['Eleanor'][1])