#!/bin/bash

# 합칠 텍스트 파일의 경로와 이름을 설정합니다.
OUTPUT_FILE="DIST/KR3e_merged.txt"
INPUT_FILE="의가류"

# 기존의 파일이 있다면 삭제합니다.
if [ -f "$OUTPUT_FILE" ]; then
    rm "$OUTPUT_FILE"
fi

# INPUT_FILE 디렉토리 아래의 모든 텍스트 파일을 찾아서 합칩니다.
find "$INPUT_FILE" -type f -name "*.txt" -exec cat {} + > "$OUTPUT_FILE"

echo "모든 텍스트 파일이 $OUTPUT_FILE 파일로 합쳐졌습니다."