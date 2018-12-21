import scrapeTools
from bs4 import BeautifulSoup
raw_html = open('https://www.symbolab.com/solver/derivative-calculator/%5Cfrac%7Bd%7D%7Bdx%7D%5Cleft(x%5E%7B2%7D%5Cright)').read()
html = BeautifulSoup(raw_html, 'html.parser')
for p in html.select('p'):
    if p['class'] == 'solution_step_result':
        print(p.text)