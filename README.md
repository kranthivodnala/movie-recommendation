# Marvel Movie Recommendation Microservices Project

This project implements a Marvel-themed movie recommendation system using microservices architecture. It consists of three main components: a movie service, a recommendation service, and a Python Flask-based frontend with Marvel-themed visuals.

## Project Structure
movie-recommendation/
├── movie-service/          (Movie data CRUD API, Flask)
├── recommendation-service/ (Recommendation engine API, Flask)
├── python-frontend/        (Python Flask frontend with Marvel theme)
├── docker-compose.yml

## Services

### 1. Movie Service (`movie-service`)

-   Provides CRUD (Create, Read, Update, Delete) operations for movie data.
-   Built with Flask.
-   Uses an in-memory data store (for demonstration purposes; replace with a database in production).
-   Exposes the following API endpoints:
    -   `GET /movies`: Retrieves all movies.
    -   `GET /movies/<movie_id>`: Retrieves a specific movie.
    -   `POST /movies`: Creates a new movie.
    -   `PUT /movies/<movie_id>`: Updates a movie.
    -   `DELETE /movies/<movie_id>`: Deletes a movie.

### 2. Recommendation Service (`recommendation-service`)

-   Provides movie recommendations based on genre.
-   Built with Flask.
-   Uses a simple rule-based system for demonstration.
-   Exposes the following API endpoint:
    -   `GET /recommendations?genre=<genre>`: Retrieves movies based on the specified genre.
    -   `GET /recommendations`: Retrieves all movies if no genre filter provided.

### 3. Python Flask Frontend (`python-frontend`)

-   A Python Flask application that serves as the web frontend.
-   Uses Jinja2 templates to render HTML pages.
-   Incorporates Marvel-themed images and attractive transitions.
-   Communicates with the `movie-service` and `recommendation-service` to display and manipulate movie data.
-   Features a slideshow and styled interface using CSS and JavaScript.

## Getting Started

### Prerequisites

-   Docker
-   Docker Compose (optional, for local development)
-   AWS account (for deployment to ECS)

### Local Development

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd movie-recommendation
    ```

2.  **Build and run the services with Docker Compose:**

    ```bash
    docker-compose up --build
    ```

3.  **Access the frontend:**

    Open your browser and navigate to `http://localhost:5002`.

### Deployment to AWS ECS

1.  **Build and push Docker images to Docker Hub:**

    ```bash
    docker build -t movie-service ./movie-service
    docker tag movie-service yourusername/movie-service:latest
    docker push yourusername/movie-service:latest

    docker build -t recommendation-service ./recommendation-service
    docker tag recommendation-service yourusername/recommendation-service:latest
    docker push yourusername/recommendation-service:latest

    docker build -t python-frontend ./python-frontend
    docker tag python-frontend yourusername/python-frontend:latest
    docker push yourusername/python-frontend:latest
    ```

    Replace `yourusername` with your Docker Hub username.

2.  **Create an ECS cluster, task definitions, and services in the AWS console.**

3.  **Configure an Application Load Balancer (ALB) to expose the frontend.**

4.  **(Optional) Configure Route 53 to point your domain to the ALB.**

### Testing

1.  **Access the frontend through the ALB's DNS name.**
2.  **Use the frontend's interface to perform CRUD operations on movies and view recommendations.**
3.  **(Optional) Use tools like Postman or `curl` to test the API endpoints directly.**

## API Endpoints

-   **Movie Service:**
    -   `GET /movies`
    -   `GET /movies/{movie_id}`
    -   `POST /movies`
    -   `PUT /movies/{movie_id}`
    -   `DELETE /movies/{movie_id}`
-   **Recommendation Service:**
    -   `GET /recommendations?genre={genre}`

## Important Notes

-   This project uses an in-memory data store for the movie service. For production, replace it with a persistent database.
-   Implement proper security measures, such as IAM roles, security groups, and HTTPS, when deploying to AWS.
-   Consider using ECS auto-scaling and CloudWatch monitoring for scalability and observability.
-   Set up a CI/CD pipeline to automate the deployment process.
-   Ensure that the `static` directory in `python-frontend` contains the necessary images, css and javascript files.
