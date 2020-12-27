import os

DEBUG = True

PORT = int(os.environ.get('PORT', default='8080'))

SPACES_KEY = os.environ.get('SPACES_KEY')
SPACES_SECRET = os.environ.get('SPACES_SECRET')

SPACES_BUCKET = os.environ.get('SPACES_BUCKET', default='sistem-space')
SPACES_ENDPOINT = os.environ.get('SPACES_ENDPOINT', default='https://fra1.digitaloceanspaces.com')
SPACES_REGION = os.environ.get('SPACES_REGION', default='fra1')

FILES_FOLDER = os.environ.get('FILE_DOWNLOAD_FOLDER', default='data')
UPLOAD_FOLDER = os.environ.get('FILE_DOWNLOAD_FOLDER', default='upload_data')

os.makedirs(FILES_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB