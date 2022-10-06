import requests

reviews = requests.get("https://abdulrahman1s-fiverr-api.deno.dev/abdulrahman1s/reviews").json()
content = '\n'.join(map(lambda r: f"- {r.username}: **{r.comment}**", reviews))

print(content)
