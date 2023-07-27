import json
from time import sleep
from jsonschema import validate

BIRD_PROPERTY_COUNT = 55 # when new required properties are added to a birds.json element, increment this number
SCHEMA = {
    "properties": {
        "name": {"type": "string"},
        "scientific_name": {"type": "string"},
        "expansion": {"type": "string"},
        "name": {"type": "string"},
        "power_color": {"type": "string"},
        "power_text": {"type": "string"},
        
        "__description1__": {"type": "string"},
        "predator": {"type": "boolean"},
        "flocking": {"type": "boolean"},
        "bonus_card": {"type": "boolean"},
        
        "victory_points": {"type": "integer"},

        "nest_type": {"type": "string"},
        "egg_capacity": {"type": "integer"},
        "wingspan": {"type": "integer"},

        "__description2__": {"type": "string"},
        "forest": {"type": "boolean"},
        "grasslands": {"type": "boolean"},
        "wetlands": {"type": "boolean"},

        "__description3__": {"type": "string"},
        "invertebrate": {"type": "integer"},
        "seed": {"type": "integer"},
        "fish": {"type": "integer"},
        "fruit": {"type": "integer"},
        "rodent": {"type": "integer"},
        "nectar": {"type": "integer"},
        "wild": {"type": "integer"},
        
        "__description4__": {"type": "string"},
        "/_food_cost": {"type": "boolean"},

        "__description5__": {"type": "string"},
        "*_food_cost": {"type": "boolean"},

        "total_food_cost": {"type": "integer"},

        "__description6__": {"type": "string"},
        "anatomist": {"type": "boolean"},
        "cartographer": {"type": "boolean"},
        "historian": {"type": "boolean"},
        "photographer": {"type": "boolean"},
        "backyard_birder": {"type": "boolean"},
        "bird_bander": {"type": "boolean"},
        "bird_counter": {"type": "boolean"},
        "bird_feeder": {"type": "boolean"},
        "diet_specialist": {"type": "boolean"},
        "enclosure_builder": {"type": "boolean"},
        "falconer": {"type": "boolean"},
        "fishery_manager": {"type": "boolean"},
        "food_web_expert": {"type": "boolean"},
        "forester": {"type": "boolean"},
        "large_bird_specialist": {"type": "boolean"},
        "nest_box_builder": {"type": "boolean"},
        "omnivore_expert": {"type": "boolean"},
        "passerine_specialist": {"type": "boolean"},
        "platform_builder": {"type": "boolean"},
        "prairie_manager": {"type": "boolean"},
        "rodentologist": {"type": "boolean"},
        "viticulturist": {"type": "boolean"},
        "wetland_scientist": {"type": "boolean"},
        "wildlife_gardener": {"type": "boolean"}
    },
    "additionalProperties": False,
    "minProperties": BIRD_PROPERTY_COUNT
}

EXPANSIONS = [] #TODO: populate this list

def bird_init() -> list:
    bird_list = []
    #TODO: add user input requesting used expansions
    with open(".\\data\\birds.json", 'r') as data:
        birds = json.load(data)
        for i, bird in enumerate(birds):
            try:
                validate(instance=bird, schema=SCHEMA)
                bird_list.append(bird)
                print("Validated", bird["name"], "             ", end="\r") # whitespace added to avoid "leftover" characters
                sleep(0.5)
                #TODO: skip over template and all non-included expansions
                #TODO: add bird to list in memory and tie it to its function
            except:
                try:
                    print("Invalid entry in birds.json at index", i, "- bird named", bird["name"], "- skipping...")
                except:
                    print("Invalid entry in birds.json at index", i, "- no name found - skipping...")
        
    return bird_list