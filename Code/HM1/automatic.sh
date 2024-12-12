#!/bin/bash

merged_dir="merged_files"
mkdir -p "$merged_dir"


echo "Processing chain folders..."
for i in {A..C}; do
    chain_folder="Chain${i}"

    if [[ -d "$chain_folder" ]]; then
        echo "Processing $chain_folder..."
        pushd "$chain_folder" > /dev/null

        start=$(date +%s)
        python3 "Chain${i}.py" --s 0.5 --r 1
        end=$(date +%s)
        execution_time=$(( end - start ))
        echo "Execution time was ${execution_time} seconds."

        popd > /dev/null
    else
        echo "Warning: Directory $chain_folder does not exist."

    fi
done


echo "Merging result files..."
files=()
for i in {A..C}; do
    file="Chain${i}/Chain${i}_correlation.csv"
    if [[ -f "$file" ]]; then
        files+=("$file")
    else
        echo "Warning: File $file does not exist."
    fi
done

merged_file="${merged_dir}/data_distribution.csv"
header_added=false

for file in "${files[@]}"; do
    if [ "$header_added" = false ]; then
        cat "$file" > "$merged_file"
        header_added=true
    else
        tail -n +2 "$file" >> "$merged_file"
    fi
done

echo "Merged file created: $merged_file"