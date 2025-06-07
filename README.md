# intapp_assessment
Assessment Part 2 Scripts

This git repository contains all scripts relevant to Part 2 of the Technical Assessment for the Intapp Data Migration Consultant role:

Files:
- **requirements.txt**: all python library requirements to run scripts
- **constants.py**: stores all table paths as constant values
- **cleaner.py**: creates class to load, clean, and transform all spreadsheets
- **build_contacts.py**: builds Contacts table containing a contacts Firm, Name, Title, Group, Sub-Vertical, E-mail, Phone, Secondary Phone, City, Birthday, Coverage Person, Preferred Contact Method, Tier, and finally, their attendee status at both the Leaders and Partners Dinner & the 2019 Market Re-Cap events.
- **build_marketing_participants.py**: builds a Marketing Participants table containing a participants Name, E-mail, attendee status at the Leaders and Partners Dinner, attendee status at the 2019 Market Re-Cap, Firm, Title, Group, Sub-Vertical, Phone, Secondary Phone, City, Birthday, & Preferred Contact Method
- **build_companies.py**: builds a Companies table which contains the Company Name, Business Description, Vertical, Sub Vertical, Current Owner, its historical EBITDA, LTM Revenue, LTM EBITDA, Enterpise Value & The Lead MD.
- **build_deals.py**: builds a Deals table which contains the Pipeline, Company Name, Current Owner, Business Description, Vertical, Sub Vertical, Enterprise Value, Equity Ivestment Est., Project Name, Date Added, Sourcing, Status, Portfolio Company Status, Active Stage, Passed Rationale, Invest. bank, Banker, Banker Email, Banker Phoen Number, Transaction Type, Lead MD. 
