#main agent
from google.adk.agents import Agent
from . import prompt

from .sub_agents.customer_lms import customer_lms_agent
from .sub_agents.customer_support import customer_support_agent
from .sub_agents.customer_vendor import customer_vendor_agent

class ReadFileTool(PythonTool):
    name = "read_file"
    description = "Reads a file from local filesystem and returns its contents."

    def call(self, file_path: str) -> str:
        with open(file_path, 'r') as f:
            return f.read()


audio_summarizer = Agent(
    model='gemini-2.5-pro',
    name='audio_summarizer',
    description='A helpful assistant for user questions.',
    instruction=prompt.LMS_PROMPT,
    sub_agents = [customer_lms_agent, customer_support_agent, customer_vendor_agent]
)

root_agent = audio_summarizer
