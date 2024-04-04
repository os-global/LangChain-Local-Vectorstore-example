# LangChain-Local-Vectorstore-example

Sanbox for chatting about data loaded with document loader using FAISS local vectorstore. Query PDF in this example.

## setup
- install dependencies
`pip3 install -r requirements.txt`
- create .env file with api key of supported llm
```ini
MISTRAL_API_KEY=mistral_api_key
;or other llm key:
;OPENAI_API_KEY=open_api_key
```
- select llm in `main.py`
```python
from langchain_mistralai import ChatMistralAI
# for OpenAI:
# from langchain.chat_models import ChatOpenAI
```
- check [`main.py`](main.py) for promt and setup. Default presetup is `Give me the gist of AI in 3 sentences` about [`What_Is_AI.pdf`](https://www.researchgate.net/publication/343611353_What_Is_AI)

## execute
`python3 main.py`

## output example
```
Artificial Intelligence (AI) is the study of intelligent agents that receive percepts from the environment and take actions based on them, implemented by functions that map percepts to actions. AI can be represented in various ways, such as production systems, reactive agents, logical planners, neural networks, and decision-theoretic systems. Current AI works best in constrained environments and has trouble with open worlds, poorly defined problems, and abstractions, but it continues to improve through the development of subfields like machine learning.
```