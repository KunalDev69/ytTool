# from flask import Flask, render_template, request, redirect
# import yt_dlp
# import os

# app = Flask(__name__)

# # Download dir for Render compatibility
# DOWNLOAD_DIR = "/tmp/downloads"
# COOKIES_PATH = "cookies.txt"

# os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/fetch', methods=['POST'])
# def fetch():
#     url = request.form['url']

#     ydl_opts = {
#         'quiet': True,
#         'skip_download': True,
#         'format': 'best',
#         'http_headers': {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
#         }
#     }

#     if os.path.exists(COOKIES_PATH):
#         ydl_opts['cookiefile'] = COOKIES_PATH

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#     except Exception as e:
#         return render_template('error.html', message=f"❌ Failed to fetch video: {str(e)}")

#     formats = []
#     seen = set()

#     for f in info.get('formats', []):
#         ext = f.get('ext')
#         format_id = f.get('format_id')
#         filesize = f.get('filesize') or 0
#         height = f.get('height')
#         vcodec = f.get('vcodec')
#         acodec = f.get('acodec')

#         # Only include formats that have audio and video
#         if ext not in ['mp4', 'webm', 'm4a'] or not format_id:
#             continue
#         if vcodec == 'none' and acodec != 'none':
#             continue  # Skip video-only formats (with audio)
#         if acodec == 'none':
#             continue  # Skip formats with no audio
#         if vcodec == 'none':
#             continue  # Skip formats with no video

#         if (format_id, ext) in seen:
#             continue
#         seen.add((format_id, ext))

#         resolution = "Audio only" if vcodec == 'none' else f"{height}p" if height else "Video"
#         size_mb = round(filesize / (1024 * 1024), 2) if filesize else "Unknown"

#         formats.append({
#             'format_id': format_id,
#             'ext': ext,
#             'resolution': resolution,
#             'filesize': f"{size_mb} MB" if filesize != 0 else "Unknown"
#         })

#     if not formats:
#         return render_template('error.html', message="⚠️ No downloadable formats found.")

#     video_data = {
#         'title': info.get('title', 'Unknown'),
#         'thumbnail': info.get('thumbnail'),
#         'duration': info.get('duration_string', 'N/A'),
#         'formats': formats,
#         'url': url,
#         'video_id': info['id']
#     }

#     return render_template('result.html', video=video_data)

# @app.route('/download', methods=['POST'])
# def download():
#     url = request.form['url']
#     format_id = request.form['format_id']

#     ydl_opts = {
#         'format': f"{format_id}+bestaudio/best",
#         'quiet': True,
#         'skip_download': True,
#         'noplaylist': True,
#         'http_headers': {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
#         }
#     }

#     if os.path.exists(COOKIES_PATH):
#         ydl_opts['cookiefile'] = COOKIES_PATH

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)

#         direct_url = None
#         for f in info.get('formats', []):
#             if f.get('format_id') == format_id:
#                 direct_url = f.get('url')
#                 break

#         if not direct_url:
#             return render_template('error.html', message="⚠️ Direct download link not found.")

#         return redirect(direct_url)

#     except Exception as e:
#         return render_template('error.html', message=f"❌ Download failed: {str(e)}")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)





# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=5000)




from flask import Flask, render_template, request, redirect
import yt_dlp
import os

app = Flask(__name__)

# Download dir for Render compatibility
DOWNLOAD_DIR = "/tmp/downloads"
COOKIES_PATH = "cookies.txt"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form['url']

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': 'bestvideo+bestaudio/best',  # Fetch both best video and audio
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
        },
        'merge_output_format': 'mp4',  # Merge audio and video in mp4 format
        'noplaylist': True,
    }

    if os.path.exists(COOKIES_PATH):
        ydl_opts['cookiefile'] = COOKIES_PATH

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return render_template('error.html', message=f"❌ Failed to fetch video: {str(e)}")

    formats = []
    seen = set()

    # Filter for formats with both audio and video
    for f in info.get('formats', []):
        ext = f.get('ext')
        format_id = f.get('format_id')
        filesize = f.get('filesize') or 0
        height = f.get('height')
        vcodec = f.get('vcodec')
        acodec = f.get('acodec')

        # Only include formats that have both audio and video
        if ext not in ['mp4', 'webm', 'mkv'] or not format_id:
            continue
        if vcodec == 'none' or acodec == 'none':
            continue  # Skip formats with no video or no audio

        if (format_id, ext) in seen:
            continue
        seen.add((format_id, ext))

        resolution = f"{height}p" if height else "Video"
        size_mb = round(filesize / (1024 * 1024), 2) if filesize else "Unknown"

        formats.append({
            'format_id': format_id,
            'ext': ext,
            'resolution': resolution,
            'filesize': f"{size_mb} MB" if filesize != 0 else "Unknown"
        })

    if not formats:
        return render_template('error.html', message="⚠️ No downloadable formats found.")

    video_data = {
        'title': info.get('title', 'Unknown'),
        'thumbnail': info.get('thumbnail'),
        'duration': info.get('duration_string', 'N/A'),
        'formats': formats,
        'url': url,
        'video_id': info['id']
    }

    return render_template('result.html', video=video_data)

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    format_id = request.form['format_id']

    ydl_opts = {
        'format': f"{format_id}+bestaudio/best",  # Ensure best audio is selected with the video
        'quiet': True,
        'skip_download': True,
        'noplaylist': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
        },
        'merge_output_format': 'mp4',  # Ensure output format is mp4 for merged video and audio
    }

    if os.path.exists(COOKIES_PATH):
        ydl_opts['cookiefile'] = COOKIES_PATH

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        direct_url = None
        for f in info.get('formats', []):
            if f.get('format_id') == format_id:
                direct_url = f.get('url')
                break

        if not direct_url:
            return render_template('error.html', message="⚠️ Direct download link not found.")

        return redirect(direct_url)

    except Exception as e:
        return render_template('error.html', message=f"❌ Download failed: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
