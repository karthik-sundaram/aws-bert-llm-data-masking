# Timeout
# 0min30sec

# Memory
 # 256MB

# Ephemeral storage
# 512MB


import os
import json
import time
import requests
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY
)

def lambda_handler(event, context):
    try:
        
        body = json.loads(event['body'])  
        input_text = body.get('text', '')  

        if not input_text:
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "Missing or empty 'text' parameter"}),
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }

        hf_response = call_huggingface_api(input_text)
        resp_j = hf_response.json()
        masked_text = mask_sensitive_data(input_text, resp_j)

        assistant_reply = call_openai_api(masked_text)

        return {
            'statusCode': 200,
            'body': json.dumps({
                "your_input_after_masking": masked_text,  
                "llm_response": assistant_reply
            }),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Invalid JSON in request body"}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }


## for JSON input from POST API call
# def lambda_handler(event, context):
#     try:
#         body = json.loads(event['body'])
#         input_text = body.get('text', '')

#         if not input_text:
#             return {
#                 'statusCode': 400,
#                 'body': json.dumps({"error": "Missing or empty 'text' parameter"}),
#                 'headers': {
#                     'Content-Type': 'application/json',
#                     'Access-Control-Allow-Origin': '*'
#                 }
#             }

#         hf_response = call_huggingface_api(input_text)

#         resp_j = hf_response.json()
#         masked_text = mask_sensitive_data(input_text, resp_j)

#         assistant_reply = call_openai_api(masked_text)

#         return {
#             'statusCode': 200,
#             'body': json.dumps({
#                 "your_input_after_masking": masked_text,
#                 "llm_response": assistant_reply
#             }),
#             'headers': {
#                 'Content-Type': 'application/json',
#                 'Access-Control-Allow-Origin': '*'
#             }
#         }

#     except json.JSONDecodeError:
#         return {
#             'statusCode': 400,
#             'body': json.dumps({"error": "Invalid JSON in request body"}),
#             'headers': {
#                 'Content-Type': 'application/json',
#                 'Access-Control-Allow-Origin': '*'
#             }
#         }
#     except Exception as e:
#         return {
#             'statusCode': 500,
#             'body': json.dumps({"error": str(e)}),
#             'headers': {
#                 'Content-Type': 'application/json',
#                 'Access-Control-Allow-Origin': '*'
#             }
#         }



def call_huggingface_api(input_text, max_retries=3, retry_delay=2):
    HF_API_URL = "https://api-inference.huggingface.co/models/karthiknitt/data_masking_distilbert_finetuned_ai4privacy"
    HF_API_TOKEN = os.getenv("HF_API_TOKEN") 
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    
    for attempt in range(max_retries):
        hf_response = requests.post(HF_API_URL, headers=headers, json={"inputs": input_text})
        
        if hf_response.status_code == 200:
            return hf_response
        
        print(f"Hugging Face API call failed. Attempt {attempt + 1} of {max_retries}. Status Code: {hf_response.status_code}")
        
        time.sleep(retry_delay)

    raise Exception(f"Hugging Face API failed after {max_retries} attempts. Last status code: {hf_response.status_code}")


def mask_sensitive_data(input_text, resp_j):
    dict_ind = 0
    final_op = ""
    len_sofar = 0

    while len_sofar < len(input_text):
        if dict_ind < len(resp_j):
            if len_sofar == resp_j[dict_ind]['start']:
                final_op += "[MASKED]"
                len_sofar = resp_j[dict_ind]['end']
                dict_ind += 1
            else:
                final_op += input_text[len_sofar]
                len_sofar += 1
        else:
            final_op += input_text[len_sofar]
            len_sofar += 1

    return final_op.strip()

def call_openai_api(masked_text):
    response = client.chat.completions.create(
        model="gpt-4o",  
        messages=[
            {"role": "user", "content": masked_text}
        ],
        temperature=0
    )
    
    assistant_reply = response.choices[0].message.content
    return assistant_reply
