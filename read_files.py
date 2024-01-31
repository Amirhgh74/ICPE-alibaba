import os
import pandas as pd

def concatenate_directory_files(directory):
    # Initialize an empty list to store DataFrames
    df_list = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path)
            df_list.append(df)

    # Concatenate all DataFrames in the list
    return pd.concat(df_list, ignore_index=True)

# Define your directories (update paths as needed)
directories = {
    'CallGraph': '/home/amirhgh/projects/def-naser2/amirhgh/data/CallGraph',
    'MSMetrics': '/home/amirhgh/projects/def-naser2/amirhgh/data/MSMetrics',
    'MSRTMCR': '/home/amirhgh/projects/def-naser2/amirhgh/data/MSRTMCR',
    'NodeMetrics': '/home/amirhgh/projects/def-naser2/amirhgh/data/NodeMetrics'
}

result = {}

# Process each directory
for name, directory in directories.items():
    combined_df = concatenate_directory_files(directory)
    result[name] = combined_df


node_df = result['NodeMetrics']


# Sequential joins
# Step 1: Join Node and MSResource
combined_df = pd.merge(node_df, result['MSMetrics'], on=['timestamp', 'nodeid'], how='inner')

# Step 2: Join with MSRTMCR
combined_df = pd.merge(combined_df, result['MSRTMCR'], on=['timestamp', 'nodeid'], how='inner')

# Step 3: Join with MSCallGraph
# This step depends on the exact nature of your data and which columns align logically
combined_df = pd.merge(combined_df, result['CallGraph'], on=['timestamp'], how='inner')



combined_df.to_csv(f'/home/amirhgh/projects/def-naser2/amirhgh/data//combined.csv', index=False)

top_rows = combined_df.head(n=500000)

combined_df.to_csv(f'/home/amirhgh/projects/def-naser2/amirhgh/data/combined_top.csv', index=False)
print ("done")

