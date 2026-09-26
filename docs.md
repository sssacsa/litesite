# litesite docs

## 1. Install & translating instructions
Download Python, then download the translator. That's it. 
<br>
To translate use `ltst.py [filename.ltst]`!<br>
##### Multiple ltst files can be translated at once! 
*Adding the translator to PATH is recommended*

## 2. HTML
`#text%#` - h1 <br>
`!text%!` - **bold** text <br>
`\text%!` - *italic* text <br>
`~text%~` - ~~strikethrough~~ text <br>
`!escaped%! text/!/!` - escaped text <br>
`--text` - comment <br>
`*title%*` - page title <br>
`*l* "URL"** text %l*` - link <br>
`*r*` - horizontal row <br>
`*n*` - new line <br>
`*c*`, `%c*` - centered line

## 2.1. CSS
`*s*`, `%s*` - style mode <br>
`bgc red$` - sets background color to red <br>
`txc green$` - sets text color to green <br>
`*imp` - import to CSS <br>
`ffa` - font family <br>
`fsz` - font size <br>
`fwg` - font weight <br>
`$` - this is the semicolon for no reason

## 3. Miscellaneous
`*i*`, `%i*` - import other ltst files
