# Obsidian-Related Tools
These are scripts that I made to use for my works. Anyone can use this script under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.

## Obsidian - Jekyll Footnote Converter
Obsidian and Jekyll have different ways of rendering footnotes. Obsidian uses `^[footnote contents]`, whereas Jekyll uses `[^footnote_index]` with the `[^footnote_index]: footnote contents` at the end of the article. To convert the Obsidian format of footnote to Jekyll format, I made the python script [obsidian_jekyll_footnote_converter.py](obsidian_jekyll_footnote_converter.py) to achieve the task.

- All you need to do is to assign your directory (`input_dir`) at which Obsidian markdown files are located and directory (`output_dir`)at which the converted markdown files will be saved. 
- Run the script and the converted markdown file will be saved in the designated folder.

## Wikilink - to - Markdown Link Converter
Obsidian supports wikilink format of hyperlink `[[address|text_shown]]`. Since this is not supported by regular markdown, Wikilink should be converted into a regular markdown link `[text_shown](address)`. To convert the Wikilinks to Markdown links, you can use the python script [wikilinks_to_mdlinks.py](wikilinks_to_mdlinks.py) to do the task.

- All you need to do is to assign your directory (`input_dir`) at which Obsidian markdown files are located and directory (`output_dir`)at which the converted markdown files will be saved. 
- Run the script and the converted markdown file will be saved in the designated folder.
- Note that block links `[[#^block_id|shown_text]]` are converted to `[shown_text](#block_id)`, NOT `[shown_text](#^block_id)`. This is to enable block links in regular HTML using 'blocklink_enabler.py', which I recommend running AFTER converting Wikilinks to Markdown links.

## Block Link Enabler
Obsidian supports block link using Wikilink format. For example,

"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et tortor vel dui feugiat blandit id nec ligula. Aliquam erat volutpat. Ut eleifend consequat tortor, vitae pharetra enim. Duis sit amet porttitor massa, id ultricies tellus. Cras bibendum vulputate tortor ac placerat. Duis varius elit tortor, in ullamcorper orci varius in. Maecenas rhoncus, sapien at convallis placerat, nunc nunc interdum tortor, a molestie nisl quam sit amet enim. In tristique risus nisi, at ultrices ante bibendum eget. Proin vel finibus dui. Aliquam ultrices mollis risus, quis hendrerit lacus aliquam ut. Nunc sed lectus id metus ultrices commodo. Nam mattis sed nulla quis tempor. Integer lacinia tortor ac sollicitudin fermentum. Etiam et dui ut nulla auctor accumsan. ^1c3df4

As shown in [[#^1c3df4|the first paragraph]], blahblahblah. "

However, this format is not supported by regular markdown and thus not active in the resulting HTML file. In order to achieve this, I made the python script [blocklink_enabler.py](blocklink_enabler.py). 

- Scan the text and find block identifer (e.g. `^1d4f8d` or `^block-1` etc.).
- Convert the block identifer to the anchor element. (e.g. `1d4f8d` to `<a id="1d4f8d"></a>`)
- Now you can use the block identifer in markdown in-text links. (e.g. "As mentioned in [the first paragraph](#1d4f8d), blah blah blah.")



