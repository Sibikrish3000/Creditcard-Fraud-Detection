<!-- markdownlint-disable -->
<p align="center">
<a href = "https://github.com/Sibikrish3000/Creditcard-Fraud-Detection" > <img src = "https://github.com/Sibikrish3000/Creditcard-Fraud-Detection/blob/main/static/images/creditcard1.jpg?raw=true" alt = "fraud detection image"  width=500 height=280> </a>
</p>
<h1 align="center"> Credit Card Fraud Detection Application </h1>

<p align="center">
This application leverages machine learning to detect fraudulent credit card transactions.
</p>

<p align="center">
<a href="https://github.com/Sibikrish3000/Creditcard-Fraud-Detection/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Sibikrish3000/Creditcard-Fraud-Detection" alt="GitHub license"></a>
<a href="https://github.com/Sibikrish3000/Creditcard-Fraud-Detection/stargazers"><img src="https://img.shields.io/github/stars/Sibikrish3000/Creditcard-Fraud-Detection?style=social" alt="GitHub stars"></a>
<a href="https://github.com/Sibikrish3000/Creditcard-Fraud-Detection/issues"><img src="https://img.shields.io/github/issues/Sibikrish3000/Creditcard-Fraud-Detection" alt="GitHub issues">
</p>
<p align="center">
<a href="https://scikit-learn.org/"><img src=https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white alt="sklearn"></a>
<a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white" alt="language"></a>
<a href="https://fastapi.tiangolo.com/" ><img src="https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white " alt="fastapi"></a> <a href="https://hub.docker.com/repository/docker/sibikrish3000/creditcard-fraud-detection/"><img src="https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white" alt= "docker"></a>





</p>


This project contains a Fraud Detection application that includes a FastAPI server for the backend and a Gradio interface for the frontend. The application can predict if a transaction is fraudulent using either XGBoost or RandomForest models.

[Dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection)
## Overview

1. **FastAPI Backend**: Handles prediction requests using machine learning models.
2. **Gradio Frontend**: Provides a user-friendly web interface for users to input transaction details and get predictions.


## Project Structure

```

/Creditcard-Fraud-Detection
│
├──/model
│   ├── xgboost.pkl
│   └── randomforest.pkl
├──/Encoder
│   └── WOEEncoder.pkl
│
├──/static
│   └──/images
│       ├── github.svg
│       └── api.png
│
├── app.py
├── gradio_app.py
├── docker_app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── features.py

````

- `app.py`: Defines the FastAPI application.
- `gradio_app.py`: Defines the Gradio interface.
- `docker_app.py`: Gradio interface for docker
- `Dockerfile`: Dockerfile for building the Docker image.
- `docker-compose.yml`: Docker Compose file for orchestrating the services.
- `requirements.txt`: List of dependencies.
- `features.py`: List of features.
-  `model/`: Directory containing pre-trained machine learning models.
- `Encoder/`: Directory containing encoders used for data preprocessing.
- `static/`: Directory containing static files such as images used in the interface.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

**Clone the repository:**

   ```bash
   git clone https://github.com/Sibikrish3000/Creditcard-Fraud-Detection.git
   cd Creditcard-Fraud-Detection
   ```
   ```
   git install lfs
   git lfs ls-files
   ```
   ```
   git lfs pull
   ```


## Running Locally

### Using Docker Compose

1. Build and start the containers:
   ```sh
   docker network create AIservice
   ```
    ```sh
    docker-compose up --build
    ```

2. Access the Gradio interface at [http://localhost:7860](http://localhost:7860).

### Using Docker image

```sh
docker network create AIservice
```
```sh
docker pull sibikrish/creditcard-fraud-detection:latest
docker run sibikrish/creditcard-fraud-detection:latest #or 
docker run -d -p 7860:7860 sibikrish/creditcard-fraud-detection:latest
 ``` 
### Run with Huggingface Docker Space
```
docker run -it -p 7860:7860 --platform=linux/amd64 \ registry.hf.space/sibikrish-creditcard-fraud-detection:latest python gradio_app.py
```
### Manually

To run the application locally without Docker, ensure you have Python installed and follow these steps:

1. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI server:**

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

3. **Run the Gradio interface:**

   ```bash
   python gradio_app.py
   ```

## Development
### Running in a Gitpod Cloud Environment

**Click the button below to start a new development environment:**

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Sibikrish3000/Creditcard-Fraud-Detection)




## Usage

1. **Access the Gradio Interface:**

   Open your web browser and navigate to `http://localhost:7860` to access the Gradio interface.

    - **Inputs**: Users can input transaction details such as credit card frequency, job, age, gender, category, distance, hour, hours difference between transactions, amount, and choose a model.
    - **Output**: The application returns a prediction indicating whether the transaction is legitimate or fraudulent.
    - **Flag Option**: Users can enable a flag option to provide feedback on incorrect or suspicious predictions.


2. **Access the FastAPI Documentation:**

   Open your web browser and navigate to `http://localhost:8000/docs` to access the FastAPI documentation.

### API Endpoints

- **POST /predict**

  Predict if a transaction is fraudulent.

  **Request:**

  ```json
  {
    "cc_freq": int,
    "cc_freq_class": int,
    "job": str,
    "age": int,
    "gender_M": int,
    "category": str,
    "distance_km": float,
    "hour": str,
    "hours_diff_bet_trans": float,
    "amt": float
  }
  ```

  **Response:**

  ```json
  {
    "prediction": 0 for legitimate, 1 for fraudulent
  }
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


