from transformers import pipeline


# more information about this model can be found on https://huggingface.co/cardiffnlp/twitter-roberta-base-irony
TEXT_CLASSIFICATION_MODEL = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-irony")

def get_text_classification_model():
    return TEXT_CLASSIFICATION_MODEL