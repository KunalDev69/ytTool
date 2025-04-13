# from flask import Flask, render_template, request, send_file
# import yt_dlp
# import os
# import uuid

# app = Flask(__name__)
# DOWNLOAD_DIR = "downloads"

# if not os.path.exists(DOWNLOAD_DIR):
#     os.makedirs(DOWNLOAD_DIR)

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
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=False)

#     video_data = {
#         'title': info['title'],
#         'thumbnail': info['thumbnail'],
#         'duration': info['duration_string'] if 'duration_string' in info else info['duration'],
#         'formats': [
#             {'format_id': f['format_id'], 'ext': f['ext'], 'resolution': f.get('resolution', f.get('abr', 'Audio'))}
#             for f in info['formats']
#             if f['ext'] in ['mp4', 'webm', 'm4a'] and 'filesize' in f
#         ],
#         'url': url,
#         'video_id': info['id']
#     }

#     return render_template('result.html', video=video_data)

# @app.route('/download', methods=['POST'])
# def download():
#     url = request.form['url']
#     format_id = request.form['format_id']
#     filename = str(uuid.uuid4())

#     filepath = os.path.join(DOWNLOAD_DIR, f"{filename}.%(ext)s")

#     ydl_opts = {
#         'format': format_id,
#         'outtmpl': filepath,
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.download([url])

#     downloaded_file = next((f for f in os.listdir(DOWNLOAD_DIR) if filename in f), None)
#     return send_file(os.path.join(DOWNLOAD_DIR, downloaded_file), as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)


# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=5000, debug=True)

# # new app



# # from flask import Flask, render_template, request, send_file
# # import yt_dlp
# # import os
# # import uuid
# # from time import sleep

# # app = Flask(__name__)
# # DOWNLOAD_DIR = 'downloads'

# # # Ensure the download directory exists
# # if not os.path.exists(DOWNLOAD_DIR):
# #     os.makedirs(DOWNLOAD_DIR)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/fetch', methods=['POST'])
# # def fetch():
# #     url = request.form['url']

# #     ydl_opts = {
# #         'quiet': True,
# #         'skip_download': True,
# #         'forcejson': True,
# #     }

# #     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #         info = ydl.extract_info(url, download=False)

# #     # Filter formats that include both video and audio, with video resolutions from 360p and above
# #     formats = [
# #         {
# #             'format_id': f['format_id'],
# #             'ext': f['ext'],
# #             'resolution': f.get('resolution') or f.get('abr', 'Audio'),
# #         }
# #         for f in info.get('formats', [])
# #         if 'audio' in f and 'video' in f and f['ext'] in ['mp4', 'm4a'] and f.get('resolution')
# #         and int(f.get('height', 0)) >= 360  # Ensures video is at least 360p
# #     ]

# #     video_data = {
# #         'title': info.get('title', 'Unknown'),
# #         'thumbnail': info.get('thumbnail'),
# #         'duration': info.get('duration_string', 'N/A'),
# #         'formats': formats[:10],  # Limit to 10 best formats
# #         'url': url,
# #         'video_id': info['id']
# #     }

# #     return render_template('result.html', video=video_data)

# # @app.route('/download', methods=['POST'])
# # def download():
# #     url = request.form['url']
# #     format_id = request.form['format_id']
# #     unique_name = str(uuid.uuid4())
# #     filepath = os.path.join(DOWNLOAD_DIR, f"{unique_name}.%(ext)s")

# #     ydl_opts = {
# #         'format': format_id,
# #         'outtmpl': filepath,
# #         'noplaylist': True,
# #         'quiet': True,
# #         'no_warnings': True,
# #         'restrictfilenames': True,
# #     }

# #     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #         info = ydl.extract_info(url, download=True)

# #     # Find the actual file
# #     downloaded_file = next(f for f in os.listdir(DOWNLOAD_DIR) if unique_name in f)
# #     full_path = os.path.join(DOWNLOAD_DIR, downloaded_file)

# #     # Optional: create nice filename for user
# #     ext = downloaded_file.split('.')[-1]
# #     title = info.get('title', 'video').replace(' ', '_').replace('/', '_')
# #     download_name = f"{title}.{ext}"

# #     # Simulating the download and return file
# #     return send_file(full_path, as_attachment=True, download_name=download_name)


# # print("Request received at /fetch")




# # from flask import Flask, render_template, request, send_file
# # import yt_dlp
# # import os
# # import uuid
# # import logging

# # app = Flask(__name__)
# # DOWNLOAD_DIR = 'downloads'

# # # Ensure the download directory exists
# # if not os.path.exists(DOWNLOAD_DIR):
# #     os.makedirs(DOWNLOAD_DIR)

# # # Set up logging
# # logging.basicConfig(level=logging.DEBUG)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/fetch', methods=['POST'])
# # def fetch():
# #     url = request.form['url']
# #     logging.debug(f"Fetching details for URL: {url}")

# #     ydl_opts = {
# #         'quiet': True,
# #         'skip_download': True,
# #         'forcejson': True,
# #     }

# #     try:
# #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(url, download=False)
# #             logging.debug(f"Video info: {info}")
# #     except Exception as e:
# #         logging.error(f"Error fetching video details: {e}")
# #         return render_template('error.html', message="Failed to fetch video details.")

# #     # Filter formats that include both video and audio, with video resolutions from 360p and above
# #     formats = [
# #         {
# #             'format_id': f['format_id'],
# #             'ext': f['ext'],
# #             'resolution': f.get('resolution') or f.get('abr', 'Audio'),
# #         }
# #         for f in info.get('formats', [])
# #         if 'audio' in f and 'video' in f and f['ext'] in ['mp4', 'm4a'] and f.get('resolution')
# #         and int(f.get('height', 0)) >= 360  # Ensures video is at least 360p
# #     ]
    
# #     if not formats:
# #         logging.warning("No valid formats found.")
# #         return render_template('error.html', message="No valid video formats found.")

# #     video_data = {
# #         'title': info.get('title', 'Unknown'),
# #         'thumbnail': info.get('thumbnail'),
# #         'duration': info.get('duration_string', 'N/A'),
# #         'formats': formats[:10],  # Limit to 10 best formats
# #         'url': url,
# #         'video_id': info['id']
# #     }

# #     return render_template('result.html', video=video_data)

# # @app.route('/download', methods=['POST'])
# # def download():
# #     url = request.form['url']
# #     format_id = request.form['format_id']
# #     logging.debug(f"Downloading video from URL: {url} with format ID: {format_id}")

# #     unique_name = str(uuid.uuid4())
# #     filepath = os.path.join(DOWNLOAD_DIR, f"{unique_name}.%(ext)s")

# #     ydl_opts = {
# #         'format': format_id,
# #         'outtmpl': filepath,
# #         'noplaylist': True,
# #         'quiet': True,
# #         'no_warnings': True,
# #         'restrictfilenames': True,
# #     }

# #     try:
# #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(url, download=True)
# #             logging.debug(f"Download completed: {info}")
# #     except Exception as e:
# #         logging.error(f"Error downloading video: {e}")
# #         return render_template('error.html', message="Failed to download video.")

# #     # Find the actual file
# #     downloaded_file = next(f for f in os.listdir(DOWNLOAD_DIR) if unique_name in f)
# #     full_path = os.path.join(DOWNLOAD_DIR, downloaded_file)

# #     # Optional: create nice filename for user
# #     ext = downloaded_file.split('.')[-1]
# #     title = info.get('title', 'video').replace(' ', '_').replace('/', '_')
# #     download_name = f"{title}.{ext}"

# #     # Simulating the download and return file
# #     return send_file(full_path, as_attachment=True, download_name=download_name)

# # @app.errorhandler(404)
# # def page_not_found(e):
# #     return render_template('error.html', message="Page not found"), 404

# # @app.errorhandler(500)
# # def internal_server_error(e):
# #     return render_template('error.html', message="Internal server error occurred."), 500

# # if __name__ == '__main__':
# #     app.run(debug=True)



# # from flask import Flask, render_template, request, send_file
# # import yt_dlp
# # import os
# # import uuid
# # import logging

# # app = Flask(__name__)
# # DOWNLOAD_DIR = 'downloads'

# # # Ensure the download directory exists
# # if not os.path.exists(DOWNLOAD_DIR):
# #     os.makedirs(DOWNLOAD_DIR)

# # # Set up logging
# # logging.basicConfig(level=logging.DEBUG)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/fetch', methods=['POST'])
# # def fetch():
# #     url = request.form['url']
# #     logging.debug(f"Fetching details for URL: {url}")

# #     ydl_opts = {
# #         'quiet': True,
# #         'skip_download': True,
# #         'forcejson': True,
# #     }

# #     try:
# #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(url, download=False)
# #             logging.debug(f"Video info: {info}")
# #     except Exception as e:
# #         logging.error(f"Error fetching video details: {e}")
# #         return render_template('error.html', message="Failed to fetch video details.")

# #     # Filter formats that include both video and audio, with video resolutions from 360p and above
# #     formats = [
# #         {
# #             'format_id': f['format_id'],
# #             'ext': f['ext'],
# #             'resolution': f.get('resolution') or f.get('abr', 'Audio'),
# #         }
# #         for f in info.get('formats', [])
# #         if 'audio' in f and 'video' in f and f['ext'] in ['mp4', 'm4a'] and f.get('resolution')
# #         and int(f.get('height', 0)) >= 360  # Ensures video is at least 360p
# #     ]
    
# #     if not formats:
# #         logging.warning("No valid formats found.")
# #         return render_template('error.html', message="No valid video formats found.")

# #     video_data = {
# #         'title': info.get('title', 'Unknown'),
# #         'thumbnail': info.get('thumbnail'),
# #         'duration': info.get('duration_string', 'N/A'),
# #         'formats': formats[:10],  # Limit to 10 best formats
# #         'url': url,
# #         'video_id': info['id']
# #     }

# #     return render_template('result.html', video=video_data)

# # @app.route('/download', methods=['POST'])
# # def download():
# #     url = request.form['url']
# #     format_id = request.form['format_id']
# #     logging.debug(f"Downloading video from URL: {url} with format ID: {format_id}")

# #     unique_name = str(uuid.uuid4())
# #     filepath = os.path.join(DOWNLOAD_DIR, f"{unique_name}.%(ext)s")

# #     ydl_opts = {
# #         'format': format_id,
# #         'outtmpl': filepath,
# #         'noplaylist': True,
# #         'quiet': True,
# #         'no_warnings': True,
# #         'restrictfilenames': True,
# #     }

# #     try:
# #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(url, download=True)
# #             logging.debug(f"Download completed: {info}")
# #     except Exception as e:
# #         logging.error(f"Error downloading video: {e}")
# #         return render_template('error.html', message="Failed to download video.")

# #     # Find the actual file
# #     downloaded_file = next(f for f in os.listdir(DOWNLOAD_DIR) if unique_name in f)
# #     full_path = os.path.join(DOWNLOAD_DIR, downloaded_file)

# #     # Optional: create nice filename for user
# #     ext = downloaded_file.split('.')[-1]
# #     title = info.get('title', 'video').replace(' ', '_').replace('/', '_')
# #     download_name = f"{title}.{ext}"

# #     # Simulating the download and return file
# #     return send_file(full_path, as_attachment=True, download_name=download_name)

# # @app.errorhandler(404)
# # def page_not_found(e):
# #     return render_template('error.html', message="Page not found"), 404

# # @app.errorhandler(500)
# # def internal_server_error(e):
# #     return render_template('error.html', message="Internal server error occurred."), 500

# # if __name__ == '__main__':
# #     app.run(debug=True)



# # from flask import Flask, render_template, request, send_file
# # import yt_dlp
# # import os
# # import uuid

# # app = Flask(__name__)
# # DOWNLOAD_DIR = "downloads"

# # # Create downloads directory if it doesn't exist
# # if not os.path.exists(DOWNLOAD_DIR):
# #     os.makedirs(DOWNLOAD_DIR)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/fetch', methods=['POST'])
# # def fetch():
# #     url = request.form['url']

# #     ydl_opts = {
# #         'quiet': True,
# #         'skip_download': True,
# #         'format': 'best',
# #     }

# #     try:
# #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             info = ydl.extract_info(url, download=False)
# #     except Exception as e:
# #         return f"<h1>Error</h1><p>{str(e)}</p><a href='/'>Go back to home</a>"

# #     formats = []
# #     for f in info.get('formats', []):
# #         if f.get('ext') in ['mp4', 'webm', 'm4a'] and f.get('filesize'):
# #             resolution = f.get('resolution') or f.get('height') or f.get('abr', 'Audio')
# #             formats.append({
# #                 'format_id': f['format_id'],
# #                 'ext': f['ext'],
# #                 'resolution': str(resolution)
# #             })

# #     if not formats:
# #         return "<h1>Error</h1><p>No valid video formats found.</p><a href='/'>Go back to home</a>"

# #     video_data = {
# #         'title': info.get('title', 'Unknown'),
# #         'thumbnail': info.get('thumbnail'),
# #         'duration': info.get('duration_string', 'N/A'),
# #         'formats': formats[:10],
# #         'url': url,
# #         'video_id': info['id']
# #     }

# #     return render_template('result.html', video=video_data)

# # @app.route('/download', methods=['POST'])
# # def download():
# #     url = request.form['url']
# #     format_id = request.form['format_id']
# #     filename = str(uuid.uuid4())
# #     out_path = os.path.join(DOWNLOAD_DIR, f"{filename}.%(ext)s")

# #     ydl_opts = {
# #         'format': format_id,
# #         'outtmpl': out_path,
# #         'quiet': True,
# #         'no_warnings': True,
# #         'noplaylist': True
# #     }

# #     try:
# #         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #             ydl.download([url])
# #     except Exception as e:
# #         return f"<h1>Error downloading video</h1><p>{str(e)}</p><a href='/'>Go back to home</a>"

# #     # Find the actual downloaded file
# #     downloaded_file = next((f for f in os.listdir(DOWNLOAD_DIR) if filename in f), None)

# #     if not downloaded_file:
# #         return "<h1>Download Error</h1><p>File not found.</p><a href='/'>Go back to home</a>"

# #     return send_file(os.path.join(DOWNLOAD_DIR, downloaded_file), as_attachment=True)

# # # Run Flask app on all network interfaces for phone access
# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=5000, debug=True)







# from flask import Flask, render_template, request, send_file
# import yt_dlp
# import os
# import uuid

# app = Flask(__name__)
# DOWNLOAD_DIR = "downloads"
# COOKIES_PATH = "cookies.txt"  # Place your exported cookies here

# # Create downloads directory if it doesn't exist
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
#     }

#     # Optional cookies support
#     if os.path.exists(COOKIES_PATH):
#         ydl_opts['cookiefile'] = COOKIES_PATH

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#     except Exception as e:
#         return render_template('error.html', message=str(e))

#     formats = []
#     for f in info.get('formats', []):
#         ext = f.get('ext')
#         filesize = f.get('filesize')
#         if ext in ['mp4', 'webm', 'm4a'] and filesize:
#             resolution = f.get('resolution') or f.get('height') or f.get('abr') or "N/A"
#             size_mb = round(filesize / (1024 * 1024), 2)
#             formats.append({
#                 'format_id': f['format_id'],
#                 'ext': ext,
#                 'resolution': str(resolution),
#                 'filesize': f"{size_mb} MB"
#             })

#     if not formats:
#         return render_template('error.html', message="No valid video formats found.")

#     video_data = {
#         'title': info.get('title', 'Unknown'),
#         'thumbnail': info.get('thumbnail'),
#         'duration': info.get('duration_string', 'N/A'),
#         'formats': formats[:10],  # Limit formats shown
#         'url': url,
#         'video_id': info['id']
#     }

#     return render_template('result.html', video=video_data)

# @app.route('/download', methods=['POST'])
# def download():
#     url = request.form['url']
#     format_id = request.form['format_id']
#     filename = str(uuid.uuid4())
#     out_path = os.path.join(DOWNLOAD_DIR, f"{filename}.%(ext)s")

#     ydl_opts = {
#         'format': format_id,
#         'outtmpl': out_path,
#         'quiet': True,
#         'no_warnings': True,
#         'noplaylist': True
#     }

#     if os.path.exists(COOKIES_PATH):
#         ydl_opts['cookiefile'] = COOKIES_PATH

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#     except Exception as e:
#         return render_template('error.html', message=f"Error downloading: {str(e)}")

#     # Find actual downloaded file
#     downloaded_file = next((f for f in os.listdir(DOWNLOAD_DIR) if filename in f), None)

#     if not downloaded_file:
#         return render_template('error.html', message="Download failed: file not found.")

#     return send_file(os.path.join(DOWNLOAD_DIR, downloaded_file), as_attachment=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

#new code start here 

# from flask import Flask, render_template, request, send_file
# import yt_dlp
# import os
# import uuid

# app = Flask(__name__)
# DOWNLOAD_DIR = "downloads"
# COOKIES_PATH = "cookies.txt"

# # Create downloads directory if it doesn't exist
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
#     }

#     if os.path.exists(COOKIES_PATH):
#         ydl_opts['cookiefile'] = COOKIES_PATH

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#     except Exception as e:
#         return render_template('error.html', message=str(e))

#     formats = []
#     for f in info.get('formats', []):
#         format_id = f.get('format_id')
#         ext = f.get('ext')
#         filesize = f.get('filesize') or 0
#         height = f.get('height')
#         acodec = f.get('acodec')
#         vcodec = f.get('vcodec')

#         if format_id and ext:
#             if 'none' in (vcodec or '') and 'none' not in (acodec or ''):
#                 resolution = "audio only"
#             else:
#                 resolution = f"{height}p" if height else "N/A"

#             size_mb = round(filesize / (1024 * 1024), 2) if filesize else "?"
#             formats.append({
#                 'format_id': format_id,
#                 'ext': ext,
#                 'resolution': resolution,
#                 'filesize': f"{size_mb} MB" if filesize else "Unknown"
#             })

#     if not formats:
#         return render_template('error.html', message="No valid formats found.")

#     video_data = {
#         'title': info.get('title', 'Unknown'),
#         'thumbnail': info.get('thumbnail'),
#         'duration': info.get('duration_string', 'N/A'),
#         'formats': formats[:20],  # Show more options
#         'url': url,
#         'video_id': info.get('id')
#     }

#     return render_template('result.html', video=video_data)

# @app.route('/download', methods=['POST'])
# def download():
#     url = request.form['url']
#     format_id = request.form['format_id']
#     filename = str(uuid.uuid4())
#     out_path = os.path.join(DOWNLOAD_DIR, f"{filename}.%(ext)s")

#     ydl_opts = {
#         'format': format_id,
#         'outtmpl': out_path,
#         'quiet': True,
#         'no_warnings': True,
#         'noplaylist': True
#     }

#     if os.path.exists(COOKIES_PATH):
#         ydl_opts['cookiefile'] = COOKIES_PATH

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#     except Exception as e:
#         return render_template('error.html', message=f"Error downloading: {str(e)}")

#     try:
#         downloaded_file = next((f for f in os.listdir(DOWNLOAD_DIR) if filename in f), None)
#         if not downloaded_file:
#             raise FileNotFoundError("Download completed but file not found.")
#         return send_file(os.path.join(DOWNLOAD_DIR, downloaded_file), as_attachment=True)
#     except Exception as e:
#         return render_template('error.html', message=f"Download failed: {str(e)}")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



#last update code 


# from flask import Flask, render_template, request, send_file
# import yt_dlp
# import os
# import uuid

# app = Flask(__name__)
# DOWNLOAD_DIR = "downloads"
# COOKIES_PATH = "cookies.txt"

# # Create downloads directory if it doesn't exist
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
#     }

#     if os.path.exists(COOKIES_PATH):
#         ydl_opts['cookiefile'] = COOKIES_PATH

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#     except Exception as e:
#         return render_template('error.html', message=f"Failed to fetch video: {str(e)}")

#     formats = []
#     seen = set()

#     for f in info.get('formats', []):
#         ext = f.get('ext')
#         format_id = f.get('format_id')
#         filesize = f.get('filesize') or 0
#         height = f.get('height')
#         vcodec = f.get('vcodec')
#         acodec = f.get('acodec')

#         if ext not in ['mp4', 'webm', 'm4a'] or not format_id:
#             continue

#         if (format_id, ext) in seen:
#             continue
#         seen.add((format_id, ext))

#         # Label resolution or audio-only
#         if vcodec == 'none':
#             resolution = "Audio only"
#         else:
#             resolution = f"{height}p" if height else "Video"

#         size_mb = round(filesize / (1024 * 1024), 2) if filesize else "?"
#         formats.append({
#             'format_id': format_id,
#             'ext': ext,
#             'resolution': resolution,
#             'filesize': f"{size_mb} MB" if filesize else "Unknown"
#         })

#     if not formats:
#         return render_template('error.html', message="No downloadable formats found.")

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
#     filename = str(uuid.uuid4())
#     out_template = os.path.join(DOWNLOAD_DIR, f"{filename}.%(ext)s")

#     ydl_opts = {
#         'format': format_id,
#         'outtmpl': out_template,
#         'quiet': True,
#         'no_warnings': True,
#         'noplaylist': True
#     }

#     if os.path.exists(COOKIES_PATH):
#         ydl_opts['cookiefile'] = COOKIES_PATH

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=True)
#             downloaded_path = ydl.prepare_filename(info)

#         return send_file(downloaded_path, as_attachment=True)
#     except Exception as e:






#one last update code 




from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

# Use /tmp for Render compatibility
DOWNLOAD_DIR = "/tmp/downloads"
COOKIES_PATH = "cookies.txt"

# Ensure the downloads directory exists
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
        'format': 'best',
    }

    if os.path.exists(COOKIES_PATH):
        ydl_opts['cookiefile'] = COOKIES_PATH

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return render_template('error.html', message=f"Failed to fetch video: {str(e)}")

    formats = []
    seen = set()

    for f in info.get('formats', []):
        ext = f.get('ext')
        format_id = f.get('format_id')
        filesize = f.get('filesize') or 0
        height = f.get('height')
        vcodec = f.get('vcodec')

        if ext not in ['mp4', 'webm', 'm4a'] or not format_id:
            continue

        if (format_id, ext) in seen:
            continue
        seen.add((format_id, ext))

        resolution = "Audio only" if vcodec == 'none' else f"{height}p" if height else "Video"
        size_mb = round(filesize / (1024 * 1024), 2) if filesize else "Unknown"

        formats.append({
            'format_id': format_id,
            'ext': ext,
            'resolution': resolution,
            'filesize': f"{size_mb} MB" if filesize else "Unknown"
        })

    if not formats:
        return render_template('error.html', message="No downloadable formats found.")

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
    filename = str(uuid.uuid4())
    output_template = os.path.join(DOWNLOAD_DIR, f"{filename}.%(ext)s")

    ydl_opts = {
        'format': format_id,
        'outtmpl': output_template,
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True
    }

    if os.path.exists(COOKIES_PATH):
        ydl_opts['cookiefile'] = COOKIES_PATH

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_file = ydl.prepare_filename(info)

        # Confirm file exists before sending
        if not os.path.exists(downloaded_file):
            return render_template('error.html', message="File was not downloaded.")

        return send_file(downloaded_file, as_attachment=True)
    except Exception as e:
        return render_template('error.html', message=f"Download failed: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

        return render_template('error.html', message=f"Download failed: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
