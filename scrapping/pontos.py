from bs4 import BeautifulSoup
import requests
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

url = 'https://lnb.com.br/nbb/estatisticas/pontos/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find(name = 'table')

table_str = str(table)
df = pd.read_html(table_str)[0]

df.rename(columns={
    'Pos.' : 'posicao',
    'Jogador' : 'jogador',
    'Equipe' : 'equipe',
    'JO' : 'jogos',
    'Min' : 'minutos',
    'Pts' : 'pontos',
    '3P' : 'media_tres_pontos',
    '2P' : 'media_dois_pontos',
    'LL' : 'media_lance_livre'
}, inplace=True)