#!/data/data/com.termux/files/usr/bin/bash

echo "Iniciando instalação..."

# Atualiza os repositórios
pkg update -y

# Instala o Python e o pip
pkg install python python3-pip -y

# Instala o yt-dlp
pip install yt-dlp

# Baixa script de download
wget https://raw.githubusercontent.com/LaelsonCG/termux-youtube-downloader/main/yt-mp4.py

echo "Instalação concluída com sucesso!"
echo "Agora você pode usar o yt-dlp com: yt-mp4.py -o <URL_do_vídeo>"
