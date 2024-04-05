import argparse
from lang_detect import detect_language

def main():
    parser = argparse.ArgumentParser(description='Detect the most likely programming language of a code snippet.')
    parser.add_argument('code_snippet', help='The code snippet to analyze')
    args = parser.parse_args()

    language = detect_language(args.code_snippet)
    print("Detected language:", language)

if __name__ == '__main__':
    main()
