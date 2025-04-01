import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from agents import Agent_with_memory
from pydantic_ai.models.openai import OpenAIModel
from memory_management import *
from mem0 import Memory

load_dotenv()

def main():
    
    #open_ai_api_key = os.getenv("OPENAI_API_KEY")
    
    system_prompt = ("""You are an highly intelligent chat-bot who proveides help with everything.
                You proveide answers only if you know the answer with a very high leve of confidece.
                You don not like formal language and speak cheeky language with influnce of youth 
                culture from time to time. You also like to answer scrastically.""")
                
    model = OpenAIModel("gpt-4")
    
    agent = Agent(model, system_prompt=system_prompt)
    
    conversation = []
    
    user_question = input("Stelle eine Frage an das Orakel:\n")

    
    #response = agent.run_sync(user_question)
    #conversation.append(response)
    
    
    #print(conversation)
    
    agent2 = Agent_with_memory()
    result2 = agent2.process_with_memories(user_question)
    print(result2)
    
    
    
if __name__ == "__main__":
    main()
