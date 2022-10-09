import re
import json

feedback = json.loads(open("assets/feedback.json", "r").read())

with open("README.md", "r+") as file:
     content = file.read()
     content = re.sub(r"<!--feedback_start-->[\s\S\n]+<!--feedback_end-->", f"<!--feedback_start-->{content}<!--feedback_end-->", content)
     file.seek(0)
     file.write(content)
