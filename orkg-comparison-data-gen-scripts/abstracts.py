import pandas as pd
from bs4 import BeautifulSoup

# path to orkg_abstracts file
df = pd.read_csv('')


def get_abstract(id):
    uri = f'http://orkg.org/orkg/resource/{id}'
    row = df.loc[df['uri'] == uri]
    try:
        html = row.iloc[0]['abstract']
        soup = BeautifulSoup(html, "html.parser")
        return soup.text
    except:
        return None
