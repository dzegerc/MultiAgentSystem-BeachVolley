import spade
from spade.template import Template
from behaviors.player_behaviour import ServeBehaviour, ReceiveBehaviour, SetBehaviour, SpikeBehaviour

class PlayerAgent(spade.agent.Agent):
    def __init__(self, jid, password, team_name="Team", player_name="Player", role="server"):
        super().__init__(jid, password, verify_security=False)
        self.team_name = team_name
        self.player_name = player_name
        self.role = role 
    
    async def setup(self):
        print(f"[{self.jid}] PlayerAgent pokrenut - {self.player_name} iz {self.team_name}, role: {self.role}")
        if self.role == "server":
            behaviour = ServeBehaviour()
            template = Template()
            template.set_metadata("performative", "request")
            template.body = "SERVE_NOW"
            self.add_behaviour(behaviour, template)
        elif self.role == "receive":
            behaviour = ReceiveBehaviour()
            template = Template()
            template.set_metadata("performative", "request")
            template.body = "RECEIVE_NOW"
            self.add_behaviour(behaviour, template)
        elif self.role == "set":
            behaviour = SetBehaviour()
            template = Template()
            template.set_metadata("performative", "request")
            template.body = "SET_NOW"
            self.add_behaviour(behaviour, template)
        elif self.role == "spike":
            behaviour = SpikeBehaviour()
            template = Template()
            template.set_metadata("performative", "request")
            template.body = "SPIKE_NOW"
            self.add_behaviour(behaviour, template)
        else:
            print(f"[{self.jid}] Nepoznata role: {self.role}")

if __name__ == "__main__":
    
    agent_jid = "playera1@localhost"
    agent_password = "agenta1"
    role = "server"  
    player_agent = PlayerAgent(agent_jid, agent_password, team_name="TeamA", player_name="A1", role=role)
    future = player_agent.start()
    future.result()
    try:
        while True:
            pass 
    except KeyboardInterrupt:
        print("Prekid rada agenta...")
    finally:
        player_agent.stop()
