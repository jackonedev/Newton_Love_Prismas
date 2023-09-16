import pendulum
from tools.feed import split_text, split_fragments_into_files, nombrar_subfolder_numerada, convert_fragments_into_corpus

pendulum.set_locale('es')

dt = pendulum.now()
dt = dt.format('dddd DD MMMM YYYY')

path_out = f"./data/output/{dt}"
path_out = nombrar_subfolder_numerada(path_out)

file_name = "The Adventures of Sherlock Holmes"
if not file_name.endswith(".txt"):
    file_name += ".txt"

# convertimos de txt a pd.DataFrame
df = split_text(
    "./data/input/The Adventures of Sherlock Holmes.txt", encoding="'utf-8-sig'")

# Exportamos de DataFrame a txt
split_fragments_into_files(df, path_out)

# convertimos de txt a pickle, obtenemos un pd.DataFrame de features
corpus = convert_fragments_into_corpus(df, path_out)
