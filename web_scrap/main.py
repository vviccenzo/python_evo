from urllib.request import urlopen

# Project made with help of https://realpython.com/python-web-scraping-practical-introduction/

#URL que será puxada criação do WebScrap
url = "http://olympus.realpython.org/profiles/aphrodite"

#Para abrir a URL
page = urlopen(url)
print(page) #Retorna um HTTP response object

#Extrair o HTML da página
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html) #Retorna o HTML da página
print("-------------------------------")
# ---------------------------------------------------------------
# É possível utilizar o método .find() para encontrar o texto
# .find() retorna o primeiro índice do texto encontrado
# Assim que ele começar a ser encontrado, ele retorna o índice
start_index = html.find("<title>") + len("<title>")
# E para finalizar ele busca pelo final do title, e então retorna o indice
end_index = html.find("</title>")
print(html[start_index:end_index])