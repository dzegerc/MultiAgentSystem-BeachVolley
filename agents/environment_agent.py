import spade
from behaviors.environment_behaviour import ManageGameStateBehaviour
from environment.volley_environment import BeachVolleyballEnvironment

class EnvironmentAgent(spade.agent.Agent):
    def __init__(self, jid, password, team_a_name="TeamA", team_b_name="TeamB", max_points=16):
        super().__init__(jid, password, verify_security=False)
        self.env = BeachVolleyballEnvironment(team_a_name, team_b_name, max_points)

    async def setup(self):
        try:
            print(f"[{self.jid}] EnvironmentAgent pokrenut (prije registracije behaviour-a).")
            self.add_behaviour(ManageGameStateBehaviour())
            print(f"[{self.jid}] Behaviour uspješno dodan.")
        except Exception as e:
            print(f"[{self.jid}] Greška u setup(): {e}")

if __name__ == "__main__":
    
    import asyncio
    agent_jid = "env@localhost"
    agent_password = "environment"
    environment_agent = EnvironmentAgent(agent_jid, agent_password)
    future = environment_agent.start()
    future.result()
    try:
        while True:
            asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Prekid rada agenta...")
    finally:
        environment_agent.stop()
