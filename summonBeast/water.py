multiline
<drac2>
args = argparse(&ARGS&)

lev = args.last("l",2,int)
hp = 30 + ((lev - 2) * 5)
ac = 11 + lev
character().set_cvar("beastLevel",lev)

if combat():
    combat().get_combatant("Somnira").set_group("Somnira & her Beast Spirit")

</drac2>
!i madd "Water Beast" -group "Somnira & her Beast Spirit" -hp {hp} -name "Champignon" -h -ac {ac}
!embed -title "Somnira summons a Water Beast!" -f "Spell Slot|Level {lev}" -f "{ac} AC|11 + the level of the spell (natural armor)" -f "{hp} HP|30 (Land and Water only) + 5 for each spell level above 2nd" -f "**Speed**|Swim 30 ft. (Water only)" -thumb "https://pbs.twimg.com/media/Er7GzYQXYAE24Q7?format=jpg&name=orig" -f "**Pack Tactics (Land and Water Only).**| The beast has advantage on an attack roll against a creature if at least one of the beast’s allies is within 5 feet of the creature and the ally isn’t incapacitated." -f "**Water Breathing (Water Only).**|The beast can breathe only underwater." -f "**Multiattack: {{floor(lev/2)}} Attack(s)**|The beast makes a number of attacks equal to half this spell’s level (rounded down)." -f "**Maul.** To Hit: +{wisdomMod + proficiencyBonus}, Damage: 1d8+{{4+lev}} Piercing| *Melee Weapon Attack*: your spell attack modifier to hit ({wisdomMod + proficiencyBonus}), reach 5 ft., one target. Hit: 1d8 + 4 + the spell’s level piercing damage." -f "https://www.dndbeyond.com/spells/summon-beast"
