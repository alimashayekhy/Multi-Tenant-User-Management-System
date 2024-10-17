# multi-tenant-user-ms Backend

## Table of Contents

- [multi-tenant-user-ms Backend](#multi-tenant-user-ms-Backend)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
  - [License](#license)

## Introduction

Multi-Tenant User Management System with Custom Permissions: A Django-based system that supports multiple organizations with isolated user data. It features custom roles and permissions for fine-grained access control, and a RESTful API for managing users, roles, and access securely across tenants.

This is the backend source code of MTUMS. used django rest framework and postgres database

## Features

- Multi-tenancy with data isolation using PostgreSQL schemas
- Custom user roles: Admin, Technician, Operator, Regular User
- JWT Authentication
- RESTful APIs for managing tenants and users

## Getting Started

1. **Clone the Repository**
   To get this repository, run the following command inside your terminal
   ```shell
   git clone https://github.com/alimashayekhy/multi-tenant-user-management.git
   ```

### Installation

Before proceeding with the installation, make sure to perform the following steps:

1. **Edit Environment Files:**

   - Navigate to the following paths within your project directory:

     ```shell
     envs/prod/db/.env.sample
     envs/prod/django/.env.sample
     ```

   - Rename these `.env.sample` files to `.env`.

   - Open each `.env` file and configure your environment variables as needed for your project.

2. **Edit Nginx Configuration:**

   - Locate the `default.conf` file in the root directory of your project.

   - Open the `default.conf` file and customize the Nginx configuration settings according to your project requirements.

3. **Docker Setupn:**

If you want to run the project locally, make sure you have Docker installed. You can download it from Docker's official website.

4. **Running the Project:**

To run the project for development purposes, use the following command:

```shell
docker-compose up -d
```

These commands will start the necessary Docker containers and run your project. Make sure to replace docker-compose-prod with the actual name of your production Docker Compose file if it's different.

After starting the Docker container, follow these commands to set up your database and create a superuser:

**Migrate Database:**

Run the following commands to apply database migrations:

```shell
docker exec -it backend sh -c "python manage.py startapp tenants"
docker exec -it backend sh -c "python manage.py startapp users"
docker exec -it backend sh -c "python manage.py startapp authentication"
docker exec -it backend sh -c "python manage.py migrate"
```

**create Super User:**

```
docker exec -it backend sh -c "python manage.py createsuperuser"
```

**Run the Command to Create Tenants:**

```
python manage.py create_sample_tenants
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
