__author__ = 'Yoni Rosenfeld'

import requests
import json
import csv


def main():
    username = input("Enter your Zendesk username ")
    password = input("Enter your Zendesk password ")
    response = requests.get('https://redislabs.zendesk.com/api/v2/organizations.json',
                            auth=(username, password))
    print("Searching for CC in organizations settings of Zendesk accounts")
    json_string = json.loads(response.text)
    org_list = []
    next_page = (json_string['next_page'])
    while next_page is not None:
        for cc in json_string['organizations']:
            org_list.append(cc)
            # can add code for deleting here
        response = requests.get(next_page,
                                auth=(username, password))
        json_string = json.loads(response.text)
        next_page = (json_string['next_page'])
        print(".", end=" ")
    for cc in json_string['organizations']:
        org_list.append(cc)

    # for a in org_list:
    #     if a['organization_fields']['cc_on_all_org_tickets'] is not None:
    #         print("Organization ID =", a['id'])
    #         print("Organization Name =", a['name'])
    #         print("CC = ", a['organization_fields']['cc_on_all_org_tickets'])

    print("\nWriting results to organization_list.csv file")
    with open('organization_list.csv', mode='w', newline='', encoding='utf-8') as employee_file:
        fieldnames = ['Organization_ID', 'Organization_Name', 'cc_on_all_org_tickets']
        writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
        writer.writeheader()
        for a in org_list:
            if a['organization_fields']['cc_on_all_org_tickets'] is not None:
                writer.writerow({'Organization_ID': a['id'], 'Organization_Name': a['name'],
                                 'cc_on_all_org_tickets': a['organization_fields']['cc_on_all_org_tickets']})
    print("Total Records reviewed -->", len(org_list))


if __name__ == '__main__':
    main()
