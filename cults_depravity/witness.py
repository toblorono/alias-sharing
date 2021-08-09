embed
<drac2>
args, c, n, f = argparse(&ARGS&), combat(), "\n", ""

combatants = args.get("t")

for targ in combatants:
    if cb := c.get_combatant(targ):
        if e := cb.get_effect("Cult's Depravity"):
            stacks = int(e.name[18:])+1
            cb.remove_effect("Cult's Depravity")
        else:
            stacks = 1
        if "clear" not in args:
            cb.add_effect(f"Cult's Depravity: {stacks}", "")
            adj = "Witnessed"
        else:
            stacks = "Absolved"
            adj = "Shaken"
        f = f + f"""-f "{cb.name}|Cult's Depravity: {stacks}{n}" """
    else:
        f = f + f""" -f "{targ}|Combatant not found." """

</drac2>
-title "The Flesh Mound's Depravity is {{adj}}!" 
-desc "Any creature within 60 feet that can see the Flesh Mound must make a DC 14 intelligence Saving throw or take 7 (2d6) psychic damage and gain 1 stack of the Cult's Depravity as it is assailed with horrible visions of the cult's sacrifices in the ritual chamber. The target takes half damage and is not afflicted by a Cult's Depravity stack on a successful save. {{n}}{{n}}Any target afflicted by the Cult's Depravity takes 1d4 psychic damage at the start of its turn, which increases by 1d4 damage per stack accumulated. An afflicted target can use their action to shake these visions entirely and eliminate all existing stacks of the Cult's Depravity." 
-thumb <image> 
{{f}} 
-footer "Usage: !witness [clear] -t [targ1] -t [targ2] ... -t [targN]"
