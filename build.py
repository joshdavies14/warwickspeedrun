import os

import markdown
# TODO
from jinja2 import Environment, FileSystemLoader

rendered_content = dict()
env = Environment(
    loader=FileSystemLoader("templates"),
)
jinja_template = env.get_template('template.html')

for file_name in os.listdir("content"):
    if file_name.endswith(".md"):
        with open(os.path.join("content", file_name)) as file:
            content_md = file.read()
            content_html = markdown.markdown(content_md, extensions=['extra'])

            rendered_content[file_name.strip(".md")] = content_html

with open(os.path.join("dist", "index.html"), mode="w") as out_file:
    out_file.write(jinja_template.render(**rendered_content))
