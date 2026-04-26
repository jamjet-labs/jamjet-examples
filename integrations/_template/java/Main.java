import dev.jamjet.runtime.DurableAgent;

/**
 * Minimal {{Framework}} × JamJet integration template.
 *
 * Replace this whole class body with your actual integration. The structure
 * below shows the canonical Pattern B shape:
 *
 *   1. Define your agent using {{Framework}}'s normal API.
 *   2. Annotate with @DurableAgent (or equivalent) so JamJet provides
 *      durability/audit/HITL/policy/cost/memory underneath.
 *   3. Run it.
 */
@DurableAgent(name = "{{framework}}-example")
public class Main {
    public static void main(String[] args) {
        // 1. Construct the {{Framework}} agent using its normal API.
        // 2. Run it.
        // 3. Print the final result.
        System.out.println("replace me");
    }
}
