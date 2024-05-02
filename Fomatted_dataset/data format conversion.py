import pandas as pd

# Load the original CSV file
df = pd.read_csv('my_data_test_o.csv')

# Function to format each row according to the Llama 2 prompt template
def format_row(row):
    return f'<s> [INST] <<SYS>> {row["text"]} <</SYS>> {row["instruction"]} [/INST] {row["output"]} </s>'

# Apply the formatting function to each row
df["formatted"] = df.apply(format_row, axis=1)

# Save the formatted data to a new CSV file
formatted_csv_path = 'mining_concepts_formatted_test_o.csv'
df["formatted"].to_csv(formatted_csv_path, index=False, header=False)

print(f'Formatted dataset saved to {formatted_csv_path}')


