# imports

import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from openai import OpenAI

# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print(
        "An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print(
        "An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")

openai = OpenAI()

# A class to represent a Webpage

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


class Website:

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)


system_prompt = "You are a researcher that analyzes the contents of a research paper \
and provides a comprehensive summary of the paper along with highlighting their results and major contribution, how is the suggested technique is better than other similar techniques and list some research ideas that can be explored based on that paper. \
Respond in markdown."


def user_prompt_for_rp(paper):
    user_prompt = f"You are looking at a research paper titled {paper.title}"
    user_prompt += "\nThe contents of this paper is as follows; \
provide a comprehensive summary of the paper along with highlighting their results and major contribution, how is the suggested technique is better than other similar techniques and list some research ideas that can be explored based on this paper.\n\n"
    user_prompt += paper.text
    return user_prompt


# Step 2: Make the messages list



def summarize_rp(url):
    paper = Website(url)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt_for_rp(paper)}
        ]
    )

    return response.choices[0].message.content
