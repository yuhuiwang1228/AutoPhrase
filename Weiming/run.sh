pip install -r requirements.txt

python ./Weiming/clean_txt.py -i ./Weiming/textbook_grade7_termA.txt -o ./Weiming/textbook_grade7_termA_clean.txt
python ./Weiming/docx_to_txt.py --d ./Weiming/quality_grade7_termA.docx --t ./Weiming/quality_grade7_termA.txt

cp ./Weiming/textbook_grade7_termA_clean.txt ./data/EN
cp ./Weiming/quality_grade7_termA.txt ./data/EN/wiki_quality_extend.txt
cat ./data/EN/wiki_quality.txt >> ./data/EN/wiki_quality_extend.txt

sudo docker run -v $PWD/data:/autophrase/data -v $PWD/models:/autophrase/models -it \
    -e RAW_TRAIN=data/EN/textbook_grade7_termA_clean.txt \
    -e ENABLE_POS_TAGGING=1 \
    -e MIN_SUP=30 -e THREAD=10 \
    -e MODEL=models/MyModel \
    -e TEXT_TO_SEG=data/EN/textbook_grade7_termA_clean.txt \
    remenberl/autophrase
./auto_phrase.sh