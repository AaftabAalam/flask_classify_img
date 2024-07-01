# Image Classification Web Application

This project implements an image classification web application using Flask, designed to classify images using a pre-trained model (ResNet50). Users can upload images through a web interface and receive predictions on the content of the image.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Files Included](#files-included)
- [Setup Instructions](#setup-instructions)
  - [Local Setup](#local-setup)
  - [Deployment on Heroku](#deployment-on-heroku)
- [Technologies Used](#technologies-used)

## Overview

This project implements a Flask-based web application for image classification using a pre-trained ResNet50 model. Users can easily upload images via a user-friendly interface and receive instant predictions on their content. The application aims to demonstrate the seamless integration of machine learning with web development, providing a practical example of how complex algorithms can be deployed and accessed through a simple web interface. Targeting students, developers, and researchers interested in machine learning applications, this project showcases the power of AI in real-time image analysis without the need for local setup. Deployable on Heroku for accessibility, it serves as an educational tool and a practical solution for tasks like content moderation, automated tagging, and more.

## Features

List key features and functionalities of your application:

- Upload images for classification.
- Display predictions with confidence scores.
- Support for multiple image formats (e.g., JPG, PNG).

## Files Included

- `app.py`: Flask application that handles image uploads, preprocessing, model prediction, and rendering HTML templates.
- `requirements.txt`: List of Python dependencies required to run the application.
- `Procfile`: Configuration file for Heroku deployment.
- `model.ipynb` or `model.py`: Jupyter Notebook or Python script containing the model creation and training process.
- `templates/`: Directory containing HTML templates for user interface (`upload.html`, `predict.html`).
- `static/`: Directory for static files such as CSS stylesheets, JavaScript scripts, and uploaded images.

## Setup Instructions

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AaftabAalam/flask_classify_img.git
   cd flask_classify_img
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000` to access the application.

### Deployment on Heroku

1. Sign up for a free Heroku account at [https://signup.heroku.com/](https://signup.heroku.com/) if you haven't already.

2. Install the Heroku CLI on your local machine: [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

3. Log in to Heroku CLI:
   ```bash
   heroku login
   ```

4. Initialize a git repository if not already initialized:
   ```bash
   git init
   ```

5. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```

6. Deploy your application to Heroku:
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

7. Open your deployed application in the browser:
   ```bash
   heroku open
   ```

## Technologies Used

- Flask
- Python 3.x
- HTML/CSS
- Heroku
- TensorFlow/Keras (for model training)
