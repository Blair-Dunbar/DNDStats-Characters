from __future__ import print_function
from Tkinter import *
import random
import tkinter.messagebox


final=' '

Gender = ('Female', 'Male') # 2 Items
Race = ('Changling', 'Dragonborn', 'Dwarf', 'Elf', 'Gith', 'Gnome', 'Halfling', 'Human', 'Minotaur', 'Orc', 'Shifter', 'Teifling', 'Tortle', 'Warforged') #14 Items
Class = ('Artificer','Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Mystic','Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard') #14 Items
    #^^^ ABOVE SECTION ARE GENDER, RACE, AND CLASS LISTS TO BE SELECTED FROM FOR EACH GENDER, RACE, AND CLASS ^^^
        
# ChangelingSubrace = No Subraces
DragonbornSubrace = ('Black Dragon', 'Blue Dragon', 'Brass Dragon', 'Bronze Dragon', 'Copper Dragon', 'Gold Dragon', 'Green Dragon', 'Red Dragon', 'Silver Dragon', 'White Dragon') #10 Items
DwarfSubrace = ('Hill Dwarf', 'Grey Dwarf (Duergar)', 'Mountain Dwarf') #3 Items
ElfSubrace = ('Avariel', 'Dark-Elf (Drow)', 'Eladrin', 'Grugach', 'Half-Elf', 'High-Elf', 'Sea-Elf', 'Shadar-kai', 'Wood-Elf') #9 items
GithSubrace = ('Githyanki', 'Githzerai') #2 Items
GnomeSubrace = ('Deep Gnome (Svirfneblin)', 'Forest Gnome', 'Rock Gnome') #3 Items
HalflingSubrace = ('Lightfoot Halfling', 'Stout Halfling') #2 Items
HumanSubrace = ('Aquatic Human', 'Standard Human') #2 Items
# MinotaurSubrace = No Subraces
OrcSubrace = ('Half-Orc', 'Half-Orc') #2 Items
ShifterSubrace = ('Beasthide', 'Cliffwalk', 'Longstrider', 'Longtooth', 'Razorclaw', 'Wildhunt') #6 Items
TieflingSubrace = ('Abyssal Tiefling', 'Infernal Tiefling') #2 Items
# TortleSubrace = No Subraces
WarforgedSubrace = ('Composite Warforged', 'Metal Warforged', 'Wooden Warforged') #3 Items
   #^^^ ABOVE SECTION ARE SUBRACE LISTS TO BE SELETCTED FROM FOR EACH RACE ^^^

ArtificerSubclass = ('Alchemy', 'Gunsmith') #2 Items
BarbarianSubclass = ('Path of the Ancestral Guardian', 'Path of the Battlerager (Dwarves only)', 'Path of the Berserker', 'Path of the Storm Herald', 'Path of the Totem Warrior', 'Path of the Zealot') #6 Items
BardSubclass = ('College of Glamour', 'College of Lore', 'College of Satire', 'College of Swords', 'College of Valor', 'College of Whispers') #6 Items
ClericSubclass = ('Ambition', 'Arcana', 'Death', 'Forge', 'Grave', 'Knowledge', 'Life', 'Light', 'Nature', 'Order', 'Protection', 'Solidarity', 'Strength', 'Tempest', 'Trickery', 'War', 'Zeal') #17 Items
DruidSubclass = ('Circle of Dreams', 'Circle of the Land', 'Circle of the Moon', 'Circle of the Shepherd', 'Circle of Twilight', 'Circle of Spores') #6 Items
FighterSubclass = ('Arcane Archer', 'Purple Dragon Knight', 'Battle Master', 'Cavalier', 'Champion', 'Eldritch Knight', 'Knight', 'Samurai', 'Sharpshooter', 'Brute') #10 Items
MonkSubclass = ('Way of the Drunken Master', 'Way of the Four Elements', 'Way of the Kensei', 'Way of the Long Death', 'Way of the Open Hand', 'Way of Shadow', 'Way of the Sun Soul', 'Way of Tranquility') #8 Items
MysticSubclass = ('Order of the Avatar', 'Order of the Awakened', 'Order of the Immortal', 'Order of the Nomad', 'Order of the Soul Knife', 'Order of the Wu Jen') #6 Items
PaladinSubclass = ('Oath of the Ancients', 'Oath of Conquest', 'Oath of the Crown', 'Oath of Devotion', 'Oath of Redemption', 'Oath of Treachery', 'Oath of Vengeance', 'Oathbreaker') #8 Items
RangerSubclass = ('Beast Master', 'Gloom Stalker', 'Horizon Walker', 'Hunter', 'Monster Slayer', 'Primeval Guardian') #6 Items
RogueSubclass = ('Arcane Trickster', 'Assassin', 'Inquisitive',  'Mastermind', 'Scout', 'Swashbuckler', 'Thief') #7 Items
SorcererSubclass = ('Divine Soul', 'Draconic Bloodline', 'Phoenix Sorcery', 'Sea Sorcery', 'Shadow Magic', 'Stone Sorcery', 'Storm Sorcery', 'Wild Magic') #8 Items
WarlockSubclass = ('The Archfey', 'The Celestial', 'The Fiend', 'The Great Old One', 'The Hexblade', 'The Raven Queen', 'The Seeker', 'The Undying') #8 Items
WizardSubclass = ('Bladesinging', 'Lore Mastery', 'School of Abjuration', 'School of Conjuration', 'School of Divination', 'School of Enchantment', 'School of Evocation', 'School of Illusion', 'School of Necromancy', 'School of Transmutation', 'School of Invention', 'Theurgy', 'War Magic') #13 Items
    #^^^ ABOVE SECTION ARE SUBCLASS LISTS TO BE SELECTED FROM FOR EACH CLASS


def dndrc():
    r1 = random.randint(0,13)
    r2 = random.randint(0,1)
    r3 = random.randint(0,13) 
    #r1-r3 generate the random integers for Race, Gender, and Class 
    
    # changelingsubr = random.randint(0,1)
    dragsubr = random.randint(0,9)
    dwarfsubr = random.randint(0,2)
    elfsubr = random.randint(0,4)
    githsubr = random.randint(0,1)
    gnomesubr = random.randint(0,2)
    halflingsubr = random.randint(0,1)
    humansubr = random.randint(0,1)
    # minotaursubr = random.randint(0,1)
    orcsubr = random.randint(0,1)
    shiftersubr = random.randint(0,5)
    tieflingsubr = random.randint(0,1)
    # tortlesubr = random.randint(0,1)
    warforgedsubr = random.randint(0,2)
        #Subrace Random generation based on race

        #r1-r3 generate random integers for selection of race, gender, and class
    r = Race[r1]
    g = Gender[r2]
    c = Class[r3]
    
    ###This is the area that compiles all the random integers and 
    # There are no Changeling subraces
    dbsr = DragonbornSubrace[dragsubr]
    dwsr = DwarfSubrace[dwarfsubr]
    esr = ElfSubrace[elfsubr]
    gsr = GithSubrace[githsubr]
    gnsr = GnomeSubrace[gnomesubr]
    hlsr = HalflingSubrace[halflingsubr]
    husr = HumanSubrace[humansubr]
    # There are no Minotaur subraces
    osr = OrcSubrace[orcsubr]
    ssr = ShifterSubrace[shiftersubr]
    tlsr = TieflingSubrace[tieflingsubr]
    # There are no Tortle subraces
    wfsr = WarforgedSubrace[warforgedsubr]

    Final = g + r + c
    print (g, r, c)
    
    
    #Subraces
    if r1 == 0:
        print ('There are no Changeling Subraces')
    if r1 == 1:
        print ('Dragonborn Subrace is ' + dbsr)
    if r1 == 2:
        print ('Dwarven Subrace is ' + dwsr)
    if r1 == 3:
        print ('Elven Subrace is ' + esr)
    if r1 == 4:
        print ('Gith Subrace is ' + gsr)
    if r1 == 5:
        print ('Gnome Subrace is ' + gnsr)
    if r1 == 6:
        print ('Halfling Subrace is ' + hlsr)
    if r1 == 7:
        print ('Human Subrace is ' + husr)
    if r1 == 8:
        print ('There are no Minotaur Subraces')
    if r1 == 9:
        print ('Orc Subrace is ' + osr)
    if r1 == 10:
        print ('Shifter Subrace is ' + ssr)    
    if r1 == 11:
        print ('Teifling Subrace is ' + tlsr)
    if r1 == 12:
        print ('There are no Tortle Subraces')
    if r1 == 13:
        print ('Warforged Subrace is ' + wfsr)
   
    artificersubc = random.randint(0,1)
    barbariansubc = random.randint(0,5) 
    bardsubc = random.randint(0,5)
    clericsubc = random.randint(0,16)
    druidsubc = random.randint(0,5)
    fightersubc = random.randint(0,9)
    monksubc = random.randint(0,7)
    mysticsubc = random.randint(0,5)
    paladinsubc = random.randint(0,7)
    rangersubc = random.randint(0,5)
    roguesubc = random.randint(0,6)
    sorcerersubc = random.randint(0,7)
    warlocksubc = random.randint(0,7)
    Wizardsubc = random.randint(0,12)
    
    artsc = ArtificerSubclass[artificersubc]
    bbsc = BarbarianSubclass[barbariansubc]
    bdsc = BardSubclass[bardsubc]
    clsc = ClericSubclass[clericsubc]
    drsc = DruidSubclass[druidsubc]
    fsc = FighterSubclass[fightersubc]
    msc = MonkSubclass[monksubc]
    mysc = MysticSubclass[mysticsubc]
    palsc = PaladinSubclass[paladinsubc]
    rngsc = RangerSubclass[rangersubc]
    rosc = RogueSubclass[roguesubc]
    scsc = SorcererSubclass[sorcerersubc]
    warsc = WarlockSubclass[warlocksubc]
    wizsc = WizardSubclass[Wizardsubc]
    #Subclasses
    if r3 == 0:
        print ('Artificer Specialty is ' + artsc)
    if r3 == 1:
        print ('Barbarian Path is ' + bbsc)
    if r3 == 2:
        print ('Bard College is ' + bdsc)
    if r3 == 3:
        print ('Cleric Domain is ' + clsc)
    if r3 == 4:
        print ('Druid Circle is ' + drsc)
    if r3 == 5:
        print ('Fighter Archetype is ' + fsc)
    if r3 == 6:
        print ('Monk Subclass is ' + msc)
    if r3 == 7:
        print ('Mystic Order is the ' + mysc)
    if r3 == 8:
        print ('Paladin Oath is the ' + palsc)
    if r3 == 9:
        print ('Ranger Subclass is ' + rngsc)
    if r3 == 10:
        print ('Rogue Archetype is ' + rosc)
    if r3 == 11:
        print ('Sorcerer Bloodline is ' + scsc)
    if r3 == 12:
        print ('Warlock Patron is ' + warsc)
    if r3 == 13:
        print ('Wizard Specialization is ' + wizsc)

def display_dndrc():
    final = retrieve_dndrc()
    tkinter.messagebox.showinfo('Your Character is a...', text = final)
    
def retrieve_dndrc():
    return dndrc()

root = Tk()

text = Label(root, text='Click generate to\nmake a random\nDungeons and Dragons\nCharacter')
text.pack()

Button = Button(root, text='Generate', command = display_dndrc())
Button.pack()

root.title('AutoGen')
root.geometry('250x100+720+250') 
root.resizable(0, 0) 

root.mainloop()