from matplotlib import pyplot as plt
import pandas as pd

def doPlot(filename):
    plt.style.use('seaborn')
    
    df = pd.read_csv(filename)
    
    hand = df['outcome'].value_counts().index.tolist()
    count = df['outcome'].value_counts().tolist()
    pct = df['outcome'].value_counts(normalize=True).tolist()
    title = 'Probability of hands from '+str(df.index[-1] + 1)+' games'
    
    fig, ax = plt.subplots()
    
    bar_x = hand
    bar_height = [c for c in count]
    bar_tick_label = [h for h in hand]
    bar_label = [str(round(c*100,2))+'%' for c in pct]
    
    bar_plot = plt.bar(bar_x,bar_height,tick_label=bar_tick_label, color='green')
    
    def autolabel(rects):
        for idx,rect in enumerate(bar_plot):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    bar_label[idx],
                    ha='center', va='bottom', rotation=0)
    
    autolabel(bar_plot)
    plt.xticks(rotation=45)
    plt.ylim(0,df.index[-1]/2)
    
    plt.title(title)
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    doPlot('handData.csv')