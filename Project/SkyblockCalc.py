import sys
import requests
import json
x=0
while x == x:
  def greeting():
	  print("\nThis is a list of what the code can calculate:")
	  print("")
	  print("Effective HP (Ehp in command)")
	  print("Damage Calculator (Dmg in command)")
	  print("Ability Damage Calculator (Ability in command)")
	  print("Minion Profit Calculator (Minion in command)\n")
	  print("If you want to exit out of the session, input exit as your command!\n")
	  global data_1
	  data_1 = str(input("What are you trying to calculate?\n\nCommand: "))
  def ehp():
	  print("\nPlease put your responses in numbers like 1000 instead of 1k!\n")
	  hp = int(input("What is your HP?\nHP: "))
	  defense = int(input("\nWhat is your Defense?\nDefense: "))
	  true_def = int(input("\nWhat is your True Defense?\nTrue Defense: "))
	  ehp = (hp * (defense/100))+ true_def
	  print("\nYour effective HP is:", ehp, "\n")
  def damage():
	  crit_Damage = int(input("\nHow much Crit Damage do you have? Please put them in numbers like 333 instead of 333%!\nCritical Damage: "))
	  crit_Damage = crit_Damage/100
	  strength = int(input("\nHow much Strength do you have? Please put them in numbers like 1000 instead of 1k!\nStrength: "))
	  weapon_Damage = int(input("\nWhat is your weapon base damage?\nDamage: "))
	  combat_Level = int(input("\nWhat is your combat level?\nCombat Level: "))
	  base_Damage = (5+weapon_Damage + (strength/5))*(1+(strength/100))
	  print("\nThe next question will ask you which mob are you trying to kill. Here are the list/choices!")
	  print("")
	  print("End (for Enderdragons and Endermen)")
	  print('Undead (for Zombies, Zombie Pigmen, Withers, Wither Skeletons, and Skeletons)')
	  print("Spider (for Cave Spiders, Spiders and Silverfish)")
	  print("Cube (for Creepers, Magma Cubes, and Slimes)")
	  mob_Type = str(input("\nWhat mob type are you trying to kill?\nMob Type: "))
	  print("The following questions will involve in the enchants that your sword has. If your sword does not have the specified enchant, please put 0 as your input!")
	  ender_Slayer = 0
	  sharpness = 0
	  smite = 0
	  arthropods = 0
	  giant_Killer = 0
	  dragon_Hunter = 0
	  cubism = 0
	  sharpness = int(input("\nWhat level enchant is your Sharpness?\nEnchant Level: "))
	  if mob_Type == "End" or mob_Type == "end":
		  ender_Slayer = int(input("\nWhat level enchant is your Ender Slayer?\nEnchant Level: "))
		  dragons = str(input("\nAre you fighting the EnderDragon? yes or no?\nCommand: "))
		  if dragons == "yes":
			  dragon_Hunter = int(input("\nWhat level enchant is your Dragon Slayer?\nEnchant Level: "))
		  if dragons == "no":
			  dragon_Hunter == 0
	  if mob_Type == "Undead" or mob_Type == "undead" and sharpness == 0:
		  smite = int(input("\nWhat level enchant is your smite?\nEnchant Level: "))
	  if mob_Type == "Spider" or mob_Type == "spider" and sharpness == 0:
		  arthropods = int(input("\nWhat level enchant is your Bane of Arthropods?\nEnchant Level: "))
	  if mob_Type == "Cube" or mob_Type == "cube":
		  cubism = int(input("\nWhat level enchant is your Cubism?\n"))
	  #Giant Killer Enchant
	  hp = int(input("\nWhat is your HP?\nHP: "))
	  giant_Killer = int(input("\nWhat level enchant is your Giant Killer?\nEnchant Level: "))
	  if giant_Killer != 0:
		  enemy_HP = int(input("\nHow much HP does your enemy have?\nEnemy HP: "))
	  giant_Damage = ((enemy_HP - hp)/hp)* 0.1 * giant_Killer * 1
	  if giant_Damage > 0.25:
		  giant_Damage = 0.25
	  elif giant_Killer == 0:
		  giant_Damage = 0
      #Execute Enchant
	  execute = int(input("\nWhat is your execute enchant level\nEnchant Level: "))
	  if execute != 0:
		  current_HP = str(input("\nWhat is your current HP? (Input <same> if its the same HP)\nCurrent HP: "))
		  if current_HP == "same" or current_HP == "Same":
			  current_HP = hp
		  if current_HP != "same" or current_HP != "Same":
			  current_HP = int(current_HP)
	  else:
		  execute_Damage = 0
	  execute_Damage = ((hp - current_HP)/hp)*0.002* execute * 1
	  #First Strike Enchant
	  first_Strike = int(input("\nWhat is your First Strike enchant level?\nEnchant Level: "))
	  #Impaling Enchant
	  impaling = int(input("\nWhat is your Impaling enchant level?\nEnchant Level: "))
	  #Armor Damage Multiplier
	  data_1 = str(input("\nAre you wearing a tux? yes/no\nCommand: "))
	  if data_1 != "yes" and data_1 != "no":
		  print("You have entered the wrong input!")
		  data_1 = str(input("\nAre you wearing a tux? yes/no\nCommand: "))
	  if data_1 == "yes":
		  print("\nWhich type of tux are you wearing:")
		  print("")
		  data_2 = str(input("Cheap, Fancy, or Elegant?\nTux: "))
		  if data_2 == "Cheap" or data_2 == "cheap":
			  damage_Armor = 1.5
			  hp = 75
		  if data_2 == "Fancy" or data_2 == "fancy":
			  damage_Armor = 2
			  hp = 150
		  if data_2 == "Elegant" or data_2 == "elegant":
			  damage_Armor = 2.5
			  hp = 250
		  else:
			  print("You have entered the wrong input!")
			  data_2 = str(input("\nCheap, Fancy, or Elegant?\nTux: "))
	  if data_1 == "no":
		  damage_Armor = 1
	  damage_Multiply = 1 + (combat_Level * 0.04)+((sharpness * 0.05)+(smite * 0.08)+(ender_Slayer * 0.12)+(dragon_Hunter * 0.08)+(arthropods * 0.08)+(cubism * 0.1)+(first_Strike * 0.25)+(impaling * 0.125)+execute_Damage+giant_Damage)
	  final_Damage = base_Damage * damage_Multiply * damage_Armor * (1+crit_Damage)
	  print("\nYou will deal", final_Damage, "to", mob_Type, "mobs\n")
  def ability():
	  print("Here is the list that you can choose from!\n")
	  print("Yeti for Yeti Sword\n Frozen for Frozen Scythe\n Golem for Golem Sword\n Ink for Ink wand\n Leap for Leaping Sword\n Silk for Silk Edge Sword\n Pig for Pigman Sword\n Aotd for Aspect of the Dragons\n Voodoo for Voodoo Doll\n Dread for Dreadlord Sword\n Bonzo for Bonzo's Staff\n Spirit for Spirit Sceptre\n Giant for Giant's Sword\n Midas for Midass Staff\n")
	  magic_Weapon = str(input("\nWhich weapon are you using?\nWeapon: "))
	  mana = int(input("How much mana do you have?\nMana: "))
	  base_Ability = float(input("What is the base damage that is displayed in the weapon lore?\nBase Damage: "))
	  if magic_Weapon == "Yeti" or magic_Weapon == "yeti":
		  ability_Scale = 0.3
	  if magic_Weapon == "Frozen" or magic_Weapon == "frozen":
		  ability_Scale = 0.3
	  if magic_Weapon == "Golem" or magic_Weapon == "golem":
		  ability_Scale = 1.0
	  if magic_Weapon == "Ink" or magic_Weapon == "ink":
		  ability_Scale = 1.0
	  if magic_Weapon == "Leap" or magic_Weapon == "leap":
		  ability_Scale = 1.0
	  if magic_Weapon == "Silk" or magic_Weapon == "silk":
		  ability_Scale = 1.1
	  if magic_Weapon == "Pig" or magic_Weapon == "pig":
		  ability_Scale = 0.1
	  if magic_Weapon == "Voodoo" or magic_Weapon == "voodoo":
		  ability_Scale = 1.0
	  if magic_Weapon == "Dread" or magic_Weapon == "dread":
		  ability_Scale = 2/3
	  if magic_Weapon == "Bonzo" or magic_Weapon == "bonzo":
		  ability_Scale = 0.2
	  if magic_Weapon == "Giant" or magic_Weapon == "giant":
		  ability_Scale = 0.05
	  if magic_Weapon == "Midas" or magic_Weapon == "midas":
		  ability_Scale = 1.0
	  if magic_Weapon == "AOTD" or magic_Weapon == "Aotd" or magic_Weapon == "aotd":
		  ability_Scale = 0.1
	  if magic_Weapon == "Spirit" or magic_Weapon == "spirit":
		  ability_Scale = 0.2
	  damage_Ability = base_Ability * (1 + (mana/100)*ability_Scale)
	  print("Your weapon will deal:", damage_Ability, "to mobs!")
  def minion():
	  import random
	  bz_Data = requests.get("https://api.hypixel.net/skyblock/bazaar?key=API+Key")
	  bz_Data = json.loads(bz_Data.text)
	  bz_Data == bz_Data
	  all_fish_Price = 0
	  all_spiderPrice = 0
	  all_slayer_Price = 0
	  all_farm_Price = 0
	  price = 0
	  time_Format = str(input("\nDo you want to calculate profit in hours or days?\nCommand: "))
	  if time_Format == "Days" or time_Format == "days":
		  time_Days = int(input("\nHow much days?\nCommand: "))
		  time_Hours = time_Days * 24
		  time_Minutes = time_Hours * 60
	  if time_Format == "Hours" or time_Format == "hours" or time_Format == "Hour" or time_Format == "hour":
		  time_Hours = int(input("\nHow much hours?\nCommand: ")) 
		  time_Minutes = time_Hours * 60
	  time_Seconds = time_Minutes * 60
	  farming_list_15 = [15,15,13,13,11,11,10,10,9,9,8]
	  farming_list_20 = [20,20,18,18,16,16,14,14,12,12,10]
	  farming_list_32 = [32,32,30,30,27,27,24,24,20,20,16]
	  fishing_list_32 = [32,32,30,30,27.5,27.5,24,24,20,20,16]
	  combat_list_32 = [32,32,30,30,28,28,25,25,22,22,18]
	  farming_list_24 = [24,24,22.5,22.5,21,21,18.5,18.5,16,16,13]
	  farming_list_30 = [30,30,28,28,26,26,23,23,20,20,16]
	  farming_list_27 = [27,27,25,25,23,23,21,21,18,18,15]
	  combat_list_27 = [27,27,25,25,23,23,21,21,18,18,14]
	  farming_list_22 = [22,22,20,20,18,18,16,16,14.5,14.5,12]
	  farming_list_26 = [26,26,24,24,22,22,20,20,17,17,13]
	  mining_list_26 = [26,26,24,24,22,22,19,19,16,16,12]
	  combat_list_26 = [26,26,24,24,22,22,19,19,16,16,13]
	  combats_list_26 = [26,26,24,24,22,22,19,19,16,16,12]
	  farming_list_50 = [50,50,47,47,44,44,41,41,38,38,32]
	  combat_list_50 = [50,50,47,47,44,44,41,41,38,38,32]
	  mining_list_14 = [14,14,12,12,10,10,9,9,8,8,7]
	  mining_list_15 = [15,15,13,13,12,12,10,10,9,9,7]
	  mining_list_17 = [17,17,15,15,14,14,12,12,10,10,8]
	  mining_list_22 = [22,22,20,20,18,18,16,16,14,14,11]
	  dmining_list_29 = [29,29,27,27,25,25,22,22,19,19,15]
	  mining_list_29 = [29,29,27,27,25,25,23,23,21,21,18]
	  mining_list_28 = [28,28,26,26,24,24,21,21,18,18,14]
	  mining_list_22_5 = [22.5,22.5,21,21,19,19,17,17,14.5,14.5,11.5]
	  mining_list_45 = [45,45,42,42,39,39,35,35,30,30,24]
	  mining_list_25 = [25,25,23,23,21,21,19,19,16,16,13]
	  combat_list_33 = [33,33,31,31,28.5,28.5,25,25,21,21,16.5]
	  slayer_list_29 = [29,29,26,26,23,23,19,19,14.5,14.5,10]
	  foraging_list_48 = [48,48,45,45,42,42,38,38,33,33,27]
	  fishing_list_78 = [78,75,72,72,68,68,62.5,62.5,53,53,35]
	  other_list_13 = [13,13,12,12,11,11,9.5,9.5,8,8,6.5]
	  other_list_30 = [30,29,28,27,26,25,24,23,22,20,18]
	  category = str(input("\nWhat type of minion are you calculating?\nCombat, Farming, Fishing, Foraging, or Mining?\n(Snow minions and Flower minions are in the other categories so input (other) for these minions!)\nMinion Category: "))
	  minion = str(input("\nPlease list the minion that you would like to calculate the production!\n (Example: Magma instead of Magma Cube minion or Nether instead of Nether Wart Minion or Ender instead of Enderman)\nMinion Name: "))
	  tier_info = int(input("\nWhat tier is your minion? (Example: 11 instead of XI)\nMinion Tier: "))
	  minion_Tier = tier_info - 1
	  minion_Action = 0
	  drop = 0
	  drop2 = 0
	  price2 = 0
	  additional_Drop = 0
	  additional_Price = 0
	  if category == "Combat" or category == "combat":
		  if minion == "Ender" or minion == "ender" or minion == "magma" or minion == "Magma":
			  minion_Action = combat_list_32[minion_Tier]
			  if minion == "Ender" or minion == "ender":
				  drop = 1
				  price = float(bz_Data["products"]["ENDER_PEARL"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "magma" or minion == "Magma":
				  drop = 1.8
				  price = float(bz_Data["products"]["MAGMA_CREAM"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Creeper" or minion == "creeper":
			  minion_Action = combat_list_27[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["SULPHUR"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Zombie" or minion == "zombie" or minion == "Skeleton" or minion == "skeleton" or minion == "spider" or minion == "Spider" or minion == "cave" or minion == "Cave":
			  minion_Action = combat_list_26[minion_Tier]
			  if minion == "Zombie" or minion == "zombie" or minion == "Skeleton" or minion == "skeleton":
				  drop = 1
				  if minion == "Zombie" or minion == "zombie":
					  price = float(bz_Data["products"]["ROTTEN_FLESH"]["sell_summary"][0]["pricePerUnit"])
				  if minion == "Skeleton" or minion == "skeleton":
					  price = float(bz_Data["products"]["BONE"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "cave" or minion == "Cave":
				  minion_FA = minion_Action * 2
				  minion_Time = time_Seconds/minion_FA
				  eye_Price = float(bz_Data["products"]["SPIDER_EYE"]["sell_summary"][0]["pricePerUnit"])
				  string_Price = bz_Data["products"]["STRING"]["sell_summary"][0]["pricePerUnit"]
				  round_minion_time = int(minion_Time)
				  drop = 1
				  string_Drop = 0
				  for n in range(round_minion_time):
					  string_RNG = random.randint(1,10)
					  if string_RNG >= 5:
						  string_Drop = string_Drop + 1
					  else:
						  string_Drop = string_Drop + 0
				  all_spiderPrice = (string_Drop * string_Price) + ((minion_Time * drop) * eye_Price)
			  if minion == "spider" or minion == "Spider":
				  minion_FA = minion_Action * 2
				  minion_Time = time_Seconds/minion_FA
				  eye_Price = float(bz_Data["products"]["SPIDER_EYE"]["sell_summary"][0]["pricePerUnit"])
				  string_Price = float(bz_Data["products"]["STRING"]["sell_summary"][0]["pricePerUnit"])
				  round_minion_time = int(minion_Time)
				  drop = 1
				  eye_Drop = 0
				  for n in range(round_minion_time):
					  eye_RNG = random.randint(1,10)
					  if eye_RNG >= 5:
						  eye_Drop = eye_Drop + 1
					  else:
						  eye_Drop = eye_Drop + 0
				  all_spiderPrice = (eye_Drop * eye_Price) + ((minion_Time * drop) * string_Price)
		  if minion == "slime" or minion == "Slime":
			  minion_Action = combats_list_26[minion_Tier]
			  drop = 1.8
			  price = float(bz_Data["products"]["SLIME_BALL"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Ghast" or minion == "ghast":
			  minion_Action = combat_list_50[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["GHAST_TEAR"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Blaze" or minion == "blaze":
			  minion_Action = combat_list_33[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["BLAZE_ROD"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Revenant" or minion == "revenant" or minion == "Tarantula" or minion == "tarantula" or minion == "rev" or minion == "Rev" or minion == "Tara" or minion == "tara":
			  minion_Action = slayer_list_29[minion_Tier]
			  if minion == "Revenant" or minion == "revenant" or minion == "rev" or minion == "Rev":
				  rotten_Price = float(bz_Data["products"]["ROTTEN_FLESH"]["sell_summary"][0]["pricePerUnit"])
				  minion_FA = minion_Action * 2
				  minion_Time = time_Seconds/minion_FA
				  round_minion_time = int(minion_Time)
				  diamond_Price = float(bz_Data["products"]["DIAMOND"]["sell_summary"][0]["pricePerUnit"])
				  drop = 3
				  diamond_Drop = 0
				  for n in range(round_minion_time):
					  diamond_RNG = random.randint(1,10)
					  if diamond_RNG >= 8:
						  diamond_Drop = diamond_Drop + 1
					  else:
						  diamond_Drop = diamond_Drop + 0
				  all_slayer_Price = (diamond_Drop * diamond_Price) + ((minion_Time * drop)* rotten_Price)
			  if minion == "Tarantula" or minion == "tarantula" or minion == "Tara" or minion == "tara":
				  string_Price = float(bz_Data["products"]["STRING"]["sell_summary"][0]["pricePerUnit"])
				  eye_Price = float(bz_Data["products"]["SPIDER_EYE"]["sell_summary"][0]["pricePerUnit"])
				  minion_FA = minion_Action * 2
				  minion_Time = time_Seconds/minion_FA
				  round_minion_time = int(minion_Time)
				  iron_Price = float(bz_Data["products"]["IRON_INGOT"]["sell_summary"][0]["pricePerUnit"])
				  drop = 3
				  eye_Drop = 1
				  iron_Drop = 0
				  for n in range(round_minion_time):
					  iron_RNG = random.randint(1,10)
					  if iron_RNG >= 8:
						  iron_Drop = iron_Drop + 1
					  else:
						  iron_Drop = iron_Drop + 0
				  all_slayer_Price = (iron_Drop * iron_Price) + ((minion_Time * drop)* string_Price) + ((minion_Time * eye_Drop)* eye_Price)
	  if category == "Farming" or category == "farming":
		  if minion == "wheat" or minion == "Wheat":
			  minion_Action = farming_list_15[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["WHEAT"]["sell_summary"][0]["pricePerUnit"])
			  price2 = float(bz_Data["products"]["SEEDS"]["sell_summary"][0]["pricePerUnit"])
			  drop2 = 1
		  if minion == "Carrot" or minion == "carrot" or minion == "potato" or minion == "Potato":
			  minion_Action = farming_list_20[minion_Tier]
			  if minion == "Carrot" or minion == "carrot":
				  drop = 3
				  price = float(bz_Data["products"]["CARROT_ITEM"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "potato" or minion == "Potato":
				  drop = 3
				  price = float(bz_Data["products"]["POTATO_ITEM"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Pumpkin" or minion == "pumpkin":
			  minion_Action = farming_list_32[minion_Tier]
			  drop = 2
			  price = float(bz_Data["products"]["PUMPKIN"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Melon" or minion == "melon":
			  minion_Action = farming_list_24[minion_Tier]
			  drop = 9
			  price = float(bz_Data["products"]["MELON"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Mushroom" or minion == "mushroom":
			  minion_Action = farming_list_30[minion_Tier]
			  minion_FA = minion_Action * 2
			  minion_Time = time_Seconds/minion_FA
			  round_minion_time = int(minion_Time)
			  red_Price = float(bz_Data["products"]["RED_MUSHROOM"]["sell_summary"][0]["pricePerUnit"])
			  brown_Price = float(bz_Data["products"]["BROWN_MUSHROOM"]["sell_summary"][0]["pricePerUnit"])
			  red_Drop = 0
			  brown_Drop = 0
			  for n in range(round_minion_time):
				  rng_Drop = random.randint(1,10)
				  if rng_Drop <= 5:
					  red_Drop = red_Drop + 1
				  if rng_Drop > 5:
					  brown_Drop = brown_Drop + 1
			  all_farm_Price = (red_Drop * red_Price) + (brown_Drop * brown_Price)
		  if minion == "Cocoa" or minion == "cocoa" or minion == "cactus" or minion == "Cactus":
			  minion_Action = farming_list_27[minion_Tier]
			  drop = 3
			  price = float(bz_Data["products"]["INK_SAC:3"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Sugar" or minion == "sugar":
			  minion_Action = farming_list_22[minion_Action]
			  drop = 3
			  price = float(bz_Data["products"]["SUGAR_CANE"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "cow" or minion == "Cow" or minion == "Sheep" or minion == "sheep" or minion == "pig" or minion == "Pig" or minion == "Rabbit" or minion == "rabbit" or minion == "Chicken" or minion == "chicken":
			  minion_Action = farming_list_26[minion_Tier]
			  if minion == "cow" or minion == "Cow":
				  price = float(bz_Data["products"]["RAW_BEEF"]["sell_summary"][0]["pricePerUnit"])
				  price2 = float(bz_Data["products"]["LEATHER"]["sell_summary"][0]["pricePerUnit"])
				  drop = 1
				  drop2 = 1
			  if minion == "Sheep" or minion == "sheep":
				  price = float(bz_Data["products"]["MUTTON"]["sell_summary"][0]["pricePerUnit"])
				  drop = 1
				  price2 = 2
				  drop2 = 1
			  if minion == "pig" or minion == "Pig":
				  drop = 1
				  price = float(bz_Data["products"]["PORK"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "Rabbit" or minion == "rabbit":
				  drop = 1
				  minion_FA = minion_Action * 2
				  minion_Time = time_Seconds/minion_FA
				  round_minion_time = int(minion_Time)
				  hide_Price = float(bz_Data["products"]["RABBIT_HIDE"]["sell_summary"][0]["pricePerUnit"])
				  foot_Price = float(bz_Data["products"]["RABBIT_FOOT"]["sell_summary"][0]["pricePerUnit"])
				  raw_Price = float(bz_Data["products"]["RABBIT"]["sell_summary"][0]["pricePerUnit"])
				  hide_Drop = 0
				  foot_Drop = 0
				  for n in range(round_minion_time):
					  rng_Drop = random.randint(0,100)
					  if rng_Drop <= 35:
						  hide_Drop = hide_Drop + 1
					  if rng_Drop >= 75:
						  foot_Drop = foot_Drop + 1
				  all_farm_Price = (raw_Price * drop * minion_Time) + (hide_Price * hide_Drop) + (foot_Price * foot_Drop)
			  if minion == "Chicken" or minion == "chicken":
				  price = float(bz_Data["products"]["RAW_CHICKEN"]["sell_summary"][0]["pricePerUnit"])
				  price2 = float(bz_Data["products"]["FEATHER"]["sell_summary"][0]["pricePerUnit"])
				  drop = 1
				  drop2 = 1
				  condition = str(input("\nDo you have an enchanted egg equipped? Yes or No?\nCommand: "))
				  if condition == "Yes" or condition == "yes" or condition == "Y" or condition == "y":
					  additional_Price = float(bz_Data["products"]["ENCHANTED_EGG"]["sell_summary"][0]["pricePerUnit"])/144
					  additional_Drop = 1
		  if minion == "Nether" or minion == "nether" or minion == "Netherwart" or minion == "netherwart":
			  minion_Action = farming_list_50[minion_Tier]
			  drop = 3
			  price = float(bz_Data["products"]["NETHER_STALK"]["sell_summary"][0]["pricePerUnit"])
	  if category == "Fishing" or category == "fishing":
		  if minion == "Clay" or minion == "clay":
			  minion_Action = fishing_list_32[minion_Tier]
			  drop = 4
			  price = float(bz_Data["products"]["CLAY_BALL"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Fish" or minion == "fish" or minion == "Fishing" or minion == "fishing":
			  minion_Action = fishing_list_78[minion_Tier]
			  minion_FA = minion_Action * 2
			  minion_Time = time_Seconds/minion_FA
			  fish_Price = float(bz_Data["products"]["RAW_FISH"]["sell_summary"][0]["pricePerUnit"])
			  salmon_Price = float(bz_Data["products"]["RAW_FISH:1"]["sell_summary"][0]["pricePerUnit"])
			  puffer_Price = float(bz_Data["products"]["RAW_FISH:3"]["sell_summary"][0]["pricePerUnit"])
			  clown_Price = float(bz_Data["products"]["RAW_FISH:2"]["sell_summary"][0]["pricePerUnit"])
			  crystal_Price = float(bz_Data["products"]["PRISMARINE_CRYSTALS"]["sell_summary"][0]["pricePerUnit"])
			  shard_Price = float(bz_Data["products"]["PRISMARINE_SHARD"]["sell_summary"][0]["pricePerUnit"])
			  sponge_Price = float(bz_Data["products"]["SPONGE"]["sell_summary"][0]["pricePerUnit"])
			  round_minion_time = int(minion_Time)
			  fish_Drop = 0
			  salmon_Drop = 0
			  puffer_Drop = 0
			  clown_Drop = 0
			  crystal_Drop = 0
			  shard_Drop = 0
			  sponge_Drop = 0
			  for n in range(round_minion_time):
				  rng_Drop = random.randint(1,100)
				  if rng_Drop >= 50:
					  fish_Drop = 1 + fish_Drop
				  if 50 < rng_Drop <= 75:
					  salmon_Drop = 1 + salmon_Drop
				  if 75 < rng_Drop <= 87:
					  puffer_Drop = 1 + puffer_Drop
				  if 87 < rng_Drop <= 91:
					  clown_Drop = 1 + clown_Drop
				  if 91 < rng_Drop <= 94:
					  crystal_Drop = 1 + crystal_Drop
				  if 94 < rng_Drop <= 97:
					  shard_Drop = 1 + shard_Drop
				  if 97 < rng_Drop <= 100:
					  sponge_Drop = 1 + sponge_Drop
			  allfish_Price = fish_Drop * fish_Price
			  allsalmon_Price = salmon_Drop * salmon_Price
			  allpuffer_Price = puffer_Price * puffer_Drop
			  allclown_Price = clown_Price * clown_Drop
			  allcrystal_Price = crystal_Price * crystal_Drop
			  allshard_Price = shard_Price * shard_Drop
			  allSponge_Price = sponge_Price * sponge_Drop
			  all_fish_Price = allfish_Price + allsalmon_Price + allpuffer_Price + allclown_Price + allcrystal_Price + allshard_Price + allSponge_Price
	  if category == "Mining" or category == "mining":
		  if minion == "Sand" or minion == "sand" or minion == "Gravel" or minion == "gravel" or minion == "flint" or minion == "Flint" or minion == "Endstone" or minion == "endstone" or minion == "end" or minion == "End":
			  if minion == "Sand" or minion == "sand":
				  price = float(bz_Data["products"]["SAND"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "Gravel" or minion == "gravel" or minion == "flint" or minion == "Flint":
				  price = float(bz_Data["products"]["FLINT"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "Endstone" or minion == "endstone" or minion == "end" or minion == "End":
				  price = float(bz_Data["products"]["ENDER_STONE"]["sell_summary"][0]["pricePerUnit"])
			  minion_Action = mining_list_26[minion_Tier]
			  drop = 1
		  if minion == "Cobble" or minion == "Cobble" or minion == "Cobblestone" or minion == "cobblestone" or minion == "Ice" or minion == "ice":
			  minion_Action = mining_list_14[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["COBBLESTONE"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Coal" or minion == "coal":
			  minion_Action = mining_list_15[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["COAL"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Iron" or minion == "iron":
			  minion_Action = mining_list_17[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["IRON_INGOT"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Gold" or minion == "gold":
			  minion_Action = mining_list_22[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["GOLD_INGOT"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Diamond" or minion == "diamond":
			  minion_Action = dmining_list_29[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["DIAMOND"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Lapis" or minion == "lapis" or minion == "red" or minion == "Red" or minion == "Redstone" or minion == "redstone":
			  minion_Action = mining_list_29[minion_Tier]
			  if minion == "Lapis" or minion == "lapis":
				  drop = 6
				  price = float(bz_Data["products"]["INK_SACK:4"]["sell_summary"][0]["pricePerUnit"])
			  else:
				  drop = 4.5
				  price = float(bz_Data["products"]["REDSTONE"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "emerald" or minion == "Emerald":
			  minion_Action = mining_list_28[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["EMERALD"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Quartz" or minion == "quartz":
			  minion_Action = mining_list_22_5[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["QUARTZ"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Obsidian" or minion == "obsidian":
			  minion_Action = mining_list_45[minion_Tier]
			  drop = 1
			  price = float(bz_Data["products"]["OBSIDIAN"]["sell_summary"][0]["pricePerUnit"])
		  if minion == "Glow" or minion == "glow" or minion == "Glowstone" or minion == "glowstone":
			  minion_Action = mining_list_25[minion_Tier]
			  drop = 3
			  price = float(bz_Data["products"]["GLOWSTONE_DUST"]["sell_summary"][0]["pricePerUnit"])
	  if category == "Foraging" or category == "foraging":
		  if minion == "Oak" or minion == "oak" or minion == "Spruce" or minion == "spruce" or minion == "Dark" or minion == "dark" or minion == "Dark Oak" or minion == "dark oak" or minion == "Dark oak" or minion == "dark Oak" or minion == "Birch" or minion == "birch" or minion == "Acacia" or minion == "acacia" or minion == "Jungle" or minion == "jungle":
			  minion_Action = foraging_list_48[minion_Tier]
			  drop = 4
			  if minion == "Oak" or minion == "oak":
				   price = float(bz_Data["products"]["LOG"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "Spruce" or minion == "spruce":
				  price = float(bz_Data["products"]["LOG:1"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "Dark" or minion == "dark" or minion == "Dark Oak" or minion == "dark oak" or minion == "Dark oak" or minion == "dark Oak":
				  price = float(bz_Data["products"]["LOG_2:1"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "Birch" or minion == "birch":
				  price = float(bz_Data["products"]["LOG:2"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "Acacia" or minion == "acacia":
				  price = float(bz_Data["products"]["LOG_2"]["sell_summary"][0]["pricePerUnit"])
			  if minion == "Jungle" or minion == "jungle":
				  price = float(bz_Data["products"]["LOG:3"]["sell_summary"][0]["pricePerUnit"])
	  if category == "Other" or category == "others" or category == "Others" or category == "other":
		  if minion == "Snow" or minion == "snow":
			  minion_Action = other_list_13[minion_Tier]
			  drop = 4
			  price = 1
		  if minion == "Flower" or minion == "flower":
			  minion_Action = other_list_30[minion_Tier]
			  drop = 1
			  price = 1
	  minion_FA = minion_Action * 2
	  minion_Time2 = time_Seconds / minion_FA
	  all_Price = all_fish_Price + all_spiderPrice + all_slayer_Price + all_farm_Price + ((minion_Time2 * drop)* price) + ((minion_Time2 * drop2)* price2) + ((minion_Time2 * additional_Drop)* additional_Price)
	  if time_Format == "Days" or time_Format == "days":
		  print("\nYou will earn", all_Price,"coins in", time_Days, "days")
	  if time_Format == "Hours" or time_Format == "hours" or time_Format == "Hour" or time_Format == "hour":
		  print("\nYou will earn", all_Price,"coins in", time_Hours, "hours")
  #
  if x == 1:
	  print("\nWelcome to the Skyblocks Calculator, a project developed by Sub01!\n\nFeel free to check out my forums page as well!\nhttps://hypixel.net/members/thelapissub01.3848075/")
	  greeting()
	  if data_1 == "ehp" or data_1 == "Ehp":
		  print("\nWelcome to the EHP Calculator!\n")
		  ehp()
	  if data_1 == "dmg" or data_1 == "Dmg":
		  print("\n Welcome to the Damage Calculator!\n")
		  damage()
	  if data_1 == "ability" or data_1 == "Ability":
		  print("\nWelcome to the Ability Damage Calculator!\n")
		  ability()
	  if data_1 == "minion" or data_1 == "minions" or data_1 == "Minion" or data_1 == "Minion":
		  print("\nWelcome to the Minion Profit Calculator!\n")
		  minion()
	  if data_1 == "exit" or data_1 == "Exit":
		  sys.exit()
  if x > 1:
	  data_2 = str(input("\nWould you like to continue with the calculator? Yes or No\nCommand: "))
	  if data_2 == "Yes" or data_2 == "yes" or data_2 == "y" or data_2 == "Y":
		  greeting()
		  if data_1 == "ehp" or data_1 == "Ehp":
			  print("\nWelcome to the EHP Calculator!\n")
			  ehp()
		  if data_1 == "dmg" or data_1 == "Dmg":
		      print("\n Welcome to the Damage Calculator!\n")
		      damage()
		  if data_1 == "ability" or data_1 == "Ability":
		      print("\nWelcome to the Ability Damage Calculator!\n")
		      ability()
		  if data_1 == "minion" or data_1 == "minions" or data_1 == "Minion" or data_1 == "Minion":
		      print("\nWelcome to the Minion Profit Calculator!\n")
		      minion()
		  if data_1 == "exit" or data_1 == "Exit":
		      sys.exit()
	  if data_2 == "No" or data_2 == "no" or data_2 == "n" or   data_2 == "N":
		  print("\nI hope you have enjoyed using this calculator! See you again!\n")
		  sys.exit()
  x += 1
