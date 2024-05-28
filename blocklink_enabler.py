# -*- coding: utf-8 -*-

import re
import os

# Set the input and output directories
input_dir = "C:/R"
output_dir = "C:/R"


# Regex patter for block identifier e.g. "^unique-idenfier"
#block_id_pattern = r'^(.*?)\^(\w+)$'
block_id_pattern = r'^(?![^$]*\$[^$]*\$.*?\^)(.+?)\^(\w+)$' # To exclude those cases where caret is included in Latex Mathmode.


def blocklink_enabler(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    # Use a regular expression to find all block identifiers in the text
    block_identifiers = re.findall(block_id_pattern, content, re.MULTILINE)

    # Replace each block identifier with the corresponding HTML anchor
    for block_text, identifier in block_identifiers:
        replacement = f'{block_text}<a id="{identifier}"></a>'
        content = content.replace(f'{block_text}^{identifier}', replacement)

    output_file_path = os.path.join(output_dir, os.path.basename(file_path).split(".")[0] + "_blconverted.md")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(content)

# Iterate over files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".md"):
        file_path = os.path.join(input_dir, filename)
        blocklink_enabler(file_path)