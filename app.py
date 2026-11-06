import os
from flask import Flask, render_template, request, send_file
import yt_dlp

app = Flask(__name__, template_folder='templates', static_folder='static')

DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        fmt = request.form.get('format')
        
        if not url:
            return render_template('index.html', error="Por favor, insira um link válido!")

        ydl_opts = {}
        
        if fmt == 'mp3':
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif fmt == 'high':
            ydl_opts = {
                'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
            }
        else:  # original
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
            }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                
                if fmt == 'mp3':
                    filename = os.path.splitext(filename)[0] + '.mp3'
                else:
                    base, _ = os.path.splitext(filename)
                    potential_mp4 = base + '.mp4'
                    if os.path.exists(potential_mp4):
                        filename = potential_mp4

            if os.path.exists(filename):
                return send_file(filename, as_attachment=True)
            else:
                return render_template('index.html', error="Erro ao processar o ficheiro de saída.")
        except Exception as e:
            return render_template('index.html', error=f"Erro no download: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template, request, send_file, redirect, url_for
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        format_type = request.form.get('format')
        # Aqui você pode integrar a lógica de processamento do link (yt-dlp)
        return render_template('index.html', success=True, url=url, format=format_type)
    return render_template('index.html', success=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
