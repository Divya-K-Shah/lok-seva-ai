import pickle
from preprocess import preprocess_text

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_category(text):
    processed = preprocess_text(text)
    vec = vectorizer.transform([processed])
    return model.predict(vec)[0]