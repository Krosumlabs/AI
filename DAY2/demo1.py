
from langchain_ollama import OllamaLLM
llm_obj = OllamaLLM(model='gemma2:2b')
response = llm_obj.invoke('What is GenAI?')
print(type(response),len(response))
