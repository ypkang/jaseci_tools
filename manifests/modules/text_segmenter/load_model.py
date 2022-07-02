import spacy
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("dennlinger/roberta-cls-consec")
model = AutoModelForSequenceClassification.from_pretrained(
    "dennlinger/roberta-cls-consec"
)

# Download the pretrained model pipeline
spacy.cli.download("en_core_web_sm")
# loading space model for sentence tokenization
#pipeline = spacy.load("en_core_web_sm")