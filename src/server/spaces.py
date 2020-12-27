import os

import boto3
import server.config as config

session = boto3.session.Session()
client = session.client('s3',
                        region_name=config.SPACES_REGION,
                        endpoint_url=config.SPACES_ENDPOINT,
                        aws_access_key_id=config.SPACES_KEY,
                        aws_secret_access_key=config.SPACES_SECRET)


def upload_file(filename, content) -> None:
    """
    Uploads file to bucketstorage.
    :param filename: Name of a file to upload.
    :param content: Actual file data to upload.
    """
    client.put_object(Bucket=config.SPACES_BUCKET,
                      Key=filename,
                      Body=content,
                      ACL='private')


def download_file(filename) -> tuple:
    """
    Downloads file with filename from bucketstorage.
    Returns path where file is saved.
    :param filename: File to download
    :return: Tuple folder, location where downloaded file is saved.
    """
    save_path = os.path.join(config.FILES_FOLDER, filename)

    client.download_file(config.SPACES_BUCKET,
                         filename,
                         save_path)
    return config.FILES_FOLDER, filename


def delete_file(filename):
    """
    Delete file from bucket storage.
    :param filename:
    :return:
    """
    client.delete_object(Bucket=config.SPACES_BUCKET,
                         Key=filename)
