#!/data/data/com.termux/files/usr/bin/python

print("INICIANDO O YT-MP4 DOWNLOADER")
import sys
import subprocess
import os

def download_video(url):
    # Pasta de destino para salvar o vídeo
    destino = "/sdcard/Videos"

    # Verifica se a pasta de destino existe, se não, cria-a
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Comando para chamar o yt-dlp e baixar o vídeo em formato MP4
    comando = f"yt-dlp {url} -o '{destino}/%(title)s.%(ext)s' -f mp4"

    try:
        # Executa o comando
        subprocess.run(comando, shell=True, check=True)
        print("\nDownload concluído com sucesso!")
        print("CRÉDITOS PELO SCRIPT - @LaelsonCG")
    except subprocess.CalledProcessError as e:
        print(f"Erro durante o download: {e}")

if __name__ == "__main__":
    # Verifica se o URL do vídeo foi fornecido como argumento
    if len(sys.argv) != 2:
        print("Uso: ./yt-mp4.py <URL do vídeo>")
        sys.exit(1)

    # Obtém o URL do vídeo a partir dos argumentos de linha de comando
    url_video = sys.argv[1]

    # Chama a função para baixar o vídeo
    download_video(url_video)
