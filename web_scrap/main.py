from urllib.request import urlopen

#URL que será puxada criação do WebScrap
url = "http://olympus.realpython.org/profiles/aphrodite"

#Para abrir a URL
page = urlopen(url)

#urlopen() retorna um HTTPResponse object
print(page)

#Extrair o HTML da página
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)