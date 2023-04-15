import openai
from llm_prompt_cache import LLMPromptCache

# Replace with your OpenAI API key
openai.api_key = "your_api_key_here"

# Initialize the cache with a similarity threshold of 0.5
cache = LLMPromptCache(similarity_threshold=0.5)

def get_openai_completion(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# User-provided input
user_input = "What is the capital of France?"

# Check if the key is in the cache
response = cache.get_response(user_input)

if response:
    print(f"Response from cache: {response}")
else:
    # Use OpenAI Completion API to get the completion
    response = get_openai_completion(user_input)
    print(f"Response from OpenAI: {response}")
    cache.add_to_cache(user_input, response, 'davinci-codex')
