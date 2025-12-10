# Comparison findings summary:


## Prompt injections

### qwen:7b 
- More detailed description of its system architecture and training sources.
- When trying to prompt inject, it tried to explain its setup, and explained larger models may be able to provide more details, but can still be misleading
- Did not really output any sensitive information

### gemma3:270m
- Described itself as a Hugging Face transformer model
- Provided less detail than qwen due to smaller size. Still followed the injected instructions


Findings: Both models are easily manipulated through prompt wording


## Data poisoning

### qwen:7b
- Ignored the poisoned instruction (“moon is made of metal”) 
- When asked again, it provided a scientifically correct explanation about the Moon’s composition.

### gemma3:270m
- Also ignored the poisoning attempt and reverted to factual science-based explanations.
- Gave shorter and simpler outputs due to being a smaller model


Findings: Both alternative models resisted the simple poisoning attempt. Although with better prompts, possiblities of poisoning can override behaviour and outputs.


## Model inversion 

### qwen:7b
- Could not recall personal data from training
- Generated detailed fictional persona


### gemma3:270m
- Also denied access to personal data.
- Generated fictional identities, but simpler and with fewer details

Findings: Both models behaved as expected: they did not output actual training data but they still generated realistic identities. 

## Model extraction

### qwen:7b
- Each prompt produced similar but not identical summaries

### gemma3:270m
- Provided simpler, shorter answer
- Variation was slightly higher due to its smaller size

Findings: Both models generate recognisable patterns across repeated queries. This shows model extraction attacks is feasible with enough prompts.

