import os
from utils.common import question_generation_prompt
from utils.common import evaluate_candidate
from dotenv import load_dotenv
import google.generativeai as gen_ai



load_dotenv()

class Agents:
    def __init__(self):
        self.GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        gen_ai.configure(api_key=self.GOOGLE_API_KEY)
        self.model = gen_ai.GenerativeModel('gemini-pro')

    
    def question_generation_agent(self,data):
        prompt = question_generation_prompt(data)
        response = self.model.generate_content(prompt)
        return response.text
    
    def evaluate_candidate_agent(self,data):
        prompt = evaluate_candidate(data)
        response = self.model.generate_content(prompt)
        return response.text

