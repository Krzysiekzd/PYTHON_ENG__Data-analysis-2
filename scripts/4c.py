import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
def main():
    df = pd.read_csv('temperature_clean.csv')
    countries = df['country_id'].unique().tolist()
    years = df['year'].unique().tolist()
    years.sort()
    data = {}
    data_years = {}
    for country in countries:
        country_df = df.loc[(df['country_id']==country)]
        country_data = []
        country_years = []
        for year in years:
            mean = country_df.loc[country_df['year']== year]['AverageTemperatureCelsius'].mean()
            if not np.isnan(mean): 
                country_data.append(mean)
                country_years.append(year)
        data[country]=country_data
        data_years[country]=country_years

    fig, ax = plt.subplots(figsize=(10,5))
    ax.grid(zorder=1)

    for country in countries:
        ax.plot(data_years[country],data[country], label=country)

    ax.set_xlabel('year')
    ax.set_ylabel('country avarage')

    # Shrink current axis by 5%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.95, box.height])
    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Country')

if __name__=='__main__':
    main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            plt.show()
        elif int(sys.argv[1])==1:
            plt.savefig('4c.png')
            print('Saved to 4c.png')
    else: sys.exit('No argument given.')

