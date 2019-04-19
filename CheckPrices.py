#Importing necessary modules
import urllib.request, json, pandas as pd, time, os

cwd = os.getcwd()
#The link to OS Buddy's API
url = "https://rsbuddy.com/exchange/summary.json?ts=" + str(int(time.time()))
#Grabs OS Buddy's API
response = urllib.request.urlopen(url)
#Sets OS Buddy's API to a Variable
data = json.loads(response.read())

#Creates the empty item_list and combine_list dictionaries
item_list = dict()
combine_list = dict()
separate_list = dict()
decant_list = dict()
decant_item_for_table = []
safe_decant_for_table = []
unsafe_decant_for_table = []
set_combine_item_for_table = []
safe_set_combine_for_table = []
unsafe_set_combine_for_table = []
set_separate_item_for_table = []
safe_set_separate_for_table = []
unsafe_set_separate_for_table = []
flips_for_table = []

#Importing all of the set names and buy limits from OS Buddy
combine_list['Adamant gold-trimmed set (lg)'] = ['Adamant gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Adamant gold-trimmed set (sk)'] = ['Adamant gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Adamant set (lg)'] = ['Adamant set (lg)', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Adamant set (sk)'] = ['Adamant set (sk)', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Adamant trimmed set (lg)'] = ['Adamant trimmed set (lg)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Adamant trimmed set (sk)'] = ['Adamant trimmed set (sk)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Ahrim\u0027s armour set'] = ['Ahrim\u0027s armour set', 0, 'Safe', 10, 0, 'Combine', 'NA']
combine_list['Ancestral robes set'] = ['Ancestral robes set', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Ancient rune armour set (lg)'] = ['Ancient rune armour set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Ancient rune armour set (sk)'] = ['Ancient rune armour set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Ancient dragonhide set'] = ['Ancient dragonhide set', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Armadyl rune armour set (lg)'] = ['Armadyl rune armour set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Armadyl rune armour set (sk)'] = ['Armadyl rune armour set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Armadyl dragonhide set'] = ['Armadyl dragonhide set', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Bandos rune armour set (lg)'] = ['Bandos rune armour set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Bandos rune armour set (sk)'] = ['Bandos rune armour set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Bandos dragonhide set'] = ['Bandos dragonhide set', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Black dragonhide set'] = ['Black dragonhide set', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Black gold-trimmed set (lg)'] = ['Black gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Black gold-trimmed set (sk)'] = ['Black gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Black set (lg)'] = ['Black set (lg)', 0, 'Safe', 100, 0, 'Combine', 'NA']
combine_list['Black set (sk)'] = ['Black set (sk)', 0, 'Safe', 100, 0, 'Combine', 'NA']
combine_list['Black trimmed set (lg)'] = ['Black trimmed set (lg)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Black trimmed set (sk)'] = ['Black trimmed set (sk)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Blue dragonhide set'] = ['Blue dragonhide set', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Book of law page set'] = ['Book of law page set', 0, 'Safe', 5, 0, 'Combine', 'NA']
combine_list['Book of darkness page set'] = ['Book of darkness page set', 0, 'Safe', 5, 0, 'Combine', 'NA']
combine_list['Book of balance page set'] = ['Book of balance page set', 0, 'Safe', 5, 0, 'Combine', 'NA']
combine_list['Book of war page set'] = ['Book of war page set', 0, 'Safe', 5, 0, 'Combine', 'NA']
combine_list['Bronze set (lg)'] = ['Bronze set (lg)', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Bronze set (sk)'] = ['Bronze set (sk)', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Bronze trimmed set (lg)'] = ['Bronze trimmed set (lg)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Bronze trimmed set (sk)'] = ['Bronze trimmed set (sk)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Bronze gold-trimmed set (lg)'] = ['Bronze gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Bronze gold-trimmed set (sk)'] = ['Bronze gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Combat potion set'] = ['Combat potion set', 0, 'Safe', 2000, 0, 'Combine', 'NA']
combine_list['Dharok\u0027s armour set'] = ['Dharok\u0027s armour set', 0, 'Safe', 10, 0, 'Combine', 'NA']
combine_list['Dragon armour set (lg)'] = ['Dragon armour set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Dragon armour set (sk)'] = ['Dragon armour set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Dwarf cannon set'] = ['Dwarf cannon set', 0, 'Safe', 10, 0, 'Combine', 'NA']
combine_list['Gilded armour set (lg)'] = ['Gilded armour set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Gilded armour set (sk)'] = ['Gilded armour set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Green dragonhide set'] = ['Green dragonhide set', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Guthan\u0027s armour set'] = ['Guthan\u0027s armour set', 0, 'Safe', 10, 0, 'Combine', 'NA']
combine_list['Guthix armour set (lg)'] = ['Guthix armour set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Guthix armour set (sk)'] = ['Guthix armour set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Guthix dragonhide set'] = ['Guthix dragonhide set', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Halloween mask set'] = ['Halloween mask set', 0, 'Safe', 5, 0, 'Combine', 'NA']
combine_list['Holy book page set'] = ['Holy book page set', 0, 'Safe', 5, 0, 'Combine', 'NA']
combine_list['Initiate harness m'] = ['Initiate harness m', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Iron gold-trimmed set (lg)'] = ['Iron gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Iron gold-trimmed set (sk)'] = ['Iron gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Iron set (lg)'] = ['Iron set (lg)', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Iron set (sk)'] = ['Iron set (sk)', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Iron trimmed set (lg)'] = ['Iron trimmed set (lg)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Iron trimmed set (sk)'] = ['Iron trimmed set (sk)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Justiciar armour set'] = ['Justiciar armour set', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Karil\u0027s armour set'] = ['Karil\u0027s armour set', 0, 'Safe', 10, 0, 'Combine', 'NA']
combine_list['Mithril gold-trimmed set (lg)'] = ['Mithril gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Mithril gold-trimmed set (sk)'] = ['Mithril gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Mithril set (lg)'] = ['Mithril set (lg)', 0, 'Safe', 100, 0, 'Combine', 'NA']
combine_list['Mithril set (sk)'] = ['Mithril set (sk)', 0, 'Safe', 100, 0, 'Combine', 'NA']
combine_list['Mithril trimmed set (lg)'] = ['Mithril trimmed set (lg)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Mithril trimmed set (sk)'] = ['Mithril trimmed set (sk)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Obsidian armour set'] = ['Obsidian armour set', 0, 'Safe', 10, 0, 'Combine', 'NA']
combine_list['Partyhat set'] = ['Partyhat set', 0, 'Safe', 5, 0, 'Combine', 'NA']
combine_list['Proselyte harness f'] = ['Proselyte harness f', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Proselyte harness m'] = ['Proselyte harness m', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Red dragonhide set'] = ['Red dragonhide set', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Rune gold-trimmed set (lg)'] = ['Rune gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Rune gold-trimmed set (sk)'] = ['Rune gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Rune armour set (lg)'] = ['Rune armour set (lg)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Rune armour set (sk)'] = ['Rune armour set (sk)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Rune trimmed set (lg)'] = ['Rune trimmed set (lg)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Rune trimmed set (sk)'] = ['Rune trimmed set (sk)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Saradomin armour set (lg)'] = ['Saradomin armour set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Saradomin armour set (sk)'] = ['Saradomin armour set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Saradomin dragonhide set'] = ['Saradomin dragonhide set', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Steel gold-trimmed set (lg)'] = ['Steel gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Steel gold-trimmed set (sk)'] = ['Steel gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Steel set (lg)'] = ['Steel set (lg)', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Steel set (sk)'] = ['Steel set (sk)', 0, 'Safe', 125, 0, 'Combine', 'NA']
combine_list['Steel trimmed set (lg)'] = ['Steel trimmed set (lg)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Steel trimmed set (sk)'] = ['Steel trimmed set (sk)', 0, 'Safe', 70, 0, 'Combine', 'NA']
combine_list['Super potion set'] = ['Super potion set', 0, 'Safe', 2000, 0, 'Combine', 'NA']
combine_list['Torag\u0027s armour set'] = ['Torag\u0027s armour set', 0, 'Safe', 10, 0, 'Combine', 'NA']
combine_list['Unholy book page set'] = ['Unholy book page set', 0, 'Safe', 5, 0, 'Combine', 'NA']
combine_list['Verac\u0027s armour set'] = ['Verac\u0027s armour set', 0, 'Safe', 10, 0, 'Combine', 'NA']
combine_list['Zamorak armour set (lg)'] = ['Zamorak armour set (lg)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Zamorak armour set (sk)'] = ['Zamorak armour set (sk)', 0, 'Safe', 8, 0, 'Combine', 'NA']
combine_list['Zamorak dragonhide set'] = ['Zamorak dragonhide set', 0, 'Safe', 8, 0, 'Combine', 'NA']


#Importing all of the set names and buy limits from OS Buddy
separate_list['Adamant gold-trimmed set (lg)'] = ['Adamant gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Adamant gold-trimmed set (sk)'] = ['Adamant gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Adamant set (lg)'] = ['Adamant set (lg)', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Adamant set (sk)'] = ['Adamant set (sk)', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Adamant trimmed set (lg)'] = ['Adamant trimmed set (lg)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Adamant trimmed set (sk)'] = ['Adamant trimmed set (sk)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Ahrim\u0027s armour set'] = ['Ahrim\u0027s armour set', 0, 'Safe', 10, 0, 'Separate', 'NA']
separate_list['Ancestral robes set'] = ['Ancestral robes set', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Ancient rune armour set (lg)'] = ['Ancient rune armour set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Ancient rune armour set (sk)'] = ['Ancient rune armour set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Ancient dragonhide set'] = ['Ancient dragonhide set', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Armadyl rune armour set (lg)'] = ['Armadyl rune armour set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Armadyl rune armour set (sk)'] = ['Armadyl rune armour set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Armadyl dragonhide set'] = ['Armadyl dragonhide set', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Bandos rune armour set (lg)'] = ['Bandos rune armour set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Bandos rune armour set (sk)'] = ['Bandos rune armour set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Bandos dragonhide set'] = ['Bandos dragonhide set', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Black dragonhide set'] = ['Black dragonhide set', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Black gold-trimmed set (lg)'] = ['Black gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Black gold-trimmed set (sk)'] = ['Black gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Black set (lg)'] = ['Black set (lg)', 0, 'Safe', 100, 0, 'Separate', 'NA']
separate_list['Black set (sk)'] = ['Black set (sk)', 0, 'Safe', 100, 0, 'Separate', 'NA']
separate_list['Black trimmed set (lg)'] = ['Black trimmed set (lg)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Black trimmed set (sk)'] = ['Black trimmed set (sk)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Blue dragonhide set'] = ['Blue dragonhide set', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Book of law page set'] = ['Book of law page set', 0, 'Safe', 5, 0, 'Separate', 'NA']
separate_list['Book of darkness page set'] = ['Book of darkness page set', 0, 'Safe', 5, 0, 'Separate', 'NA']
separate_list['Book of balance page set'] = ['Book of balance page set', 0, 'Safe', 5, 0, 'Separate', 'NA']
separate_list['Book of war page set'] = ['Book of war page set', 0, 'Safe', 5, 0, 'Separate', 'NA']
separate_list['Bronze set (lg)'] = ['Bronze set (lg)', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Bronze set (sk)'] = ['Bronze set (sk)', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Bronze trimmed set (lg)'] = ['Bronze trimmed set (lg)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Bronze trimmed set (sk)'] = ['Bronze trimmed set (sk)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Bronze gold-trimmed set (lg)'] = ['Bronze gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Bronze gold-trimmed set (sk)'] = ['Bronze gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Combat potion set'] = ['Combat potion set', 0, 'Safe', 2000, 0, 'Separate', 'NA']
separate_list['Dharok\u0027s armour set'] = ['Dharok\u0027s armour set', 0, 'Safe', 10, 0, 'Separate', 'NA']
separate_list['Dragon armour set (lg)'] = ['Dragon armour set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Dragon armour set (sk)'] = ['Dragon armour set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Dwarf cannon set'] = ['Dwarf cannon set', 0, 'Safe', 10, 0, 'Separate', 'NA']
separate_list['Gilded armour set (lg)'] = ['Gilded armour set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Gilded armour set (sk)'] = ['Gilded armour set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Green dragonhide set'] = ['Green dragonhide set', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Guthan\u0027s armour set'] = ['Guthan\u0027s armour set', 0, 'Safe', 10, 0, 'Separate', 'NA']
separate_list['Guthix armour set (lg)'] = ['Guthix armour set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Guthix armour set (sk)'] = ['Guthix armour set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Guthix dragonhide set'] = ['Guthix dragonhide set', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Halloween mask set'] = ['Halloween mask set', 0, 'Safe', 5, 0, 'Separate', 'NA']
separate_list['Holy book page set'] = ['Holy book page set', 0, 'Safe', 5, 0, 'Separate', 'NA']
separate_list['Initiate harness m'] = ['Initiate harness m', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Iron gold-trimmed set (lg)'] = ['Iron gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Iron gold-trimmed set (sk)'] = ['Iron gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Iron set (lg)'] = ['Iron set (lg)', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Iron set (sk)'] = ['Iron set (sk)', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Iron trimmed set (lg)'] = ['Iron trimmed set (lg)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Iron trimmed set (sk)'] = ['Iron trimmed set (sk)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Justiciar armour set'] = ['Justiciar armour set', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Karil\u0027s armour set'] = ['Karil\u0027s armour set', 0, 'Safe', 10, 0, 'Separate', 'NA']
separate_list['Mithril gold-trimmed set (lg)'] = ['Mithril gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Mithril gold-trimmed set (sk)'] = ['Mithril gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Mithril set (lg)'] = ['Mithril set (lg)', 0, 'Safe', 100, 0, 'Separate', 'NA']
separate_list['Mithril set (sk)'] = ['Mithril set (sk)', 0, 'Safe', 100, 0, 'Separate', 'NA']
separate_list['Mithril trimmed set (lg)'] = ['Mithril trimmed set (lg)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Mithril trimmed set (sk)'] = ['Mithril trimmed set (sk)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Obsidian armour set'] = ['Obsidian armour set', 0, 'Safe', 10, 0, 'Separate', 'NA']
separate_list['Partyhat set'] = ['Partyhat set', 0, 'Safe', 5, 0, 'Separate', 'NA']
separate_list['Proselyte harness f'] = ['Proselyte harness f', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Proselyte harness m'] = ['Proselyte harness m', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Red dragonhide set'] = ['Red dragonhide set', 0, 'Safe', 70, 0, 'Separate']
separate_list['Rune gold-trimmed set (lg)'] = ['Rune gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Rune gold-trimmed set (sk)'] = ['Rune gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Rune armour set (lg)'] = ['Rune armour set (lg)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Rune armour set (sk)'] = ['Rune armour set (sk)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Rune trimmed set (lg)'] = ['Rune trimmed set (lg)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Rune trimmed set (sk)'] = ['Rune trimmed set (sk)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Saradomin armour set (lg)'] = ['Saradomin armour set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Saradomin armour set (sk)'] = ['Saradomin armour set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Saradomin dragonhide set'] = ['Saradomin dragonhide set', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Steel gold-trimmed set (lg)'] = ['Steel gold-trimmed set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Steel gold-trimmed set (sk)'] = ['Steel gold-trimmed set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Steel set (lg)'] = ['Steel set (lg)', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Steel set (sk)'] = ['Steel set (sk)', 0, 'Safe', 125, 0, 'Separate', 'NA']
separate_list['Steel trimmed set (lg)'] = ['Steel trimmed set (lg)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Steel trimmed set (sk)'] = ['Steel trimmed set (sk)', 0, 'Safe', 70, 0, 'Separate', 'NA']
separate_list['Super potion set'] = ['Super potion set', 0, 'Safe', 2000, 0, 'Separate', 'NA']
separate_list['Torag\u0027s armour set'] = ['Torag\u0027s armour set', 0, 'Safe', 10, 0, 'Separate', 'NA']
separate_list['Unholy book page set'] = ['Unholy book page set', 0, 'Safe', 5, 0, 'Separate', 'NA']
separate_list['Verac\u0027s armour set'] = ['Verac\u0027s armour set', 0, 'Safe', 10, 0, 'Separate', 'NA']
separate_list['Zamorak armour set (lg)'] = ['Zamorak armour set (lg)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Zamorak armour set (sk)'] = ['Zamorak armour set (sk)', 0, 'Safe', 8, 0, 'Separate', 'NA']
separate_list['Zamorak dragonhide set'] = ['Zamorak dragonhide set', 0, 'Safe', 8, 0, 'Separate', 'NA']


def refresh_data() :
    for key in data : 
        item_id = key
        item_name = data[key]['name']
        item_avg = data[key]['overall_average']
        item_sell = data[key]['sell_average']
        item_buy = data[key]['buy_average']
        item_sell_quant = data[key]['sell_quantity']
        item_buy_quant = data[key]['buy_quantity']
        set_name = 'None'
        offer_type = 'None'
        item_list[item_name] = [item_name, item_id, item_avg, item_sell, item_buy, item_sell_quant, item_buy_quant, 'None', set_name, offer_type]
        
refresh_data()
    
#Sets the buy price for an item
def set_buy_price(l):
    r = l
    if (len(r) == 10) :
        item_buy = r[4]
        item_sell = r[3]
        offer_type = r[7]
        if item_buy > 0 and item_sell > 0 and item_buy >= item_sell :
            offer_type = 'Buy'
            r.pop(2)
            r.pop(2)
            r.pop(3)
            r[2] = r[2] + int(r[2] * 0.02)
            r[4] = offer_type
            return r
        elif item_sell > 0 and item_buy > 0 and item_sell >= item_buy :
            offer_type = 'Buy'
            r.pop(2)
            r.pop(3)
            r.pop(4)
            r[2] = r[2] + int(r[2] * 0.02)
            r[4] = offer_type
            return r
        else:
            offer_type = 'None'
            r.pop(2)
            r.pop(2)
            r.pop(3)
            r[4] = offer_type
            return r
    else :
        return
    
#Sets the sell price for an item
def set_sell_price(l):
    r = l
    if (len(r) == 10) :
        item_buy = r[4]
        item_sell = r[3]
        offer_type = r[7]
        if item_buy > 0 and item_sell > 0 and item_buy <= item_sell :
            offer_type = 'Sell'
            r.pop(2)
            r.pop(2)
            r.pop(3)
            r[4] = offer_type
            return r
        elif item_sell > 0 and item_buy > 0 and item_sell <= item_buy :
            offer_type = 'Sell'
            r.pop(2)
            r.pop(3)
            r.pop(4)
            r[4] = offer_type
            return r
        else:
            offer_type = 'None'
            r.pop(2)
            r.pop(3)
            r.pop(4)
            r[4] = offer_type
            return r
    else :
        return


#Calculates earnings of set combination
def combine_set_flip(packed, parts):
    #Sets variables
    refresh_data()
    fl = combine_list[packed]
    c = item_list[packed]
    
    i = dict()
    price = 0
    cost = 0
    
    #Calls the set_price_type methods and adds the items to the item dataframe list
    set_sell_price(c)
    c[5] = packed
    c[6] = 'Combine'
    set_combine_item_for_table.append(c)
    for each in parts:
        i[each] = item_list[each]
        set_buy_price(i[each])
        i[each][5] = packed
        i[each][6] = 'Combine'
        set_combine_item_for_table.append(i[each])
        
    #Decides if a flip is safe or not
    if (c[4]=='None'):
        fl[2] = 'Not Safe'
    for each in parts:
        if (i[each][4]=='None' or i[each][3]<fl[3]/2):
            fl[2] = 'Not Safe'
            
        
    #Calculates Estimated Profit and adds flips to dataframe list
    if (fl[2] == 'Safe') :
        price += c[2]
        for each in i:
            cost += i[each][2]
        price -= cost
        fl[1] = price
        fl[4] = fl[1]*fl[3]
        safe_set_combine_for_table.append(fl)
    elif (fl[2] == 'Not Safe') :
        fl[1] = 0
        fl[4] = fl[1]*fl[3]
        safe_set_combine_for_table.append(fl)
        
#Separating Sets Flip
def separate_set_flip(packed, parts):
    #Sets variables
    refresh_data()
    fl = separate_list[packed]
    c = item_list[packed]
    
    i = dict()
    price = 0
    cost = 0
    
    #Calls the set_price_type methods and adds the items to the item dataframe list
    set_buy_price(c)
    c[5] = packed
    c[6] = 'Separate'
    set_separate_item_for_table.append(c)
    for each in parts:
        i[each] = item_list[each]
        set_sell_price(i[each])
        i[each][5] = packed
        i[each][6] = 'Separate'
        set_separate_item_for_table.append(i[each])
        
    #Decides if a flip is safe or not
    if (c[4]=='None'):
        fl[2] = 'Not Safe'
    for each in parts:
        if (i[each][4]=='None' or i[each][3]<(fl[3]/2)):
            fl[2] = 'Not Safe'
            
        
    #Calculates Estimated Profit and adds flips to dataframe list
    if (fl[2] == 'Safe') :
        for each in i:
            price += i[each][2]
        cost += c[2]
        price -= cost
        fl[1] = price
        fl[4] = fl[1]*fl[3]
        safe_set_separate_for_table.append(fl)
    elif (fl[2] == 'Not Safe') :
        fl[1] = 0
        fl[4] = fl[1]*fl[3]
        safe_set_separate_for_table.append(fl)
        

#Function for potion decant flips
def decant_flip(pot, lim) :
    refresh_data()
    #Set parameters
    profit = 0
    potname = pot
    buy_limit = lim
    pot1 = potname + '(1)'
    pot2 = potname + '(2)'
    pot3 = potname + '(3)'
    pot4 = potname + '(4)'
    
    #print('Original Pot Data')
    #print(pot1)
    #print(pot2)
    #print(pot3)
    #print(pot4)
    #print('')
    
    #Get data for items
    pot1buydata = item_list[pot1]
    pot2buydata = item_list[pot2]
    pot3buydata = item_list[pot3]
    pot4buydata = item_list[pot4]
    
    #print('Original Pot Buy Data')
    #print(pot1buydata)
    #print(pot2buydata)
    #print(pot3buydata)
    #print(pot4buydata)
    #print('')
    
    #Set Up Decant Options
    pot1to2 = decant_list[pot1 + ' to ' + pot2] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot1 + ' to ' + pot2]
    pot1to3 = decant_list[pot1 + ' to ' + pot3] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot1 + ' to ' + pot3]
    pot1to4 = decant_list[pot1 + ' to ' + pot4] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot1 + ' to ' + pot4]
    pot2to1 = decant_list[pot2 + ' to ' + pot1] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot2 + ' to ' + pot1]
    pot2to3 = decant_list[pot2 + ' to ' + pot3] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot2 + ' to ' + pot3]
    pot2to4 = decant_list[pot2 + ' to ' + pot4] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot2 + ' to ' + pot4]
    pot3to1 = decant_list[pot3 + ' to ' + pot1] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot3 + ' to ' + pot1]
    pot3to2 = decant_list[pot3 + ' to ' + pot2] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot3 + ' to ' + pot2]
    pot3to4 = decant_list[pot3 + ' to ' + pot4] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot3 + ' to ' + pot4]
    pot4to1 = decant_list[pot4 + ' to ' + pot1] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot4 + ' to ' + pot1]
    pot4to2 = decant_list[pot4 + ' to ' + pot2] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot4 + ' to ' + pot2]
    pot4to3 = decant_list[pot4 + ' to ' + pot3] = [potname, 0, 'Not Safe', buy_limit, 0, 'Decant', pot4 + ' to ' + pot3]
    #Sets buy data and appends Buy Data to decant_items_for_table
    pot1buy = set_buy_price(pot1buydata)
    pot1buy[5] = potname
    pot1buy[6] = 'Decant'
    decant_item_for_table.append(pot1buy)
    pot2buy = set_buy_price(pot2buydata)
    pot2buy[5] = potname
    pot2buy[6] = 'Decant'
    decant_item_for_table.append(pot2buy)
    pot3buy = set_buy_price(pot3buydata)
    pot3buy[5] = potname
    pot3buy[6] = 'Decant'
    decant_item_for_table.append(pot3buy)
    pot4buy = set_buy_price(pot4buydata)
    pot4buy[5] = potname
    pot4buy[6] = 'Decant'
    decant_item_for_table.append(pot4buy)
    
    #print('Original Pot Buy')
    #print(pot1buydata)
    #print(pot2buydata)
    #print(pot3buydata)
    #print(pot4buydata)
    #print('')
    
    #Resets potdata
    refresh_data()
    pot1selldata = item_list[pot1]
    pot2selldata = item_list[pot2]
    pot3selldata = item_list[pot3]
    pot4selldata = item_list[pot4]
    
    #print('Original Pot Sell')
    #print(pot1selldata)
    #print(pot2selldata)
    #print(pot3selldata)
    #print(pot4selldata)
    #print('')
    
    #Sets sell data and appends sell Data to decant_items_for_table
    pot1sell = set_sell_price(pot1selldata)
    pot1sell[5] = potname
    pot1sell[6] = 'Decant'
    decant_item_for_table.append(pot1sell)
    pot2sell = set_sell_price(pot2selldata)
    pot2sell[5] = potname
    pot2sell[6] = 'Decant'
    decant_item_for_table.append(pot2sell)
    pot3sell = set_sell_price(pot3selldata)
    pot3sell[5] = potname
    pot3sell[6] = 'Decant'
    decant_item_for_table.append(pot3sell)
    pot4sell = set_sell_price(pot4selldata)
    pot4sell[5] = potname
    pot4sell[6] = 'Decant'
    decant_item_for_table.append(pot4sell)
    
    #print('Original Pot Sell')
    #print(pot1sell)
    #print(pot2sell)
    #print(pot3sell)
    #print(pot4sell)
    #print('')
    
    #1 to 2 Decant    
    if(pot1buy[2]>0 and pot2sell[2]>0 and pot1buy[3]>=(buy_limit/2) and pot2sell[3]>=(buy_limit/2) and 2*pot1buy[2]<pot2sell[2]+3):
        profit = (pot2sell[2]+3)-(2*pot1buy[2])
        pot1to2[2] = 'Safe'
        pot1to2[1] = profit
        pot1to2[4] = pot1to2[1]*(pot1to2[3]/2)
        safe_decant_for_table.append(pot1to2)
    else :
        unsafe_decant_for_table.append(pot1to2)
    #1 to 3 Decant
    if(pot1buy[2]>0 and pot3sell[2]>0 and pot1buy[3]>=(buy_limit/2) and pot3sell[3]>=(buy_limit/2) and 3*pot1buy[2]<pot3sell[2]+6):
        profit = (pot3sell[2]+6)-(3*pot1buy[2])
        pot1to3[2] = 'Safe'
        pot1to3[1] = profit
        pot1to3[4] = pot1to3[1]*(pot1to3[3]/3)
        safe_decant_for_table.append(pot1to3)
    else :
        unsafe_decant_for_table.append(pot1to3)
    #1 to 4 Decant
    if(pot1buy[2]>0 and pot4sell[2]>0 and pot1buy[3]>=(buy_limit/2) and pot4sell[3]>=(buy_limit/2) and 4*pot1buy[2]<pot4sell[2]+9):
        profit = (pot4sell[2]+9)-(4*pot1buy[2])
        pot1to4[2] = 'Safe'
        pot1to4[1] = profit
        pot1to4[4] = pot1to4[1]*(pot1to4[3]/4)
        safe_decant_for_table.append(pot1to4)
    else :
        unsafe_decant_for_table.append(pot1to4)
    #2 to 1 Decant
    if(pot2buy[2]>0 and pot1sell[2]>0 and pot2buy[3]>=(buy_limit/2) and pot1sell[3]>=(buy_limit/2) and pot2buy[2]+3<2*pot1sell[2]):
        profit = (2*pot1sell[2])-(pot2buy[2]+3)
        pot2to1[2] = 'Safe'
        pot2to1[1] = profit
        pot2to1[4] = pot2to1[1]*pot2to1[3]
        safe_decant_for_table.append(pot2to1)
    else :
        unsafe_decant_for_table.append(pot2to1)
    #2 to 3 Decant
    if(pot2buy[2]>0 and pot3sell[2]>0 and pot2buy[3]>=(buy_limit/2) and pot3sell[3]>=(buy_limit/2) and 1.5*pot2buy[2]<pot3sell[2]+3):
        profit = (pot3sell[2]+3)-(1.5*pot2buy[2])
        pot2to3[2] = 'Safe'
        pot2to3[1] = profit
        pot2to3[4] = pot2to3[1]*(pot2to3[3]/1.5)
        safe_decant_for_table.append(pot2to3)
    else :
        unsafe_decant_for_table.append(pot2to3)
    #2 to 4 Decant
    if(pot2buy[2]>0 and pot4sell[2]>0 and pot2buy[3]>=(buy_limit/2) and pot4sell[3]>=(buy_limit/2) and 2*pot2buy[2]<pot4sell[2]+3):
        profit = (pot4sell[2]+3)-(2*pot2buy[2])
        pot2to4[2] = 'Safe'
        pot2to4[1] = profit
        pot2to4[4] = pot2to4[1]*(pot2to4[3]/2)
        safe_decant_for_table.append(pot2to4)
    else :
        unsafe_decant_for_table.append(pot2to4)
    #3 to 1 Decant   
    if(pot3buy[2]>0 and pot1sell[2]>0 and pot3buy[3]>=(buy_limit/2) and pot1sell[3]>=(buy_limit/2) and pot3buy[2]+6<3*pot1sell[2]):
        profit = (3*pot1sell[2])-(pot3buy[2]+6)
        pot3to1[2] = 'Safe'
        pot3to1[1] = profit
        pot3to1[4] = pot3to1[1]*pot3to1[3]
        safe_decant_for_table.append(pot3to1)
    else :
        unsafe_decant_for_table.append(pot3to1)
    #3 to 2 Decant
    if(pot3buy[2]>0 and pot2sell[2]>0 and pot3buy[3]>=(buy_limit/2) and pot2sell[3]>=(buy_limit/2) and 2*pot3buy[2]+3<3*pot2sell[2]):
        profit = (3*pot2sell[2])-(2*pot3buy[2]+3)
        pot3to2[2] = 'Safe'
        pot3to2[1] = profit
        pot3to2[4] = pot3to2[1]*(pot3to2[3]/2)
        safe_decant_for_table.append(pot3to2)
    else :
        unsafe_decant_for_table.append(pot3to2)
    #3 to 4 Decant
    if(pot3buy[2]>0 and pot4sell[2]>0 and pot3buy[3]>=(buy_limit/2) and pot4sell[3]>=(buy_limit/2) and 4*pot3buy[2]<((3*pot4sell[2])+3)):
        profit = ((3*pot4sell[2])+3)-(4*pot3buy[2])
        pot3to4[2] = 'Safe'
        pot3to4[1] = profit
        pot3to4[4] = pot3to4[1]*(pot3to4[3]/4)
        safe_decant_for_table.append(pot3to4)
    else :
        unsafe_decant_for_table.append(pot3to4)
    #4 to 1 Decant
    if(pot4buy[2]>0 and pot1sell[2]>0 and pot4buy[3]>=(buy_limit/2) and pot1sell[3]>=(buy_limit/2) and pot4buy[2]+9<4*pot1sell[2]):
        profit = (4*pot1sell[2])-(pot4buy[2]+9)
        pot4to1[2] = 'Safe'
        pot4to1[1] = profit
        pot4to1[4] = pot4to1[1]*pot4to1[3]
        safe_decant_for_table.append(pot4to1)
    else :
        unsafe_decant_for_table.append(pot4to1)
    #4 to 2 Decant
    if(pot4buy[2]>0 and pot2sell[2]>0 and pot4buy[3]>=(buy_limit/2) and pot2sell[3]>=(buy_limit/2) and pot4buy[2]+3<2*pot2sell[2]):
        profit = (2*pot2sell[2])-(pot4buy[2]+3)
        pot4to2[2] = 'Safe'
        pot4to2[1] = profit
        pot4to2[4] = pot4to2[1]*pot4to2[3]
        safe_decant_for_table.append(pot4to2)
    else :
        unsafe_decant_for_table.append(pot4to2)
    #4 to 3 Decant
    if(pot4buy[2]>0 and pot3sell[2]>0 and pot4buy[3]>=(buy_limit/2) and pot3sell[3]>=(buy_limit/2) and 3*pot4buy[2]+3<4*pot3sell[2]):
        profit = (4*pot3sell[2])-(3*pot4buy[2]+3)
        pot4to3[2] = 'Safe'
        pot4to3[1] = profit
        pot4to3[4] = pot4to3[1]*(pot4to3[3]/3)
        safe_decant_for_table.append(pot4to3)
    else :
        unsafe_decant_for_table.append(pot4to3)
        

#Adding combine_set_flip function to all item sets in Runescape
combine_set_flip(packed='Adamant gold-trimmed set (lg)', parts=('Adamant platebody (g)','Adamant platelegs (g)','Adamant full helm (g)','Adamant kiteshield (g)'))
combine_set_flip(packed='Adamant gold-trimmed set (sk)', parts=('Adamant platebody (g)','Adamant plateskirt (g)','Adamant full helm (g)','Adamant kiteshield (g)'))
combine_set_flip(packed='Adamant set (lg)', parts=('Adamant platebody','Adamant platelegs','Adamant full helm','Adamant kiteshield'))
combine_set_flip(packed='Adamant set (sk)', parts=('Adamant platebody','Adamant plateskirt','Adamant full helm','Adamant kiteshield'))
combine_set_flip(packed='Adamant trimmed set (lg)', parts=('Adamant platebody (t)','Adamant platelegs (t)','Adamant full helm (t)','Adamant kiteshield (t)'))
combine_set_flip(packed='Adamant trimmed set (sk)', parts=('Adamant platebody (t)','Adamant plateskirt (t)','Adamant full helm (t)','Adamant kiteshield (t)'))
combine_set_flip(packed='Ahrim\u0027s armour set', parts=('Ahrim\u0027s hood','Ahrim\u0027s robetop','Ahrim\u0027s robeskirt','Ahrim\u0027s staff'))
combine_set_flip(packed='Ancestral robes set', parts=('Ancestral hat','Ancestral robe top','Ancestral robe bottom',))
combine_set_flip(packed='Ancient rune armour set (lg)', parts=('Ancient platebody','Ancient platelegs','Ancient full helm','Ancient kiteshield'))
combine_set_flip(packed='Ancient rune armour set (sk)', parts=('Ancient platebody','Ancient plateskirt','Ancient full helm','Ancient kiteshield'))
combine_set_flip(packed='Ancient dragonhide set', parts=('Ancient coif','Ancient d\u0027hide','Ancient chaps','Ancient bracers'))
combine_set_flip(packed='Armadyl rune armour set (lg)', parts=('Armadyl platebody','Armadyl platelegs','Armadyl full helm','Armadyl kiteshield'))
combine_set_flip(packed='Armadyl rune armour set (sk)', parts=('Armadyl platebody','Armadyl plateskirt','Armadyl full helm','Armadyl kiteshield'))
combine_set_flip(packed='Armadyl dragonhide set', parts=('Armadyl coif','Armadyl d\u0027hide','Armadyl chaps','Armadyl bracers'))
combine_set_flip(packed='Bandos rune armour set (lg)', parts=('Bandos platebody','Bandos platelegs','Bandos full helm','Bandos kiteshield'))
combine_set_flip(packed='Bandos rune armour set (sk)', parts=('Bandos platebody','Bandos plateskirt','Bandos full helm','Bandos kiteshield'))
combine_set_flip(packed='Bandos dragonhide set', parts=('Bandos coif','Bandos d\u0027hide','Bandos chaps','Bandos bracers'))
combine_set_flip(packed='Black dragonhide set', parts=('Black d\u0027hide body','Black d\u0027hide chaps','Black d\u0027hide vamb'))
combine_set_flip(packed='Black gold-trimmed set (lg)', parts=('Black platebody (g)','Black platelegs (g)','Black full helm (g)','Black kiteshield (g)'))
combine_set_flip(packed='Black gold-trimmed set (sk)', parts=('Black platebody (g)','Black plateskirt (g)','Black full helm (g)','Black kiteshield (g)'))
combine_set_flip(packed='Black set (lg)', parts=('Black platebody','Black platelegs','Black full helm','Black kiteshield'))
combine_set_flip(packed='Black set (sk)', parts=('Black platebody','Black plateskirt','Black full helm','Black kiteshield'))
combine_set_flip(packed='Black trimmed set (lg)', parts=('Black platebody (t)','Black platelegs (t)','Black full helm (t)','Black kiteshield (t)'))
combine_set_flip(packed='Black trimmed set (sk)', parts=('Black platebody (t)','Black plateskirt (t)','Black full helm (t)','Black kiteshield (t)'))
combine_set_flip(packed='Blue dragonhide set', parts=('Blue d\u0027hide body','Blue d\u0027hide chaps','Blue d\u0027hide vamb'))
combine_set_flip(packed='Book of law page set', parts=('Armadyl page 1','Armadyl page 2','Armadyl page 3','Armadyl page 4'))
combine_set_flip(packed='Book of darkness page set', parts=('Ancient page 1','Ancient page 2','Ancient page 3','Ancient page 4'))
combine_set_flip(packed='Book of balance page set', parts=('Guthix page 1','Guthix page 2','Guthix page 3','Guthix page 4'))
combine_set_flip(packed='Book of war page set', parts=('Bandos page 1','Bandos page 2','Bandos page 3','Bandos page 4'))
combine_set_flip(packed='Bronze gold-trimmed set (lg)', parts=('Bronze platebody (g)','Bronze platelegs (g)','Bronze full helm (g)','Bronze kiteshield (g)'))
combine_set_flip(packed='Bronze gold-trimmed set (sk)', parts=('Bronze platebody (g)','Bronze plateskirt (g)','Bronze full helm (g)','Bronze kiteshield (g)'))
combine_set_flip(packed='Bronze set (lg)', parts=('Bronze platebody','Bronze platelegs','Bronze full helm','Bronze kiteshield'))
combine_set_flip(packed='Bronze set (sk)', parts=('Bronze platebody','Bronze plateskirt','Bronze full helm','Bronze kiteshield'))
combine_set_flip(packed='Bronze trimmed set (lg)', parts=('Bronze platebody (t)','Bronze platelegs (t)','Bronze full helm (t)','Bronze kiteshield (t)'))
combine_set_flip(packed='Bronze trimmed set (sk)', parts=('Bronze platebody (t)','Bronze plateskirt (t)','Bronze full helm (t)','Bronze kiteshield (t)'))
combine_set_flip(packed='Combat potion set', parts=('Attack potion(4)','Strength potion(4)','Defence potion(4)'))
combine_set_flip(packed='Dharok\u0027s armour set', parts=('Dharok\u0027s helm','Dharok\u0027s platebody','Dharok\u0027s platelegs','Dharok\u0027s greataxe'))
combine_set_flip(packed='Dragon armour set (lg)', parts=('Dragon platebody','Dragon platelegs','Dragon full helm','Dragon kiteshield'))
combine_set_flip(packed='Dragon armour set (sk)', parts=('Dragon platebody','Dragon plateskirt','Dragon full helm','Dragon kiteshield'))
combine_set_flip(packed='Dwarf cannon set', parts=('Cannon barrels','Cannon base','Cannon furnace','Cannon stand'))
combine_set_flip(packed='Gilded armour set (lg)', parts=('Gilded platebody','Gilded platelegs','Gilded full helm','Gilded kiteshield'))
combine_set_flip(packed='Gilded armour set (sk)', parts=('Gilded platebody','Gilded plateskirt','Gilded full helm','Gilded kiteshield'))
combine_set_flip(packed='Green dragonhide set', parts=('Green d\u0027hide body','Green d\u0027hide chaps','Green d\u0027hide vamb'))
combine_set_flip(packed='Guthan\u0027s armour set', parts=('Guthan\u0027s helm','Guthan\u0027s platebody','Guthan\u0027s chainskirt','Guthan\u0027s warspear'))
combine_set_flip(packed='Guthix armour set (lg)', parts=('Guthix platebody','Guthix platelegs','Guthix full helm','Guthix kiteshield'))
combine_set_flip(packed='Guthix armour set (sk)', parts=('Guthix platebody','Guthix platelegs','Guthix full helm','Guthix kiteshield'))
combine_set_flip(packed='Guthix dragonhide set', parts=('Guthix coif','Guthix dragonhide','Guthix chaps','Guthix bracers'))
combine_set_flip(packed='Halloween mask set', parts=('Red halloween mask','Green halloween mask','Blue halloween mask'))
combine_set_flip(packed='Holy book page set', parts=('Saradomin page 1','Saradomin page 2','Saradomin page 3','Saradomin page 4'))
combine_set_flip(packed='Initiate harness m', parts=('Initiate sallet','Initiate hauberk','Initiate cuisse'))
combine_set_flip(packed='Iron gold-trimmed set (lg)', parts=('Iron platebody (g)','Iron platelegs (g)','Iron full helm (g)','Iron kiteshield (g)'))
combine_set_flip(packed='Iron gold-trimmed set (sk)', parts=('Iron platebody (g)','Iron plateskirt (g)','Iron full helm (g)','Iron kiteshield (g)'))
combine_set_flip(packed='Iron set (lg)', parts=('Iron platebody','Iron platelegs','Iron full helm','Iron kiteshield'))
combine_set_flip(packed='Iron set (sk)', parts=('Iron platebody','Iron plateskirt','Iron full helm','Iron kiteshield'))
combine_set_flip(packed='Iron trimmed set (lg)', parts=('Iron platebody (t)','Iron platelegs (t)','Iron full helm (t)','Iron kiteshield (t)'))
combine_set_flip(packed='Iron trimmed set (sk)', parts=('Iron platebody (t)','Iron plateskirt (t)','Iron full helm (t)','Iron kiteshield (t)'))
combine_set_flip(packed='Justiciar armour set', parts=('Justiciar faceguard','Justiciar chestguard','Justiciar legguards'))
combine_set_flip(packed='Karil\u0027s armour set', parts=('Karil\u0027s coif','Karil\u0027s leathertop','Karil\u0027s leatherskirt','Karil\u0027s crossbow'))
combine_set_flip(packed='Mithril gold-trimmed set (lg)', parts=('Mithril platebody (g)','Mithril platelegs (g)','Mithril full helm (g)','Mithril kiteshield (g)'))
combine_set_flip(packed='Mithril gold-trimmed set (sk)', parts=('Mithril platebody (g)','Mithril plateskirt (g)','Mithril full helm (g)','Mithril kiteshield (g)'))
combine_set_flip(packed='Mithril set (lg)', parts=('Mithril platebody','Mithril platelegs','Mithril full helm','Mithril kiteshield'))
combine_set_flip(packed='Mithril set (sk)', parts=('Mithril platebody','Mithril plateskirt','Mithril full helm','Mithril kiteshield'))
combine_set_flip(packed='Mithril trimmed set (lg)', parts=('Mithril platebody (t)','Mithril platelegs (t)','Mithril full helm (t)','Mithril kiteshield (t)'))
combine_set_flip(packed='Mithril trimmed set (sk)', parts=('Mithril platebody (t)','Mithril plateskirt (t)','Mithril full helm (t)','Mithril kiteshield (t)'))
combine_set_flip(packed='Obsidian armour set', parts=('Obsidian helmet','Obsidian platebody','Obsidian platelegs'))
combine_set_flip(packed='Partyhat set', parts=('Red partyhat','Yellow partyhat','Green partyhat','Blue partyhat','Purple partyhat','White partyhat'))
combine_set_flip(packed='Proselyte harness f', parts=('Proselyte sallet','Proselyte hauberk','Proselyte cuisse'))
combine_set_flip(packed='Proselyte harness m', parts=('Proselyte sallet','Proselyte hauberk','Proselyte tasset'))
combine_set_flip(packed='Red dragonhide set', parts=('Red d\u0027hide body','Red d\u0027hide chaps','Red d\u0027hide vamb'))
combine_set_flip(packed='Rune gold-trimmed set (lg)', parts=('Rune platebody (g)','Rune platelegs (g)','Rune full helm (g)','Rune kiteshield (g)'))
combine_set_flip(packed='Rune gold-trimmed set (sk)', parts=('Rune platebody (g)','Rune plateskirt (g)','Rune full helm (g)','Rune kiteshield (g)'))
combine_set_flip(packed='Rune armour set (lg)', parts=('Rune platebody','Rune platelegs','Rune full helm','Rune kiteshield'))
combine_set_flip(packed='Rune armour set (sk)', parts=('Rune platebody','Rune plateskirt','Rune full helm','Rune kiteshield'))
combine_set_flip(packed='Rune trimmed set (lg)', parts=('Rune platebody (t)','Rune platelegs (t)','Rune full helm (t)','Rune kiteshield (t)'))
combine_set_flip(packed='Rune trimmed set (sk)', parts=('Rune platebody (t)','Rune plateskirt (t)','Rune full helm (t)','Rune kiteshield (t)'))
combine_set_flip(packed='Saradomin armour set (lg)', parts=('Saradomin platebody','Saradomin platelegs','Saradomin full helm','Saradomin kiteshield'))
combine_set_flip(packed='Saradomin armour set (sk)', parts=('Saradomin platebody','Saradomin plateskirt','Saradomin full helm','Saradomin kiteshield'))
combine_set_flip(packed='Saradomin dragonhide set', parts=('Saradomin coif','Saradomin d\u0027hide','Saradomin chaps','Saradomin bracers'))
combine_set_flip(packed='Steel gold-trimmed set (lg)', parts=('Steel platebody (g)','Steel platelegs (g)','Steel full helm (g)','Steel kiteshield (g)'))
combine_set_flip(packed='Steel gold-trimmed set (sk)', parts=('Steel platebody (g)','Steel plateskirt (g)','Steel full helm (g)','Steel kiteshield (g)'))
combine_set_flip(packed='Steel set (lg)', parts=('Steel platebody','Steel platelegs','Steel full helm','Steel kiteshield'))
combine_set_flip(packed='Steel set (sk)', parts=('Steel platebody','Steel plateskirt','Steel full helm','Steel kiteshield'))
combine_set_flip(packed='Steel trimmed set (lg)', parts=('Steel platebody (t)','Steel platelegs (t)','Steel full helm (t)','Steel kiteshield (t)'))
combine_set_flip(packed='Steel trimmed set (sk)', parts=('Steel platebody (t)','Steel plateskirt (t)','Steel full helm (t)','Steel kiteshield (t)'))
combine_set_flip(packed='Super potion set', parts=('Super attack(4)','Super strength(4)','Super defence(4)'))
combine_set_flip(packed='Torag\u0027s armour set', parts=('Torag\u0027s helm','Torag\u0027s platebody','Torag\u0027s platelegs','Torag\u0027s hammers'))
combine_set_flip(packed='Unholy book page set', parts=('Zamorak page 1','Zamorak page 2','Zamorak page 3','Zamorak page 4'))
combine_set_flip(packed='Verac\u0027s armour set', parts=('Verac\u0027s helm','Verac\u0027s brassard','Verac\u0027s plateskirt','Verac\u0027s flail'))
combine_set_flip(packed='Zamorak armour set (lg)', parts=('Zamorak platebody','Zamorak platelegs','Zamorak full helm','Zamorak kiteshield'))
combine_set_flip(packed='Zamorak armour set (sk)', parts=('Zamorak platebody','Zamorak plateskirt','Zamorak full helm','Zamorak kiteshield'))
combine_set_flip(packed='Zamorak dragonhide set', parts=('Zamorak coif','Zamorak d\u0027hide','Zamorak chaps','Zamorak bracers'))


#Adding combine_set_flip function to all item sets in Runescape
separate_set_flip(packed='Adamant gold-trimmed set (lg)', parts=('Adamant platebody (g)','Adamant platelegs (g)','Adamant full helm (g)','Adamant kiteshield (g)'))
separate_set_flip(packed='Adamant gold-trimmed set (sk)', parts=('Adamant platebody (g)','Adamant plateskirt (g)','Adamant full helm (g)','Adamant kiteshield (g)'))
separate_set_flip(packed='Adamant set (lg)', parts=('Adamant platebody','Adamant platelegs','Adamant full helm','Adamant kiteshield'))
separate_set_flip(packed='Adamant set (sk)', parts=('Adamant platebody','Adamant plateskirt','Adamant full helm','Adamant kiteshield'))
separate_set_flip(packed='Adamant trimmed set (lg)', parts=('Adamant platebody (t)','Adamant platelegs (t)','Adamant full helm (t)','Adamant kiteshield (t)'))
separate_set_flip(packed='Adamant trimmed set (sk)', parts=('Adamant platebody (t)','Adamant plateskirt (t)','Adamant full helm (t)','Adamant kiteshield (t)'))
separate_set_flip(packed='Ahrim\u0027s armour set', parts=('Ahrim\u0027s hood','Ahrim\u0027s robetop','Ahrim\u0027s robeskirt','Ahrim\u0027s staff'))
separate_set_flip(packed='Ancestral robes set', parts=('Ancestral hat','Ancestral robe top','Ancestral robe bottom',))
separate_set_flip(packed='Ancient rune armour set (lg)', parts=('Ancient platebody','Ancient platelegs','Ancient full helm','Ancient kiteshield'))
separate_set_flip(packed='Ancient rune armour set (sk)', parts=('Ancient platebody','Ancient plateskirt','Ancient full helm','Ancient kiteshield'))
separate_set_flip(packed='Ancient dragonhide set', parts=('Ancient coif','Ancient d\u0027hide','Ancient chaps','Ancient bracers'))
separate_set_flip(packed='Armadyl rune armour set (lg)', parts=('Armadyl platebody','Armadyl platelegs','Armadyl full helm','Armadyl kiteshield'))
separate_set_flip(packed='Armadyl rune armour set (sk)', parts=('Armadyl platebody','Armadyl plateskirt','Armadyl full helm','Armadyl kiteshield'))
separate_set_flip(packed='Armadyl dragonhide set', parts=('Armadyl coif','Armadyl d\u0027hide','Armadyl chaps','Armadyl bracers'))
separate_set_flip(packed='Bandos rune armour set (lg)', parts=('Bandos platebody','Bandos platelegs','Bandos full helm','Bandos kiteshield'))
separate_set_flip(packed='Bandos rune armour set (sk)', parts=('Bandos platebody','Bandos plateskirt','Bandos full helm','Bandos kiteshield'))
separate_set_flip(packed='Bandos dragonhide set', parts=('Bandos coif','Bandos d\u0027hide','Bandos chaps','Bandos bracers'))
separate_set_flip(packed='Black dragonhide set', parts=('Black d\u0027hide body','Black d\u0027hide chaps','Black d\u0027hide vamb'))
separate_set_flip(packed='Black gold-trimmed set (lg)', parts=('Black platebody (g)','Black platelegs (g)','Black full helm (g)','Black kiteshield (g)'))
separate_set_flip(packed='Black gold-trimmed set (sk)', parts=('Black platebody (g)','Black plateskirt (g)','Black full helm (g)','Black kiteshield (g)'))
separate_set_flip(packed='Black set (lg)', parts=('Black platebody','Black platelegs','Black full helm','Black kiteshield'))
separate_set_flip(packed='Black set (sk)', parts=('Black platebody','Black plateskirt','Black full helm','Black kiteshield'))
separate_set_flip(packed='Black trimmed set (lg)', parts=('Black platebody (t)','Black platelegs (t)','Black full helm (t)','Black kiteshield (t)'))
separate_set_flip(packed='Black trimmed set (sk)', parts=('Black platebody (t)','Black plateskirt (t)','Black full helm (t)','Black kiteshield (t)'))
separate_set_flip(packed='Blue dragonhide set', parts=('Blue d\u0027hide body','Blue d\u0027hide chaps','Blue d\u0027hide vamb'))
separate_set_flip(packed='Book of law page set', parts=('Armadyl page 1','Armadyl page 2','Armadyl page 3','Armadyl page 4'))
separate_set_flip(packed='Book of darkness page set', parts=('Ancient page 1','Ancient page 2','Ancient page 3','Ancient page 4'))
separate_set_flip(packed='Book of balance page set', parts=('Guthix page 1','Guthix page 2','Guthix page 3','Guthix page 4'))
separate_set_flip(packed='Book of war page set', parts=('Bandos page 1','Bandos page 2','Bandos page 3','Bandos page 4'))
separate_set_flip(packed='Bronze gold-trimmed set (lg)', parts=('Bronze platebody (g)','Bronze platelegs (g)','Bronze full helm (g)','Bronze kiteshield (g)'))
separate_set_flip(packed='Bronze gold-trimmed set (sk)', parts=('Bronze platebody (g)','Bronze plateskirt (g)','Bronze full helm (g)','Bronze kiteshield (g)'))
separate_set_flip(packed='Bronze set (lg)', parts=('Bronze platebody','Bronze platelegs','Bronze full helm','Bronze kiteshield'))
separate_set_flip(packed='Bronze set (sk)', parts=('Bronze platebody','Bronze plateskirt','Bronze full helm','Bronze kiteshield'))
separate_set_flip(packed='Bronze trimmed set (lg)', parts=('Bronze platebody (t)','Bronze platelegs (t)','Bronze full helm (t)','Bronze kiteshield (t)'))
separate_set_flip(packed='Bronze trimmed set (sk)', parts=('Bronze platebody (t)','Bronze plateskirt (t)','Bronze full helm (t)','Bronze kiteshield (t)'))
separate_set_flip(packed='Combat potion set', parts=('Attack potion(4)','Strength potion(4)','Defence potion(4)'))
separate_set_flip(packed='Dharok\u0027s armour set', parts=('Dharok\u0027s helm','Dharok\u0027s platebody','Dharok\u0027s platelegs','Dharok\u0027s greataxe'))
separate_set_flip(packed='Dragon armour set (lg)', parts=('Dragon platebody','Dragon platelegs','Dragon full helm','Dragon kiteshield'))
separate_set_flip(packed='Dragon armour set (sk)', parts=('Dragon platebody','Dragon plateskirt','Dragon full helm','Dragon kiteshield'))
separate_set_flip(packed='Dwarf cannon set', parts=('Cannon barrels','Cannon base','Cannon furnace','Cannon stand'))
separate_set_flip(packed='Gilded armour set (lg)', parts=('Gilded platebody','Gilded platelegs','Gilded full helm','Gilded kiteshield'))
separate_set_flip(packed='Gilded armour set (sk)', parts=('Gilded platebody','Gilded plateskirt','Gilded full helm','Gilded kiteshield'))
separate_set_flip(packed='Green dragonhide set', parts=('Green d\u0027hide body','Green d\u0027hide chaps','Green d\u0027hide vamb'))
separate_set_flip(packed='Guthan\u0027s armour set', parts=('Guthan\u0027s helm','Guthan\u0027s platebody','Guthan\u0027s chainskirt','Guthan\u0027s warspear'))
separate_set_flip(packed='Guthix armour set (lg)', parts=('Guthix platebody','Guthix platelegs','Guthix full helm','Guthix kiteshield'))
separate_set_flip(packed='Guthix armour set (sk)', parts=('Guthix platebody','Guthix platelegs','Guthix full helm','Guthix kiteshield'))
separate_set_flip(packed='Guthix dragonhide set', parts=('Guthix coif','Guthix dragonhide','Guthix chaps','Guthix bracers'))
separate_set_flip(packed='Halloween mask set', parts=('Red halloween mask','Green halloween mask','Blue halloween mask'))
separate_set_flip(packed='Holy book page set', parts=('Saradomin page 1','Saradomin page 2','Saradomin page 3','Saradomin page 4'))
separate_set_flip(packed='Initiate harness m', parts=('Initiate sallet','Initiate hauberk','Initiate cuisse'))
separate_set_flip(packed='Iron gold-trimmed set (lg)', parts=('Iron platebody (g)','Iron platelegs (g)','Iron full helm (g)','Iron kiteshield (g)'))
separate_set_flip(packed='Iron gold-trimmed set (sk)', parts=('Iron platebody (g)','Iron plateskirt (g)','Iron full helm (g)','Iron kiteshield (g)'))
separate_set_flip(packed='Iron set (lg)', parts=('Iron platebody','Iron platelegs','Iron full helm','Iron kiteshield'))
separate_set_flip(packed='Iron set (sk)', parts=('Iron platebody','Iron plateskirt','Iron full helm','Iron kiteshield'))
separate_set_flip(packed='Iron trimmed set (lg)', parts=('Iron platebody (t)','Iron platelegs (t)','Iron full helm (t)','Iron kiteshield (t)'))
separate_set_flip(packed='Iron trimmed set (sk)', parts=('Iron platebody (t)','Iron plateskirt (t)','Iron full helm (t)','Iron kiteshield (t)'))
separate_set_flip(packed='Justiciar armour set', parts=('Justiciar faceguard','Justiciar chestguard','Justiciar legguards'))
separate_set_flip(packed='Karil\u0027s armour set', parts=('Karil\u0027s coif','Karil\u0027s leathertop','Karil\u0027s leatherskirt','Karil\u0027s crossbow'))
separate_set_flip(packed='Mithril gold-trimmed set (lg)', parts=('Mithril platebody (g)','Mithril platelegs (g)','Mithril full helm (g)','Mithril kiteshield (g)'))
separate_set_flip(packed='Mithril gold-trimmed set (sk)', parts=('Mithril platebody (g)','Mithril plateskirt (g)','Mithril full helm (g)','Mithril kiteshield (g)'))
separate_set_flip(packed='Mithril set (lg)', parts=('Mithril platebody','Mithril platelegs','Mithril full helm','Mithril kiteshield'))
separate_set_flip(packed='Mithril set (sk)', parts=('Mithril platebody','Mithril plateskirt','Mithril full helm','Mithril kiteshield'))
separate_set_flip(packed='Mithril trimmed set (lg)', parts=('Mithril platebody (t)','Mithril platelegs (t)','Mithril full helm (t)','Mithril kiteshield (t)'))
separate_set_flip(packed='Mithril trimmed set (sk)', parts=('Mithril platebody (t)','Mithril plateskirt (t)','Mithril full helm (t)','Mithril kiteshield (t)'))
separate_set_flip(packed='Obsidian armour set', parts=('Obsidian helmet','Obsidian platebody','Obsidian platelegs'))
separate_set_flip(packed='Partyhat set', parts=('Red partyhat','Yellow partyhat','Green partyhat','Blue partyhat','Purple partyhat','White partyhat'))
separate_set_flip(packed='Proselyte harness f', parts=('Proselyte sallet','Proselyte hauberk','Proselyte cuisse'))
separate_set_flip(packed='Proselyte harness m', parts=('Proselyte sallet','Proselyte hauberk','Proselyte tasset'))
separate_set_flip(packed='Red dragonhide set', parts=('Red d\u0027hide body','Red d\u0027hide chaps','Red d\u0027hide vamb'))
separate_set_flip(packed='Rune gold-trimmed set (lg)', parts=('Rune platebody (g)','Rune platelegs (g)','Rune full helm (g)','Rune kiteshield (g)'))
separate_set_flip(packed='Rune gold-trimmed set (sk)', parts=('Rune platebody (g)','Rune plateskirt (g)','Rune full helm (g)','Rune kiteshield (g)'))
separate_set_flip(packed='Rune armour set (lg)', parts=('Rune platebody','Rune platelegs','Rune full helm','Rune kiteshield'))
separate_set_flip(packed='Rune armour set (sk)', parts=('Rune platebody','Rune plateskirt','Rune full helm','Rune kiteshield'))
separate_set_flip(packed='Rune trimmed set (lg)', parts=('Rune platebody (t)','Rune platelegs (t)','Rune full helm (t)','Rune kiteshield (t)'))
separate_set_flip(packed='Rune trimmed set (sk)', parts=('Rune platebody (t)','Rune plateskirt (t)','Rune full helm (t)','Rune kiteshield (t)'))
separate_set_flip(packed='Saradomin armour set (lg)', parts=('Saradomin platebody','Saradomin platelegs','Saradomin full helm','Saradomin kiteshield'))
separate_set_flip(packed='Saradomin armour set (sk)', parts=('Saradomin platebody','Saradomin plateskirt','Saradomin full helm','Saradomin kiteshield'))
separate_set_flip(packed='Saradomin dragonhide set', parts=('Saradomin coif','Saradomin d\u0027hide','Saradomin chaps','Saradomin bracers'))
separate_set_flip(packed='Steel gold-trimmed set (lg)', parts=('Steel platebody (g)','Steel platelegs (g)','Steel full helm (g)','Steel kiteshield (g)'))
separate_set_flip(packed='Steel gold-trimmed set (sk)', parts=('Steel platebody (g)','Steel plateskirt (g)','Steel full helm (g)','Steel kiteshield (g)'))
separate_set_flip(packed='Steel set (lg)', parts=('Steel platebody','Steel platelegs','Steel full helm','Steel kiteshield'))
separate_set_flip(packed='Steel set (sk)', parts=('Steel platebody','Steel plateskirt','Steel full helm','Steel kiteshield'))
separate_set_flip(packed='Steel trimmed set (lg)', parts=('Steel platebody (t)','Steel platelegs (t)','Steel full helm (t)','Steel kiteshield (t)'))
separate_set_flip(packed='Steel trimmed set (sk)', parts=('Steel platebody (t)','Steel plateskirt (t)','Steel full helm (t)','Steel kiteshield (t)'))
separate_set_flip(packed='Super potion set', parts=('Super attack(4)','Super strength(4)','Super defence(4)'))
separate_set_flip(packed='Torag\u0027s armour set', parts=('Torag\u0027s helm','Torag\u0027s platebody','Torag\u0027s platelegs','Torag\u0027s hammers'))
separate_set_flip(packed='Unholy book page set', parts=('Zamorak page 1','Zamorak page 2','Zamorak page 3','Zamorak page 4'))
separate_set_flip(packed='Verac\u0027s armour set', parts=('Verac\u0027s helm','Verac\u0027s brassard','Verac\u0027s plateskirt','Verac\u0027s flail'))
separate_set_flip(packed='Zamorak armour set (lg)', parts=('Zamorak platebody','Zamorak platelegs','Zamorak full helm','Zamorak kiteshield'))
separate_set_flip(packed='Zamorak armour set (sk)', parts=('Zamorak platebody','Zamorak plateskirt','Zamorak full helm','Zamorak kiteshield'))
separate_set_flip(packed='Zamorak dragonhide set', parts=('Zamorak coif','Zamorak d\u0027hide','Zamorak chaps','Zamorak bracers'))


#Decant Flips
decant_flip('Agility potion',2000)
decant_flip('Anti-venom',2000)
decant_flip('Anti-venom+',2000)
decant_flip('Antidote+',4000)
decant_flip('Antidote++',4000)
decant_flip('Antifire potion',2000)
decant_flip('Antipoison',2000)
decant_flip('Attack potion',2000)
decant_flip('Bastion potion',2000)
decant_flip('Battlemage potion',2000)
decant_flip('Combat potion',2000)
decant_flip('Compost potion',50)
decant_flip('Defence potion',2000)
decant_flip('Energy potion',2000)
decant_flip('Extended antifire',2000)
decant_flip('Extended super antifire',2000)
decant_flip('Fishing potion',2000)
decant_flip('Guthix balance',2000)
decant_flip('Hunter potion',2000)
decant_flip('Magic potion',2000)
decant_flip('Olive oil',2000)
decant_flip('Prayer potion',2000)
decant_flip('Ranging potion',2000)
decant_flip('Relicym\u0027s balm',2000)
decant_flip('Restore potion',2000)
decant_flip('Sacred oil',2000)
decant_flip('Sanfew serum',2000)
decant_flip('Saradomin brew',2000)
decant_flip('Serum 207 ',2000)
decant_flip('Stamina potion',2000)
decant_flip('Strength potion',2000)
decant_flip('Super antifire potion',2000)
decant_flip('Super attack',2000)
decant_flip('Super combat potion',2000)
decant_flip('Super defence',2000)
decant_flip('Super energy',2000)
decant_flip('Super restore',2000)
decant_flip('Super strength',2000)
decant_flip('Superantipoison',2000)
decant_flip('Zamorak brew',2000)


#Creating the set_combine item table
set_combine_item_table = pd.DataFrame(set_combine_item_for_table, columns = ['Item_Name', 'ID', 'Price', 'Transactions', 'Offer', 'Set_Name', 'Type'])
#Creating the flipping table and saving it as a csv
safe_set_combine_table = pd.DataFrame(safe_set_combine_for_table, columns = ['Set_Name', 'Profit', 'Safety', 'Buy_Limit', 'Total_Profit', 'Type', 'Dec_Type'])
set_combine_table = safe_set_combine_table.merge(set_combine_item_table, how='right', on = ['Set_Name', 'Type'])
set_combine_table.sort_values("Total_Profit", axis = 0, ascending = False, inplace = True, na_position = 'last')
set_combine_table.to_csv(cwd + r'\Set_Combines.csv')
#Creating the set_separate item table
set_separate_item_table = pd.DataFrame(set_separate_item_for_table, columns = ['Item_Name', 'ID', 'Price', 'Transactions', 'Offer', 'Set_Name', 'Type'])
#Creating the flipping table and saving it as a csv
safe_set_separate_table = pd.DataFrame(safe_set_separate_for_table, columns = ['Set_Name', 'Profit', 'Safety', 'Buy_Limit', 'Total_Profit', 'Type', 'Dec_Type'])
set_separate_table = safe_set_separate_table.merge(set_separate_item_table, how='right', on = ['Set_Name', 'Type'])
set_separate_table.sort_values("Total_Profit", axis = 0, ascending = False, inplace = True, na_position = 'last')
set_separate_table.to_csv(cwd + r'\Set_Separates.csv')

#Creating the decant item table and saving it as a csv
decant_item_table = pd.DataFrame(decant_item_for_table, columns = ['Item_Name', 'ID', 'Price', 'Transactions', 'Offer', 'Set_Name', 'Type'])
#Creating the decant table and saving it as a csv
safe_decant_table = pd.DataFrame(safe_decant_for_table, columns = ['Set_Name', 'Profit', 'Safety', 'Buy_Limit', 'Total_Profit', 'Type', 'Dec_Type'])
decant_table = safe_decant_table.merge(decant_item_table, how='right')
decant_table.sort_values("Total_Profit", axis = 0, ascending = False, inplace = True, na_position = 'last')
decant_table.to_csv(cwd + r'\Decants.csv')

set_combine_and_set_separate_table = set_combine_table.append(set_separate_table)
full_flips_table = set_combine_and_set_separate_table.append(decant_table)
full_flips_table = full_flips_table[full_flips_table.Total_Profit > 0]
flips_table = full_flips_table
flips_table.sort_values(["Total_Profit","Offer","Item_Name"], axis = 0, ascending = False, inplace = True, na_position = 'last')
flips_table.to_csv(cwd + r'\Flips.csv')


#Opens the csv file
os.startfile(cwd + r'\Flips.csv')
        
