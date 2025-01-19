import spade
import asyncio
from spade.message import Message

class ManageGameStateBehaviour(spade.behaviour.CyclicBehaviour):
    async def run(self):
        env_obj = self.agent.env

       
        if not env_obj.ball_in_play:
            serve_agent_jid = "playera1@localhost"  
            msg = Message(to=serve_agent_jid)
            msg.set_metadata("performative", "request")
            msg.body = "SERVE_NOW"
            print(f"[EnvironmentAgent] Šaljem poruku {msg.body} -> {serve_agent_jid}")
            await self.send(msg)
            env_obj.ball_in_play = True
            env_obj.phase = "SERVE_WAIT"
        
        elif env_obj.phase == "SERVE_WAIT":
            msg = await self.receive(timeout=1)
            if msg:
                print(f"[EnvironmentAgent] Primljena poruka (SERVE faza): {msg.body}")
                if msg.body == "SERVE_DONE":
                    env_obj.phase = "RECEIVE"
                    receiver_jid = "playerb1@localhost"
                    out_msg = Message(to=receiver_jid)
                    out_msg.set_metadata("performative", "request")
                    out_msg.body = "RECEIVE_NOW"
                    print(f"[EnvironmentAgent] Šaljem poruku {out_msg.body} -> {receiver_jid}")
                    await self.send(out_msg)
                elif msg.body == "SERVE_FAULT":
                    print("[EnvironmentAgent] Servis fault – poen za protivnički tim!")
                    env_obj.update_score(env_obj.team_b)
                    env_obj.print_score()
                    env_obj.reset_round()
        
        elif env_obj.phase == "RECEIVE":
            msg = await self.receive(timeout=1)
            if msg:
                print(f"[EnvironmentAgent] Primljena poruka (RECEIVE faza): {msg.body}")
                if msg.body == "RECEIVE_DONE":
                    env_obj.phase = "SET"
                    set_agent_jid = "playera2@localhost"
                    out_msg = Message(to=set_agent_jid)
                    out_msg.set_metadata("performative", "request")
                    out_msg.body = "SET_NOW"
                    print(f"[EnvironmentAgent] Šaljem poruku {out_msg.body} -> {set_agent_jid}")
                    await self.send(out_msg)
                elif msg.body == "RECEIVE_ERROR":
                    print("[EnvironmentAgent] Prijem neuspješan – poen za servisni tim!")
                    env_obj.update_score(env_obj.team_a)
                    env_obj.print_score()
                    env_obj.reset_round()
        
        elif env_obj.phase == "SET":
            msg = await self.receive(timeout=1)
            if msg:
                print(f"[EnvironmentAgent] Primljena poruka (SET faza): {msg.body}")
                if msg.body == "SET_DONE":
                    env_obj.phase = "SPIKE"
                    spike_agent_jid = "playerb2@localhost"
                    out_msg = Message(to=spike_agent_jid)
                    out_msg.set_metadata("performative", "request")
                    out_msg.body = "SPIKE_NOW"
                    print(f"[EnvironmentAgent] Šaljem poruku {out_msg.body} -> {spike_agent_jid}")
                    await self.send(out_msg)
                elif msg.body == "SET_ERROR":
                    print("[EnvironmentAgent] Set error – poen za protivnički tim!")
                    env_obj.update_score(env_obj.team_a)
                    env_obj.print_score()
                    env_obj.reset_round()
        
        elif env_obj.phase == "SPIKE":
            msg = await self.receive(timeout=1)
            if msg:
                print(f"[EnvironmentAgent] Primljena poruka (SPIKE faza): {msg.body}")
                if msg.body == "SPIKE_DONE":
                    print("[EnvironmentAgent] Smeč uspješan – poen za napadački tim!")
                    env_obj.update_score(env_obj.team_b)
                elif msg.body == "SPIKE_ERROR":
                    print("[EnvironmentAgent] Smeč error – poen za obrambeni tim!")
                    env_obj.update_score(env_obj.team_a)
                
              
                set_winner = env_obj.check_set_winner()
                if set_winner:
                    print(f"[EnvironmentAgent] Set osvojen od strane tima: {set_winner}")
                    if set_winner == env_obj.team_a:
                        env_obj.sets_team_a += 1
                    else:
                        env_obj.sets_team_b += 1
                    env_obj.print_score()
                    env_obj.reset_set()
                    
                    match_winner = env_obj.get_match_winner()
                    if match_winner:
                        print(f"[EnvironmentAgent] Utakmica je završena! Pobjednik: {match_winner}")
                        await self.agent.stop()
                        return
                env_obj.reset_round()
        await asyncio.sleep(2)
