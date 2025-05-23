# transformer-semeval25

Task 1
AdMIRe - Advancing Multimodal Idiomaticity Representation:
https://semeval2025-task1.github.io/


Notebooks:

subtaskA_1 : similarity between compound and/or sentence and captions embeddings with SBERT; random baseline

subtaskA_captions_cut: different ranking for idiomatic; captions cut to certain word / sentence count

subtaskA_train_preprocessing: basic approach from subtaskA_1 adapted to include preprocessing

subtaskA_descriptions: integrating ChatGPT descriptions & captions; alternative similarity scores

subtaskA_dev: subtaskA_1 adapted for development data

subtaskA_regression: trying out logistic regression and similar methods for ranking and judging idiomatic / literal

subtaskA_BERT_embeddings: computes sentence and compound embeddings of all sentence-like columns. Embeddings are saved in pkl file

subtaskA_predictions_from_BERT : computes binary idomatic/literal classification predictions and ranking predictions on BERT embeddings. Needs a pkl file generated with notebook subtaskA_BERT_embeddings. Generates a pkl file binary_pred with binary classification predictions

subtaskA_1_experiments: Adaption of subtaskA_1 that uses SBERT to generate ranking predictions. Needs pkl file generated in subtaskA_predictions_from_BERT 

subtaskA_combine_BERT_SBERT : uses predictions from subtaskA_predictions_from_BERT (needs pkl file) for literal / idiomatic information & SBERT for ranking

subtaskA_test: get submission format for test data with best combination from subtaskA_dev (compound & preprocessing) & from subtaskA_combine_BERT_SBERT

subtaskB: SBERT & cosine similarity

subtaskB_expreiments: SBERT, BERT , cosine similarity 

Dataset Overview - **_gpt-desc.csv_**


This dataset was generated using ChatGPT-4 (chatgpt4o) and combined with existing data from the SemEval task to create a comprehensive training dataset. It consists of entries structured with a Compound Noun, sentence type, Meaning, Illustration, and Illustrative Sentence. The dataset is designed to support linguistic model training, focusing on compound nouns and idiomatic expressions.


The ChatGPT-generated data was created across multiple sessions on 17.11.2024 and 24.11.2024, while the SemEval dataset provides additional context and examples for real-world application.

**Dataset Construction:**

ChatGPT-Generated Data
This part of the dataset was created through iterative prompts aimed at generating creative examples of compound nouns and idiomatic phrases.

Example prompt structure:


_**Explain me "Outer space" in one sentence and give me an illustration but without picture and provide me an illustrative sentence.**_


ChatGPT responses included the following structure:


_**Meaning: A concise explanation of the term.**_


_**sentence type: A type of the Illustration.**_


_**Illustration (sentence): A vivid, text-based depiction designed to enhance understanding.**_


_**Illustrative Sentence (pic_sentence): A contextual example of usage.**_


Example Entry:


**Outer Space**

Meaning: Outer space refers to the vast, nearly empty expanse beyond Earth's atmosphere, where celestial bodies such as stars, planets, and galaxies exist.


Illustration: For an illustration, imagine a black, star-studded void with the Earth in the foreground, its blue and green hues illuminated by sunlight. Surrounding it, the moon orbits at a distance, while further away, tiny, glowing stars and planets punctuate the endless darkness, emphasizing the immense scale and mystery of outer space.


Illustrative Sentence: The astronauts stared out of their capsule into the vast expanse of outer space, marveling at the distant stars and galaxies.




**Fine-Tuning BERT for Subtask A**

This repository contains a Jupyter Notebook for fine-tuning a pre-trained BERT model on Subtask A. The notebook includes steps for model training, evaluation, and uploading the trained model to Hugging Face.


**Dataset and Model**

The data used for this project is in the Jupyter Notebook named subtaskA_bert-model-fine-tuning.ipynb. The pre-trained model is based on bert-base-uncased. The model is fine-tuned using the dataset gpt-desc.csv to learn the compound, sentence type, and sentence. The goal is to recognize whether a given sentence is literal or idiomatic.


**Features**

Maps idiomatic and literal types: Literal sentences are labeled as 0, while idiomatic sentences are labeled as 1.

Combines sentence type and compound: Uses [SEP] to separate components, ensuring compatibility with Hugging Face.

Splits data: Uses an 80% training and 20% test split.

Uses Hugging Face Trainer API: Automates training instead of manual tuning and tracks results with wandb.

Monitors performance: Tracks training loss and validation loss.

Uploads to Hugging Face: The trained model is pushed for deployment.


**Requirements**

To run this notebook, install the required dependencies using:

pip install transformers datasets torch


**Usage**

Load the dataset and preprocess it.

Fine-tune the BERT model using Hugging Face's Trainer.

Evaluate the model on test data.

Save and push the model to Hugging Face.

Run the notebook step by step to execute the training process.


**Model Deployment**

Once fine-tuned, the model is pushed to Hugging Face for sharing and deployment. You can access it using:

from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained("jlsalim/bert-uncased-idiomatic-literal-recognizer")


**License**

This project is released under the MIT License.



**Acknowledgments**


This dataset combines the generative capabilities of ChatGPT-4 with the annotations from the SemEval task, creating a resource that is both creative and grounded in linguistic research.



**Codabench Pages**

TaskA model selection [[https://www.codabench.org/competitions/4920/#/results-tab]]

TaskA competition page [[https://www.codabench.org/competitions/4813/#/results-tab]]

TaskB model selection [[https://www.codabench.org/competitions/4922/#/results-tab]]

TaskB competition page [[https://www.codabench.org/competitions/4815/]]
<<<<<<< Updated upstream

Shared Task page [[https://semeval2025-task1.github.io/]]
=======
Shared Task page [[https://semeval2025-task1.github.io/]]
>>>>>>> Stashed changes
