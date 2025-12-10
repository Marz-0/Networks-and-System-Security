from ollama import chat
from ollama import ChatResponse


MODEL_NAME = "deepseek-r1:1.5b"

response: ChatResponse = chat(model=MODEL_NAME, messages=[
    {
        'role': 'user',
    'content': 'Why is the sky blue?',
    },
])
# print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)