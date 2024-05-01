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

def get_prompt(prompt_id: str) -> str:
    PROMPT_MAP.get(prompt_id)