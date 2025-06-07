"""
This class cleans all the tables to prepare them for final transformations & loading
"""
import pandas as pd
from constants import CONTACTS_PATH, EVENTS_PATH, BSP_PATH, CRHP_PATH


class ContactsCleaner:
    """
    Class to load, clean & transform raw contacts spreadsheet
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
    Class to load, clean & transform raw contacts spreadsheet
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

    def clean_and_transform(self, lpd_event, mrc_event):
        """
        Cleans and transforms raw events spreadsheet
        """
        # Rename 'Name' columns in both sheets and dedupe
        lpd_participants = lpd_event.rename(
            columns={"Name": "LPD_Name", "Attendee Status": "LPD"}
        ).drop_duplicates(subset="E-mail", keep="first")

        mrc_participants = mrc_event.rename(
            columns={"Name": "MRC_Name", "Attendee Status": "19_MRC"}
        ).drop_duplicates(subset="E-mail", keep="first")

        # Outer join the two sheets to preserve all emails
        marketing_df = pd.merge(lpd_participants, mrc_participants, on="E-mail", how="outer")

        # Create a new 'Name' column and set it to LPD_Name values, \
        # filling in N/A's with MRC_Name values
        marketing_df["Name"] = marketing_df["LPD_Name"].fillna(marketing_df["MRC_Name"])

        # Drop irrelevant columns & reorder column names
        marketing_df = marketing_df.drop(columns=["LPD_Name", "MRC_Name"])

        marketing_df = marketing_df[["Name", "E-mail", "LPD", "19_MRC"]].reset_index(drop=True)

        return marketing_df

class BSPCleaner:
    """
    Class to load, clean, and transform raw business service pipeline table
    """
    def __init__(self):
        self.path = BSP_PATH

    def clean_and_transform(self):
        """
        Cleans & transforms raw BSP table
        """
        bsp_df = pd.read_excel(
            self.path,
            sheet_name = 'Sheet1',
            header=5,
            engine="openpyxl"
        )

        bsp_df['Pipeline'] = 'Business Services'

        return bsp_df

class CRHPCleaner:
    """
    Class to load, clean, and transofrm raw cosumer retail and healthcare table
    """
    def __init__(self):
        self.path = CRHP_PATH

    def clean_and_transform(self):
        """
        Cleans and transforms raw CRHP table
        """
        crhp_df = pd.read_excel(
            self.path,
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

        crhp_df['Pipeline'] = 'Consumer Retail and Healthcare'

        return crhp_df
