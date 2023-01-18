import random

head = ["afro", "bangs", "bangs2", "bantuKnots", "bear", "bun", "bun2", "buns", 
          "cornrows", "cornrows2", "dreads1", "dreads2", "flatTop", "flatTopLong", 
          "grayBun", "grayMedium", "grayShort", "hatBeanie", "hatHip", "hijab", "long", 
          "longAfro", "longBangs", "longCurly", "medium1", "medium2", "medium3", "mediumBangs", 
          "mediumBangs2", "mediumBangs3", "mediumStraight", "mohawk", "mohawk2", "noHair1", "noHair2", 
          "noHair3", "pomp", "shaved1", "shaved2", "shaved3", "short1", "short2", "short3", "short4", "short5", "turban", "twists", "twists2"]

face = ["awe", "calm", "cheeky", "concernedFear", "contempt", "cute", "cyclops", "driven", "eatingHappy", 
          "explaining", "lovingGrin1", "lovingGrin2", "monster", "old", "smile", "smileBig", "smileLOL", "smileTeethGap", "solemn"]

facial_hair = ["chin", "full", "full2", "full3", "full4", "goatee1", "goatee2", "moustache1", "moustache2", 
                "jmoustache3", "moustache4", "moustache5", "moustache6", "moustache7", "moustache9"]

accessories = ["glasses", "glasses2", "glasses3", "glasses4", "glasses5"]

skin_color = ["variant01", "variant02", "variant03"]

clothing_color = ["red01", "orange01", "yellow01", "green01", "tail01", "lue01", "pink01"]

hair_color = ["variant01", "variant02", "variant03", "variant04", "variant05", "variant06", "variant07", "variant08", "variant09", "variant10"]


def open_peeps_icon():
  icon = {
    "head" : None,
    "face" : None,
    "facial_hair" : None,
    "accessories" : None,
    "skin_color" : None,
    "clothing_color" : None,
    "hair_color" : None,
  }
  
  icon["head"] = random.choice(head)
  icon["face"] = random.choice(face)

  if 3 >= random.randint(1, 10):
    icon["facial_hair"] = random.choice(facial_hair)

  if 3 >= random.randint(1, 10):
    icon["accessories"] = random.choice(accessories)

  icon["skin_color"] = random.choice(skin_color)
  icon["clothing_color"] = random.choice(clothing_color)

  #髪色を指定のものだけにするか？
  icon["hair_color"] = random.choice(hair_color)

  return icon
