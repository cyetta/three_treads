#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import pandas as pd


#  Parse a site to search and display a given table
#  return DataFrame if all ok, None otherwise
#  example print_table('https://www.w3schools.com/html/html_tables.asp', 'ws-table-all')
def print_table(site_url, table_class_name):
    # Get a plane text of site page
    try:
        response = requests.get(site_url)
    except:
        print(f'Some problem with the site "{site_url}"')
        return None
    soup = BeautifulSoup(response.text, 'html.parser')

    # Search given table  by tag 'class:'
    table = soup.find('table', attrs={'class': table_class_name})
    if table == None:
        print(f'Table "{table_class_name}" not find')
        return None

    # Get a header from table and create DataFrame
    header = []
    for row in table.find_all('th'):
        header.append(row.text)
    df = pd.DataFrame(columns=header)

    # Create a for loop to fill data
    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(df)
        df.loc[length] = row

    print(df.to_string(index=None))
    return df
