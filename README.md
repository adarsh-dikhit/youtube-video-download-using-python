
# YouTube Video Search and Download

This web application allows you to search for YouTube videos and download them by providing a video URL. It integrates the YouTube Data API for searching and the `pytube` library for downloading videos.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (3.x recommended) installed on your machine.
- Required Python packages installed. You can install them using `pip`:

pip install flask google-api-python-client pytube


- A Google Cloud Console project with the YouTube Data API enabled. Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/) and replace `'YOUR_API_KEY'` in the code with your actual API key.

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/adarsh-dikhit/youtube-video-download-using-python.git


2. Navigate to the project directory:

cd your-repo-name


3. Run the Flask application:

python app.py


The web application will be accessible at `http://localhost:5000/` in your web browser.

## Usage

- Access the application by opening a web browser and navigating to `http://localhost:5000/`.
- Use the search bar to search for YouTube videos.
- Click on a video link to view more details or click the "Download" button to download the video.

Additionally, you can manually input a video URL in the "Download a Video by URL" section and click the "Download" button to initiate the download.

## Configuration

- To configure the project, replace `'YOUR_API_KEY'` in the code (`app.py`) with your Google Cloud Console API key.
- Customize the project as needed by modifying the HTML templates (`index.html` and `search_results.html`) and the Flask routes.

## Troubleshooting

If you encounter any issues or errors while using the application, please check the following:

- Verify that your API key is correctly configured and has access to the YouTube Data API.
- Check your network connectivity.
- Inspect the browser console for JavaScript errors.
- Review the Flask app's routes and templates for any potential issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/): Web framework for Python.
- [Google API Python Client](https://github.com/googleapis/google-api-python-client): Python client library for Google APIs.
- [pytube](https://github.com/pytube/pytube): Python library for downloading YouTube videos.
