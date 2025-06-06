import pandas as pd

# pe_comps_file_path = "PE Comps.xlsx"
bsp_file_path = "Business Services Pipeline.xlsx"
crhp_file_path = "Consumer Retail and Healthcare Pipeline.xlsx"

bsp_df = pd.read_excel(
    bsp_file_path, 
    sheet_name = 'Sheet1',
    header=5,
    engine="openpyxl"
)

crhp_df = pd.read_excel(
    crhp_file_path,
    sheet_name = 'CR&H Master',
    header = 8,
    engine = "openpyxl"
)

crhp_df.drop("Unnamed: 0", axis=1, inplace=True)

crhp_df.dropna(how="all", inplace=True)

crhp_df.reset_index(drop=True, inplace=True)

crhp_df.drop(crhp_df.index[-2:], axis=0, inplace=True)

crhp_df.rename(
    columns={
        'Est. Equity Investment': 'Equity Investment Est.'
    },
    inplace=True
)

bsp_df['Pipeline'] = 'Business Services'
crhp_df['Pipeline'] = 'Consumer Retail and Healthcare'

combined_pipelines_df = pd.concat([bsp_df, crhp_df], ignore_index=True)

company_df = combined_pipelines_df[
    [
        'Company Name',
        'Business Description',
        'Vertical',
        'Sub Vertical',
        'Current Owner',
        '2014A EBITDA',
        '2015A EBITDA',
        '2016A EBITDA',
        '2017A/E EBITDA',
        '2018E EBITDA',
        'LTM Revenue',
        'LTM EBITDA',
        'Enterprise Value',
        'Lead MD',
    ]
]

deals_df = combined_pipelines_df[
    [
        'Pipeline',
        'Company Name',
        'Current Owner',
        'Business Description',
        'Vertical',
        'Sub Vertical',
        'Enterprise Value',
        'Equity Investment Est.',
        'Project Name',
        'Date Added',
        'Sourcing',
        'Status',
        'Portfolio Company Status',
        'Active Stage',
        'Passed Rationale',
        'Invest. Bank',
        'Banker',
        'Banker Email',
        'Banker Phone Number',
        'Transaction Type',
        'Lead MD',
    ]
]

print(company_df)
print(deals_df)
