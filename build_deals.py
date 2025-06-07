"""
Script to create Deals table
"""

import pandas as pd
from cleaner import BSPCleaner, CRHPCleaner

bsp_df = BSPCleaner().clean_and_transform()
crhp_df = CRHPCleaner().clean_and_transform()

# Concatenate the two dataframes
combined_pipelines_df = pd.concat([bsp_df, crhp_df], ignore_index=True)

# Select relevant columns for Deals table
deals_df = combined_pipelines_df[
    [
        "Pipeline",
        "Company Name",
        "Current Owner",
        "Business Description",
        "Vertical",
        "Sub Vertical",
        "Enterprise Value",
        "Equity Investment Est.",
        "Project Name",
        "Date Added",
        "Sourcing",
        "Status",
        "Portfolio Company Status",
        "Active Stage",
        "Passed Rationale",
        "Invest. Bank",
        "Banker",
        "Banker Email",
        "Banker Phone Number",
        "Transaction Type",
        "Lead MD",
    ]
]

print(deals_df)
