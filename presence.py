from pypresence import Presence
from datetime import date
from time import sleep
from random import choice

client_id = "1154405516131455068"
RPC = Presence(client_id)
RPC.connect()

dayz = (date.today() - date(2023, 7, 29)).days
descs = ["I'm a better person now",
         "My life got better",
         "I have a girlfriend now",
         "Doing something better rn"]

while True:
    #RPC.update(state=choice(descs), details=f"LoL-sober for {dayz} days :)")

    RPC.update(
        large_image=choice(["happy0", "happy1", "happy2", "happy3"]),
        large_text="REMEMBER KIDS, LOL IS BAD!",
        details=f"LoL-sober for {dayz} days :)",
        state=choice(descs),
        buttons=[{"label":"my links btw","url":"https://linktr.ee/adas_per"}, {"label":"this presence's code","url":"https://github.com/afdkapsx/python-discord-presence"}]
    )

    sleep(15)