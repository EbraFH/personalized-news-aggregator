# Personalized News Update Aggregator

## Introduction

The Personalized News Update Aggregator is a microservice-based application that aggregates news and technology updates based on user preferences. The system fetches the latest news, picks the most interesting news using AI based on user preferences, generates concise summaries using AI, and sends this information to users via email.

## Prerequisites

- Docker
- Docker Compose
- Python 3.9
- Node.js

## Installation

  1. Clone the repository:

    ```bash
  git clone https://github.com/your-repo/personalized-news-update-aggregator.git
  cd personalized-news-update-aggregator



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
