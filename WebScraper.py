from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"

# Pegar url
# Pegar x informações do site
# utilizar infromações
# imprimir informações

#Requisita HTTP para o url
response = requests.get(url)

#Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    titles = soup.find_all('a', class_='storylink')
    for title in titles:
        print(title.text)
else:
    print("Erro ao carregar a página")