import re
import random
import requests
from dotenv import dotenv_values

key = dotenv_values(".env").get("RAPID_API")


# ---------------------------------------------------------------------------------------------------------
class Facts:
    def getCatFacts() -> str:
        response = requests.get("https://catfact.ninja/fact")
        response = response.json()
        fact = response["fact"]
        return fact

    def getFunFact() -> str:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        response = response.json()
        fact = response["text"]
        return fact

    def getRandomNumberFact() -> str:
        url = "https://numbersapi.p.rapidapi.com/random/trivia"
        querystring = {"min": "10", "max": "20", "fragment": "true", "json": "true"}
        headers = {
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com",
        }
        response = requests.get(url, headers=headers, params=querystring)
        response = response.json()
        fact = f"{response['number']} is {response['text']}"
        return fact

    def getGivenNumberFact(number: int) -> str:
        url = f"https://numbersapi.p.rapidapi.com/{number}/trivia"
        querystring = {"fragment": "true", "notfound": "floor", "json": "true"}
        headers = {
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "numbersapi.p.rapidapi.com",
        }
        response = requests.get(url, headers=headers, params=querystring)
        response = response.json()
        fact = str(response["text"]).capitalize()
        return fact

    def getFacts(query: str) -> dict:
        pattern = r"\d+"
        response = re.findall(pattern, query)
        if len(response) > 0:
            fact = Facts.getGivenNumberFact(response[0])
        else:
            if "cat" in query:
                fact = Facts.getCatFacts()
            elif "number" in query:
                fact = Facts.getRandomNumberFact()
            else:
                fact = Facts.getFunFact()

        return {"text": [fact], "sticker": "", "audio": ""}


# ---------------------------------------------------------------------------------------------------------


class APIS:
    # -------------------------------------------------------------------------------------------------------
    def getJokes() -> dict:
        try:
            response = requests.get(
                "https://v2.jokeapi.dev/joke/Miscellaneous,Dark?type=twopart"
            )
            response = response.json()
            setup = response["setup"]
            delivery = response["delivery"]
            emoji = random.choice(["🤣🤣🤣", "😂😂😂", "🤣😂🤣", "😅😅😆"])
            return {"text": (setup, delivery, emoji), "sticker": "", "audio": ""}
        except:
            return {
                "text": (
                    "I'm sorry, it seems my humor circuits are in need of an upgrade.",
                    "I'm not able to come up with a joke right now.",
                    "Is there anything else I can assist you with?",
                ),
                "sticker": "",
                "audio": "",
            }

    # -------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------
    def getRiddles() -> dict:
        try:
            response = requests.get("https://riddles-api.vercel.app/random")
            response = response.json()
            riddle = response["riddle"]
            answer = response["answer"]
            return {"text": (riddle, answer), "sticker": "", "audio": ""}
        except:
            return {
                "text": (
                    "Apologies, it appears that my riddle-solving skills are temporarily out of order.",
                    "I'm unable to come up with a riddle right now.",
                    "How else can I be of help to you?",
                ),
                "sticker": "",
                "audio": "",
            }

    # -------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------
    def getPoems() -> dict:
        try:
            response = requests.get(
                "https://poetrydb.org/author,title/Shakespeare;Sonnet"
            )
            response = random.choice(response.json())
            poem = response["lines"]
            return {"text": poem, "sticker": "", "audio": ""}
        except:
            return {
                "text": [
                    "I apologize, it seems that my poetry library is currently unavailable.",
                    "I'm unable to provide a poem at the moment.",
                    "Is there anything else I can assist you with?",
                ],
                "sticker": "",
                "audio": "",
            }

    # -------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------
    def getQuotes() -> dict:
        try:
            response = requests.get("https://zenquotes.io/api/random")
            response = response.json()
            author = f"{response[0]['a']}, once said"
            quote = response[0]["q"]
            return {"text": (author, quote), "sticker": "", "audio": ""}
        except:
            return {
                "text": (
                    "I regret to inform you that my quote repertoire seems to be on vacation.",
                    "Unfortunately, I can't provide a quote at this time.",
                    "How else can I be of assistance?",
                ),
                "sticker": "",
                "audio": "",
            }

    # -------------------------------------------------------------------------------------------------------
