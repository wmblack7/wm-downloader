git add .
git commit -m "Atualizar caminhos do Flask"
git pushimport os
from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    opcao = request.form.get('format')

    if not url:
        return "Nenhum link fornecido!", 400

    # Configurações baseadas nas 3 opções solicitadas
    if opcao == 'mp3':
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    elif opcao == 'alta_resolucao':
        # Pega a melhor qualidade combinada (HD/Full HD/4K)
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        }
    else:
        # Resolução original padrão fornecida pela plataforma
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'best',
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            if opcao == 'mp3':
                filename = os.path.splitext(filename)[0] + '.mp3'
            elif opcao == 'alta_resolucao':
                filename = os.path.splitext(filename)[0] + '.mp4'

        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"Ocorreu um erro ao processar o arquivo: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
import os
from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    modo = request.form.get('format')

    if not url:
        return "Nenhum link fornecido!", 400

    # Configurações do yt-dlp baseadas na escolha do usuário
    if modo == 'mp3':
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    elif modo == 'mp4_best':
        # Pega a melhor qualidade de vídeo e áudio combinadas (Full HD/4K se disponível)
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        }
    else:
        # MP4 padrão (mais leve)
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'mp4',
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            # Se for MP3, a extensão do arquivo baixado muda para .mp3
            if modo == 'mp3':
                filename = os.path.splitext(filename)[0] + '.mp3'
            elif modo == 'mp4_best':
                filename = os.path.splitext(filename)[0] + '.mp4'

        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"Ocorreu um erro ao processar o arquivo: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
import os
from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')
    if not url:
        return "Nenhum link fornecido!", 400

    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'format': 'best',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"Ocorreu um erro ao baixar o vídeo: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Meu Primeiro Site no Termux!</h1><p>O site está a funcionar perfeitamente.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

