# Personalized News Update Aggregator

## Overview

The Personalized News Update Aggregator is a microservice-based application that aggregates news and technology updates based on user preferences. It fetches the latest news, selects the most interesting news using AI, generates concise summaries, and sends the information to users via email.

## Purpose of the System

The system aims to provide users with personalized news updates, ensuring that they receive the most relevant and interesting news based on their preferences. The application leverages AI for summarizing news articles, making it easier for users to consume information quickly.

## System Diagram

### Components:

- **User Service** 
    Manages user registration and preferences.
    Interacts with a database to store user information.

- **News Aggregation Service**
    Fetches the latest news based on user preferences from NewsData.io.
    Uses AI Service to summarize the news articles.

- **Email Service**
    Sends summarized news to users via email.
    Interacts with an SMTP server to send emails.

- **AI Service**
    Uses Gemini Free Tier API to process and summarize text.

- **API Gateway**
    Acts as a single entry point for the clients.
    Routes requests to appropriate services and aggregates responses.

- **UI**
    Provides a user interface for interacting with the application.
    Users can register, set preferences, and view news summaries.

### Interactions:
    The User Service receives requests from the UI to register users and set preferences. It stores user data in the database.
    The API Gateway receives requests from the UI to aggregate news. It interacts with the News Aggregation Service to fetch and summarize news.
    The News Aggregation Service fetches news from NewsData.io based on user preferences and uses the AI Service to summarize the news.
    The AI Service processes and summarizes news articles using the Gemini Free Tier API.
    The News Aggregation Service sends the summarized news to the Email Service.
    The Email Service sends the summarized news to users via email.
    The UI displays the news summaries to users.

 Diagram:
+---------------------------+                +----------------------------+
|          User             |                |         API Gateway        |
|   Interface (UI)          |<-------------->|                            |
|  (Register, Preferences,  |                |                            |
|    View Summaries)        |                +----------------------------+
+---------------------------+                             |
                                                         / \
                                                          |
                                                          |
+---------------------------+                             |
|      User Service         |<----------------------------+
|  (Register, Preferences)  |                             |
|       [Database]          |                             |
+---------------------------+                             |
                                                          |
                                                          |
+---------------------------+                             |
|  News Aggregation Service |<----------------------------+
|    (Fetch & Summarize     |                             |
|        News)              |                             |
+---------------------------+                             |
                    |                                     |
                    |                                     |
                    |                                     |
                    |                                     |
                    v                                     v
+---------------------------+                  +--------------------------+
|      AI Service           |                  |       Email Service      |
|   (Summarize Text)        |<---------------->|   (Send Summaries via    |
+---------------------------+                  |           Email)         |
                                               +--------------------------+


 Project Structure

personalized-news-aggregator/
│
├── user-service/
│ ├── app/
│ │ ├── init.py
│ │ ├── views.py
│ │ ├── manager.py
│ │ ├── engine.py
│ │ ├── accessor.py
│ │ ├── resource.py
│ │ └── tests.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── news-aggregation-service/
│ ├── app/
│ │ ├── init.py
│ │ ├── views.py
│ │ ├── manager.py
│ │ ├── engine.py
│ │ ├── accessor.py
│ │ └── tests.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── email-service/
│ ├── app/
│ │ ├── init.py
│ │ ├── views.py
│ │ ├── manager.py
│ │ ├── engine.py
│ │ ├── accessor.py
│ │ └── tests.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── ai-service/
│ ├── app/
│ │ ├── init.py
│ │ ├── views.py
│ │ ├── manager.py
│ │ ├── engine.py
│ │ ├── accessor.py
│ │ └── tests.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── api-gateway/
│ ├── app/
│ │ ├── init.py
│ │ ├── views.py
│ │ ├── manager.py
│ │ ├── engine.py
│ │ ├── accessor.py
│ │ └── tests.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── ui/
│ ├── public/
│ │ ├── index.html
│ ├── src/
│ │ ├── App.js
│ │ ├── index.js
│ │ ├── components/
│ │ │ ├── Register.js
│ │ │ ├── Preferences.js
│ │ │ └── NewsSummaries.js
│ ├── Dockerfile
│ └── package.json
│
├── docker-compose.yml
├── .env
├── README.md
└── postman_collection.json


## Steps to Run the Application Locally

### Prerequisites

- Docker and Docker Compose

### Steps

1. Clone the repository.
   ```bash
   git clone https://github.com/your-username/personalized-news-aggregator.git
   cd personalized-news-aggregator


2. Create a .env file in the root directory with the following content:
    FLASK_APP=app
    FLASK_ENV=development
    SQLALCHEMY_DATABASE_URI=sqlite:///users.db
    NEWS_API_KEY=your_newsdata_api_key
    GEMINI_API_KEY=your_gemini_api_key
    EMAIL_HOST=smtp.example.com
    EMAIL_PORT=587
    EMAIL_USERNAME=your_email@example.com
    EMAIL_PASSWORD=your_password


3. Run docker-compose up --build to start the services.`
    ``bash
    docker-compose up --build

4. Access the UI at http://localhost:3000.
   
#### Instructions for Testing the Application
1. Unit Tests
    Unit tests are provided for each service. To run the tests, navigate to the respective service directory and execute the following command:
    ``bash
    python -m unittest discover -s app -p "tests.py"

2. Integration Tests
    - Integration tests are included in the Postman collection. To run the integration tests:
    - Import the postman_collection.json file into Postman.

#### Run the collection in Postman to test the API endpoints.
    Technologies Used :
    - Flask
    - React
    - Docker
    - Requests
    - SQLAlchemy

#### Environment Variables
    Ensure you replace placeholders in the .env file (like API keys and email credentials) with actual values or use environment variables.

#### Exception Handling
    Each service includes basic exception handling. You can enhance it further by adding custom exceptions and more detailed error logging.

#### IDesign Analysis Architecture Method
    The project follows the IDesign analysis architecture method, using manager, engine, accessor, and resource files for clean and maintainable code.


## System Diagram
User Interface (UI)
      |
API Gateway
      |
      +--------------------------------+
      |                                |
User Service  News Aggregation  Email Service  AI Service
      |            |                 |              |
   Redis       External API       SMTP           External API
               (NewsData.io)                    (Hugging Face)
            +--------------------------------+
            |          Dapr Components       |
            +--------------------------------+
