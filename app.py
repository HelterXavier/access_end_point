import requests
from utils.helpes import format_date_str, translate


end_point = "https://api.nasa.gov/planetary/apod?api_key=eUbZeVfhkGSMYE4Eiwp0r76TKWz6o3jhyKcDNYsF"

response = requests.get(end_point)

if response.status_code == 200:
  data = response.json()

  print(data)

  date = format_date_str(data['date']) # STR
  title = translate(data['title'])
  explanation = translate(data['explanation'])

  with open("access_end_point/infos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Data: {date}\n")
    arquivo.write(f"Título: {title}\n")
    arquivo.write(f"Explicação: {explanation}\n")
    arquivo.write(f"Vídeo Youtube: {data['url']}\n")



else:
    print(f"Erro na requisição: {response.status_code}")
