from googleapiclient.discovery import build
from datetime import datetime
import os

# Datos de tu proyecto de Google Cloud
API_KEY = os.getenv('YOUTUBE_API_KEY')
CHANNEL_ID = 'UC7mJ2EDXFomeDIRFu5FtEbA'

# Inicializa el cliente de la API
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Establecer la fecha desde la cual buscar los videos
published_after = datetime(2024, 9, 7).isoformat("T") + "Z"

# Realiza la consulta a la API para obtener los videos
request = youtube.search().list(
    part='snippet',
    channelId=CHANNEL_ID,
    publishedAfter=published_after,
    order='date',  # Ordenar por fecha
    type='video',  # Asegurarse de que solo busca videos
    maxResults=10  # Puedes ajustar esto según tus necesidades
)

response = request.execute()

# Mostrar los títulos de los videos y su fecha de publicación
for item in response['items']:
    title = item['snippet']['title']
    published_at = item['snippet']['publishedAt']
    print(f"Título: {title}, Publicado en: {published_at}")