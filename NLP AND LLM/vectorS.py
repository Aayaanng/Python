from sentence_transformers import SentenceTransformer,util
from huggingface_hub import login
login(token="your hugging face id")

# Load a pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')
# Convert sentences to vectors
sentences = ['I love pizza', 'Pizza is my favourite food', 'I enjoy football']
embeddings = model.encode(sentences)

print(f"The embedding shape is{embeddings.shape}")   # (3, 384) — 3 sentences, 384 numbers each
print(f"Theses are the vectors{embeddings[0]}")      # The vector for 'I love pizza'
#COSINE similarity
sentence1 = 'I love eating pizza'
sentence2 = 'Pizza is my favourite food'
sentence3 = 'I enjoy playing football'

# Create embeddings
emb1 = model.encode(sentence1)
emb2 = model.encode(sentence2)
emb3 = model.encode(sentence3)

# Calculate similarity (returns a 2D tensor)
score_12 = util.cos_sim(emb1, emb2)
score_13 = util.cos_sim(emb1, emb3)

# FIX: Use .item() to convert the tensor values to standard Python floats
print(f'Pizza vs Pizza: {score_12.item():.2f}')     # Output: ~0.80
print(f'Pizza vs Football: {score_13.item():.2f}')  # Output: ~0.17
#Tokens — How LLMs See Text
# Example tokenisation (approximate)
#'Hello, how are you?'  -->  ['Hello', ',', ' how', ' are', ' you', '?']

# This sentence = 6 tokens
