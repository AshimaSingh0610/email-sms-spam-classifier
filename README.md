

<div align="center">  
  <h1>📧 Email & SMS Spam Classifier ✉️</h1>    
  <p>A Machine Learning project that helps classify emails and SMS messages into Spam or Non-Spam using NLP techniques.</p>  
  <a href="https://github.com/AshimaSingh0610/email-sms-spam-classifier/issues">
    <img src="https://img.shields.io/github/issues/AshimaSingh0610/email-sms-spam-classifier.svg" alt="Issues">
  </a>  
  <a href="https://github.com/AshimaSingh0610/email-sms-spam-classifier/pulls">
    <img src="https://img.shields.io/github/issues-pr/AshimaSingh0610/email-sms-spam-classifier.svg" alt="Pull Requests">
  </a>
</div>

---

## 📖 **Introduction**

Welcome to the **Email & SMS Spam Classifier** project! This project leverages **Natural Language Processing (NLP)** techniques and **Machine Learning** to accurately classify messages as **Spam** or **Non-Spam (Ham)**. Whether you want to filter out annoying spam messages or identify legitimate communications, this tool is designed to help you. 

With an intuitive **user interface** built using **Streamlit**, users can easily input emails or SMS messages and receive real-time classification results.

---

## 🚀 **Key Features**

- **💡 Advanced NLP Techniques**: The classifier employs cutting-edge **NLP algorithms** like **Naive Bayes** and **Support Vector Machines (SVM)** to ensure high accuracy.
- **📲 Multi-Platform**: Supports classification for both **Emails** and **SMS** messages.
- **👨‍💻 User-Friendly Interface**: Built using **Streamlit**, providing a simple and clean UI for users to interact with the model easily.
- **📈 High Accuracy**: Achieved a **95% accuracy rate** with significant reduction in false positives, ensuring reliable classifications.
- **⚡ Real-Time Results**: Quickly processes inputs and delivers instant predictions, making it useful for fast-paced environments.

---

## 🛠️ **Technologies Used**

This project integrates various tools and libraries to achieve high performance and ease of use:

- **Python**: The primary language for building the model and backend logic.
- **Scikit-learn**: For building, training, and validating the machine learning models.
- **Natural Language Toolkit (NLTK)**: Used for text preprocessing, tokenization, and feature extraction.
- **Streamlit**: Framework used for creating the web interface for easy interaction with the classifier.
- **Pandas**: For efficient data handling and manipulation.
- **Google Colab**: Used for faster model training and experimentation in the cloud.

---

## 🎯 **How the Model Works**

The spam classifier analyzes the textual content of emails and SMS messages to predict whether they are spam or ham. Here’s how it works:

1. **Data Collection**: A dataset of labeled email and SMS messages is used to train the model.
2. **Preprocessing**: The textual data is preprocessed using techniques such as tokenization, removing stop words, and lemmatization.
3. **Feature Extraction**: Relevant features are extracted using **TF-IDF** (Term Frequency-Inverse Document Frequency) to convert text into numerical vectors.
4. **Model Training**: Using algorithms like **Naive Bayes** and **SVM**, the classifier is trained on this preprocessed and feature-extracted data.
5. **Prediction**: The trained model is used to predict whether a new email or SMS message is spam or non-spam.

---

## 🔍 **Model Performance**

- **Accuracy**: Achieved **95% accuracy** in distinguishing between spam and ham.
- **Error Reduction**: False positives were reduced by **80%**, ensuring reliable spam filtering.
- **Cross-Validation**: 5-fold cross-validation was performed to ensure model robustness.

---

## 💻 **Installation Guide**

### Step-by-Step Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AshimaSingh0610/email-sms-spam-classifier.git

2. **Navigate to the Project Directory**  
   Change your directory to the cloned project folder:
   ```bash
   cd email-sms-spam-classifier

3. **Create a Virtual Environment**  
   It's a good practice to create a virtual environment for Python projects to manage dependencies:
   ```bash
   python3 -m venv venv
   
4. **Install Required Dependencies**  
  Install the necessary Python libraries using the requirements file included in the project:
   ```bash
   pip install -r requirements.txt

5. **Run the Application**  
  Start the Streamlit web app with the following command:
   ```bash
   streamlit run app.py
  
6. **Access the App**  
Open your web browser and go to http://localhost:8501/ to access the Email & SMS Spam Classifier interface.
 
---

## 🖼️ **Software Design**

Below is the software design for the Email & SMS Spam Classifier project:

![Software Design II](https://github.com/user-attachments/assets/d5bf8d8c-5100-48a9-b816-097d04eeffe5)
![Software Design ](https://github.com/user-attachments/assets/f4cd7dad-7554-47c7-9cf7-f45c06ba9939)


---

## 🚀 **Features to be Added**

### Planned Enhancements

- **📈 Model Improvement**: Continuously refine the spam classification model using more advanced machine learning algorithms and techniques.
  
- **🌍 Multi-Language Support**: Expand the model to classify spam messages in multiple languages, enhancing usability for a global audience.
  
- **📊 Analytics Dashboard**: Integrate a dashboard that provides insights into spam detection rates, types of spam messages, and user interactions.
  
- **🔔 Real-time Notifications**: Implement a notification system that alerts users when spam messages are detected, allowing for immediate action.

- **🛠️ User Customization**: Allow users to customize spam filters based on their preferences, improving the accuracy of the classifier.

- **🔒 Enhanced Security Features**: Incorporate measures to ensure user data privacy and security, especially when processing sensitive information.

---


## 🙌 **Contributing**

We love contributions! Help us make this repository even better by contributing to the project. Your input is highly valued. 🤗

1. **Fork the Project**: Click the "Fork" button at the top right of the repository page.
2. **Create your Feature Branch**:
    ```bash
    git checkout -b feature/AmazingFeature
    ```
3. **Commit your Changes**:
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
4. **Push to the Branch**:
    ```bash
    git push origin feature/AmazingFeature
    ```
5. **Open a Pull Request**:
    1. Navigate to the "Pull Requests" tab in the repository.
    2. Click "New Pull Request".
    3. Select your feature branch and compare it with the main branch.
    4. Add a descriptive title and comments about your changes.
    5. Click "Create Pull Request".

---
## ✍️ **Authors**

- [@AshimaSingh0610](https://github.com/AshimaSingh0610) - Creator & Maintainer





