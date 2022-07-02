from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings
from transformers import AutoTokenizer, AutoModelForTokenClassification

embedding_types = [
    # GloVe embeddings
    WordEmbeddings("glove"),
    # contextual string embeddings, forward
    FlairEmbeddings("news-forward"),
    # contextual string embeddings, backward
    FlairEmbeddings("news-backward"),
]

model_path = 'prajjwal1/bert-tiny'
AutoTokenizer.from_pretrained(model_path)
AutoModelForTokenClassification.from_pretrained(model_path)