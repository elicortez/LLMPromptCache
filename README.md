# LLM Prompt Cache

A caching library for language model prompts and responses.
Initial version uses [Jaccard similarity](https://en.wikipedia.org/wiki/Jaccard_index).

## Installation

pip install git+https://github.com/yourusername/llm-prompt-cache.git

## Usage

```python
from llm_prompt_cache import LLMPromptCache

cache = LLMPromptCache(similarity_threshold=0.5)

prompt1 = 'What is the capital of France?'
response1 = 'The capital of France is Paris.'
cache.add_to_cache(prompt1, response1, 'gpt-3')

prompt2 = 'What is the largest ocean on Earth?'
response2 = 'The largest ocean on Earth is the Pacific Ocean.'
cache.add_to_cache(prompt2, response2, 'gpt-3')

