mapping_df_skipped.reset_index(drop=True, inplace=True)

country_name_column = mapping_df_skipped.columns[2] # Assuming this column contains country names
location_code_column = mapping_df_skipped.columns[4] # Assuming this column contains location codes

# Extracting the relevant columns and removing any duplicates or NaN values
country_and_code_corrected = mapping_df_skipped[[country_name_column, location_code_column]].dropna().drop_duplicates()

country_and_code_corrected.columns = ['Country Name', 'Location Code']
country_and_code_corrected.head()
