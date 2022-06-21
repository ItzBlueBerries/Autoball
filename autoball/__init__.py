import random

normal = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]

uwu = ["As i see iwt, yes.", "ask again watew.", "bettew nowt teww uwu now.", "cannot pwedict now.", "concentwate awnd awsk again.", "don’t count own iwt.", "it iws cewtain.", "it iws decidedwy so.", "most wikewy.", "my wepwy iws no.", "my souwces say no.", "outwook nowt so good.", "outwook good.", "wepwy hazy, twy again.", "signs point tuwu yes.", "vewy doubtfuw.", "without a doubt.", "yes.", "yes – definitewy.", "you may wewy own iwt."]

custom = []

class Auto:

  def randoball(ver):
    if ver == "normal":
      return random.choice(normal)
    elif ver == "uwu":
      return random.choice(uwu)