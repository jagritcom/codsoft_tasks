# Task 2 — Tic-Tac-Toe AI

## Objective
Implement an AI agent that plays Tic-Tac-Toe against a human player using Minimax.

## How it works
- The human plays as `X`; the AI plays as `O`.
- The game checks rows, columns, diagonals, and draws.
- Minimax recursively evaluates possible future board states.
- AI win = `+1`, human win = `-1`, draw = `0`.
- The AI selects the move with the highest score.

## Run
```bash
pip install -r ../requirements.txt
streamlit run app.py
```
