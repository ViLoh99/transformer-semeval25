import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def prepare_text(raw_text):
    
    # Convert text to lowercase and remove punctuation
    normalized_text = raw_text.lower()
    normalized_text = re.sub(r"[^a-zA-Z\s]", "", normalized_text)

    # Tokenize the normalized text
    tokens = word_tokenize(normalized_text)

    # Apply POS tagging and retain only nouns, verbs
    pos_tags = nltk.pos_tag(tokens, tagset='universal')
    pos_tags_to_keep = {"NOUN", "VERB"}
    filtered_tokens = [word for word, pos in pos_tags if pos in pos_tags_to_keep]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_text = [word for word in filtered_tokens if word.lower() not in stop_words]

    # Lemmatize the remaining tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_text = [lemmatizer.lemmatize(word) for word in filtered_text]
    
    return " ".join(lemmatized_text)
