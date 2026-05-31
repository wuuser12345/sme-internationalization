from pathlib import Path

import pandas as pd


processed_file = Path("data/processed/panel_clean.parquet")
output_dir = Path("output/tables")
output_dir.mkdir(parents=True, exist_ok=True)

if not processed_file.exists():
    raise FileNotFoundError(
        "Clean panel not found. Please run code/02_clean.py first."
    )

df = pd.read_parquet(processed_file)

# Variables for descriptive statistics
desc_vars = ["roa", "firm_size", "leverage", "at", "nicon"]

available_vars = [var for var in desc_vars if var in df.columns]

summary = df[available_vars].describe().T

summary.to_csv(output_dir / "descriptive_statistics.csv")

# Firm-year count
firm_years = df.groupby("conm")["fyear"].count().reset_index()
firm_years.columns = ["company", "number_of_firm_year_observations"]
firm_years.to_csv(output_dir / "firm_year_counts.csv", index=False)

print("Descriptive statistics completed successfully.")
print(f"Saved summary table to: {output_dir / 'descriptive_statistics.csv'}")
print(f"Saved firm-year counts to: {output_dir / 'firm_year_counts.csv'}")
print(summary)
