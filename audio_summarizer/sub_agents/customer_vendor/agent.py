from google.adk.agents import Agent
from . import prompt


customer_vendor_agent = Agent(
    model='gemini-2.5-pro',
    name='customer_vendor_agent',
    description='A helpful assistant for user questions.',
    instruction=prompt.CUSTOMER_VENDOR,
)
