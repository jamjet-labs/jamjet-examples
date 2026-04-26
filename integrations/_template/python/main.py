"""Minimal {{Framework}} × JamJet integration template.

Replace this docstring and the body below with your actual integration.
The structure below shows the canonical Pattern B shape:

    1. Define your agent using {{Framework}}'s normal API.
    2. Wrap calls in a JamJet @workflow.step so each step is checkpointed —
       on crash + restart, JamJet replays from the last completed step
       instead of re-running everything.
    3. Run it.

For the full SDK, see https://github.com/jamjet-labs/jamjet.
"""

from pydantic import BaseModel

from jamjet import Workflow

# from <framework> import Agent  # uncomment and replace with your framework's import

workflow = Workflow("{{framework}}-example")


@workflow.state
class State(BaseModel):
    query: str
    result: str | None = None


@workflow.step
async def run(state: State) -> State:
    """Replace this with your integration's entrypoint.

    1. Construct the {{Framework}} agent using its normal API.
    2. Run it against `state.query`.
    3. Return `state.model_copy(update={"result": ...})`.
    """
    return state.model_copy(update={"result": "replace me"})


if __name__ == "__main__":
    import asyncio

    initial = State(query="hello world")
    final = asyncio.run(run(initial))
    print(final.result)
