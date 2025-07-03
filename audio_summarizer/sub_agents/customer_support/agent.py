from google.adk.agents import Agent
from . import prompt


customer_support_agent = Agent(
    model='gemini-2.5-pro',
    name='customer_support_agent',
    description='A helpful assistant for user questions.',
    instruction=prompt.CUSTOMER_SUPPORT,
)
