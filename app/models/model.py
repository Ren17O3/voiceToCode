from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task= "text-generation",
    temperature=0.0
)

model = ChatHuggingFace(llm=llm)

def generate_response(prompt: str) -> str:
    response = model.invoke(prompt)
    return response.content