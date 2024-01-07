import sys
import subprocess
import os

def download_video(url):
    # Pasta de destino para salvar o vídeo
    destino = "/sdcard/Videos"

    # Verifica se a pasta de destino existe, se não, cria-a
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Comando para chamar o SpotDL e baixar o vídeo
    comando = f"spotdl {url} --output {destino}"

    try:
        # Executa o comando
        subprocess.run(comando, shell=True, check=True)
        print("Download concluído com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro durante o download: {e}")

if __name__ == "__main__":
    # Verifica se o URL do vídeo foi fornecido como argumento
    if len(sys.argv) != 2:
        print("Uso: python yt-mp4.py <URL do vídeo>")
        sys.exit(1)

    # Obtém o URL do vídeo a partir dos argumentos de linha de comando
    url_video = sys.argv[1]

    # Chama a função para baixar o vídeo
    download_video(url_video)
