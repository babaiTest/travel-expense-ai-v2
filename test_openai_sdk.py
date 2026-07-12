from openai import AzureOpenAI
from app import config

print("Endpoint:", config.AZURE_OPENAI_ENDPOINT)
print("Deployment:", config.AZURE_OPENAI_DEPLOYMENT)
print("API Version:", config.AZURE_OPENAI_API_VERSION)

client = AzureOpenAI(
    api_key=config.AZURE_OPENAI_KEY,
    api_version=config.AZURE_OPENAI_API_VERSION,
    azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
)

response = client.chat.completions.create(
    model=config.AZURE_OPENAI_DEPLOYMENT,
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: Azure OpenAI is working"
        }
    ]
)

print(response.choices[0].message.content)