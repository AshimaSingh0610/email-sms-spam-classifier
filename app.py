import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Tokenize text
    text = nltk.word_tokenize(text)

    # Remove non-alphanumeric characters
    text = [i for i in text if i.isalnum()]

    # Remove stopwords and punctuation
    text = [i for i in text if i not in stopwords.words('english') and i not in string.punctuation]

    # Perform stemming
    text = [ps.stem(i) for i in text]

    return " ".join(text)

# Load the TF-IDF vectorizer and the classification model
tfidf = pickle.load(open(r'email-sms-spam-classifier\vectorizer.pkl', 'rb'))
model = pickle.load(open(r'email-sms-spam-classifier\model.pkl', 'rb'))

# Streamlit UI
st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. Preprocessing
    transformed_sms = transform_text(input_sms)

    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])

    # 3. Predict
    result = model.predict(vector_input)[0]

    # 4. Display result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

# Background box for examples
with st.markdown(
    """
    <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
        <p style='font-weight: bold;'>Example snippets are:</p>
        <ul>
            <li>Congratulations you won 1000 call on this number to get your prize.</li>
        </ul>
        <ul>
            <li>Reminder: Your meeting is scheduled for tomorrow at 10 AM in Conference Room A.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
):
    pass