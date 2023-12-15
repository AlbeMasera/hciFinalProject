# Helper functions for api endpoints
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


# Predict whether the text is suicidal
def predict(text_list):
    from scipy.sparse import spmatrix

    # Load the classifier and vectorizer
    classifier = pickle.load(open("model/model.pkl", "rb"))
    vocabulary = pickle.load(open("model/vectorizer_obj.pkl", "rb"))

    vectorizer2 = TfidfVectorizer(vocabulary=vocabulary)

    # Define new input
    new_input = text_list

    # Transform the new input using the loaded vectorizer
    to_pred_dense = vectorizer2.fit_transform(new_input).toarray()

    # Make predictions on the new input
    new_input_pred = classifier.predict(to_pred_dense)

    new_input_pred = np.round(new_input_pred)
    print("Prediction for the new input:", new_input_pred)
    pred_list = []
    for elem in new_input_pred:
        pred_list.append(elem[0])
    return pred_list
