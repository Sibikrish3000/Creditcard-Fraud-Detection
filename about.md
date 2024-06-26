# Credit Card Fraud Detection App built with Gradio, FastAPI, and Docker

This Credit Card Fraud Detection App leverages Machine Learning models served as an API to identify potentially fraudulent credit card transactions, empowering users to assess transaction legitimacy based on various input features including credit card frequency, job, age, gender, category, distance, hour, hours difference between transactions, amount, and model choice (XGBoost or RandomForest).
### Features:

1. **FastAPI Backend**: The backend of the application is implemented using FastAPI, a modern web framework for building APIs with Python. It exposes an endpoint `/predict` that accepts POST requests with transaction data and returns predictions.

2. **Gradio Frontend**: The frontend of the application is implemented using Gradio, a Python library that allows for the creation of customizable UI components for machine learning models. Users interact with the application through a user-friendly interface where they can input transaction details and receive predictions.

 3. **Models**:  The utilization of both XGBoost and RandomForest models ensures robust prediction capabilities, leveraging powerful machine learning algorithms widely recognized for their effectiveness in classification and regression tasks.

4. **Flagging Option**: Users can flag examples in the interface, providing feedback on predictions that seem incorrect or suspicious. This functionality allows for continuous improvement of the model.

### Usage:

- Users can run the application locally by executing the provided Python script.
- They can interact with the application through the Gradio interface in their web browser, inputting transaction details and receiving predictions.
- The application provides predictions in real-time, leveraging machine learning models trained on historical transaction data.

### Deployment:

- The application can be deployed locally or on a cloud platform using Docker. Docker containers encapsulate both the FastAPI backend and the Gradio frontend, making deployment straightforward.
- Additionally, the application can be deployed to a serverless platform like Vercel or Heroku, leveraging their respective deployment methods.

### Future Improvements:

1. Enhance model performance by fine-tuning hyperparameters or using more sophisticated models.
2. Add more features to improve prediction accuracy.
3. Implement user authentication and authorization for secure access to the application.
4. Integrate with a database to store flagged examples for analysis and model improvement.

### Development:

- Developers can extend and enhance the application by adding new features, improving model accuracy, or optimizing performance.
- The codebase is modular and well-structured, facilitating easy maintenance and collaboration among developers.

Overall, this Fraud Detection application provides a practical solution for identifying potentially fraudulent transactions, helping businesses and organizations mitigate financial risks.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Sibikrish3000/Creditcard-Fraud-Detection/blob/main/LICENSE) file for details.

The Jupyter notebook, trained model, and accompanying documentation, including Dockerfiles, FastAPI script, and Gradio Interface script, can be accessed through the GitHub repository linked below:

[GitHub Repository](https://github.com/Sibikrish3000/Creditcard-Fraud-Detection)

[![size](https://img.shields.io/github/repo-size/Sibikrish3000/Creditcard-Fraud-Detection)](https://github.com/Sibikrish3000/)

Please feel free to explore and utilize these resources for credit card fraud detection purposes.

### [@Sibi Krishnamoorthy](https://sibikrish3000.github.io/portfolio/)
___

<h5 align="center">
Sibi Krishnamoorthy
</h5><p align="center">
A Data Science student with a passion for Machine Learning and Artificial intelligence
</p><p style="color:teal" align="center">
&copy Sibikrish. All rights reserved 2024
</p>


