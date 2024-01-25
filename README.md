# Haron Computers CRM

## Setup

### Pre-requisites

- [Docker](https://docs.docker.com/get-docker/)

### Installation

1. Clone the repository

    ```bash
    git clone https://github.com/mubareksd/haron_crm.git
    ```

2. Copy the `.env.example` file to `.env`

    ```bash
    cp .env.example .env
    ```

3. Update the `.env` file with your application settings

4. Build the containers

    ```bash
    docker-compose build
    ```

5. Start the containers

    ```bash
    docker-compose up -d
    ```

## Usage

### Accessing the application

The application will be available at [http://172.52.0.2](http://172.52.0.2)

### Accessing the database

phpMyAdmin will be available at [http://172.52.0.4](http://172.52.0.4)