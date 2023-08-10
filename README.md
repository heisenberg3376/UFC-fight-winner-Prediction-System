# UFC Fight Winner Prediction System

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Demo](#demo)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Description
Welcome to the UFC Fight Winner Prediction System project! This repository contains the code and resources for a machine learning model that predicts the outcome of UFC fights based on historical data. The project utilizes a Kaggle dataset spanning from 1993 to 2021, employs Logistic Regression for prediction, integrates fighter images using the www.fightingtomatoes.com API, and offers a user-friendly web app powered by Streamlit for fight outcome predictions.

## Features
- Utilizes a Kaggle dataset covering UFC fights from 1993 to 2021 for training and prediction.
- Implements Logistic Regression to predict fight outcomes based on historical data.
- Enhances user experience by fetching fighter images through the fightingtomatoes API.
- Presents a user-friendly web interface with Streamlit for easy fight winner predictions.

## Demo
Try out the [live demo](https://ufc-winner-prediction-system.streamlit.app) of the UFC Fight Winner Prediction System and test its accuracy in predicting fight outcomes!

## Getting Started
Follow these steps to set up the project locally:

1. Clone the repository:
   git clone https://github.com/heisenberg3376/UFC-fight-winner-Prediction-System.git
3. Install the required Python packages:
   pip install -r requirements.txt
3. Run the Streamlit app:
   streamlit run app.py
4. Open your web browser and navigate to `http://localhost:8501` to access the app.

## Usage
1. Open the Streamlit app in your web browser.
2. Input the names of two fighters competing in a UFC match.
3. Click the "Predict" button to receive the predicted outcome of the fight.

## Dependencies
The project relies on the following key dependencies:
- Python (>=3.6)
- Streamlit (>=1.0)
- Pandas (>=1.3)
- Scikit-learn (>=0.24)
- Streamlit-option-menu

For a complete list of dependencies, please refer to the `requirements.txt` file.

## Contributing
Contributions are welcome! If you find a bug or want to enhance the project, feel free to submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License
This project is licensed under the [MIT License](LICENSE).




