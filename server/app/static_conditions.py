from .extensions import db
from .models.condition import Condition

#This file adds static conditions to the database upon creation
STATIC_CONDITIONS = [
    {"name": "Blessed", 
     "description": "A blessed creature adds a 1d4 to all attack rolls and saving throws.", 
     "is_debuff": False},
    {"name": "Blinded", 
     "description": "A blinded creature can’t see and automatically fails any ability check that requires sight. Attack rolls against the creature have advantage, and the creature’s attack rolls have disadvantage.", 
     "is_debuff": True},
     {"name": "Charmed", 
     "description": "A charmed creature can’t attack the charmer or target the charmer with harmful abilities or magical effects. The charmer has advantage on any ability check to interact socially with the creature.", 
     "is_debuff": True},
     {"name": "Deafened", 
     "description": "A deafened creature can’t hear and automatically fails any ability check that requires hearing.", 
     "is_debuff": True},
     {"name": "Frightened", 
     "description": "A frightened creature has disadvantage on ability checks and attack rolls while the source of its fear is within line of sight. The creature can’t willingly move closer to the source of its fear.", 
     "is_debuff": True},
    {"name": "Grappled", 
     "description": "A grappled creature’s speed becomes 0, and it can’t benefit from any bonus to its speed. The condition ends if the grappler is incapacitated. The condition also ends if an effect removes the grappled creature from the reach of the grappler or grappling effect, such as when a creature is hurled away by the thunderwave spell.", 
     "is_debuff": True},
     {"name": "Inspired", 
     "description": "An inspired creature is given a bardic inspiration die by a bard, and can add that die to an attack roll, ability check, or saving throw.", 
     "is_debuff": False},
     {"name": "Incipacitated", 
     "description": "An incapacitated creature can’t take actions or reactions.", 
     "is_debuff": True},
     {"name": "Invisible", 
     "description": "An invisible creature is impossible to see without the aid of magic or a special sense. For the purpose of hiding, the creature is heavily obscured. The creature’s location can be detected by any noise it makes or any tracks it leaves. Attack rolls against the creature have disadvantage, and the creature’s attack rolls have advantage.", 
     "is_debuff": False},
     {"name": "Paralyzed", 
     "description": "A paralyzed creature is incapacitated (see the condition) and can’t move or speak. The creature automatically fails Strength and Dexterity saving throws. Attack rolls against the creature have advantage. Any attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.", 
     "is_debuff": True},
     {"name": "Poisoned", 
     "description": "A poisoned creature has disadvantage on attack rolls and ability checks.", 
     "is_debuff": True},
     {"name": "Prone", 
     "description": "A prone creature’s only movement option is to crawl, unless it stands up and thereby ends the condition. The creature has disadvantage on attack rolls. An attack roll against the creature has advantage if the attacker is within 5 feet of the creature. Otherwise, the attack roll has disadvantage.", 
     "is_debuff": True},
     {"name": "Restrained", 
     "description": "A restrained creature’s speed becomes 0, and it can’t benefit from any bonus to its speed. Attack rolls against the creature have advantage, and the creature’s attack rolls have disadvantage. The creature has disadvantage on Dexterity saving throws.", 
     "is_debuff": True},
     {"name": "Stunned", 
     "description": "A stunned creature is incapacitated (see the condition), can’t move, and can speak only falteringly. The creature automatically fails Strength and Dexterity saving throws. Attack rolls against the creature have advantage.", 
     "is_debuff": True},
     {"name": "Unconscious", 
     "description": "An unconscious creature is incapacitated (see the condition), can’t move or speak, and is unaware of its surroundings. The creature drops whatever it’s holding and falls prone. The creature automatically fails Strength and Dexterity saving throws. Attack rolls against the creature have advantage. Any attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.", 
     "is_debuff": True}
]

def seed_conditions():
    if Condition.query.first():
        return  

    else:
        db.session.add_all([Condition(**cond) for cond in STATIC_CONDITIONS])
        db.session.commit()