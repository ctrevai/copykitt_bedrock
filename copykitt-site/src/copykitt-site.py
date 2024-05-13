import streamlit as st
import requests

url = "https://ndl2jkznvl.execute-api.us-east-1.amazonaws.com/prod/"

resource = "generate-snippet-and-keywords"

st.title("CopyKitt | AI Marketing")

prompt = st.text_input(label="Input your product", value="")

if st.button("Generate"):

    data = {"prompt": prompt}
    response = requests.get(url=url+resource, params=data)
    response_json = response.json()
    # print(f"API response for PROMPT: {prompt} is {response.text}")
    st.write(f"Here are your results: Snippet: {response_json["snippet"]} Keywords: {response_json["keywords"]}")
