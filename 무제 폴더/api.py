import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  engine="davinci",
  prompt="Create an outline for an essay about Walt Disney and his contributions to animation:\n\nI: Introduction",
  temperature=0.7,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response["choices"][0]["text"])