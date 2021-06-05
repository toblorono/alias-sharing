multiline
<drac2>
args = argparse(&ARGS&)

lev = args.last("l",2,int)
hp = 20 + ((lev - 2) * 5)
ac = 11 + lev
character().set_cvar("beastLevel",lev)

if combat():
    combat().get_combatant("Somnira").set_group("Somnira & her Beast Spirit")

</drac2>
!i madd "Land Beast" -group "Somnira & her Beast Spirit" -hp {hp} -name "Shiitake" -h -ac {ac}
!embed -title "Somnira summons an Air Beast!" -f "Spell Slot|Level {lev}" -f "{ac} AC|11 + the level of the spell (natural armor)" -f "{hp} HP|20 (Air only) + 5 for each spell level above 2nd" -f "**Speed**|Fly 60 ft. (Air only)" -thumb "https://pbs.twimg.com/media/Er7GzYWXIAcgKN2?format=jpg&name=orig" -f "**Flyby (Air Only).** The beast doesn’t provoke opportunity attacks when it flies out of an enemy’s reach."  -f "**Multiattack: {{floor(lev/2)}} Attack(s)**|The beast makes a number of attacks equal to half this spell’s level (rounded down)." -f "**Maul.** To Hit: +{wisdomMod + proficiencyBonus}, Damage: 1d8+{{4+lev}} Piercing| *Melee Weapon Attack*: your spell attack modifier to hit ({wisdomMod + proficiencyBonus}), reach 5 ft., one target. Hit: 1d8 + 4 + the spell’s level piercing damage." -f "https://www.dndbeyond.com/spells/summon-beast"
