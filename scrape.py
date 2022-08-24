import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'
#definição da pagina pra fazer scrape
response = requests.get(url)
#faz o request e cria uma especie de copia do html da página
soup = BeautifulSoup(response.text,'lxml')
#aqui é feito o parse do documento html criando um objeto navegável
quotes = soup.find_all("span", class_="text")
# define como quotes todos os elementos span com a classe text dentro de soup
authors = soup.find_all("small", class_="author")
# define como authors todos os elementos small com a classe author dentro de soup
tags = soup.find_all("div", class_="tags")
# mesmo que acima, mas aqui ele define a div mãe
scrapedArchives = "scrapedArchives.txt"
scrapedTxt = open(scrapedArchives, "w")
for i in range(0,len(quotes)):
    #le items por item em quotes
    scrapedTxt.write(quotes[i].text + '\n')
    scrapedTxt.write("Author:\t" + authors[i].text + '\n')
    #escreve no arquivo
    print(quotes[i].text)
    print(authors[i].text)
    #O '.text' faz printar apenas o texto, sem os elementos html que o soup também trás
    quoteTags = tags[i].find_all('a',class_='tag')
    #aqui quoteTags é definido com cada tag de uma quote
    scrapedTxt.write("tags:\t")
    for quoteTag in quoteTags:
        #aqui são lidas individualmente as tags de um quote
        print(quoteTag.text)
        scrapedTxt.write("  |  " + quoteTag.text)
    scrapedTxt.write("  |  \n\n")