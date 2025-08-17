from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from typing import Literal

load_dotenv()

def init_llm(
        provider: Literal["openai", "anthropic", "google", "ollama"],
        model: str,
        temperature: float = 0.5,
):
    if provider == "openai":
        return ChatOpenAI(model=model, temperature=temperature)
    elif provider == "anthropic":
        return ChatAnthropic(model=model, temperature=temperature)
    elif provider == "google":
        return ChatGoogleGenerativeAI(model=model, temperature=temperature)
    elif provider == "ollama":
        return ChatOllama(model=model, temperature=temperature)