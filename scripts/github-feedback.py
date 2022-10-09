import json
import os

env = os.environ

review =  {
            "user_id": env["USER_ID"],
            "username": env["USERNAME"],
            "avatar": env["AVATAR_URL"] if "AVATAR_URL" in env else None,
            "content": '\n'.join(env["BODY"].splitlines()[2:]),
            "created_at": env["CREATED_AT"],
            "source": "github",
}

with open("assets/feedback.json", "r+") as file:
   feedback = {}
   array = json.loads(file.read())
   array.append(review)

   # Remove duplicates
   for r in array:
      feedback[r["username"]] = r

   file.seek(0)
   file.write(json.dumps(list(feedback.values())))
