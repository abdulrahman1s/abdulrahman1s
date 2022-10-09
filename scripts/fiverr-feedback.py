import requests
import re

username = "abdulrahman1s"
limit = 100
reviews = requests.get(f"https://abdulrahman1s-fiverr-api.deno.dev/{username}/reviews?limit={limit}").json()


def format_review(review):
    username = review["username"]
    comment = review["comment"]
    return f"- [@{username}](https://fiverr.com/{username}): **{comment}**"


content = '\n'.join(map(format_review, filter(lambda r: r["value"] >= 4, reviews)))

with open("README.md", "r+") as file:
   file_content = file.read()
   file_content = re.sub(
               r"<!--fiverr_feedback_start-->[\s\S\n]+<!--fiverr_feedback_end-->", 
               f"<!--fiverr_feedback_start-->\n{content}\n<!--fiverr_feedback_end-->", file_content)

   file.seek(0)
   file.write(file_content)
