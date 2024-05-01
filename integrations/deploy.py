import os, requests, time
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint

PROMPT_MAP = {
    'llama-base': 
    '''
<s>[INST] <<SYS>>
You are a helpful assistant that generates action items (e.g. deliverables, future meetings, tasks) from meeting notes and transcripts. 
You are given these transcripts as input and are expected to generate action items based on the content of the meeting. These action 
items should be clear, concise, and actionable. These action items must be relevant to future work discussed in the meeting and not 
just a summary of the meeting. The action items should be generated in the form of a JSON object with the following structure:

{
    "action_items": [
        {
            "id": "Unique identifier for the action item (initially null)",
            "description": "The description of the action item",
            "assignee": "The person responsible for completing the action item (initially null)",
            "created_date": "The date the action item was created (initially null)",
            "due_date": "The due date for the action item (initially null)",
            "status": "The status of the action item (initially 'open')",
        },
        ...
    ]
}
<<SYS>>

{meeting_notes}[\INST]
    ''',
}

class HF:
    def __init__(self, prompt_id: str):
        self.prompt = PromptTemplate(PROMPT_MAP.get(prompt_id))
        self.llm = HuggingFaceEndpoint(
            endpoint_url=os.environ.get('HUGGING_FACE_ENDPOINT'),
            max_new_tokens=512,
            huggingfacehub_api_token=os.environ.get('HUGGING_FACE_HUB_TOKEN')
        )
    
    def initialize_endpoint(self, max_retries: int = 5, delay: int = 5):
        for _ in range(max_retries):
            response = requests.get(self.hf_endpoint_url, headers=self.headers)
            if response.status_code == 503:
                print(f"Endpoint is not ready. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                return False

        raise Exception("Hugging Face endpoint is not ready. Please try again later.")
    
    def initialize_chain(self):
        chain = LLMChain()
    
    


