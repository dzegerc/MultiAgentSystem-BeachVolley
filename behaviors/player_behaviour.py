import asyncio
import random
from spade.behaviour import CyclicBehaviour
from spade.message import Message


class ServeBehaviour(CyclicBehaviour):
    async def run(self):
        try:
            msg = await self.receive(timeout=1)
            if msg:
                print(f"[{self.agent.jid} - SERVER] Prima poruku: {msg.body}")
               
                if random.random() < 0.9:
                    outcome = "SERVE_DONE"
                    print(f"[{self.agent.jid} - SERVER] Servis uspješan.")
                else:
                    outcome = "SERVE_FAULT"
                    print(f"[{self.agent.jid} - SERVER] Servis neuspješan (fault).")
                
               
                response = Message(to="env@localhost")
                response.set_metadata("performative", "inform")
                response.body = outcome
                await self.send(response)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"[{self.agent.jid} - SERVER] Greška: {e}")


class ReceiveBehaviour(CyclicBehaviour):
    async def run(self):
        try:
            msg = await self.receive(timeout=1)
            if msg:
                print(f"[{self.agent.jid} - RECEIVE] Prima poruku: {msg.body}")
               
                if random.random() < 0.85:
                    outcome = "RECEIVE_DONE"
                    print(f"[{self.agent.jid} - RECEIVE] Prijem uspješan.")
                else:
                    outcome = "RECEIVE_ERROR"
                    print(f"[{self.agent.jid} - RECEIVE] Prijem neuspješan.")
                
                response = Message(to="env@localhost")
                response.set_metadata("performative", "inform")
                response.body = outcome
                await self.send(response)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"[{self.agent.jid} - RECEIVE] Greška: {e}")

class SetBehaviour(CyclicBehaviour):
    async def run(self):
        try:
            msg = await self.receive(timeout=1)
            if msg:
                print(f"[{self.agent.jid} - SET] Prima poruku: {msg.body}")
                if random.random() < 0.9:
                    outcome = "SET_DONE"
                    print(f"[{self.agent.jid} - SET] Set uspješan.")
                else:
                    outcome = "SET_ERROR"
                    print(f"[{self.agent.jid} - SET] Set neuspješan")
                
                response = Message(to="env@localhost")
                response.set_metadata("performative", "inform")
                response.body = outcome
                await self.send(response)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"[{self.agent.jid} - SET] Greška: {e}")

class SpikeBehaviour(CyclicBehaviour):
    async def run(self):
        try:
            msg = await self.receive(timeout=1)
            if msg:
                print(f"[{self.agent.jid} - SPIKE] Prima poruku: {msg.body}")
                if random.random() < 0.8:
                    outcome = "SPIKE_DONE"
                    print(f"[{self.agent.jid} - SPIKE] Smeč uspješan.")
                else:
                    outcome = "SPIKE_ERROR"
                    print(f"[{self.agent.jid} - SPIKE] Smeč neuspješan.")
                
                response = Message(to="env@localhost")
                response.set_metadata("performative", "inform")
                response.body = outcome
                await self.send(response)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"[{self.agent.jid} - SPIKE] Greška: {e}")
