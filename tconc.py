embed

<drac2>
c = combat()
warcaster = 'warcaster' in get('feats', '').lower().replace(' ', '')
transmuter = 'con' in get('transmuter', '').lower().replace(' ', '')
args = argparse(&ARGS& + (["adv"] if warcaster else []))
effect = None

target = args.last('t', name)
self = target == name
dc = args.last('dc', 10, int)
b = args.join("b", ' + ')
adv = args.adv(boolwise=True)
bladesong = args.last('bs') if target == name else None

if c and (target := c.get_combatant(target)):
 effect     = ([eff for eff in target.effects if eff.conc] + [None])[0]
 bladesong  = bladesong or target.get_effect("Bladesong")
 sb         = ' + '.join([eff.effect.sb for eff in target.effects if 'sb' in eff.effect])
 rollString = f"{target.saves.get('constitution').d20(adv)}" +  \
             (f' + {b}' if b else '') +  \
             (f' + {sb}' if sb else '') + \
             (f''' + {target.stats.prof_bonus}[transmuter's stone]''' if transmuter else '') + \
             (f' + {max(1, (target.stats.get_mod("int")))} [bladesong]' if bladesong else '')
 concRoll   = vroll(rollString)
 success    = concRoll.total >= dc
 concOut    = f"""-title "{target.name} makes a Concentration check!"
 -desc "**DC {dc}**
 {concRoll}; {["Failure! Concentration Dropped", "Success!"][success]}" """
 if not success:
  if effect:
   concOut   = concOut[:-2] + f"""\nYou are no longer concentrating on {effect.name} and the effects have been removed." """
   if "Mind Sharpener" in get("infusions",""):
    character().set_cvar("lastEffect", dump_json([target.get_effect(effect.name).name, target.get_effect(effect.name).remaining]))
    concOut   = concOut + f"""-f "Mind Sharpener|Effect stored for Mind Sharpener Infusion." """
   target.remove_effect(effect.name)
  else:
   concOut   = concOut[:-2] + f"""\nYou weren't concentrating on a spell in init." """
elif target == name:
 target = character()
 rollString = f"{target.saves.get('constitution').d20(adv)}" +  \
             (f' + {b}' if b else '') + \
             (f' + {max(1, (target.stats.constitution-10)//2)} [bladesong]' if bladesong else '')
 concRoll   = vroll(rollString)
 success    = concRoll.total >= dc
 concOut    = f"""-title "{name} makes a Concentration check!"
 -desc "**DC {dc}**
 {concRoll}; {["failure!", "success!"][success]}" """
else:
 concOut = f"""-title "{ctx.author.name} had a brain fart."
 -desc "**Invalid target.**
 Either join initiative with `{ctx.prefix}init join`, or select a valid target with `-t <name>`." """
return concOut
</drac2>


-color <color>
{{f"-thumb {image}" if self else ""}}
