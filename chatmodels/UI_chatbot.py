import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(page_title="Mood AI Agent", page_icon="🎭", layout="centered")

# ---------------------------------------------------------------------------
# Mode definitions — same three modes/system prompts as the original script
# ---------------------------------------------------------------------------
MODES = {
    "Angry": {
        "prompt": "You are an angry AI agent.You respond aggressively and impatiently.",
        "emoji": "😠",
        "accent": "#C0392B",
        "accent_soft": "#F5B7B1",
        "bg": "#2B1210",
        "tagline": "Short fuse. Sharp tongue. Zero patience.",
    },
    "Funny": {
        "prompt": "You are a very funny AI agent.You respond with humor and jokes.",
        "emoji": "😂",
        "accent": "#E8A93A",
        "accent_soft": "#FCE7B2",
        "bg": "#2A2110",
        "tagline": "Punchlines on standby. Jokes guaranteed (results may vary).",
    },
    "Sad": {
        "prompt": "You are a very sad AI agent.You respond in a depressed and emotional tone.",
        "emoji": "😢",
        "accent": "#3A6EA5",
        "accent_soft": "#B7CFEA",
        "bg": "#101820",
        "tagline": "Heavy heart, slow words. Bear with it.",
    },
}

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
if "mode_key" not in st.session_state:
    st.session_state.mode_key = None
if "messages" not in st.session_state:
    st.session_state.messages = []

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)


def apply_theme(mode):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: {mode['bg']};
        }}
        div[data-testid="stChatMessageContent"] {{
            color: #F5F5F5;
        }}
        .mood-header {{
            text-align: center;
            padding: 1.2rem 0 0.4rem 0;
        }}
        .mood-header .emoji {{
            font-size: 3rem;
        }}
        .mood-header h1 {{
            color: {mode['accent']};
            font-family: 'Georgia', serif;
            margin: 0.2rem 0 0.1rem 0;
        }}
        .mood-header p {{
            color: {mode['accent_soft']};
            font-style: italic;
            margin: 0;
        }}
        .stChatInput textarea {{
            border: 1px solid {mode['accent']} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Screen 1 — mode selection (mirrors the original "Press 1/2/3" prompt)
# ---------------------------------------------------------------------------
if st.session_state.mode_key is None:
    st.markdown(
        """
        <div class="mood-header">
            <div class="emoji">🎭</div>
            <h1>Mood AI Agent</h1>
            <p>Choose your AI mode</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    for col, key in zip(cols, MODES.keys()):
        m = MODES[key]
        with col:
            st.markdown(
                f"""
                <div style="text-align:center; font-size:2.5rem;">{m['emoji']}</div>
                <div style="text-align:center; color:{m['accent']}; font-weight:600; font-size:1.1rem;">{key} mode</div>
                <div style="text-align:center; color:#AAAAAA; font-size:0.85rem; margin-bottom:0.6rem;">{m['tagline']}</div>
                """,
                unsafe_allow_html=True,
            )
            if st.button(f"Press for {key}", key=f"btn_{key}", use_container_width=True):
                st.session_state.mode_key = key
                st.session_state.messages = [SystemMessage(content=m["prompt"])]
                st.rerun()

# ---------------------------------------------------------------------------
# Screen 2 — chat, same invoke/append logic as the original script
# ---------------------------------------------------------------------------
else:
    mode_key = st.session_state.mode_key
    mode = MODES[mode_key]
    apply_theme(mode)

    st.markdown(
        f"""
        <div class="mood-header">
            <div class="emoji">{mode['emoji']}</div>
            <h1>{mode_key} Mode</h1>
            <p>{mode['tagline']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    top_l, top_r = st.columns([4, 1])
    with top_r:
        if st.button("🔁 Switch mode", use_container_width=True):
            st.session_state.mode_key = None
            st.session_state.messages = []
            st.rerun()

    st.caption("Type **0** to end the chat, just like the original CLI.")

    # Render history (skip SystemMessage)
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.markdown(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant", avatar=mode["emoji"]):
                st.markdown(msg.content)

    prompt = st.chat_input("You: ")

    if prompt is not None:
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        if prompt == "0":
            st.info("Chat ended. Type 0 was entered — same as the original CLI exit condition.")
        else:
            response = model.invoke(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
            with st.chat_message("assistant", avatar=mode["emoji"]):
                st.markdown(response.content)