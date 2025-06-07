"""
This class cleans all the tables to prepare them for final transformations & loading
"""
import pandas as pd
from constants import CONTACTS_PATH, EVENTS_PATH


class ContactsCleaner:
    """
    Class to clean & transform raw contacts spreadsheet
    """
    def __init__(self):
        self.path = CONTACTS_PATH
        self.tier_sheets ={
            'tier1': "Tier 1's",
            'tier2': "Tier 2's",
        }

    def clean_and_transform(self):
        """
        Cleans and transforms contacts spreadsheet
        """
        # Read in both of the sheets in 'Contacts'
        t1_contacts_df = pd.read_excel(
            self.path,
            sheet_name=self.tier_sheets['tier1'],
            header=0,
            engine="openpyxl"
        )

        t2_contacts_df = pd.read_excel(
            self.path,
            sheet_name=self.tier_sheets["tier2"],
            header=0,
            engine="openpyxl"
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

        return contacts_df

class EventsCleaner:
    """
    Class to clean & transform raw contacts spreadsheet
    """
    def __init__(self):
        self.path = EVENTS_PATH
        self.tier_sheets ={
            'lpd': "Leaders and Partners Dinner",
            '19_MRC': "2019 Market Re-Cap",
        }

    def load(self):
        """
        Loads in sheets for each event
        """
        lpd_event = pd.read_excel(
            EVENTS_PATH,
            sheet_name=self.tier_sheets['lpd'],
            header=0,
            engine="openpyxl",
        )

        mrc_event = pd.read_excel(
            EVENTS_PATH,
            sheet_name="2019 Market Re-Cap",
            header=0,
            engine="openpyxl"
        )

        return lpd_event, mrc_event
