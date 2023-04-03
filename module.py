import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config["OPENAI_API_KEY"]

initial_prompt = """
Tolong parafrase dalam bahasa Indonesia
\n
"""


def generate(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        # prompt=initial_prompt+prompt,
        prompt=prompt,
        temperature=0.7,
        max_tokens=4000,
        n=1,
        stop=None,
        timeout=15
    )
    return response.choices[0].text.strip()
