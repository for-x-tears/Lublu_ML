import os
from openai import OpenAI


OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL','HELLO ')

#OPENAI_API_KEY = os.environ["OPEN_API_KEY"]


print(OPENAI_BASE_URL)
#print(OPENAI_API_KEY)

