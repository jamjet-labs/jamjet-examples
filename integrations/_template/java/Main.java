import dev.jamjet.runtime.instrument.annotations.Checkpoint;
import dev.jamjet.runtime.instrument.annotations.DurableAgent;

/**
 * Minimal {{Framework}} × JamJet integration template.
 *
 * Replace this whole class body with your actual integration. The structure
 * below shows the canonical Pattern B shape:
 *
 *   1. Annotate the class with @DurableAgent — JamJet instruments it for
 *      replay-or-execute durability.
 *   2. Mark steps that should be checkpointed with @Checkpoint — completed
 *      steps are skipped on replay after a crash, so you don't re-pay for
 *      prior LLM/tool calls.
 *   3. Call your {{Framework}} agent inside a @Checkpoint method.
 *
 * For the runtime, see https://github.com/jamjet-labs/jamjet-runtime-java.
 */
@DurableAgent("{{framework}}-example")
public class Main {

    public static void main(String[] args) {
        Main agent = new Main();
        String result = agent.run("hello world");
        System.out.println(result);
    }

    @Checkpoint
    public String run(String query) {
        // 1. Construct the {{Framework}} agent using its normal API.
        // 2. Run it against `query`.
        // 3. Return the final result.
        return "replace me";
    }
}
