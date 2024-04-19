from openai import OpenAI

class DocumentAnalystAssistant():
    def __init__(self):
        pass
        #client = OpenAI(
        #    organization='YOUR_ORG_ID',
        #    project='$PROJECT_ID',
        #)
        
        #self.assistant = client.beta.assistants.create(
        #    name="Document Analyst Assistant",
        #    instructions="You are an document analyst. Use you knowledge base to answer questions about that.",
        #    model="gpt-4-turbo",
        #    tools=[{"type": "file_search"}],
        #)
        
    def analyseDocument(self, prompt: str, docs: list):
        return "This is a test, your prompt is: " + prompt