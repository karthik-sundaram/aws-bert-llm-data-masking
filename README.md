# AWS deployment - Sensitive Data Masking with Named Entity Recognition (NER) Using DistilBERT

This project demonstrates how a DistilBERT-based NER model can be fine-tuned to detect and mask sensitive information such as personal names, addresses, passwords, and other identifiable data.
It showcases how we can enhance data privacy in real-world applications like healthcare or finance especially with being cautious about inadvertently sending out sensitive information into LLM/GenAi tool prompts.
It also includes deployment and hosting using **AWS services**

# ARCHITECTURE:

    
![image](https://github.com/user-attachments/assets/cb8c3e9a-b8af-44b3-b4c3-33a27fa958ed)



# WORKING:

    
![image](https://github.com/user-attachments/assets/64ef563a-4627-4a4b-8c26-4605a27a41bd)

  
## Input:  
_I am facing an error here. help me resolve in short:_  
  
_import psycopg2_  
_conn = psycopg2.connect(host='192.168.1.100', port='5432', database='production_db', user='john_doe', password='1jhg$#12%9^f5')_  
_cursor = conn.cursorr()_   
_cursor.execute("SELECT * FROM users WHERE email = 'john.doe@example.com'")_    

## Masking of input: 
_I am facing an error here. help me resolve in short:_  
  
_import psycopg2 _
_conn = psycopg2.connect(host='[MASKED]', port='[MASKED]', database='production_db', user='[MASKED]', password='[MASKED]')_  
_cursor = conn.cursorr()_    
_cursor.execute("SELECT * FROM users WHERE email = '[MASKED]'")_  

## LLM Response:  
_The error in your code is due to a typo in the method call `cursorr()`. It should be `cursor()`. Here's the corrected code:_
  
```python 
import psycopg2  
  
conn = psycopg2.connect(  
    host='[MASKED]',   
    port='[MASKED]',   
    database='production_db',   
    user='[MASKED]',   
    password='[MASKED]'  
)  
cursor = conn.cursor()  # Corrected this line  
cursor.execute("SELECT * FROM users WHERE email = '[MASKED]'")  
```  
  
_Make sure to replace `[MASKED]` with your actual database credentials._ 


# PROJECT OVERVIEW
  
We leverage two datasets:

- ai4privacy/pii-masking-43k  
- English Balanced 10K

These datasets contain labeled text with **116 entity types/labels to mask** listed below, including personal names, addresses, passwords, and more. The DistilBERT model is fine-tuned to recognize and mask such entities in the input text to ensure privacy.  
  
_["0": "B-PREFIX", "1": "I-PREFIX", "2": "B-FIRSTNAME", "3": "I-FIRSTNAME", "4": "B-MIDDLENAME", "5": "B-LASTNAME", "6": "I-LASTNAME", "7": "O", "8": "B-JOBDESCRIPTOR", "9": "B-JOBTITLE", "10": "I-JOBTITLE", "11": "B-COMPANY_NAME", "12": "I-COMPANY_NAME", "13": "B-JOBAREA", "14": "B-EMAIL", "15": "I-EMAIL", "16": "B-TIME", "17": "I-TIME", "18": "B-DATE", "19": "I-DATE", "20": "B-URL", "21": "I-URL", "22": "B-BITCOINADDRESS", "23": "I-BITCOINADDRESS", "24": "B-ETHEREUMADDRESS", "25": "I-ETHEREUMADDRESS", "26": "B-ACCOUNTNAME", "27": "I-ACCOUNTNAME", "28": "B-IBAN", "29": "I-IBAN", "30": "B-ACCOUNTNUMBER", "31": "I-ACCOUNTNUMBER", "32": "B-BIC", "33": "I-BIC", "34": "B-IPV4", "35": "I-IPV4", "36": "B-STREETADDRESS", "37": "I-STREETADDRESS", "38": "B-CITY", "39": "I-CITY", "40": "B-ZIPCODE", "41": "I-ZIPCODE", "42": "B-USERNAME", "43": "I-USERNAME", "44": "B-IPV6", "45": "I-IPV6", "46": "B-CREDITCARDNUMBER", "47": "I-CREDITCARDNUMBER", "48": "B-VEHICLEVIN", "49": "I-VEHICLEVIN", "50": "B-SUFFIX", "51": "I-SUFFIX", "52": "B-AMOUNT", "53": "I-AMOUNT", "54": "B-CURRENCY", "55": "I-CURRENCY", "56": "B-PASSWORD", "57": "I-PASSWORD", "58": "B-JOBTYPE", "59": "B-STATE", "60": "B-BUILDINGNUMBER", "61": "I-BUILDINGNUMBER", "62": "B-VEHICLEVRM", "63": "I-VEHICLEVRM", "64": "B-PHONEIMEI", "65": "I-PHONEIMEI", "66": "I-JOBAREA", "67": "I-STATE", "68": "B-COUNTY", "69": "B-CURRENCYNAME", "70": "I-CURRENCYNAME", "71": "B-CURRENCYSYMBOL", "72": "B-MASKEDNUMBER", "73": "I-MASKEDNUMBER", "74": "B-PHONE_NUMBER", "75": "I-PHONE_NUMBER", "76": "B-SECONDARYADDRESS", "77": "I-SECONDARYADDRESS", "78": "B-SSN", "79": "I-SSN", "80": "B-CURRENCYCODE", "81": "B-LITECOINADDRESS", "82": "I-LITECOINADDRESS", "83": "B-MAC", "84": "I-MAC", "85": "B-CREDITCARDISSUER", "86": "I-CREDITCARDISSUER", "87": "B-CREDITCARDCVV", "88": "I-CREDITCARDCVV", "89": "B-USERAGENT", "90": "I-USERAGENT", "91": "B-IP", "92": "I-IP", "93": "B-SEX", "94": "B-STREET", "95": "I-STREET", "96": "B-PIN", "97": "I-PIN", "98": "I-JOBTYPE", "99": "I-MIDDLENAME", "100": "I-CURRENCYCODE", "101": "I-CURRENCYSYMBOL", "102": "B-FULLNAME", "103": "I-FULLNAME", "104": "B-NAME", "105": "I-NAME", "106": "B-GENDER", "107": "B-NUMBER", "108": "I-NUMBER", "109": "I-GENDER", "110": "B-NEARBYGPSCOORDINATE", "111": "I-NEARBYGPSCOORDINATE", "112": "B-DISPLAYNAME", "113": "I-DISPLAYNAME", "114": "B-SEXTYPE", "115": "B-ORDINALDIRECTION"]_

# PROCESS OUTLINE

## 1. Model Training    
- **Data Preprocessing**: Tokenization and label alignment to ensure that sensitive entities are properly identified and labeled, even after tokenization splits words into subwords.
- **Model Training**: Fine-tuned DistilBERT using Hugging Face's transformers library for token classification.
- **Post-processing**: Masking sensitive entities in the output text by replacing identified entities with [MASKED].     
- **HF Spaces hosting**: Pushed fine tuned model to **karthiknitt/data_masking_distilbert_finetuned_ai4privacy**

![image](https://github.com/user-attachments/assets/f2b1161f-17d2-4a36-8b25-b6069f11f482)


## 2. AWS-Powered Inference Pipeline    
The inference pipeline leverages AWS Lambda as the orchestrator, coordinating requests and model execution, and integrates with API Gateway and CloudWatch for monitoring. The pipeline ensures data privacy before text is sent for further processing by OpenAI.  

### Inference Flow:    
- **Gradio Frontend**: Users input text via a Gradio interface hosted on Hugging Face Spaces. **(karthiknitt/LLM_data_masking)**
- **API Gateway**: Secures and routes API calls between the frontend and Lambda  
- **Lambda Orchestration**: Lambda handles the request and interacts with the **fine-tuned model (hosted on Hugging Face)** to mask sensitive data.  
- **CloudWatch**: Monitors the Lambda functions and logs API interactions for performance tracking.   
- **OpenAI API**: The masked text is sent to OpenAI for further processing (e.g., text completion).   
- **Response**: The final response is returned and displayed on the Gradio UI.   
 


# Model Performace:  

![image](https://github.com/user-attachments/assets/414d3498-7d38-427b-ae94-065a9d93653d)  
(Check complete performance pivoted on each of 116 labels inside the links below)    


  
# Kaggle Notebook Link:  

https://www.kaggle.com/code/karthiksundaram123/ner-bert-privacy/edit  
  

          
# Watch a small demo here: 

[![Watch the video](https://img.youtube.com/vi/TEne9pKfwbo/maxresdefault.jpg)](https://www.youtube.com/watch?v=TEne9pKfwbo)  

[![Watch the video](https://img.youtube.com/vi/A1sinX2p_Ww/maxresdefault.jpg)](https://www.youtube.com/watch?v=A1sinX2p_Ww)  





