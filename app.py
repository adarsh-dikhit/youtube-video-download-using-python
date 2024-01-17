from flask import Flask, request, jsonify, render_template
from googleapiclient.discovery import build
import youtube_dl
from pytube import YouTube

app = Flask(__name__)

# Your API key from the Google Cloud Console
api_key = 'AIzaSyDRq8wuQb6wHjNkLrXddCmoyB8qHQJyNBw'

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('query')

    # Use the YouTube Data API to search for videos
    search_response = youtube.search().list(
        q=search_query,
        type='video',
        part='id',
        maxResults=10  # You can adjust this to limit the number of results
    ).execute()

    # Extract video IDs from the search results
    video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]

    # Generate video links from video IDs
    video_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids]

    return render_template('search_results.html', video_links=video_links)

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form.get('video_url')

    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Choose the desired video stream (e.g., highest resolution)
        stream = yt.streams.get_highest_resolution()
        
        # Download the video to the "downloads" folder
        stream.download(output_path='downloads/')
        
        return 'Download completed!'
    except Exception as e:
        return 'Download failed: ' + str(e)

if __name__ == '__main__':
    app.run(debug=True)