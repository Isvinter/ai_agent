from pydantic_ai import Agent
from memory_management import *
from mem0 import Memory

class Agent_with_memory(Agent):
    memory = Memory.from_config(config_dict=config)
    
    #add new info to the vector storage:
    def remember(self, text: str, metadata: dict = None):
        """stores informations in long-term-memory"""
        self.memory.add_memory(text, metadata)
        
    def recall(self, query: str, k: int = 5):
        """retrieve memory from long-term-storage"""
        results = self.memory.search(query, k)
        return results if results is not None else []
        
    def process_with_memories(self, query):
        """add contextual information from memory to the query"""
        query_with_context = ""
        relevant_memories = self.recall(query)
        
        query_with_context = query + " " + " ".join(map(str, relevant_memories))
            
        answer = self.run_sync(query_with_context, model="gpt-4")
        return answer
        
    
    
        