import os
from typing import Any, List

from openai import AzureOpenAI

API_KEY = os.getenv("AZURE_OPENAI_KEY", "a5cabfc396804fdd8c22ac74da9dd951")
API_ENDPOINT = os.getenv(
    "AZURE_OPENAI_ENDPOINT", "https://fnopenaifordev.openai.azure.com/"
)
API_VERSION = os.getenv("API_VERSION", "2023-05-15")


class GPTClient:
    def __init__(self) -> None:
        self.client = AzureOpenAI(
            api_key=API_KEY, api_version=API_VERSION, azure_endpoint=API_ENDPOINT
        )

    def chat_completions(self, model: str = None, messages=List[Any]):
        if model and messages:
            resp = self.client.chat.completions.create(model=model, messages=messages)
            print(resp)
            return resp.choices[0].message
        # resp.choices[0].message.role
        # resp.choices[0].message.content
        return None


gpt_client = GPTClient()


if __name__ == "__main__":
    # gpt40-turbo
    # gpt35-turbo
    model = "gpt40-turbo"
    messages = [
        {
            "role": "system",
            "content": "请问你现在是gpt4吗",
        }
    ]

    return_msg = gpt_client.chat_completions(
        model="gpt35-turbo",  # model = "deployment_name".
        messages=messages,
    )
    print(return_msg.role)
    print(return_msg.content)
