import pickle
import os
import psutil
import time
import re
import string

class LLMPromptCache:
    def __init__(self, similarity_threshold=0.5, max_size=None, max_elements=None, max_memory=None):
        self.cache = {}
        self.similarity_threshold = similarity_threshold
        self.saved_tokens = 0
        self.max_size = max_size
        self.max_elements = max_elements
        self.max_memory = max_memory

    def jaccard_similarity(self, str1, str2):
        set1 = set(str1.split())
        set2 = set(str2.split())
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        return len(intersection) / len(union)

    def preprocess_input(self, text):
        # Convert text to lowercase and remove punctuation
        text = text.lower()
        text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
        return text

    def add_to_cache(self, prompt, response, model_name):
        preprocessed_prompt = self.preprocess_input(prompt)
        for key in self.cache:
            cached_prompt = self.cache[key]['input']
            similarity = self.jaccard_similarity(preprocessed_prompt , cached_prompt)
            if similarity >= self.similarity_threshold:
                # Store the new prompt under the same key if it's similar enough
                self.cache[key]['similar_prompts'].append({'input': prompt, 'output': response})
                self.saved_tokens += len(prompt.split()) + len(response.split())
                return

        # If no similar prompt is found, create a new entry
        new_key = f'prompt{len(self.cache) + 1}'
        self.cache[new_key] = {
            'input': prompt,
            'output': response,
            'model_name': model_name,
            'similar_prompts': [],
            'timestamp': time.time()
        }

    def get_response(self, prompt):
        preprocessed_prompt = self.preprocess_input(prompt)

        for key in self.cache:
            cached_prompt = self.cache[key]['input']
            similarity = self.jaccard_similarity(preprocessed_prompt, cached_prompt)
            if similarity >= self.similarity_threshold:
                return self.cache[key]['output']
        return None

    def get_saved_tokens(self):
        return self.saved_tokens

    def save_to_disk(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump(self.cache, f)

    def load_from_disk(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                self.cache = pickle.load(f)
        else:
            raise FileNotFoundError(f"Cache file not found: {file_path}")
