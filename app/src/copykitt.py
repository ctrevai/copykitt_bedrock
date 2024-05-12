from typing import List
import boto3
import json
import os
import argparse
import re

#only for testing locally
#os.environ['AWS_PROFILE'] = 'ctdev'

MAX_INPUT_LENGTH = 32

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", help="input subject", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(f'User input: {user_input}')
    if validate_length(user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(f"Input is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}")
    
def validate_length(prompt: str) -> bool:
    if len(prompt) > MAX_INPUT_LENGTH:
        return False
    return True
    
def generate_keywords(prompt: str) -> List[str]:
    
    accept = 'application/json'
    contentType = 'application/json'

    bedrock = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-east-1",
    )
    modelId = "anthropic.claude-3-haiku-20240307-v1:0"

    enriched_prompt=f"Generate 10 related branding keywords for {prompt}. Send back only keywords list separated by comma."

    body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "temperature": 0,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": enriched_prompt,
                        }
                    ]
                }
            ]
        })

    response = bedrock.invoke_model(
            body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())
    response_content = response_body.get('content')

    keywords_text = response_content[0]["text"]
    keywords_array = re.split(",|\n", keywords_text)
    keywords_array = [keyword.replace(".", "") for keyword in keywords_array]
    keywords_array = [keyword.lower().strip() for keyword in keywords_array]
    print(f"Keywords: {keywords_array}")
    return keywords_array
    

def generate_branding_snippet(prompt: str) -> str:
    
    accept = 'application/json'
    contentType = 'application/json'

    bedrock = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-east-1",
    )
    modelId = "anthropic.claude-3-haiku-20240307-v1:0"

    enriched_prompt=f"Generate upbeat branding snippet for {prompt}. Send back only the branding snippet."

    body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "temperature": 0,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": enriched_prompt,
                        }
                    ]
                }
            ]
        })

    response = bedrock.invoke_model(
            body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())
    response_content = response_body.get('content')

    branding_text = response_content[0]["text"]
    print(f"Snippet: {branding_text}")
    return branding_text

if __name__ == "__main__":
    main()