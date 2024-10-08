import gradio as gr
import requests

def query_model(input_text):
    url = "https://ssuso8l9ng.execute-api.us-east-2.amazonaws.com/dev/data_masked_response"  
    headers = {
        'Content-Type': 'application/json',
    }
    
    payload = {
        "text": input_text
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)

        print(f"Raw Response Text: {response.text}")

        if response.status_code == 200:
            try:
                result = response.json() 
                if 'your_input_after_masking' in result and 'llm_response' in result:
                    masked_text = result['your_input_after_masking'].replace('\\n', '\n')
                    openai_response = result['llm_response'].replace('\\n', '\n') 
                    return masked_text, openai_response 
                else:
                    return "Invalid response format", "Missing 'your_input_after_masking' or 'llm_response'"
            except ValueError:
                return f"Failed to parse JSON. Raw response: {response.text}", ""
        else:
            return f"Error {response.status_code}: {response.text}", ""

    except requests.exceptions.RequestException as e:
        return f"Request failed: {str(e)}", ""

iface = gr.Interface(
    fn=query_model,
    inputs=gr.Textbox(lines=10, label="Input Text"),
    outputs=[
        gr.Textbox(label="Masked Input", lines=10, interactive=False),    
        gr.Textbox(label="LLM Response", lines=10, interactive=False)      
    ],  
    title="Data Masking & LLM Integration",
    description="Submit text to get it masked and processed by OpenAI"
)

iface.launch()
