import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from langdetect import detect
from deep_translator import GoogleTranslator

# 🔹 Preprocess function
def preprocess_text(text):
    try:
        if detect(text) != 'en':
            text = GoogleTranslator(source='auto', target='en').translate(text)
    except:
        pass
    return text.lower()

# 🔹 Load dataset
df = pd.read_excel("../dataset/kdmc_data.xlsx")

# 🔹 Rename columns (IMPORTANT)
df.rename(columns={
    "Complaint Description": "complaint",
    "Complaint Type": "category"
}, inplace=True)

# 🔹 Remove nulls
df = df[['complaint', 'category']].dropna()

# 🔹 Clean text
df['clean_text'] = df['complaint'].astype(str).apply(preprocess_text)

# 🔹 Features & labels
X = df['clean_text']
y = df['category']

# 🔹 Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# 🔹 Model
model = LogisticRegression(max_iter=200)
model.fit(X_vec, y)

# 🔹 Save
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained successfully on KDMC dataset")