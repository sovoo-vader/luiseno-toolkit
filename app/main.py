
# Streamlit Main Interface – Extended for 20 Script Suite
import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import importlib

st.set_page_config(layout="wide")
st.title("Luiseño Language Revival Toolkit")

# Tool categories and mappings
tools = {
    "Linguistic Analysis": [
        "interlinear_parser", "phoneme_analyzer", "morph_syntax_tree", "word_freq_visualizer", "semantic_drift_tracker"
    ],
    "Corpus & AI Tools": [
        "custom_tokenizer", "bert_finetune_trainer", "tts_synthesizer", "dialect_differentiator", "named_entity_extractor"
    ],
    "Folklore-Aware NLP": [
        "mythology_tagger", "ancestral_timeline_builder", "colonial_shift_detector", "sentiment_annotator", "cultural_context_linker"
    ],
    "Language Learning": [
        "vocab_trainer_app", "av_story_rebuilder", "morph_game_engine", "speech_to_morpheme", "alignment_tool"
    ]
}

selected_category = st.sidebar.selectbox("Tool Category", list(tools.keys()))
selected_tool = st.sidebar.selectbox("Select Tool", tools[selected_category])

if st.sidebar.button("Run Tool"):
    try:
        module = importlib.import_module(f"app.{selected_tool}")
        st.success(f"✅ Running: {selected_tool}")
        if hasattr(module, "main"):
            module.main()
        elif hasattr(module, "__name__") and module.__name__ == "__main__":
            exec(open(module.__file__).read())
        else:
            st.warning("ℹ️ Tool loaded, but has no main method. Please use CLI or integrate manually.")
    except Exception as e:
        st.error(f"❌ Failed to run {selected_tool}: {e}")
