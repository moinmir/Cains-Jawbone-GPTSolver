import openai
import os

# Set up the OpenAI API client
openai.api_key = os.getenv('OPEN_AI_KEY')

# Read the jumbled pages from a text file
input_file = "cains.txt"
with open(input_file, "r") as file:
    pages = file.read()

pages = ', \n'.join([f"\nPage {x+1}: {y.strip()}" for x, y in enumerate(pages.split('________________'))])

# Define the prompt
system = f"I have a 100-page murder mystery book with 6 murderers and 6 victims. The pages are jumbled and I need help figuring out the correct order of the pages and the names of the murderers and their victims. These are the pages: {pages}. Each page is labelled by 'Page' followed by a number. Your job is to figure out the correct order of the pages as well as the names of the murderes and their victims. Respond with the correct order of the page numbers as well as the murderers and their victims. The pages are in this format: 'Page 1:  text of page, Page 2 text of page,...'. These page numbers will not be correct and will be used to label them."

# Make the API call to generate the response
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages = [
    {"role": "system", "content": system},
    ]
)

# # Print the API response
print(response.choices[0].message.content)
