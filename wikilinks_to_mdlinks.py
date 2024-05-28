# -*- coding: utf-8 -*-

import re
import os

# Set the input and output directories
input_dir = "C:/R"
output_dir = "C:/R"

# Regex pattern for wikilinks blocklinks "[[#^]]"
block_pattern = r'\[\[\#\^(.+?)\|(.+?)\]\]'
# Regex pattern for wikilinks regular URLs "[[]]"
regular_pattern = r'\[\[(.+?)\|(.+?)\]\]'

def convert_wikilinks(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

  # Convert block links first (`[[#^id]]` to `[](#id)`)
    block_pattern = r'\[\[\#\^(.+?)\|(.+?)\]\]'
    block_links = re.findall(block_pattern, content)
    for identifier, shown_text in block_links:
        replacement = f'[{shown_text}](#{identifier})'
        content = content.replace(f'[[#^{identifier}|{shown_text}]]', replacement)

    # Convert regular wikilinks to markdown format.
    regular_pattern = r'\[\[(.+?)\|(.+?)\]\]'
    wikilinks = re.findall(regular_pattern, content)

    for link, shown_text in wikilinks:
        replacement = f'[{shown_text}]({link})'
        content = content.replace(f'[[{link}|{shown_text}]]', replacement)

    output_file_path = os.path.join(output_dir, os.path.basename(file_path).split(".")[0] + "_wkconverted.md")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(content)

# Iterate over files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".md"):
        file_path = os.path.join(input_dir, filename)
        convert_wikilinks(file_path)
        