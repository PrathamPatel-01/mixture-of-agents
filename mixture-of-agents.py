import streamlit as st
import asyncio
import os
from together import AsyncTogether, Together

st.title("Mixture of Agents LLM App")
together_api_key = st.text_input("Enter your Together API Key", type="password")

if together_api_key:
    os.environ["together_api_key"] = together_api_key
    client = Together(api_key=together_api_key)
    async_client = AsyncTogether(api_key=together_api_key)

reference_model = [
    "Qwen/Qwen2-72B-Instruct",
    "mistralai/Mistral-7B-Instruct-v0.1",
]

aggregator_model = "mistralai/Mistral-7B-Instruct-v0.1"

aggregator_system_prompt = """you have been provided with a set of responses from various models from various open-source models to the lateat user query.Your task is to synthesize these responses into a single, high-quality response.It is crucial that you do not simply concatenate the responses, but rather analyze and integrate the information to produce a coherent and comprehensive answer. Your response should be well-structured, addressing all relevant points raised in the individual responses, and should reflect a deep understanding of the topic at hand. Aim for clarity, conciseness, and depth in your synthesis."""

async def run_LLM(model):
    response = await async_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_prompt}],
        max_tokens=512,
        temperature=0.7,
    )
    return response.choices[0].message.content

async def main():
    results = await asyncio.gather(*[run_LLM(model) for model in reference_model])

    st.subheader("Responses from Reference Models:")
    for model, response in zip(reference_model, results):
        with st.expander(f"Response from {model}"):
            st.write(response)

    st.subheader("Aggregated Response:")
    finalStream = client.chat.completions.create(
        model=aggregator_model,
        messages= [
            {"role": "system", "content": aggregator_system_prompt},
            {"role": "user", "content": ",".join(response for response in results)},
        ],
        stream=True,
    )

    response_container = st.empty()
    full_response = ""
    for chunk in finalStream:
        content = chunk.choices[0].delta.content or ""
        full_response += content
        response_container.markdown(full_response + "█")
    response_container.markdown(full_response)

user_prompt = st.text_input("Enter your query here:")

if st.button("Get Answers"):
    if user_prompt:
        asyncio.run(main())
    else:
        st.warning("Please enter a query to get answers.")