"""Minimal {{Framework}} × JamJet integration template.

Replace this docstring and the body below with your actual integration.
The structure below shows the canonical Pattern B shape:

    1. Define your agent using {{Framework}}'s normal API.
    2. Wrap it with @durable_agent (or equivalent) so JamJet provides
       durability/audit/HITL/policy/cost/memory underneath.
    3. Run it.
"""

from jamjet import durable_agent  # placeholder import — replace with actual
# from <framework> import Agent  # uncomment and replace


@durable_agent(name="{{framework}}-example")
def run() -> str:
    """Replace this with your integration's entrypoint."""
    # 1. Construct the {{Framework}} agent using its normal API.
    # 2. Run it.
    # 3. Return the final result.
    return "replace me"


if __name__ == "__main__":
    print(run())
