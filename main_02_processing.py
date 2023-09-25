import rich
from rich import print
import main_01_preprocessing as pre
import pandas as pd
from tqdm import tqdm
import os

pd.options.plotting.backend = "plotly"

# path output
path_out = pre.path_out

# load DataFrame
df = pre.corpus

# apply str.replace() to each element of the DataFrame
df = df.map(lambda x: x.replace('“', '"'), na_action='ignore')
df = df.map(lambda x: x.replace('”', '"'), na_action='ignore')
df = df.map(lambda x: x.replace('’', "'"), na_action='ignore')


print("Processing Done!")

if __name__ == '__main__':
    # define the path to the folder
    folder_path = "visualization"

    # check if the folder exists
    if not os.path.exists(folder_path):
        # create the folder if it doesn't exist
        os.makedirs(folder_path)
    
    # check length of each element of the DataFrame
    lengths = {}
    for column in tqdm(df.columns):
        lengths[column] = df[column].str.len()
    lengths_df = pd.DataFrame(lengths)



    ## MANUALLY SELECT PARAGRAPH TO VISUALIZE
    parrafo = 0
    fig = lengths_df.iloc[:, parrafo].plot(kind='bar',
                                           title='Conteo de longitud de párrafos',
                                           height=400,
                                           width=1200,
                                           template='plotly_dark')


    # save fig
    fig.write_html(f"./visualization/lengths_{parrafo +1}.html")

    # print(df)
    print(lengths_df)
