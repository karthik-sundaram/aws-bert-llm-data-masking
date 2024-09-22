# Sensitive Data Masking with Named Entity Recognition (NER) Using DistilBERT

This project demonstrates how a DistilBERT-based NER model can be fine-tuned to detect and mask sensitive information such as personal names, addresses, passwords, and other identifiable data.
It showcases how we can enhance data privacy in real-world applications like healthcare or finance especially with being cautious about inadvertently sending out sensitive information into LLM/GenAi tool prompts.

**Input: "John Doe lives at 123 Main St, California 90210."  
Masked Output: "[MASKED] [MASKED] lives at [MASKED] [MASKED] [MASKED]."**    


### Project Overview
We leverage two datasets:

ai4privacy/pii-masking-43k
English Balanced 10K

These datasets contain labeled text with **116 entity types/labels to mask** listed below, including personal names, addresses, passwords, and more. The DistilBERT model is fine-tuned to recognize and mask such entities in the input text to ensure privacy.  
  
_["0": "B-PREFIX", "1": "I-PREFIX", "2": "B-FIRSTNAME", "3": "I-FIRSTNAME", "4": "B-MIDDLENAME", "5": "B-LASTNAME", "6": "I-LASTNAME", "7": "O", "8": "B-JOBDESCRIPTOR", "9": "B-JOBTITLE", "10": "I-JOBTITLE", "11": "B-COMPANY_NAME", "12": "I-COMPANY_NAME", "13": "B-JOBAREA", "14": "B-EMAIL", "15": "I-EMAIL", "16": "B-TIME", "17": "I-TIME", "18": "B-DATE", "19": "I-DATE", "20": "B-URL", "21": "I-URL", "22": "B-BITCOINADDRESS", "23": "I-BITCOINADDRESS", "24": "B-ETHEREUMADDRESS", "25": "I-ETHEREUMADDRESS", "26": "B-ACCOUNTNAME", "27": "I-ACCOUNTNAME", "28": "B-IBAN", "29": "I-IBAN", "30": "B-ACCOUNTNUMBER", "31": "I-ACCOUNTNUMBER", "32": "B-BIC", "33": "I-BIC", "34": "B-IPV4", "35": "I-IPV4", "36": "B-STREETADDRESS", "37": "I-STREETADDRESS", "38": "B-CITY", "39": "I-CITY", "40": "B-ZIPCODE", "41": "I-ZIPCODE", "42": "B-USERNAME", "43": "I-USERNAME", "44": "B-IPV6", "45": "I-IPV6", "46": "B-CREDITCARDNUMBER", "47": "I-CREDITCARDNUMBER", "48": "B-VEHICLEVIN", "49": "I-VEHICLEVIN", "50": "B-SUFFIX", "51": "I-SUFFIX", "52": "B-AMOUNT", "53": "I-AMOUNT", "54": "B-CURRENCY", "55": "I-CURRENCY", "56": "B-PASSWORD", "57": "I-PASSWORD", "58": "B-JOBTYPE", "59": "B-STATE", "60": "B-BUILDINGNUMBER", "61": "I-BUILDINGNUMBER", "62": "B-VEHICLEVRM", "63": "I-VEHICLEVRM", "64": "B-PHONEIMEI", "65": "I-PHONEIMEI", "66": "I-JOBAREA", "67": "I-STATE", "68": "B-COUNTY", "69": "B-CURRENCYNAME", "70": "I-CURRENCYNAME", "71": "B-CURRENCYSYMBOL", "72": "B-MASKEDNUMBER", "73": "I-MASKEDNUMBER", "74": "B-PHONE_NUMBER", "75": "I-PHONE_NUMBER", "76": "B-SECONDARYADDRESS", "77": "I-SECONDARYADDRESS", "78": "B-SSN", "79": "I-SSN", "80": "B-CURRENCYCODE", "81": "B-LITECOINADDRESS", "82": "I-LITECOINADDRESS", "83": "B-MAC", "84": "I-MAC", "85": "B-CREDITCARDISSUER", "86": "I-CREDITCARDISSUER", "87": "B-CREDITCARDCVV", "88": "I-CREDITCARDCVV", "89": "B-USERAGENT", "90": "I-USERAGENT", "91": "B-IP", "92": "I-IP", "93": "B-SEX", "94": "B-STREET", "95": "I-STREET", "96": "B-PIN", "97": "I-PIN", "98": "I-JOBTYPE", "99": "I-MIDDLENAME", "100": "I-CURRENCYCODE", "101": "I-CURRENCYSYMBOL", "102": "B-FULLNAME", "103": "I-FULLNAME", "104": "B-NAME", "105": "I-NAME", "106": "B-GENDER", "107": "B-NUMBER", "108": "I-NUMBER", "109": "I-GENDER", "110": "B-NEARBYGPSCOORDINATE", "111": "I-NEARBYGPSCOORDINATE", "112": "B-DISPLAYNAME", "113": "I-DISPLAYNAME", "114": "B-SEXTYPE", "115": "B-ORDINALDIRECTION"]_

## Process Outline

Data Preprocessing: Tokenization and label alignment to ensure that sensitive entities are properly identified and labeled, even after tokenization splits words into subwords.
Model Training: Fine-tuned DistilBERT using Hugging Face's transformers library for token classification.
Post-processing: Masking sensitive entities in the output text by replacing identified entities with [MASKED].  
  
Explore the Full Code on Kaggle
You can view and run the full code in the Kaggle Notebook:



### Performace:  

![image](https://github.com/user-attachments/assets/414d3498-7d38-427b-ae94-065a9d93653d)  
(Check complete performance pivoted on each of 116 labels inside the links below)    


  
### Kaggle Notebook Link:  

https://www.kaggle.com/code/karthiksundaram123/ner-bert-privacy/edit  
  

          
### Watch a small demo here: 

[![Watch the video](https://img.youtube.com/vi/6AAC1GAwzhQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=6AAC1GAwzhQ)  





