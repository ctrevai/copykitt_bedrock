import streamlit as st
import json
import requests

url = "https://2rcv6qdssl.execute-api.us-east-1.amazonaws.com/prod/"

resource = "generate-snippet-and-keywords"

st.title("CopyKitt | AI Marketing")

prompt = st.text_input(label="Input your porduct", value="")

if st.button("Generate"):

    data = {"prompt": prompt}
    response = requests.get(url=url+resource, params=data)
    response_json = response.json()
    # print(f"API response for PROMPT: {prompt} is {response.text}")
    st.write(f"Here are your results: Snippet: {
             response_json["snippet"]} Keywords: {response_json["keywords"]}")
