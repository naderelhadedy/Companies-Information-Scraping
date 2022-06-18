import ast
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

companies = os.listdir('./COMPANIES')

for i in range(len(companies)):
    print(f'Company: {companies[i]}')
    # read and prepare data
    df = pd.read_csv(f'COMPANIES/{companies[i]}/{companies[i]}.csv')
    top_unis = df['Top Universities']
    top_unis = ast.literal_eval(top_unis[0])
    counts, unis = zip(*top_unis)
    counts = tuple(map(int, counts))

    # set figure config
    sns.set_style("darkgrid")
    sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})

    # generate dashboard
    plt.figure(figsize=(10, 6))
    sns.barplot(y=list(unis), x=list(counts), palette="Blues_d")
    plt.xlabel('Number of Employees')
    plt.margins(y=0.1)
    n = range(len(unis))
    comp_total_empl = int(str(df['Employees Count'][0]).replace(',', ''))

    for j in range(len(unis)):
        plt.text(list(counts)[j], n[j]+0.1, f' {list(counts)[j]/comp_total_empl*100:.2f}%')

    plt.title("The percentage of employees in the company")

    plt.savefig(f'COMPANIES/{companies[i]}/{companies[i]}_dashboard.png', bbox_inches='tight')
    print(f'Dashboard of {companies[i]} company is saved successfully!')
