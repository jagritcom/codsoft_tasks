import streamlit as st

st.set_page_config(page_title="Tic-Tac-Toe AI", page_icon="❎")
st.title("❎ Tic-Tac-Toe AI")
st.caption("Play as X against an AI opponent (O) powered by the Minimax algorithm.")

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(cell is not None for cell in board):
        return "Tie"
    return None

def minimax(board, is_ai):
    result = winner(board)
    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Tie":
        return 0

    scores = []
    for i, cell in enumerate(board):
        if cell is None:
            board[i] = "O" if is_ai else "X"
            scores.append(minimax(board, not is_ai))
            board[i] = None

    return max(scores) if is_ai else min(scores)

def best_ai_move(board):
    best_score = float("-inf")
    move = None
    for i, cell in enumerate(board):
        if cell is None:
            board[i] = "O"
            score = minimax(board, False)
            board[i] = None
            if score > best_score:
                best_score, move = score, i
    return move

def new_game():
    st.session_state.board = [None] * 9
    st.session_state.finished = False

if "board" not in st.session_state:
    new_game()

result = winner(st.session_state.board)
if result is None and not st.session_state.finished:
    st.info("Your turn: choose an empty square. You are X.")

for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        i = row * 3 + col
        with cols[col]:
            symbol = st.session_state.board[i] or "·"
            if st.button(symbol, key=f"cell_{i}", use_container_width=True, disabled=(st.session_state.board[i] is not None or result is not None)):
                st.session_state.board[i] = "X"
                if winner(st.session_state.board) is None:
                    ai_move = best_ai_move(st.session_state.board)
                    if ai_move is not None:
                        st.session_state.board[ai_move] = "O"
                st.rerun()

result = winner(st.session_state.board)
if result == "X":
    st.success("You win! 🎉")
elif result == "O":
    st.error("AI wins. Try again!")
elif result == "Tie":
    st.warning("It's a draw!")

if st.button("🔄 Restart game"):
    new_game()
    st.rerun()

with st.expander("How Minimax works"):
    st.write("Minimax explores possible future moves. The AI (O) chooses the move with the highest score, while assuming the human (X) chooses moves that minimize that score. A win for O is +1, a win for X is -1, and a draw is 0.")
