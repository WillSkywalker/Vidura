import os
import json
import random
from pathlib import Path
from dotenv import load_dotenv, dotenv_values
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers.json import JsonOutputParser
from .models import SimulatedConversation

load_dotenv()
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = dotenv_values(Path(__file__).resolve().parent.parent)["OPENAI_API_KEY"]

PREFERENCES = {'NONE': 'No restrictions', 'VE': 'Vegetarian', 'VG': 'Vegan'}


def run_conversation():
    question = "What are your top 3 favourite foods?"
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=1.5)
    diet_pref = random.choice(["NONE", "VE", "VG"])

    prompt_template = """
    You are a foodie from somewhere in the world. A user is asking you to recommend your top 3 favorite foods, based on your dietary restrictions.

    Your task is to respond with a JSON object that includes a list:
    "favorite_foods": A JSON list of three distinct food items that are consistent with your dietary preference.

    The question: "{question}"
    Your dietary preference: {preference}

    Your JSON response:
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)

    chain = prompt | llm | JsonOutputParser()

    response = chain.invoke({'question': question,
                             'preference': PREFERENCES[diet_pref]})
    print("Dietary preference:", diet_pref, "Agent responds:", response)

    try:
        SimulatedConversation.objects.create(
            dietary_preference=diet_pref,
            favorite_foods=response.get('favorite_foods',)
        )
        print("Successfully saved conversation to database.")
    except (json.JSONDecodeError, AttributeError) as e:
        print(f"Error parsing or saving response: {e}")
