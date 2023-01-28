import pandas as pd
from faker import Faker

# Initialize Faker
faker = Faker()

# read in existing file
existing_file = pd.read_csv('/home/sakabuana31/training/create_data/source/sales_data.csv')


# Create an empty dataframe
df = pd.DataFrame(columns=['invoice_number', 'customer_name', 'product', 'quantity', 'total_price'])

# Fill the dataframe with 10 random records
for i in range(20):
    df = df.append({'invoice_number': faker.random_number(digits=5),
                   'customer_name': faker.name(),
                   'product': faker.word(),
                   'quantity': faker.random_number(digits=2),
                   'total_price': faker.random_number(digits=4)}, ignore_index=True)

# specify the directory and file name to save the CSV file
file_path = '/home/sakabuana31/training/create_data/source/sales_data.csv'

# Save the dataframe to a CSV file
df.to_csv(file_path, index=False)

# read in new file
new_file = pd.read_csv('/home/sakabuana31/training/create_data/source/sales_data.csv')

# merge the two dataframes
merged_data = pd.concat([existing_file, new_file])

# save to new csv file in specific directory
merged_data.to_csv('/home/sakabuana31/training/create_data/source/sales_data.csv', index=False)
