# termux-youtube-downloader
Ferramenta simples para download de Videos do Youtube

# Como Instalar?
python <(wget -qO- https://raw.githubusercontent.com/LaelsonCG/termux-youtube-downloader/main/install.py)

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Termux YouTube Downloader</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.8/clipboard.min.js"></script>
</head>
<body>

<h1>Termux YouTube Downloader</h1>

<p>Este é um simples script para baixar vídeos do YouTube usando o Termux.</p>

<h2>Instalação</h2>

<pre><code>python &lt;(wget -qO- https://raw.githubusercontent.com/LaelsonCG/termux-youtube-downloader/main/install.py)
</code></pre>

<h3>Como instalar:</h3>

<ol>
  <li>Copie e cole o comando acima no Termux.</li>
  <li>Execute o comando para instalar o Termux YouTube Downloader.</li>
</ol>

<h3>OU</h3>

<details>
  <summary>Clique para mostrar o comando de instalação</summary>

  <pre><code>python &lt;(wget -qO- https://raw.githubusercontent.com/LaelsonCG/termux-youtube-downloader/main/install.py)
  </code></pre>

</details>

<h2>Uso</h2>

...

<button class="copy-button" data-clipboard-target="#install-command">Copy</button>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    var clipboard = new ClipboardJS('.copy-button');

    clipboard.on('success', function (e) {
      console.info('Texto copiado:', e.text);
      e.clearSelection();
    });

    clipboard.on('error', function (e) {
      console.error('Erro ao copiar texto:', e.action, e.trigger);
    });
  });
</script>

</body>
</html>
