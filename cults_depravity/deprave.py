embed
<drac2>
args, c, n, f, fT = argparse(&ARGS&), combat(), "\n", "", ""

combatants = args.get("t")

for targ in combatants:
    if cb := c.get_combatant(targ):
        if e := cb.get_effect("Cult's Depravity"):
            stacks = int(e.name[18:])
            r = vroll(f"{stacks}d4[psychic]")
            cb.damage(r.total)
            f = f + f""" -f "{cb.name}|**Damage:** {r.result}" """
            fT = fT + f"""{cb.name}: {cb.hp_str()}{n}"""
        else:
            f = f + f""" -f "{cb.name}|No stacks of Cult's Depravity found!" """
    else:
        fT = fT + f"""{targ}: Combatant not found{n}"""
</drac2>

-title "The Flesh Mound's Depravity is Inflicted!" 
-desc "Any target afflicted by the Cult's Depravity takes 1d4 psychic damage at the start of its turn, which increases by 1d4 damage per stack accumulated. An afflicted target can use their action to shake these visions entirely and eliminate all existing stacks of the Cult's Depravity." 
-thumb <image> 
{{f}} 
-footer "{{fT}} Usage: !deprave -t [targ1] -t [targ2] ... -t [targN]"
