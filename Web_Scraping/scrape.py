import requests
import datetime
from requests_html import HTML
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
url = "https://www.boxofficemojo.com/year/world/"
now = datetime.datetime.now()
year = now.year

# Extract html code from the URL
def url_to_text(url,filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html",'w') as f:
                f.write(html_text)
        return html_text
    return ""

# Extract the data and parse into csv
def parse_and_extract(url,name='2020'):
    html_text = url_to_text(url)
    r_html = HTML(html=html_text)
    # Use selector "." to find table class
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)
    table_data = []
    header_names = []
    if len(r_table) == 1:
        parsed_table = r_table[0]
        rows = parsed_table.find("tr")
        header_row = rows[0]
        header_cols = header_row.find("th")
        header_names = [x.text for x in header_cols]

        for row in rows[1:]:
            cols = row.find("td")
            row_data = []
            for i,col in enumerate(cols):
                row_data.append(col.text)
            table_data.append(row_data)

        df = pd.DataFrame(table_data, columns=header_names)
        path = os.path.join(BASE_DIR,'data')
        os.makedirs(path,exist_ok=True)
        filepath = os.path.join('data',f'{name}.csv')
        df.to_csv(filepath, index=False)


# Execution function to extract data from current year to last 10 years`
def run(start_year=None, years_ago=10):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    for i in range(0,years_ago+1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        parse_and_extract(url,name=start_year)
        print(f"finished {start_year}")
        start_year-=1


if __name__ == "__main__":
    run()



