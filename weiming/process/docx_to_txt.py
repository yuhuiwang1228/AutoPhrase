from docx import Document
import argparse

def docx_to_txt(docx_filename, txt_filename):
    doc = Document(docx_filename)
    
    text = [paragraph.text.strip() for paragraph in doc.paragraphs]
    
    # Write the text to a TXT file
    with open(txt_filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(text))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--docx_file","-d",default=None,type=str,required=True)
    parser.add_argument("--txt_file","-t",default=None,type=str,required=True)
    args = parser.parse_args()
    
    docx_to_txt(args.docx_file, args.txt_file)