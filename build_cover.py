import os
from fpdf import FPDF

pdf = FPDF(format=(150, 200))
pdf.add_page()
pdf.set_font("Courier", size=15)
pdf.multi_cell(130, 8, txt="Facts about 15 companies\n in the egyptian market", align='C')
width = 25
a, b = 10, 30
images = os.listdir('./COMPANIES')

for i in range(len(images)):
    pdf.image(f'COMPANIES/{images[i]}/{images[i]}.jpg', a, b, w=width)
    b += 30
    if i == 4 or i == 9:
        b = 30
        a += 50


# add outer border
pdf.line(5, 5, 145, 5)
pdf.line(5, 195, 145, 195)
pdf.line(5, 5, 5, 195)
pdf.line(145, 5, 145, 195)

pdf.set_font("Courier", size=8)
pdf.set_text_color(3, 37, 126)
pdf.multi_cell(130, 1, txt="\n"*153)
pdf.cell(130, 0.3, txt="Made By: Nader Elhadedy", ln=1, align='C', link='https://www.linkedin.com/in/nader-elhadedy-8b6329191/')

pdf.output("trial.pdf")
