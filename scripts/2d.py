import pandas as pd
import matplotlib.pyplot as plt
import sys
def main():
    df = pd.read_csv('temperature_clean.csv')
    x = df['year']
    y = df['AverageTemperatureCelsius']

    fig, ax = plt.subplots(figsize=(10,5))
    ax.grid(zorder=1)
    ax.scatter(x,y, facecolor='#1E88E5', edgecolor='#1E88E5', s=5,zorder=2, alpha=0.15)
    ax.set_xlabel('year')
    ax.set_ylabel('AverageTemperatureCelsius')

if __name__=='__main__':
    main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            plt.show()
        elif int(sys.argv[1])==1:
            plt.savefig('2d.png')
            print('Saved to 2d.png')
    else: sys.exit('No argument given.')

