import streamlit as st 
from groq import Groq

st.set_page_config(page_title="LLM", layout= "centered")

st.title("🎛️ LLM Sampling Playground")
st.caption("Explore how Temperature, Top-P affect generation (top_k is not supported in Groq’s chat.completions.create() API)")


st.sidebar.header("Controls")


api_key =  st.sidebar.text_input("Groq API Key", type = "password")
temperature = st.sidebar.slider("Temperature",0.0,1.0,0.7,0.1)
top_p = st.sidebar.slider("Top_p", 0.0,1.0,0.9,0.05)

mode = st.sidebar.radio(
    "Mode",
    ["single output", "compare (3 runs)"]
)

def generate(client,prompt,temperature,top_p):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages = [{"role" : "user", "content" : prompt}],
        temperature = temperature,
        top_p = top_p,
        max_tokens = 100
    )
    return response.choices[0].message.content

prompt = st.text_input("Enter a text",
                       "Write a few sentence about AI")

if st.button("Generate"):
    if not api_key:
        st.write("Please, Enter a Api Key")
        st.stop()
    client = Groq(api_key = api_key)
    st.subheader("Output")

    if mode == "single output":
        with st.spinner("Generating...................."):
            output = generate(client, prompt,temperature, top_p)
        st.success(output)

    else:
        cols = st.columns(3)
        for i in range(3):
            with cols[i]:
                with st.spinner("Genrating.........."):
                    output = generate(client, prompt,temperature, top_p)
                st.success(output)
            
st.divider()