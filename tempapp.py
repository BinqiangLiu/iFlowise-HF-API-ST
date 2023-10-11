import requests

API_URL = "https://binqiangliu-iflowiseai.hf.space/api/v1/prediction/d60ab382-f51a-4408-ba9a-53613811ecb5"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

user_question = input("Enter your question:")
if user_question and not user_question.isspace():
    output = query({
        "question": user_question,
    })

    if 'text' in output:
        print(output['text'])
    
    if 'sourceDocuments' in output:
        count = 0
        previous_source_url = None
        for doc in output['sourceDocuments']:
            if 'metadata' in doc and 'source' in doc['metadata']:
                source_url = doc['metadata']['source']
                if source_url != previous_source_url:
                    count += 1
                    print(f"{count}: {source_url}")
                    previous_source_url = source_url
