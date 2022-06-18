import os
import pandas as pd
from fpdf import FPDF

# initializing pdf file
pdf = FPDF(format=(150, 200))  # H / (290, 138)

# building the cover page
pdf.add_page()
pdf.set_font("Courier", 'B', size=14)
pdf.multi_cell(130, 5, txt="Facts about some companies\n in the egyptian market", align='C')
pdf.set_font("Courier", 'I', size=10)
pdf.multi_cell(130, 10, txt="\"Top 5 universities that these companies hired from\"", align='C')

companies = os.listdir('./COMPANIES')
width = 25
a, b = 10, 30
comp_links = {'adamdotai': 'http://www.adam.ai/',
              'affectiva_2': 'http://www.affectiva.com/',
              'avidbeam': 'http://www.avidbeam.com/',
              'brightskies': 'https://www.brightskiesinc.com/',
              'cassbana': 'https://www.cassbana.com/',
              'dxwand': 'http://www.dxwand.com/',
              'giza-systems': 'http://www.gizasystems.com/',
              'itworx': 'http://www.itworx.com/',
              'jumia-egypt': 'https://www.jumia.com.eg/',
              'maxab': 'http://maxab.io/',
              'paymobcompany': 'http://www.paymob.com/',
              'rdi-the-engineering-company-for-digital-systems-development-': 'http://www.rdi-eg.ai/',
              'robusta-studio': 'https://robustastudio.com/',
              'synapse-analytics': 'https://synapse-analytics.io/',
              'tactfulai': 'https://www.tactful.ai/'}


# adding all images
for i in range(len(companies)):
    pdf.image(f'COMPANIES/{companies[i]}/{companies[i]}.jpg', a, b, w=width, link=comp_links[companies[i]])
    b += 30
    if i == 4 or i == 9:
        b = 30
        a += 50

# add outer border
pdf.line(5, 5, 145, 5)
pdf.line(5, 195, 145, 195)
pdf.line(5, 5, 5, 195)
pdf.line(145, 5, 145, 195)

# add footer
pdf.set_font("Courier", size=8)
pdf.set_text_color(3, 37, 126)
# pdf.multi_cell(130, 1, txt="\n"*153)
# pdf.cell(130, 0.3, txt="Made By: Nader Elhadedy", ln=1, align='C', link='https://www.linkedin.com/in/nader-elhadedy-8b6329191/')
print(f'PDF cover is added successfully!')

# building one page for each company
for i in range(len(companies)):
    print(f'Company: {companies[i]}')
    pdf.add_page()
    comp_df = pd.read_csv(f'COMPANIES/{companies[i]}/{companies[i]}.csv')
    pdf.set_font("Courier", 'B', size=15)
    pdf.set_text_color(0, 0, 0)
    # add company name
    pdf.cell(130, 5, txt=f"{comp_df['Company Name'][0]}", ln=1, align='C')
    pdf.cell(130, 5, txt="", ln=2, align='C')
    pdf.cell(130, 5, txt="", ln=3, align='C')
    pdf.set_font("Arial", size=12)
    # add company bio
    pdf.multi_cell(130, 5, txt=f"{comp_df['About Company'][0]}", align='C')
    # add company logo
    pdf.image(f'COMPANIES/{companies[i]}/{companies[i]}.jpg', 10, 40, w=35, link=comp_links[companies[i]])
    pdf.multi_cell(130, 5, txt="\n \n \n")

    # add company business type
    pdf.cell(140, 5, txt=f"- Type: {comp_df['Company Type'][0]}", ln=4, align='C')
    pdf.multi_cell(130, 5, txt="\n")
    # add company location
    pdf.cell(140, 5, txt=f"- Location: {comp_df['Company Location'][0]}", ln=5, align='C')

    if i not in [0, 1, 2, 5, 10, 11, 12, 13]:
        pdf.multi_cell(130, 5, txt="\n \n \n \n \n \n")
    else:
        pdf.multi_cell(130, 5, txt="\n \n \n \n \n")
    pdf.set_draw_color(0, 200, 70)
    pdf.line(10, 85, 135, 85)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_font("Arial", size=15)
    # add companies top 5 unis they hired from
    pdf.cell(130, 5, txt=f"Top 5 Universities {comp_df['Company Name'][0]} hired from", ln=6, align='C')
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(130, 5, txt="\n")
    # add expected total no. employees at company
    comp_total_empl = int(str(comp_df['Employees Count'][0]).replace(',', ''))
    pdf.cell(50, 5, txt=f"- Total No. Employees: {comp_total_empl}", ln=7, align='C')

    # add outer border
    pdf.line(5, 5, 145, 5)
    pdf.line(5, 195, 145, 195)
    pdf.line(5, 5, 5, 195)
    pdf.line(145, 5, 145, 195)

    # add company dashboard
    pdf.image(f'COMPANIES/{companies[i]}/{companies[i]}_dashboard.png', 8, 105, w=135, h=80)
    # pdf.image('robusta-studio-fig.png', 10, 110, w=130, h=80)

    # add footer
    # pdf.set_font("Arial", size=6)
    pdf.multi_cell(130, 0.4, txt="\n "*185)
    pdf.set_text_color(3, 37, 126)
    # pdf.set_y(-15)
    pdf.set_font('Arial', 'I', 6)
    pdf.cell(30, 0.3, txt="Made By: Nader Elhadedy", ln=8, align='C', link='https://www.linkedin.com/in/nader-elhadedy-8b6329191/')
    print(f'PDF page of {companies[i]} company is added successfully!')
    # break


# create closure page
pdf.add_page()
pdf.set_font("Courier", size=30)
pdf.set_text_color(0, 0, 0)

# add outer border
pdf.line(5, 5, 145, 5)
pdf.line(5, 195, 145, 195)
pdf.line(5, 5, 5, 195)
pdf.line(145, 5, 145, 195)

# create thanks page
pdf.multi_cell(130, 8, txt="\n\n\n\n\n\n\nThanks\n\n\n\n\n", align='C')
pdf.set_font("Courier", 'I', size=12)
pdf.set_text_color(3, 37, 126)
pdf.cell(130, 10, txt="Created in June 2022, based on LinkedIn data", ln=1, align='C')
pdf.set_font("Courier", 'B', size=10)
pdf.cell(130, 5, txt="Made By: Nader Mohamed Elhadedy", ln=2, align='C', link='https://www.linkedin.com/in/nader-elhadedy-8b6329191/')
pdf.set_font("Courier", size=7)
pdf.cell(130, 5, txt="linkedin.com/in/nader-elhadedy-8b6329191/", ln=3, align='C', link='https://www.linkedin.com/in/nader-elhadedy-8b6329191/')
# pdf.set_font("Courier", 'I', size=10)


print('Last page is finished!')

pdf.output("companies_facts.pdf")
print('####### Finished PDF Creation! #######')
