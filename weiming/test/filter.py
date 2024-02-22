from scrape import is_valid
import time
import json
import os

def filter_phrase(file_path, grade, term):
    valid_phrases = []
    interval = 0
    threshold = 0.5
    with open(file_path, 'r') as file:
        for line in file:
            interval += 1
            score, phrase = line.strip().split('\t')
            score = float(score)
            if score<threshold:
                break
            if is_valid(phrase):
                valid_phrases.append(phrase)
        if interval%50==0: 
            time.sleep(1)  

    new_phrases = []
    for phrase in valid_phrases:
        if phrase not in seen:
            seen.add(phrase)
            new_phrases.append(phrase)

    data = {
        "grade": grade,
        "term": term,
        "phrases": new_phrases
    }

    file_name = f'./weiming/output/phrase_grade{grade}_term{term}.json'
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

    return valid_phrases

if __name__ == "__main__":
    grades = ['1','2','3','4','5','6','7','8','9','R','E']
    terms = ['A','B','C','D']
    seen = set()
    for grade in grades:
        for term in terms:
            file_path = f'./models/MyModel{grade}{term}/AutoPhrase_multi-words.txt'
            if os.path.exists(file_path):
                print(f"Processing file: {file_path}")
                filter_phrase(file_path,grade,term)