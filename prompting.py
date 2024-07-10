# gpt_prompt_smurf.py

import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def generate_response(prompt):
    try:
        smurf_prompt = f"Respond always like a Smurf. {prompt}"
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate model, such as GPT-4
            prompt=smurf_prompt,
            max_tokens=150,  # Adjust this parameter as needed
            n=1,
            stop=None,
            temperature=0.7  # Controls the creativity of the response
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    prompt = input("Enter your prompt: ")
    response = generate_response(prompt)
    print("GPT-3 Response:")
    print(response)

if __name__ == "__main__":
    main()
