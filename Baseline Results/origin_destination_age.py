import pandas as pd

updated_book3_file_path = '/content/data/Book3.xlsx'
df_updated_book3 = pd.read_excel(updated_book3_file_path, header=0)

df_book3_processed = df_updated_book3[df_updated_book3['Location code'] < 900]
df_book3_final = df_book3_processed.iloc[:, 4:]

final_output_book3_path = '/content/data/final_processed_book3.csv'
df_book3_final.to_csv(final_output_book3_path, index=False)

# Group the dataframe by "Location code" and calculate the mean for each group
df_book3_avg = df_book3_final.groupby('Location code').mean().reset_index()

final_averaged_book3_path = '/content/data/final_averaged_book3.csv'
df_book3_avg.to_csv(final_averaged_book3_path, index=False)
