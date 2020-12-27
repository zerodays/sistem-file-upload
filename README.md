# Sistem file upload

Sistem microservice for file upload.

Add correct `SPACES_KEY` and `SPACES_SECRET` to environment.

Endpoints:

- `/files`, `POST`: Upload new file. Returns JSON `{'file_id': 'ID_OF_UPLOADED_FILE'}`.
- `/files/<FILE_ID>`, `GET`: Get uploaded file with given ID.
- `/files/<FILE_ID>`, `DELETE`: Delete uploaded file with given ID.
