import os
import re
import json
import requests

env = os.environ

def is_github():
    return env["GITHUB_EVENT_NAME"] == "issues"


def is_fiverr():
    return True


def trim_markdown(string):
    return re.sub(r"[`*_()[\]<>]+", "", string)


def format(review):
    username = review["username"]
    content = trim_markdown(review["content"])
    source = review["source"]
    url = f"https://github.com/{username}" if source == "github" else f"https://fiverr.com/{username}" if source == "fiverr" else ""
    return f"- [@{username}]({url}): **{content}**"


json_file = open("assets/feedback.json", "r+")
feedback = {}

for r in json.loads(json_file.read()):
    feedback[r["username"]] = r

if is_github():
    feedback[env["USER_ID"]] = {
        "user_id": env["USER_ID"],
        "username": env["USERNAME"],
        "avatar": env["AVATAR_URL"] if "AVATAR_URL" in env else None,
        "content": '\n'.join(env["BODY"].splitlines()[2:]),
        "created_at": env["CREATED_AT"],
        "source": "github"
    }

if is_fiverr():
    username = "abdulrahman1s"
    limit = 100
    url = f"https://abdulrahman1s-fiverr-api.deno.dev/{username}/reviews?limit={limit}"
    req = requests.get(url).json()

    for r in req:
        if r["value"] < 4:
            continue

        feedback[r["username"]] = {
            "user_id": None,
            "username": r["username"],
            "avatar": r["user_image_url"] if "user_image_url" in r else None,
            "content": r["comment"],
            "created_at": r["created_at"],
            "source": "fiverr",
        }

json_file.seek(0)
json_file.write(json.dumps(list(feedback.values())))
json_file.close()

with open("README.md", "r+") as file:
    formatted_feedback = '\n'.join(map(format, feedback.values()))
    content = re.sub(
        r"<!--feedback_start-->[\s\S\n]+<!--feedback_end-->",
        f"<!--feedback_start-->\n{formatted_feedback}\n<!--feedback_end-->", file.read())
    file.seek(0)
    file.write(content)
