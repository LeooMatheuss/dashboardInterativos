import pandas as pd
import os

input_file = "data/raw/transacoes_financeiras_raw.csv"
output_file = "data/processed/transacoes_financeiras_clean.csv"


df = pd.read_csv(input_file)

df['Date'] = pd.to_datetime(df['Date']) 
df['YearMonth'] = df['Date'].dt.to_period('M') 
df['Amount'] = df['Amount'].astype(float)  

os.makedirs(os.path.dirname(output_file), exist_ok=True)
df.to_csv(output_file, index=False)
print(f"Arquivo processado gerado em: {output_file}")
