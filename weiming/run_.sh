pip install -r requirements.txt

python ./AutoPhrase/weiming/quality/batch_clean_txt.py -i ./K12-Vocab/cache -o ./AutoPhrase/weiming/clean`

python ./weiming/process/docx_to_txt.py --d ./weiming/quality/小学英语词表.docx --t ./weiming/quality/primary.txt

cp ./weiming/textbook_grade7_termA_clean.txt ./data/EN

cat ./weiming/quality/primary.txt >> ./weiming/EN/junior.txt


declare -A file_model_pairs=()

for grade in {"1","2","3","4","5","6","7","8","R","E"}; do
    for term in {"A","B"}; do
        file="data/clean/textbook_grade${grade}_term${term}.txt"
        model="models/MyModel${grade}${term}"
        file_model_pairs+=(["$file"]="$model")
    done
done

for grade in {"9","R","E"}; do
    for term in {"C","D"}; do
        if [[ ("$grade" == "9" || "$grade" == "R") && "$term" == "D" ]]; then
            continue
        fi
        file="data/clean/textbook_grade${grade}_term${term}.txt"
        model="models/MyModel${grade}${term}"
        file_model_pairs+=(["$file"]="$model")
    done
done

# To print and verify the array
for key in "${!file_model_pairs[@]}"; do
    echo "[$key]=${file_model_pairs[$key]}"
done

# declare -A file_model_pairs=(
#     ["data/clean/textbook_grade7_termA.txt"]="models/MyModel7A"
#     # Add more file-model pairs here
# )

for file in "${!file_model_pairs[@]}"
do
    echo $file
    model=${file_model_pairs[$file]}
    echo "Processing file $file with model $model"
    
    sudo docker run \
        -v $PWD/weiming:/autophrase/data \
        -v $PWD/models:/autophrase/models -it \
        -e DATA_DIR=data \
        -e RAW_TRAIN="$file" \
        -e ENABLE_POS_TAGGING=1 \
        -e MIN_SUP=3 -e THREAD=10 \
        -e MODEL="$model" \
        -e TEXT_TO_SEG="$file" \
        remenberl/autophrase \
        /bin/bash -c './auto_phrase.sh'

done

python ./weiming/test/filter.py