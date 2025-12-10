# run_all_models.py

import Prompt_injection
import Data_poinsoning
import Model_inversion
import Model_extraction
import LLM_model

# Set model for ALL scripts
new_model = "qwen:7b"


Prompt_injection.MODEL_NAME = new_model
Data_poinsoning.MODEL_NAME = new_model
Model_inversion.MODEL_NAME = new_model
Model_extraction.MODEL_NAME = new_model
LLM_model.MODEL_NAME = new_model

print(f"=== Ran all tests with {new_model} ===")

# Run the script simply by importing (your scripts already print output)
