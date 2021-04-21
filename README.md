# cc_zendesk

This script will retrieve all the accounts that the cc_on_all_org_tickets field is not empty in zendesk.
It will store the results on a csv file.

## Requirements
1. python3
2. pip and virtualenv installed

On linux, if the virtualenv is missing install it by:

```
sudo apt-get install python3-pip
sudo pip3 install virtualenv virtualenvwrapper
```

 

## Installation instructions



1. Clone this repository 
```
git clone https://github.com/Redislabs-Solution-Architects/cc_zendesk.git
```
2. change directory to cc_zendesk.
3. Create a virtual environment directory:

On Windows:
```
python3 -m env env
```
On Linux and MacOS:
```
virtualenv -p /usr/bin/python3 env
```

4. Activate Virtual Environment 

```
source env/bin/activate
```

5. Install required modules
```
env/bin/pip install -r requirements.txt
```

6. Run the script by
```
env/bin/python search_cc_zendesk.py
```
The script will create an **organization_list.csv** file, containing all account with CC defined

In case of an error like:
PermissionError: [Errno 1] Operation not permitted: '/usr/bin/python3' -> '
It mean You are trying to create virtualenv on external SD card, so virtualenv cannot create symlinks and/or set executable permissions. Try to do this in your $HOME directory.
