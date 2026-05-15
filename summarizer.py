from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization")

# Input text
text = """
Artificial Intelligence (AI) is transforming industries across the world.
It is being used in healthcare, education, finance, transportation, and
many other fields. AI systems can analyze large amounts of data quickly,
helping organizations make better decisions.
"""

# Generate summary
summary = summarizer(text, max_length=60, min_length=20, do_sample=False)

print("\nOriginal Text:\n")
print(text)

print("\nSummarized Text:\n")
print(summary[0]['summary_text'])
