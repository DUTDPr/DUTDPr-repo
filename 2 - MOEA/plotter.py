import plotly.express as px
import pandas as pd
#df = pd.read_table('input_cocoon.txt',header=None,sep=" ")
df = pd.read_table('input_accumulo.txt',header=None,sep=" ")
df.columns = ['X', 'Y', 'Z', 'AB']
print(df)
fig = px.parallel_coordinates(df, labels={"X": "B",
                "Y": "U(S1)", "Z": "U(S2)",
                "AB": "U(S3)"})
fig.show()