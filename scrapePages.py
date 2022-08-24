from bs4 import BeautifulSoup
import requests
url = 'https://scrapingclub.com/exercise/list_basic/'
#definição da pagina pra fazer scrape
count = 1
#contador
response = requests.get(url)
#faz o request e cria uma especie de copia do html da página
soup = BeautifulSoup(response.text, 'lxml')
#aqui é feito o parse do documento html criando um objeto navegável
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
#define como items todos os items div com esta classe
for i in items:
    #ler item por item
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    #nome do item
    itemPrice = i.find('h5').text
    #preço do item
    print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
    #printa o número do item, seu nome e valor
    count = count + 1
    #aumenta 1 no contador para indicar o numero do próximo item
# ******************************
# Até aqui essa função lê todos os items de apenas uma página
# ******************************
pagination = soup.find('ul', class_='pagination')
#puxa a ul com todas as páginas
pages = pagination.find_all('a', class_='page-link')
#puxa cada página individualmente
urls = []
#objeto para receber as páginas
for page in pages:
    #aqui serão separadas as páginas criando um link para cada dentro do objeto urls
    pageNum = int(page.text) if page.text.isdigit() else None
    #pega a numeração das páginas e só deixa retornar numeros
    if pageNum != None:
        link = page.get('href')
        #pega o texto do href (que é o link da pagina)
        urls.append(link)
        #link é adicionado ao urls

for i in urls:
    response = requests.get(url + i)
    #vai fazer a cada repetição ir pra próxima página
    soup = BeautifulSoup(response.text, 'lxml')
    #novamente feito o parse do documento html criando um objeto navegável
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    #novamente define como items todos os "div" com esta classe
    for i in items:
        #ler item por item
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        #nome do item
        itemPrice = i.find('h5').text
        #preço do item
        print('%s) Price: %s , Item Name: %s' % (count, itemPrice, itemName))
        #printa o número do item, seu nome e valor
        count = count + 1
        #aumenta 1 no contador para indicar o numero do próximo item
