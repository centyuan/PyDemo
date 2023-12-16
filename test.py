import json
import os

import requests
from openai import AzureOpenAI
from PIL import Image

AZURE_OPENAI_API_KEY = "f5cabfc396804fdd8c22ac74da9dd958"
AZURE_OPENAI_ENDPOINT = "ac71d6444a714877851e7ee75f7fff3c"

client = AzureOpenAI(
    api_version="2023-12-01-preview",  
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
    # api_key=os.environ["AZURE_OPENAI_API_KEY"],  
    # azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT']
)

result = client.images.generate(
    model="dalle3", # the name of your DALL-E 3 deployment
    prompt="a close-up of a bear walking throughthe forest",
    n=1
)

json_response = json.loads(result.model_dump_json())

# Set the directory for the stored image
image_dir = os.path.join(os.curdir, 'images')

# If the directory doesn't exist, create it
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

# Initialize the image path (note the filetype should be png)
image_path = os.path.join(image_dir, 'generated_image.png')

# Retrieve the generated image
image_url = json_response["data"][0]["url"]  # extract image URL from response
generated_image = requests.get(image_url).content  # download the image
with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

# Display the image in the default image viewer
image = Image.open(image_path)
image.show()
