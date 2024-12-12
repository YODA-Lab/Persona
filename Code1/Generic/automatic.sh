#!/bin/bash

# 2. Run Each Chain

s_values=(0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9)
r_values=(1 2 3 4 5 6 7 8)

merged_dir="merged_files"
mkdir -p "$merged_dir"

for s in "${s_values[@]}"; do
    for r in "${r_values[@]}"; do
        echo "Processing with s=${s} and r=${r}..."

        for i in {A..C}; do
            chain_folder="Chain${i}"

            if [[ -d "$chain_folder" ]]; then
                echo "Processing $chain_folder..."
                pushd "$chain_folder" > /dev/null

                python3 "Chain${i}.py" --s "$s" --r "$r"

                popd > /dev/null
            else
                echo "Warning: Directory $chain_folder does not exist."
            fi
        done

        # Merge Results
        echo "Merging result files for s=${s} and r=${r}..."
        files=()

        for i in {A..C}; do
            file="Chain${i}/Chain${i}_correlation.csv"
            if [[ -f "$file" ]]; then
                files+=("$file")
            else
                echo "Warning: File $file does not exist."
            fi
        done

        if [ ${#files[@]} -eq 0 ]; then
            echo "No files to merge for s=${s} and r=${r}."
            continue
        fi

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
    done
done
