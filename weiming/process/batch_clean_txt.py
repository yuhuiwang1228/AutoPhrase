import os
import subprocess
import argparse
import re

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

def batch_process(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith('.txt'):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)
            process_file(input_file, output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir","-i",default=None,type=str,required=True)
    parser.add_argument("--output_dir","-o",default=None,type=str,required=True)
    args = parser.parse_args()

    batch_process(args.input_dir, args.output_dir)