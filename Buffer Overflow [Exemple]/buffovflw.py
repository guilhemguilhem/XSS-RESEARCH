import os
import openai
from IPython.display import Image
from IPython import display
from base64 import b64decode

openai.api_key = "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"

response = openai.Image.create(
  prompt="A cute baby sea otter",
  n=1,
  size="256x256",
  response_format="b64_json"
)
