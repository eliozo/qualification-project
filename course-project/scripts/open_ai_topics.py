import openai

openai.api_key = 'your-api-key'

def generate_topic_skill_identifiers(description):
    prompt = f"Translate the English description '{description}' into relevant topic or skill identifiers."

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
    )

    return response.choices[0].text.strip()

# Example usage
user_description = "problems related to programming skills"
topic_skill_identifiers = generate_topic_skill_identifiers(user_description)

print("User Description:", user_description)
print("Generated Topic/Skill Identifiers:", topic_skill_identifiers)
