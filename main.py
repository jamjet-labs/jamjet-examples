"""LangChain × JamJet integration example showing a durable agent workflow.

1. Defines a standard LangChain tool and agent.
2. Wraps the execution block inside a JamJet `@workflow.step` using Pydantic state models.
3. Saves expensive LLM token costs and API calls by checkpointing mid-run states.
"""

import os
import asyncio
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain.agents import AgentExecutor, create_openai_tools_agent

from jamjet import Workflow

# 1. Initialize the JamJet workflow wrapper
workflow = Workflow("langchain-example")


# 2. Define the exact state structure expected by JamJet
@workflow.state
class State(BaseModel):
    query: str
    result: str | None = None


# 3. Setup a mock tool to verify durability and agent execution
@tool
def calculate_square(num: int) -> int:
    """Calculates the square of a given number."""
    return num * num


# 4. The main checkpoint step where JamJet handles durability
@workflow.step
async def run(state: State) -> State:
    """Constructs the LangChain agent and executes the user's query state."""
    
    # Check for API key at runtime inside the step execution
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("Missing OPENAI_API_KEY environment variable.")

    # Define LangChain LLM and tool primitives
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [calculate_square]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Always use your square tool if a number is given."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    # Compile the standard LangChain AgentExecutor 
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    # Execute the agent synchronously inside the async thread pool wrapper
    # (Since LangChain invoke runs synchronously by default here)
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None, 
        lambda: agent_executor.invoke({"input": state.query})
    )
    
    # Return the updated state context exactly as JamJet expects
    return state.model_copy(update={"result": response["output"]})


if __name__ == "__main__":
    # Ensure local environment setup validation before execution
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: Please set your OPENAI_API_KEY before running.")
        print("Example: export OPENAI_API_KEY=sk-...")
        exit(1)

    # Triggering the workflow execution simulation
    initial = State(query="Calculate the square of 25 and append the word 'Done' to it.")
    final = asyncio.run(run(initial))
    
    print("\n--- JamJet Final Result ---")
    print(final.result)