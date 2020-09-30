# Stuffs API

## Table of Contents

## Seeding Data
To seed the database with initial data, run the custom Django management command:

This code is supposed to run inside the container
### 3. Connect to Running container
```sh
./bin/app/connect
```
And run
```sh
python manage.py seed_data
```

## CRUD Operations

#### Components CRUD
| Method | Endpoint                                    | Description                                    |
|--------|---------------------------------------------|------------------------------------------------|
| GET   | /api/stuffs/specifications/{id}/components/  | List all Components in specification           |
| POST   | /api/stuffs/specifications/{id}/components/ | Create a new Component in a specification      |
| GET    | /api/stuffs/components/{id}/                | Retrieve a specific Component                  |
| PUT    | /api/stuffs/components/{id}/                | Update a specific Component                    |
| DELETE | /api/stuffs/components/{id}/                | Delete a specific Component                    |

