# 🎛️ LLM Sampling Playground

A simple **Streamlit-based LLM Sampling Playground** that allows users to experiment with **Temperature** and **Top-P** parameters and observe how they affect AI-generated responses.

The application uses **Groq's API** with the `openai/gpt-oss-120b` model to generate responses based on the user's prompt.

---

## 🚀 Features

* 🔑 Secure Groq API key input using a password field
* 🌡️ Adjustable Temperature
* 🎯 Adjustable Top-P
* ✍️ Custom user prompts
* 🤖 AI text generation using Groq
* 📝 Single-output mode
* 🔄 Compare mode with 3 independent generations
* ⏳ Loading indicators while responses are being generated
* 🎨 Simple and interactive Streamlit interface

---

## 🛠️ Technologies Used

| Technology            | Purpose                               |
| --------------------- | ------------------------------------- |
| Python                | Programming language                  |
| Streamlit             | Creates the interactive web interface |
| Groq API              | Provides access to the LLM            |
| `openai/gpt-oss-120b` | LLM used for text generation          |

### Python Libraries

```text
streamlit
groq
```

---

## 🧠 How the Application Works

The application follows this basic flow:

```text
User opens Streamlit application
          ↓
Enters Groq API Key
          ↓
Selects Temperature
          ↓
Selects Top-P
          ↓
Selects Generation Mode
          ↓
Enters a Prompt
          ↓
Clicks "Generate"
          ↓
Groq API receives the request
          ↓
LLM generates a response
          ↓
Response is displayed in Streamlit
```

---

## 🌡️ Temperature

**Temperature controls the randomness of the generated response.**

The application provides a slider from `0.0` to `1.0`.

```python
temperature = st.sidebar.slider(
    "Temperature",
    0.0,
    1.0,
    0.7,
    0.1
)
```

### Lower Temperature

For example:

```text
Temperature = 0.0
```

The model generally produces more predictable and consistent responses.

### Higher Temperature

For example:

```text
Temperature = 1.0
```

The model generally produces more varied and creative responses.

---

## 🎯 Top-P

**Top-P controls how many likely tokens are considered during generation.**

The application provides a Top-P slider from `0.0` to `1.0`.

```python
top_p = st.sidebar.slider(
    "Top_p",
    0.0,
    1.0,
    0.9,
    0.05
)
```

A lower Top-P restricts the model to a smaller group of likely tokens, while a higher Top-P allows a broader selection.

---

## 🎯 Learning Objectives

This project demonstrates several important concepts:

* Building an interactive application with Streamlit
* Working with an LLM API
* Using the Groq Python SDK
* Understanding LLM sampling
* Understanding Temperature
* Understanding Top-P
* Working with API keys
* Sending prompts to an LLM
* Processing LLM responses
* Creating multiple LLM generations
* Comparing generated outputs

---

## 🔮 Future Improvements

Possible improvements include:

* Add response history
* Add token usage information
* Add response download functionality
* Add more LLM models
* Add side-by-side parameter comparisons
* Add a prompt history
* Add API key management using Streamlit Secrets
* Add response time measurement
* Add a visualization of Temperature and Top-P effects

---

## 👩‍💻 Author

**Aswini Kathirvel**

Built as a learning project to understand **LLM sampling parameters, Groq API integration, and Streamlit application development**.

---

## ⭐ Project Summary

**LLM Sampling Playground** is an interactive application that helps users understand how **Temperature** and **Top-P** influence LLM-generated text.

Users can enter a prompt, adjust sampling parameters, and either generate a single response or generate three responses for comparison.

Built with ❤️ using **Python + Streamlit + Groq**.
