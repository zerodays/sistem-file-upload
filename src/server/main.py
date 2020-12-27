import os
import traceback
import uuid

import server.config as config
import server.spaces as spaces
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_url_path='')

app.config.debug = config.DEBUG
app.config['MAX_CONTENT_LENGTH'] = config.MAX_FILE_SIZE


@app.route('/files', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return '', 400

    file = request.files['file']

    if file.filename == '' or not file:
        return '', 400

    file_id = uuid.uuid4().hex
    location = os.path.join(config.UPLOAD_FOLDER, file_id)
    file.save(location)

    # Upload file
    with open(location, 'rb') as f:
        spaces.upload_file(file_id, f.read())

    return jsonify({'file_id': file_id}), 200


@app.route('/files/<file_id>', methods=['GET', 'DELETE'])
def files(file_id):
    if request.method == 'GET':
        # Download file from Digital Ocean
        try:
            folder, filename = spaces.download_file(file_id)
        except Exception:
            traceback.print_exc()
            return '', 404

        # Return file
        return send_from_directory(os.path.join('..', folder), filename=filename)

    elif request.method == 'DELETE':
        # Delete file from Digital ocean
        spaces.delete_file(file_id)
        return '', 200

    return '', 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT)
