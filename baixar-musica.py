from pytubefix import YouTube
from moviepy.editor import AudioFileClip
import os

def baixar_mp3(link, destino='./Downloads'):
    try:
        yt = YouTube(link)
        print(f"Baixando: {yt.title}")
        video = yt.streams.filter(only_audio=True).first()
        arquivo_video = video.download(output_path=destino)

        nome_base = os.path.splitext(arquivo_video)[0]
        arquivo_mp3 = f"{nome_base}.mp3"
        print("Convertendo para MP3...")
        audio_clip = AudioFileClip(arquivo_video)
        audio_clip.write_audiofile(arquivo_mp3)
        audio_clip.close()

        os.remove(arquivo_video)
        print(f"Download concluído: {arquivo_mp3}")

    except Exception as e:
        print(f"Erro: {e}")

link_youtube = "https://www.youtube.com/watch?v=FxiDG-EjgLU"
baixar_mp3(link_youtube)
