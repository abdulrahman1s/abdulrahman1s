import requests
import json

username = "abdulrahman1s"
limit = 20
req = requests.get(f"https://abdulrahman1s-fiverr-api.deno.dev/{username}/reviews?limit={limit}").json()

def transform(reviews):
    reviews = filter(lambda r: r["value"] >= 4, reviews)

    def into_review(r):
        return {
            "username": r["username"],
            "avatar": r["user_image_url"] if "user_image_url" in r else None,
            "content": r["comment"],
            "created_at": r["created_at"],
            "source": "fiverr",
        }

    reviews = map(into_review, reviews)
    return reviews

with open("assets/feedback.json", "r+") as file:
   feedback = {}
   array = json.loads(file.read())
   array.extend(transform(req))

   # Remove duplicates
   for r in array:
      feedback[r["username"]] = r

   file.seek(0)
   file.write(json.dumps(list(feedback.values())))
