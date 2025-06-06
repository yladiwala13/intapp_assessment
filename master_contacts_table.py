import pandas as pd

# File paths
contacts_file_path = "Contacts.xlsx"
events_file_path = "Events.xlsx"
pe_comps_file_path = "PE Comps.xlsx"
bsp_file_path = "Business Services Pipeline.xlsx"
crhp_file_path = "Consumer Retail and Healthcare Pipeline.xlsx"

# Read in both of the sheets in 'Contacts'
t1_contacts_df = pd.read_excel(
    contacts_file_path, sheet_name="Tier 1's", header=0, engine="openpyxl"
)

t2_contacts_df = pd.read_excel(
    contacts_file_path, sheet_name="Tier 2's", header=0, engine="openpyxl"
)

# Mark if each contact is Tier 1 or Tier 2
t1_contacts_df["Tier"] = "1"
t2_contacts_df["Tier"] = "2"

# Concatenate Tier 1 & 2 contact sheets
contacts_df = pd.concat(
    [t1_contacts_df, t2_contacts_df], ignore_index=True
).sort_values("Tier")

# Keep the first occurance of each unique email
contacts_df = contacts_df.drop_duplicates(subset="E-mail", keep="first")
contacts_df.reset_index(drop=True, inplace=True)

# Read the two event attendee lists
lpd_event = pd.read_excel(
    events_file_path,
    sheet_name="Leaders and Partners Dinner",
    header=0,
    engine="openpyxl",
)

mrc_event = pd.read_excel(
    events_file_path, sheet_name="2019 Market Re-Cap", header=0, engine="openpyxl"
)

# Build series for each event. Ignoring 'Name' as it is not a key.
# Drop duplicate emails
# Set E-mail as the index and just retain Attendee Status column
lpd_event = (
    lpd_event[["E-mail", "Attendee Status"]]
    .drop_duplicates("E-mail", keep="first")
    .set_index("E-mail")["Attendee Status"]
)

mrc_event = (
    mrc_event[["E-mail", "Attendee Status"]]
    .drop_duplicates("E-mail", keep="first")
    .set_index("E-mail")["Attendee Status"]
)

# Map Attendee Status back to master contacts table
contacts_df["LPD"] = contacts_df["E-mail"].map(lpd_event)
contacts_df["19_MRC"] = contacts_df["E-mail"].map(mrc_event)

print(contacts_df)

# TODO: pytests?
