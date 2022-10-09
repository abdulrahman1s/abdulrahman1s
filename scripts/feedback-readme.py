import re
import json

feedback = json.loads(open("assets/feedback.json", "r").read())

def format(review):
    username = review["username"]
    content = review["content"]
    source = review["source"]
    url = ""
    
    if source == "github":
       url = f"https://github.com/{username}"
    elif source == "fiverr":
       url = f"https://fiverr.com/{username}"

    return f"- [@{username}]({url}): **{content}**"

feedback = '\n'.join(map(format, feedback))

with open("README.md", "r+") as file:
     content = file.read()
     content = re.sub(r"<!--feedback_start-->[\s\S\n]+<!--feedback_end-->", f"<!--feedback_start-->{feedback}<!--feedback_end-->", content)
     file.seek(0)
     file.write(content)
