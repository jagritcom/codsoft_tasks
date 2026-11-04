# Task 1 — Chatbot with Rule-Based Responses

## Objective
Build a chatbot that responds to user inputs using predefined rules.

## How it works
1. The user enters a message.
2. The program converts it to lowercase.
3. It checks for known words or phrases using `if/elif` conditions.
4. It returns the response associated with the first matching rule.
5. If no rule matches, it displays a fallback response.

## Run
```bash
pip install -r ../requirements.txt
streamlit run app.py
```

## Example
- Input: `Hello` → Output: `Hello! How can I help you today?`
- Input: `Tell me about Python` → Output: Python learning guidance.
