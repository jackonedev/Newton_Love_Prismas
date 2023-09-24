import rich
from rich import print
import main_01_preprocessing as pre
import pandas as pd
from tqdm import tqdm

pd.options.plotting.backend = "plotly"

# load DataFrame
df = pre.corpus

# apply str.replace() to each element of the DataFrame
df = df.map(lambda x: x.replace('“', '"'), na_action='ignore')
df = df.map(lambda x: x.replace('”', '"'), na_action='ignore')
df = df.map(lambda x: x.replace('’', "'"), na_action='ignore')


print("Processing Done!")

if __name__ == '__main__':
    
    # check length of each element of the DataFrame
    lengths = {}
    for column in tqdm(df.columns):
        lengths[column] = df[column].str.len()

    lengths_df = pd.DataFrame(lengths)

    # print the resulting DataFrame

    parrafo = 0
    fig = lengths_df.iloc[:, parrafo].plot(kind='bar',
                                           title='Conteo de longitud de párrafos',
                                           height=400,
                                           width=1200,
                                           template='plotly_dark')

    # save fig
    # fig.write_html("lengths.html")

    # print(df)
    print(lengths_df)
