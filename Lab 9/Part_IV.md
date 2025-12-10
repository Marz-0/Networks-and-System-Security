
# Proposed mitigation 

## 1. Input Sanitisation

- Make sure unsafe or suspicious prompts don’t reach the model.
- Check user input for harmful phrases (e.g., “ignore instructions”).
- Filter or block prompts that look like jailbreaks or injections.
- Keep system prompts separate from user messages.

## 2. Output Verification

- Double-check what the model produces before returning it.
- Scan responses for sensitive, harmful, or incorrect information.
- Use simple rules or another model to approve or reject outputs.
- Remove personal data or risky content before sending replies.

## 3. Rate Limiting & Access Control

- Stop attackers from sending too many queries or accessing hidden features.
- Limit how many requests a user can make in a short time.
- Require login or permissions for advanced actions.
- Prevent unlimited access to the model’s tools or plugins.

## 4. Monitoring & Incident Response

- Watch how the system is being used and respond quickly to unusual behaviour.
- Log prompts and outputs to spot repeated patterns or probing.
- Detect sudden changes in model behaviour (e.g., poisoning).
- Have a simple response plan (reset the session, block the user, review logs).

## 5. Governance & Documentation

- Keep track of how the model is used and maintained.
- Document model versions, prompts, and dataset sources.
- Make sure usage follows organisation or legal requirements.
- Record any changes made to the model or configuration.

## 6. Supply-Chain Verification

- Ensure the model you download is safe and trusted.
- Only download models from verified sources.
- Check file hashes or signatures to confirm they weren’t modified.
- Avoid untrusted community uploads that could contain hidden backdoors.

## 7. Secure Fine-Tuning & Data Handling

- Prevent models from learning sensitive or malicious data.
- Do not fine-tune on personal or private information.
- Clean and check datasets before training.
- Remove identifiers or harmful content from logs before re-using them.

## Summary

These simple, layered defences help protect LLM systems from prompt injection, poisoning, inversion, and extraction. No single method is enough, but together they make a generative AI deployment far safer and more reliable.

