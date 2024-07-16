import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#Valida a URL
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

#Pega o conteudo da pagina
def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None

#Extrai o titulo do html_content
def extract_titles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Encontrar os elementos de título (exemplo para títulos em h1, h2, h3 tags)
    titles = soup.find_all(['h1', 'h2', 'h3'])
    
    #joga o titulo extraido para uma lista
    extracted_titles = []
    for title in titles:
        extracted_titles.append(title.get_text(strip=True))
    
    return extracted_titles

def main():
    url = input("Digite a URL do site: ")
    
    if not is_valid_url(url):
        print("URL inválida. Tente novamente.")
        return
    
    html_content = get_page_content(url)
    
    if html_content:
        titles = extract_titles(html_content)
        if titles:
            print("Títulos encontrados:")
            for idx, title in enumerate(titles, start=1):
                print(f"{idx}. {title}")
        else:
            print("Nenhum título encontrado na página.")
    else:
        print("Falha ao recuperar o conteúdo da página.")

if __name__ == "__main__":
    main()