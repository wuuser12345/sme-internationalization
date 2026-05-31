from pathlib import Path

import pandas as pd
import statsmodels.formula.api as smf


processed_file = Path("data/processed/panel_clean.parquet")
output_dir = Path("output/tables")
output_dir.mkdir(parents=True, exist_ok=True)

if not processed_file.exists():
    raise FileNotFoundError(
        "Clean panel not found. Please run code/02_clean.py first."
    )

df = pd.read_parquet(processed_file)

# Keep only rows needed for regression
reg_df = df.dropna(subset=["roa", "firm_size", "leverage", "sic"]).copy()

# Convert industry code to categorical variable
reg_df["sic"] = reg_df["sic"].astype(str)

# Regression model
model = smf.ols(
    formula="roa ~ firm_size + leverage + C(sic)",
    data=reg_df
).fit(cov_type="HC3")

# Save regression output
with open(output_dir / "regression_results.txt", "w") as f:
    f.write(model.summary().as_text())

print("Regression completed successfully.")
print(f"Regression results saved to: {output_dir / 'regression_results.txt'}")
print(model.summary())
