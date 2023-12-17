# Helper functions for api endpoints
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from .llm_wrapper import pharaphrase_text


# Predict whether the text is suicidal
def predict(text_list, threshold):
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

    # new_input_pred = np.round(new_input_pred)
    print("Prediction for the new input:", [x for x in new_input_pred if x > threshold])

    pred_list = []
    for i in range(len(new_input_pred)):
        if new_input_pred[i][0] >= threshold:
            modified_text = pharaphrase_text(new_input[i])
            pred_list.append((new_input[i], modified_text["response"]))

    return pred_list
