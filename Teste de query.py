import pandas as pd
ratings = pd.read_csv("C:\\Users\\alunoti\\Downloads\\ml-latest-small\\ratings.csv")
ratings.query("rating < 1 ")
