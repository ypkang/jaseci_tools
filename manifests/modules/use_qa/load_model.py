import tensorflow_hub as hub
import tensorflow_text  # noqa

module = hub.load(
    "https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3"
)