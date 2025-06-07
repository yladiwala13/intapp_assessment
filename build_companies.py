"""
Script to create Companies table
"""

import pandas as pd
from cleaner import BSPCleaner, CRHPCleaner

bsp_df = BSPCleaner().clean_and_transform()
crhp_df = CRHPCleaner().clean_and_transform()

combined_pipelines_df = pd.concat([bsp_df, crhp_df], ignore_index=True)

company_df = combined_pipelines_df[
    [
        "Company Name",
        "Business Description",
        "Vertical",
        "Sub Vertical",
        "Current Owner",
        "2014A EBITDA",
        "2015A EBITDA",
        "2016A EBITDA",
        "2017A/E EBITDA",
        "2018E EBITDA",
        "LTM Revenue",
        "LTM EBITDA",
        "Enterprise Value",
        "Lead MD",
    ]
]

print(company_df)
