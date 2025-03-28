from dotenv import load_dotenv
from mem0 import Memory

load_dotenv
                
custom_fact_extraction_prompt = """Extract all facts of the conversation that might be relevant in future 
                                conversations and output them in JSON format with "facts" as a key."""

config = {"llm": {
        "provider": "openai", 
        "config": { 
            "model": "gpt-4o",
            "temperature": 0.2, 
            "max_tokens": 2000, 
        }},
        "custom_fact_extraction_prompt": custom_fact_extraction_prompt,
        "version": "v1.1"}

memory = Memory.from_config(config_dict=config)