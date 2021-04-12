# cc_zendesk

This script will retrieve all the accounts that the cc_on_all_org_tickets field is not empty in zendesk.
It will store the results on a csv file.

# Requirements
1. python3
2. pip and virtualenv installed

On linux, if the virtualenv is missing install it by:

```
sudo apt-get install python3-pip
sudo pip3 install virtualenv virtualenvwrapper
```

 

# Installation instructions



1. Clone this repository 
```
git clone https://github.com/Redislabs-Solution-Architects/cc_zendesk.git
```
2. change directory to cc_zendesk.
Run the following commands to install the requirments for the script:


```
python3 -m env env
```
On ubuntu 20 i run the following:

```
virtualenv -p /usr/bin/python3 env
```
3. Install required modules
```
source env/bin/activate
env/bin/pip install -r requirements.txt
```

4. Run the script by
```
env/bin/python search_cc_zendesk.py
```
The script will create an organization_list.csv, containing all account with CC defined
