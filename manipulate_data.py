import requests
import pandas as pd
from bs4 import BeautifulSoup
import sys

DATA = {}
COMP_NAME = sys.argv[1]


with open(f'{COMP_NAME}_soup.html', 'r', encoding='utf8') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')

# get company name and about
comp_info = soup.find('div', {'class': 'block mt2'})
comp_name = comp_info.find('span', {'dir': 'ltr'}).get_text().strip()
comp_about = comp_info.find('p', {'class': 'org-top-card-summary__tagline t-16 t-black'}).get_text().strip()

DATA['Company Name'] = [comp_name]
DATA['About Company'] = [comp_about]

# get company image
comp_img = soup.find('img', {'id': 'ember35'}) # changeable
image_url = comp_img['src']
img_data = requests.get(image_url).content

DATA['Company Logo'] = [img_data]

# save image
with open(f'{COMP_NAME}.jpg', 'wb') as handler:
    handler.write(img_data)

# get company location and type
comp_type = comp_info.find('div', {'class': 'org-top-card-summary-info-list__info-item'}).get_text().strip()
comp_location = comp_info.find('div', {'class': 'inline-block'}).find('div', {'class': 'org-top-card-summary-info-list__info-item'}).get_text().strip()

DATA['Company Type'] = [comp_type]
DATA['Company Location'] = [comp_location]

# get company's number of employees
to_comp_empl_cont = soup.find('div', {'class': 'org-top-card-secondary-content__connections display-flex mt4 mb1'})
comp_no_employees = to_comp_empl_cont.find('span', {'class': 'org-top-card-secondary-content__see-all t-normal t-black--light link-without-visited-state link-without-hover-state'}).get_text().strip()
f_comp_no_employees = comp_no_employees.split(' ')[0]

DATA['Employees Count'] = [f_comp_no_employees]

comp_analytics_block = soup.find('div', {'class': 'artdeco-card pb2'}).find('div', {'class': 'relative'}).find('div', {'class': 'org-people__insights-container'})
to_empl_unis = comp_analytics_block.find('li', {'class': 'artdeco-carousel__item ember-view'}).find('div', {'class': 'artdeco-card p4 m2 org-people-bar-graph-module__organization'}).find('div', {'class': 'insight-container'}).find_all('div', {'class': 'org-people-bar-graph-element__percentage-bar-info truncate full-width mt2 mb1 t-14 t-black--light t-normal'})
TOP = 5
employees_universities = [uni.get_text().strip() for uni in to_empl_unis]
top_employees_universities = employees_universities[:TOP]
f_top_employees_universities = [uni.split(' ', 1) for uni in top_employees_universities]

DATA['Top Universities'] = [f_top_employees_universities]

DATA_FRAME = pd.DataFrame(DATA)
print(DATA_FRAME.head())
DATA_FRAME.to_csv(f'{COMP_NAME}.csv')
