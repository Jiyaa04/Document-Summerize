from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    if len(text.strip()) == 0:
        return "No text found in the image."
    if len(text) > 1024:
        text = text[:1024]  # Truncate for model limits
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
