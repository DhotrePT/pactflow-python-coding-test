from langdetect import detect_langs

def detect_language(code_snippet):
    """
    Detect the most likely programming language of a given code snippet.

    Args:
    - code_snippet (str): The code snippet to analyze.

    Returns:
    - language (str): The detected programming language.
    """
    try:
        # Detect language using langdetect library
        detected_languages = detect_langs(code_snippet)
        most_likely_language = detected_languages[0].lang
        return most_likely_language
    except:
        return "Unknown"
