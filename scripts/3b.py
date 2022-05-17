import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as rand
import sys
def main():
    df = pd.read_csv('temperature_clean.csv')
    c_ids = df['country_id'].unique()
    data = []
    for i in c_ids:
        data.append(df.loc[df['country_id'] == i]['AverageTemperatureCelsius'].tolist())

    fig, ax = plt.subplots(figsize=(10,5))
    ax.grid(zorder=1)
    ax.boxplot(data, zorder=3)
    ax.set_xticks(list(range(1,len(c_ids)+1)),labels=c_ids)
    ax.set_xlabel('country')
    ax.set_ylabel('AverageTemperatureCelsius')

    # add 'jitter'
    for index, i in enumerate(data,1):
        plt.scatter(x=rand.uniform(low=index-0.3, high=index+0.3, size=len(i)), y=i,
        facecolor='#1E88E5', edgecolor='#1E88E5', s=5,zorder=2, alpha=0.15)


if __name__=='__main__':
    main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            plt.show()
        elif int(sys.argv[1])==1:
            plt.savefig('3b.png')
            print('Saved to 3b.png')
    else: sys.exit('No argument given.')
