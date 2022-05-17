import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.patches as mpatches
import sys
def main():
    random.seed(1403912)
    df = pd.read_csv('temperature_clean.csv')
    countries = df['country_id'].unique().tolist()
    full_names = []
    years = df['year'].unique().tolist()
    years.sort()
    data = {}
    data_years = {}
    for country in countries:
        country_df = df.loc[(df['country_id']==country)]
        full_names.append(country_df.iloc[0]['Country'])
        country_data = []
        country_years = []
        for year in years:
            mean = country_df.loc[country_df['year']== year]['AverageTemperatureCelsius'].mean()
            if not np.isnan(mean): 
                country_data.append(mean)
                country_years.append(year)
        data[country]=country_data
        data_years[country]=country_years

    numrows = 3
    numcols = 3
    fig, axs = plt.subplots(numrows,numcols,figsize=(10,5),sharex=True,sharey=True)

    # get random colors for plot
    colors = ['#%06X' % random.randint(0, 0xFFFFFF) for i in range(len(countries))]

    for row in range(numrows):
        for col in range(numcols):
            try:
                index = row*numcols + col
                country = countries[index]
                ax = axs[row,col]
                ax.set_title(full_names[index],fontsize=10)
                ax.grid(zorder=1)
                ax.plot(data_years[country],data[country], label=country, c=colors[index])
            except: pass
    plt.tight_layout(rect=(0.05,0.05,0.75,1))
    axs[2,2].remove()

    fig.supxlabel('year')
    fig.supylabel('countryAverage')

    handles = [mpatches.Patch(color=colors[i], label=full_names[i])
                for i in range(len(countries))]
    fig.legend(handles=handles, bbox_to_anchor=(0.95,0.7), title='Country')

if __name__=='__main__':
    main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            plt.show()
        elif int(sys.argv[1])==1:
            plt.savefig('5a.png')
            print('Saved to 5a.png')
    else: sys.exit('No argument given.')