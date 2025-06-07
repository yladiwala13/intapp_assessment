"""
Script to create Contacts table
"""

from cleaner import ContactsCleaner, EventsCleaner

contacts_df = ContactsCleaner().clean_and_transform()

lpd_event, mrc_event = EventsCleaner().load()

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
# TODO: Drop columns: Birthday, LPD, 19_MRC?
