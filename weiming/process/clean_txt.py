import re
import argparse

def remove_non_english(text):
    # This regular expression matches any character that is not a standard ASCII character
    return re.sub(r'[^\x00-\x7F]+', '', text)

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    processed_content = remove_non_english(content)
    processed_content = processed_content.replace('\n',' ')

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(processed_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file","-i",default=None,type=str,required=True)
    parser.add_argument("--output_file","-o",default=None,type=str,required=True)
    args = parser.parse_args()

    process_file(args.input_file, args.output_file)