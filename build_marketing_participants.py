"""
Script to create Marketing Participants Table
"""
import pandas as pd
from cleaner import ContactsCleaner, EventsCleaner

contacts_df = ContactsCleaner().clean_and_transform()

lpd_event, mrc_event = EventsCleaner().load()

marketing_df = EventsCleaner().clean_and_transform(lpd_event, mrc_event)

# Create contact info dataframe
contacts_info = contacts_df[
    [
        "E-mail",
        "Firm",
        "Title",
        "Group",
        "Sub-Vertical",
        "Phone",
        "Secondary Phone",
        "City",
        "Birthday",
        "Preferred Contact Method",
    ]
]

# Left join marketing_df to contacts_info to bring contact info for each marketing participant
marketing_participants_df = pd.merge(
    marketing_df, contacts_info, on="E-mail", how="left"
)

print(marketing_participants_df)

# TODO: change column 'Group' to 'Vertical'?
# TODO: include 'Tier'?
# TODO: pytests?