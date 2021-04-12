# cc_zendesk

This script will log in to zendesk and retrieve all the accounts that the cc_on_all_org_tickets field is not empty.

It will store the results on a csv file.

 

Installation instructions

create a directory on your computer. 
change directory to the newly created directory.

clone this repository 

From inside the directory  you created, run the following commands to install the requirments for the script:



python3 -m env env
env/bin/pip install -r requirements.txt
Run the script by



env/bin/python cc_zendesk.py
The script will create an organization_list.csv, containing all account with CC defined
