import pandas as pd
import matplotlib.pyplot as plt
import sys
def main():
    df = pd.read_csv('temperature_clean.csv')
    x = df['year']
    y = df['AverageTemperatureCelsius']

    fig, ax = plt.subplots(figsize=(10,5))
    ax.scatter(x,y, facecolor='none', edgecolor='black')
    ax.set_xlabel('year')
    ax.set_ylabel('AverageTemperatureCelsius')
    
    
if __name__=='__main__':
    main()
    if (len(sys.argv)>=2):
        if int(sys.argv[1])==0:
            plt.show()
        elif int(sys.argv[1])==1:
            plt.savefig('2a.png')
            print('Saved to 2a.png')
    else: sys.exit('No argument given.')