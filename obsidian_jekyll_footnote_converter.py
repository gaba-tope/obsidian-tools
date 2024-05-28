import re
import os

# Set the input and output directories
input_dir = "input\directory"
output_dir = "output\directory"

# Regular expression pattern for Obsidian footnotes "^[]"
obsidian_footnote_pattern = r"\^(\[(.*?)\])"
obsidian_intext_backlink_pattern = r"\[\[(#\^.*?\|)(.*?)\]\]"

# Define a function for converting
def convert_footnotes(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    footnotes = []
    converted_content = ""
    footnote_count = 1

    # Match and convert Obsidian footnotes to Jekyll footnotes
    for line in content.split("\n"):
        matches = re.findall(obsidian_footnote_pattern, line)
        start = 0
        converted_line = ""
        for match in matches:
            footnote_text = match[1]
            footnotes.append(f"[^{footnote_count}]: {footnote_text}")
            match_start = line.index("^[" + footnote_text + "]", start)
            match_end = match_start + len("^[" + footnote_text + "]")
            converted_line += line[start:match_start] + f"[^{footnote_count}]"
            start = match_end
            footnote_count += 1
        converted_line += line[start:]

        # Convert Obsidian intext backlinks to "shown text"
        # Quote the below line not to pull out the shown text out of the backlink format.
        converted_line = re.sub(obsidian_intext_backlink_pattern, r"\2", converted_line)

        converted_content += converted_line + "\n"
        
    converted_content += "\n".join(footnotes)

    output_file_path = os.path.join(output_dir, os.path.basename(file_path).split(".")[0] + "_converted.md")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(converted_content)

# Iterate over files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".md"):
        file_path = os.path.join(input_dir, filename)
        convert_footnotes(file_path)