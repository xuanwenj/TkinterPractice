
# # import os
# # import openai

# # openai.api_key = os.getenv("OPENAI_API_KEY")
# # response = openai.ChatCompletion.create(
# #     model="gpt-3.5-turbo",
# #     messages=[
# #         {"role": "user", "content": "Hi ChatGPT. Say hi back!"}
# #     ]
# # )

# # answer = response.choices[0].message.content
# # print(answer)

# import os
# from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# response = client.completions.create(model="gpt-3.5-turbo",
# prompt="Hi ChatGPT. Say hi back!",
# max_tokens=150)

# answer = response.choices[0].text
# print(answer)

import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)


