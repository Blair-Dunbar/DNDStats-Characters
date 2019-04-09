from __future__ import print_function
from Tkinter import *
import random
import tkinter.messagebox

''' GENDERS, RACES, AND CLASSES AVAILABLE'''


Gender = ('Female', 'Male') # 2 Items
Race = ('Changling', 'Dragonborn', 'Dwarf', 'Elf', 'Gith', 'Gnome', 'Halfling', 'Human', 'Minotaur', 'Orc', 'Shifter', 'Teifling', 'Tortle', 'Warforged') #14 Items
Class = ('Artificer','Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Mystic','Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard') #14 Items
    #^^^ ABOVE SECTION ARE GENDER, RACE, AND CLASS LISTS TO BE SELECTED FROM FOR EACH GENDER, RACE, AND CLASS ^^^
  
''' RACES AND THEIR SUBRACES AVAILABLE '''      
              
                          
# ChangelingSubrace = No Subraces
DragonbornSubrace = ('Black Dragon', 'Blue Dragon', 'Brass Dragon', 'Bronze Dragon', 'Copper Dragon', 'Gold Dragon', 'Green Dragon', 'Red Dragon', 'Silver Dragon', 'White Dragon') #10 Items
DwarfSubrace = ('Hill Dwarf', 'Grey Dwarf (Duergar)', 'Mountain Dwarf') #3 Items
ElfSubrace = ('Avariel', 'Dark-Elf (Drow)', 'Eladrin', 'Grugach', 'Half-Elf', 'High-Elf', 'Sea-Elf', 'Shadar-kai', 'Wood-Elf') #9 items
GithSubrace = ('Githyanki', 'Githzerai') #2 Items
GnomeSubrace = ('Deep Gnome (Svirfneblin)', 'Forest Gnome', 'Rock Gnome') #3 Items
HalflingSubrace = ('Lightfoot Halfling', 'Stout Halfling') #2 Items
HumanSubrace = ('Human', 'Human') #2 Items
# MinotaurSubrace = No Subraces
OrcSubrace = ('Half-Orc', 'Orc') #2 Items
ShifterSubrace = ('Beasthide', 'Cliffwalker', 'Longstrider', 'Longtooth', 'Razorclaw', 'Wildhunt') #6 Items
TieflingSubrace = ('Abyssal Tiefling', 'Infernal Tiefling') #2 Items
# TortleSubrace = No Subraces
WarforgedSubrace = ('Composite Warforged', 'Metal Warforged', 'Wooden Warforged') #3 Items
   #^^^ ABOVE SECTION ARE SUBRACE LISTS TO BE SELETCTED FROM FOR EACH RACE ^^^


''' CLASSES AND THEIR SUBCLASSES AVAILABLE '''

ArtificerSubclass = ('Alchemy', 'Gunsmithing') #2 Items
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
WizardSubclass = ('Bladesinging', 'Lore Mastery', 'The School of Abjuration', 'The School of Conjuration', 'The School of Divination', 'The School of Enchantment', 'The School of Evocation', 'The School of Illusion', 'The School of Necromancy', 'The School of Transmutation', 'The School of Invention', 'Theurgy', 'War Magic') #13 Items
    #^^^ ABOVE SECTION ARE SUBCLASS LISTS TO BE SELECTED FROM FOR EACH CLASS


''' DNDRC_OVERVIEW CREATES THE RACE, GENDER, AND CLASS FOR THE FIRST BUTTON '''

def dndrc_Overview():
    r1 = random.randint(0,13)
    r2 = random.randint(0,1)
    r3 = random.randint(0,13) 
    #r1-r3 generate the random integers for Race, Gender, and Class 
    


        #r1-r3 generate random integers for selection of race, gender, and class
    r = Race[r1]
    g = Gender[r2]
    c = Class[r3]
    
   
    return (g, r, c)
 
''' DNDRC_GENDER CREATES THE GENDER FOR THE SECOND BUTTON BUTTON '''
      
def dndrc_Gender():
    r = random.randint(0,1)
    g = Gender[r]
    
    return (g)

''' DNDRC_SUBR CREATES THE RACE AND SUBRACE FOR THE THIRD BUTTON ''' 
      
def dndrc_Subr():
    r1 = random.randint(0,13)

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

    #Subraces
    if r1 == 0:
        return ('Changeling')
    if r1 == 1:
        return (dbsr)
    if r1 == 2:
        return (dwsr)
    if r1 == 3:
        return (esr)
    if r1 == 4:
        return (gsr)
    if r1 == 5:
        return (gnsr)
    if r1 == 6:
        return (hlsr)
    if r1 == 7:
        return (husr)
    if r1 == 8:
        return ('Minotaur')
    if r1 == 9:
        return (osr)
    if r1 == 10:
        return (ssr + ' Shifter')    
    if r1 == 11:
        return (tlsr)
    if r1 == 12:
        return ('Tortle')
    if r1 == 13:
        return (wfsr)
   
''' DNDRC_SUBC CREATES THE CLASS AND SUBCLASS FOR THE LAST BUTTON '''
        
def dndrc_Subc():

    r3 = random.randint(0,13) 
   
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
        return ('Artificer Specializing in ' + artsc)
    if r3 == 1:
        return ('Barbarian of the ' + bbsc)
    if r3 == 2:
        return ('Bard of the ' + bdsc)
    if r3 == 3:
        return (clsc + ' Domain Cleric' )
    if r3 == 4:
        return ('Druid of the ' + drsc)
    if r3 == 5:
        return ('Fighter of the ' + fsc + ' Archetype')
    if r3 == 6:
        return ('Monk of the ' + msc)
    if r3 == 7:
        return ('Mystic of the ' + mysc)
    if r3 == 8:
        return (palsc + ' Paladin')
    if r3 == 9:
        return (rngsc + ' Archetype Ranger')
    if r3 == 10:
        return (rosc + ' Archetype Rogue')
    if r3 == 11:
        return (scsc + 'Sorcerer')
    if r3 == 12:
        return ('Warlock of ' + warsc)
    if r3 == 13:
        return ('Wizard Specializing in ' + wizsc)
        
   
''' COLLECTS AND DISPLAYS THE MESSAGE BOXES '''    
    
def display_dndrc1():
    final = retrieve_dndrc1()
    tkinter.messagebox.showinfo('Your Character is a...', message = final)
    
def retrieve_dndrc1():
    return dndrc_Overview()

def display_dndrc2():
    final = retrieve_dndrc2()
    tkinter.messagebox.showinfo('Your Character is a...', message = final)
    
def retrieve_dndrc2():
    return dndrc_Gender()

def display_dndrc3():
    final = retrieve_dndrc3()
    tkinter.messagebox.showinfo('Your Character is a(n)...', message = final)
    
def retrieve_dndrc3():
    return dndrc_Subr()

def display_dndrc4():
    final = retrieve_dndrc4()
    tkinter.messagebox.showinfo('Your Character is a(n)...', message = final)
    
def retrieve_dndrc4():
    return dndrc_Subc()


''' TKINTER '''
root = Tk()

text = Label(root, text='Click buttons below\nto make a random\nDungeons and Dragons\nCharacter') #
text.pack()

Button1 = Button(root, text='Random Character', command = display_dndrc1)
Button1.pack()

Button2 = Button(root, text='Random Gender', command = display_dndrc2)
Button2.pack()

Button3 = Button(root, text='Random Race & Subrace', command = display_dndrc3)
Button3.pack()

Button4 = Button(root, text='Random Class & Subclass', command = display_dndrc4, geometry = '100x100')
Button4.pack()

root.title('AutoGen')
root.geometry("250x175+720+250") 
root.resizable(0, 0) 

root.mainloop()