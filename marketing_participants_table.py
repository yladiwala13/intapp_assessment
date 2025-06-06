import pandas as pd

events_file_path = "Events.xlsx"
contacts_file_path = "Contacts.xlsx"

# Build Contacts table as before
# TODO: make this into a class to avoid repeat code

# Read in both of the sheets in 'Contacts'
t1_contacts_df = pd.read_excel(
    contacts_file_path,
    sheet_name="Tier 1's",
    header=0,
    engine="openpyxl"
)

t2_contacts_df = pd.read_excel(
    contacts_file_path,
    sheet_name="Tier 2's",
    header=0,
    engine="openpyxl"
)

# Mark if each contact is Tier 1 or Tier 2
t1_contacts_df['Tier'] = '1'
t2_contacts_df['Tier'] = '2'

# Concatenate Tier 1 & 2 contact sheets
contacts_df = (
    pd.concat([t1_contacts_df, t2_contacts_df], ignore_index=True)
        .sort_values("Tier")
)

# Keep the first occurance of each unique email
contacts_df = contacts_df.drop_duplicates(subset='E-mail', keep="first")
contacts_df.reset_index(drop=True, inplace=True)

# Read in the two event attendee lists
lpd_event = pd.read_excel(
    events_file_path,
    sheet_name="Leaders and Partners Dinner",
    header=0,
    engine="openpyxl"
)

mrc_event = pd.read_excel(
    events_file_path,
    sheet_name="2019 Market Re-Cap",
    header=0,
    engine="openpyxl"
)

# Rename 'Name' columns in both sheets and dedupe
lpd_participants = lpd_event.rename(columns={
    "Name": "LPD_Name",
    "Attendee Status": "LPD"
}).drop_duplicates(subset="E-mail", keep="first")

mrc_participants = mrc_event.rename(columns={
    "Name": "MRC_Name",
    "Attendee Status": "19_MRC"
}).drop_duplicates(subset="E-mail", keep="first")

# Outer join the two sheets to preserve all emails
marketing_df = pd.merge(
    lpd_participants,
    mrc_participants,
    on="E-mail",
    how="outer"
)

# Create a new 'Name' column and set it to LPD_Name values, filling in N/A's with MRC_Name values
marketing_df["Name"] = (
    marketing_df["LPD_Name"]
    .fillna(marketing_df["MRC_Name"])
)

# Drop irrelevant columns & reorder column names
marketing_df = marketing_df.drop(columns=["LPD_Name", "MRC_Name"])

marketing_df = marketing_df[
    ["Name", "E-mail", "LPD", "19_MRC"]
].reset_index(drop=True)

# Create contact info dataframe
contacts_info = contacts_df[[
    "E-mail",
    "Firm",
    "Title",
    "Group",
    "Sub-Vertical",
    "Phone",
    "Secondary Phone",
    "City",
    "Birthday",
    "Preferred Contact Method"
]]

# Left join marketing_df to contacts_info to bring contact info for each marketing participant
marketing_participants = pd.merge(
    marketing_df,
    contacts_info,
    on="E-mail",
    how="left"
)

print(marketing_participants)