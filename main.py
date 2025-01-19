import asyncio
from agents.player_agent import PlayerAgent
from agents.environment_agent import EnvironmentAgent

async def main():
    player1 = PlayerAgent("playera1@localhost", "agenta1", team_name="TeamA", player_name="A1", role="server")
    player2 = PlayerAgent("playera2@localhost", "agenta2", team_name="TeamA", player_name="A2", role="set")
    player3 = PlayerAgent("playerb1@localhost", "agentb1", team_name="TeamB", player_name="B1", role="receive")
    player4 = PlayerAgent("playerb2@localhost", "agentb2", team_name="TeamB", player_name="B2", role="spike")
    
    print("Pokrećem PlayerAgent-e...")
    await player1.start(auto_register=False)
    await player2.start(auto_register=False)
    await player3.start(auto_register=False)
    await player4.start(auto_register=False)
    print("PlayerAgent-i su pokrenuti.")
    
    await asyncio.sleep(3)
    
    print("Pokrećem EnvironmentAgent...")
    env_agent = EnvironmentAgent("env@localhost", "environment", team_a_name="TeamA", team_b_name="TeamB", max_points=6)
    await env_agent.start(auto_register=False)
    print("EnvironmentAgent pokrenut.")
    
    while env_agent.is_alive():
        await asyncio.sleep(1)
    
    print("Zaustavljam agente...")
    await player1.stop()
    await player2.stop()
    await player3.stop()
    await player4.stop()
    await env_agent.stop()
    print("Svi agenti zaustavljeni.")

if __name__ == '__main__':
    asyncio.run(main())
