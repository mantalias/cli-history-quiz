
import requests, json

url = requests.get("https://opentdb.com/api.php?amount=12&category=23&difficulty=easy&type=boolean")
text = url.text

quiz_api_data = json.loads(text)

question_data = quiz_api_data["results"]