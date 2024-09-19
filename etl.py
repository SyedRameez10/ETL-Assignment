import pandas as pd

# Function to read and clean data from the Excel file
def extract_and_transform(file_path):
    df = pd.read_excel(file_path)
    df_cleaned = df.dropna(subset=['address', 'lat', 'lng'])

    def extract_address_parts(address):
            street, city_state_zip_country = address.split(", ", 1)
            city, state_zip_country = city_state_zip_country.rsplit(", ", 1)
            state_code, zip_code = state_zip_country.split(" ")[0], state_zip_country.split(" ")[1]
            return pd.Series([street.split()[0], city, state_code, zip_code])
        

    df_cleaned[['house_no', 'city', 'state_code', 'zip_code']] = df_cleaned['address'].apply(extract_address_parts)
    df_transformed = df_cleaned.sort_values(by=['state_code', 'city'])

    return df_transformed
