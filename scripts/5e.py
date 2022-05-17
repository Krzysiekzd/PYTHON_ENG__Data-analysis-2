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

    country_cities = {}
    cities = df['City'].unique().tolist()
    cities_data = {i:[] for i in cities}
    data_years = {}
    for country in countries:
        country_df = df.loc[(df['country_id']==country)]
        full_names.append(country_df.iloc[0]['Country'])
        country_cities[country]=country_df['City'].unique().tolist()
        for city in country_cities[country]:
            city_df = df.loc[(df['City']==city)]
            city_data = []
            city_years = []
            for year in years:
                mean = city_df.loc[city_df['year']== year]['AverageTemperatureCelsius'].mean()
                if not np.isnan(mean): 
                    city_data.append(mean)
                    city_years.append(year)
            cities_data[city]=city_data
            data_years[city]=city_years

    numrows = 3
    numcols = 3
    fig, axs = plt.subplots(numrows,numcols,figsize=(10,5),sharex=True,sharey=True)

    # get random colors for plot
    colors = ['#%06X' % random.randint(0, 0xFFFFFF) for i in range(len(cities_data))]

    city_index = 0
    for row in range(numrows):
        for col in range(numcols):
            try:
                index = row*numcols + col
                country = countries[index]
                ax = axs[row,col]
                ax.set_title(full_names[index],fontsize=12,fontweight=800,color='#4f4f4f')
                ax.grid(zorder=1)
                for city in country_cities[country]:
                    ax.plot(data_years[city],cities_data[city], label=city, c=colors[city_index])
                    city_index+=1
            except: pass
    plt.tight_layout(rect=(0.05,0.05,0.8,0.95))
    axs[2,2].remove()

    fig.supxlabel('Year of observation',fontsize=14)
    fig.supylabel('Average temperature',fontsize=14)
    fig.suptitle('Average Temperature',fontsize=16,fontweight='bold')

    handles = [mpatches.Patch(color=colors[i], label=cities[i])
                for i in range(len(cities))]
    legend = fig.legend(handles=handles, bbox_to_anchor=(0.95,0.88), title='City',title_fontsize=16)

if __name__=='__main__':
    main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            plt.show()
        elif int(sys.argv[1])==1:
            plt.savefig('5e.png')
            print('Saved to 5e.png')
    else: sys.exit('No argument given.')