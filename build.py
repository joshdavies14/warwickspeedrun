import os
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader

rendered_content = dict()
env = Environment(
    loader=FileSystemLoader("templates"),
)
jinja_template = env.get_template('template.html')

# Loads and renders markdown
for file_name in os.listdir("content"):
    if file_name.endswith(".md"):
        with open(os.path.join("content", file_name)) as file:
            content_md = file.read()
            content_html = markdown.markdown(content_md, extensions=['extra'])

            rendered_content[file_name.strip(".md")] = content_html

# Load the JS for injection into the template
rendered_content["javascript"] = open(os.path.join("src", "js", "site.js"), "r").read()

with open(os.path.join("dist", "index.html"), mode="w") as out_file:
    out_file.write(jinja_template.render(**rendered_content))
