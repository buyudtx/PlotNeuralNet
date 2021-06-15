#!/bin/bash

python "$1".py
pdflatex "$1".tex

# rm *.aux *.log *.vscodeLog
# rm *.tex
# shellcheck disable=SC2035
rm *.aux *.log

if [[ "$OSTYPE" == "darwin"* ]]; then
  open "$1".pdf
else
  # xdg-open "$1".pdf  # linux 打开文件
  start "$1".pdf  # windows 打开文件
fi
