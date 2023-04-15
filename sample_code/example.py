from llm_prompt_cache import LLMPromptCache

# Initialize the cache with a similarity threshold of 0.5
cache = LLMPromptCache(similarity_threshold=0.5)

# Add prompts and responses to the cache
prompt1 = 'What is the capital of France?'
response1 = 'The capital of France is Paris.'
cache.add_to_cache(prompt1, response1, 'gpt-3')

prompt2 = 'What is the largest ocean on Earth?'
response2 = 'The largest ocean on Earth is the Pacific Ocean.'
cache.add_to_cache(prompt2, response2, 'gpt-3')

# Attempt to retrieve a response from the cache using a similar prompt
similar_prompt = 'What city is the capital of France?'
response = cache.get_response(similar_prompt)

if response:
    print(f"Response from cache: {response}")
else:
    print("No similar response found in cache")

# Save cache state to disk
cache.save_to_disk('cache_data.pkl')

# Load cache state from disk
loaded_cache = LLMPromptCache()
loaded_cache.load_from_disk('cache_data.pkl')

# Check if the loaded cache contains the same data
response = loaded_cache.get_response(similar_prompt)

if response:
    print(f"Response from loaded cache: {response}")
else:
    print("No similar response found in loaded cache")

# Check the number of saved tokens
print(f"Saved tokens: {cache.get_saved_tokens()}")
