import rich
from rich import print
import main_01_preprocessing as pre

print(pre.corpus)

"""
[Output]
                                           fragment_01                                        fragment_02  ...                                        fragment_11                                        fragment_12
0                              I. A SCANDAL IN BOHEMIA                          II. THE RED-HEADED LEAGUE  ...             XI. THE ADVENTURE OF THE BERYL CORONET           XII. THE ADVENTURE OF THE COPPER BEECHES
1    To Sherlock Holmes she is always _the_ woman. ...  I had called upon my friend, Mr. Sherlock Holm...  ...  “Holmes,” said I as I stood one morning in our...  “To the man who loves art for its own sake,” r...
2    I had seen little of Holmes lately. My marriag...  “You could not possibly have come at a better ...  ...  My friend rose lazily from his armchair and st...  “And yet,” said I, smiling, “I cannot quite ho...
3    One night—it was on the twentieth of March, 18...              “I was afraid that you were engaged.”  ...  He was a man of about fifty, tall, portly, and...  “You have erred, perhaps,” he observed, taking...
4    His manner was not effusive. It seldom was; bu...                           “So I am. Very much so.”  ...  “What on earth can be the matter with him?” I ...  “It seems to me that I have done you full just...
..                                                 ...                                                ...  ...                                                ...                                                ...
255                                 “This photograph!”                                               None  ...                                               None                                               None
256               The King stared at him in amazement.                                               None  ...                                               None                                               None
257  “Irene’s photograph!” he cried. “Certainly, if...                                               None  ...                                               None                                               None
258  “I thank your Majesty. Then there is no more t...                                               None  ...                                               None                                               None
259  And that was how a great scandal threatened to...                                               None  ...                                               None                                               None

[260 rows x 12 columns]
"""