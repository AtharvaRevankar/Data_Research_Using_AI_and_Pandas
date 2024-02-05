import pandas as pd
import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

def ask_chatgpt(playerfullname, joined1):
    # Define the prompt for ChatGPT
    prompt = f"Does the soccer {playerfullname}, who has played for {joined1} have kids (answer in yes/no) , no of kids he has(to be answered in number), gender of first child(answer male/daughter, birthday of first kid(dd/mm/yyyy) , name of the first kid(full name), the answer of these qs should be answered in rows without commas"

    # Get response from ChatGPT
    response = openai.Completion.create(
        engine="copilot",  # You can experiment with other engines if needed
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
    )

    return response.choices[0].text.strip()

# Read the Excel sheet
df = pd.read_excel('Book1.xlsx')

# Iterate through rows and ask questions
for index, row in df.iterrows():
    playerfullname = row['playerfullname']
    joined1 = row['joined1']

    # Get answers from ChatGPT
    answers = ask_chatgpt(playerfullname, joined1).split('\n')

    # Update the DataFrame with answers
    df.at[index, 'kids (yes/no)'] = answers[0]
    df.at[index, 'number_of_kids'] = answers[1]
    df.at[index, 'gender first kid'] = answers[2]
    df.at[index, 'birthday first kid'] = answers[3]
    df.at[index, 'name of first kid'] = answers[4]

# Save the updated DataFrame back to Excel
try:
    df.to_excel('Book1.xlsx', index=False)
except Exception as e:
    print(f"Error: {e}")
