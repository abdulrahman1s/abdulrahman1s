import requests
import re

username = "abdulrahman1s"
regex = r"<!--{{feedback_start}}-->[\s\S\n]+<!--{{feedback_end}}-->"
reviews = requests.get(f"https://abdulrahman1s-fiverr-api.deno.dev/{username}/reviews").json()


def format_review(review):
    username = review["username"]
    comment = review["comment"]
    return f"- [@{username}](https://fiverr.com/{username}): **{comment}**"


content = '\n'.join(map(format_review, filter(lambda r: r["value"] >= 4, reviews)))


with open("README.md", "r+") as file:
   file_content = file.read()
   file_content = re.sub(regex, "<!--{{feedback_start}}-->\n" + content + "\n<!--{{feedback_end}}-->", file_content)
   file.seek(0)
   file.write(file_content)
