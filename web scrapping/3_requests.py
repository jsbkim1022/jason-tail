import requests

res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
print("Respond :", res.status_code)  # If it is 200 normal.
res.raise_for_status()
if res.status_code == requests.codes.ok:
    print("Normal")
else:
    print("Error Occured. [Error code: ", res.status_code, "]")

print(len(res.text))

print(res.text)
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
