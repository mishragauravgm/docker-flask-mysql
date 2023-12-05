# Flask App with MySQL Database

This repository contains a simple Flask application that demonstrates how to connect to a MySQL database for simple user authentication.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) installed on your machine.

### Running the Application

1. Clone this repository:

    ```bash
    git clone https://github.com/mishragauravgm/docker-flask-mysql.git
    cd docker-flask-mysql
    ```

2. Run the Docker containers:

    ```bash
    docker-compose up
    ```

3. Access the application:

    Open a web browser and go to [http://localhost:5000/login](http://localhost:5005) to test the login functionality.

### Application Details

- The Flask application (`app.py`) provides information from a MySQL database.
- The MySQL database is initialized with a sample user table (`users`) containing one user for testing.

### Project Structure

- `app.py`: Contains the Flask application code.
- `init.sql`: Initializes the MySQL database with a sample table and user for testing.
- `Dockerfile`: Builds the Docker image for the Flask app and sets up MySQL.
- `requirements.txt`: Lists the required Python packages for the Flask app.
- `docker-compose.yml`: Configures the services (Flask app and MySQL) to run together using Docker Compose.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
