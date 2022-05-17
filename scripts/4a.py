import pandas as pd
import matplotlib.pyplot as plt
import sys
def main():
    df = pd.read_csv('temperature_clean.csv')
    years = df['year'].unique().tolist()
    years.sort()
    mean_temperatures = []

    for year in years:
        mean_temperatures.append(df.loc[df['year'] == year]['AverageTemperatureCelsius'].mean())

    fig, ax = plt.subplots(figsize=(10,5))
    ax.grid(zorder=1)
    ax.plot(years,mean_temperatures, c='black')
    ax.set_xlabel('year')
    ax.set_ylabel('Mean AverageTemperatureCelsius')


if __name__=='__main__':
    main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            plt.show()
        elif int(sys.argv[1])==1:
            plt.savefig('4a.png')
            print('Saved to 4a.png')
    else: sys.exit('No argument given.')