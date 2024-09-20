# utils.py

from googleapiclient.discovery import build
from datetime import datetime
import os

# Lista de canales a monitorear
CHANNEL_IDS = [
    'UC7mJ2EDXFomeDIRFu5FtEbA', 
    'UCvCTWHCbBC0b9UIeLeNs8ug',
    'UCWSfXECGo1qK_H7SXRaUSMg',
    'UCTHaNTsP7hsVgBxARZTuajw',
    'UC4mdhKZXjrKoq5aVG6juHEg' 
]

# INicio la api de Youtube con mis credenciales
def initialize_youtube_api():
    API_KEY = os.getenv('YOUTUBE_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    return youtube

# Funcion para buscar videos de un canal
def get_videos_from_channel(youtube, channel_id, published_after):
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        publishedAfter=published_after,
        order='date',
        type='video'
    )
    response = request.execute()
    return response['items']

# Función para sacar del json el datos que necesito
def transform_video_data(videos):
    transformed_data = []
    for video in videos:
        title = video['snippet']['title']
        published_at = video['snippet']['publishedAt']
        transformed_data.append({
            'title': title,
            'published_at': published_at
        })
    return transformed_data

# Función para agrupar datos por dia 
def group_videos_by_date(videos):
    grouped_data = {}
    for video in videos:
        date = video['published_at'].split("T")[0]
        if date not in grouped_data:
            grouped_data[date] = []
        grouped_data[date].append(video)
    return grouped_data