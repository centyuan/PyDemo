from openai import AzureOpenAI

AZURE_OPENAI_API_KEY = "f5cabfc396804fdd8c22ac74da9dd958"
AZURE_OPENAI_ENDPOINT = "ac71d6444a714877851e7ee75f7fff3c"
client = AzureOpenAI(
  azure_endpoint = AZURE_OPENAI_ENDPOINT,
  api_key=AZURE_OPENAI_API_KEY, 
  api_version="2023-05-15"
)

response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print(response.choices[0].message.content)
