# Stuffs API

Stuffs API is a Django-based application designed to manage Specifications, Groups, and Components. This application allows for creating, updating, and cloning specifications

## Table of Contents

- [Installation & Usage](#installation)
- [Seeding Data](#seeding-data)
- [Feature Documentation](#feature-documentation)
   - [Specifications CRUD](#specifications-crud)
   - [Groups CRUD](#groups-crud)
   - [Components CRUD](#components-crud)
   - [Clone Specifications](#clone-specifications)
   - [Import Specifications](#import-specifications)
   - [Export Built Specifications Report](#export-built-specifications-report)

## Installation

### 2. **Use Docker to run the project**
```sh
   docker-compose up -d
```

OR
```sh
./bin/start-all
```
That's all you will be able to access the application at localhost:8000


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

#### Specifications CRUD

#### Groups CRUD
| Method | Endpoint                               | Description                            |
|--------|----------------------------------------|----------------------------------------|
| GET   | /api/stuffs/specifications/{id}/groups  | List all groups in specification       |
| POST   | /api/stuffs/specifications/{id}/groups | Create a new group in a specification  |
| GET    | /api/stuffs/groups/{id}/               | Retrieve a specific group              |
| PUT    | /api/stuffs/groups/{id}/               | Update a specific group                |
| DELETE | /api/stuffs/groups/{id}/               | Delete a specific group                |

#### Components CRUD
| Method | Endpoint                                    | Description                                    |
|--------|---------------------------------------------|------------------------------------------------|
| GET   | /api/stuffs/specifications/{id}/components/  | List all Components in specification           |
| POST   | /api/stuffs/specifications/{id}/components/ | Create a new Component in a specification      |
| GET    | /api/stuffs/components/{id}/                | Retrieve a specific Component                  |
| PUT    | /api/stuffs/components/{id}/                | Update a specific Component                    |
| DELETE | /api/stuffs/components/{id}/                | Delete a specific Component                    |

### Implementation

- **Views**:
  - `SpecificationViewSet`: Uses Django Rest Framework's ModelViewSet to handle CRUD operations for specifications.
  - `NestedSpecificationGroupViewSet`: Uses Custom Viewset to provide List and Create operations for *groups in a specification.
  - `NestedSpecificationComponentsViewSet`: Uses Custom Viewset to provide List and Create operations for *Components* in a specification.
  - `GroupViewSet`: Uses Django Rest Framework's ModelViewSet to handle CRUD operations for groups.
  - `ComponentViewSet`: Uses Django Rest Framework's ModelViewSet to handle CRUD operations for components.

## Clone Specifications

### API Endpoint

| Method | Endpoint                                  | Description                        |
|--------|-------------------------------------------|------------------------------------|
| POST   | /api/stuffs/specifications/{id}/clone/    | Clone a specific specification     |

