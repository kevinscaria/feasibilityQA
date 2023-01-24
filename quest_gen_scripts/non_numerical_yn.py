import util
import random
import pprint
import numpy as np


def human_food(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "food_object"
    knowledge = "Humans can eat plant and meat based food like spinach, chicken etc."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has come from college and was very hungry. He started eating his favorite meal.",
            "After returning from playing football, {name} was very hungry. He started eating his favorite meal.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The meal could not have been ceramic bowl.",
        ]

        false_hypotheses = [
            "The meal could have been ceramic bowl.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the meal?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["ceramic bowl", "spinach", "plane", "football"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def flammable_object(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "flammable_object"
    knowledge = "Water is not flammable where as gasoline, acetone and alcohol are flammable."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is was driving his car and was going to a petrol station to fill his car. The petrol pump manager told {name} not to light a lighter as he was near flammable substances.",
            "The science teacher while demonstrating an experiment told {name} to be careful with the lighter as he was near flammable substances.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "Gasoline could be the flammable substance.",
        ]

        false_hypotheses = [
            "Water could be the flammable substance.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the flammable substance?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["gasoline", "acetone", "water", "alcohol"],
            answers_list=[0, 1, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def flash_point(repetition_count):
    binary_instances = []
    mcq_instances = []
    category, subcategory = "non_numerical", "flammable_object"
    knowledge = "Chemicals with higher flash points are less hazardous than chemicals with lower flash points and water does not have a flash point."
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} have to use a non-hazardous chemical to clean his car.",
            "To clean a rusty old pipe, {name} decided to use a non-hazardous chemical.",
        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)
        true_hypotheses = [
            "The chemical could be water.",
        ]
        false_hypotheses = [
            "The chemical could be acetone.",
        ]
        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )
        question_template = random.choice([
            "What could be the non hazadrous chemical?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["gasoline", "acetone", "water", "alcohol"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def filament_object(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "filament_object"
    knowledge = "Copper cannot be used for making filaments of bulb where as Tungsten, Platinum, and Rhenium can be used for the same task."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a middle school student and has just started reading about electricity. He was curious about the bulbs and how different metals can be used as filament. He used a metal to create a filament and it lighted up brightly.",
            "A scientist was working on a bulb and he was curious about the metals that can be used as filament. He used a metal to create a filament and it lighted up brightly.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "Tungsten could be the metal used.",
        ]

        false_hypotheses = [
            "Copper could not be the metal used.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the metal used as filament?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["copper", "tungsten", "platinum", "rhenium"],
            answers_list=[1, 2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def pollination_plant(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "pollination_plant"
    knowledge = "Pollination is an essential part of plant reproduction. Pollen from a flower's anther rubs or drops onto a pollinator. Methods like binary fission are not used for plant reproduction."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a child playing with flowers and he observed that over spring season the number of flowers increased. He asked his mother about it and she answered that they reproduce by sending their pollen to an anther via air.",
            "The number of flowers in spring increased rapidly. He understood this was a reproduction mechanism where pollens are sent to the anther via air.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The reproduction method could be pollination.",
        ]

        false_hypotheses = [
            "The reproduction method could be binary fission.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the reproduction process in plants?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["pollination", "binary fission",
                          "multiple fission", "regeneration"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def gas_balloon(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "gas_balloon"
    knowledge = "A gas balloon is a balloon that rises and floats in the air because it is filled with a gas lighter than air like helium, hydrogen, and neon."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s birthday is in two days and she wants balloons that rise up in her birthday party.",
            "Two days from now is {name}'s anniversary. She wants balloons that rise up into the air in her birthday party.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The gas inside the balloon could be helium.",
        ]

        false_hypotheses = [
            "The gas inside the balloon could be oxygen.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the gas used in the gas balloons?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["helium", "hydrogen", "oxygen", "neon"],
            answers_list=[0, 1, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def fuel_car(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "fuel_car"
    knowledge = "The majority of motor vehicles worldwide are powered by gasoline or diesel. "

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was going on a trip to Grand Canyon and suddenly the car ran out of fuel. He had to walk to a nearest gas station to get that fuel in a container.",
            "The car ran out of fuel thus {name} had to walk to the nearest gas station to get that fuel in a container.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The container could contain gasoline.",
        ]

        false_hypotheses = [
            "The container could contain air.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be in the container?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["gasoline", "diesel", "air", "biodiesel"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def building_material(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "building_material"
    knowledge = "Cement is mainly used as a binder in concrete, which is a basic material for all types of construction, including housing, roads, schools, hospitals, dams and ports, "

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has won the contract for the construction of a port and is now finalizing the materials including a binder which is the primary ingredient for the construction.",
            "The binder is the primary ingredient for the construction of the any building or RCC structure.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The ingredient could be cement.",
        ]

        false_hypotheses = [
            "The ingredient could be oxygen.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the ingredient?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cement", "hydrogen", "oxygen", "neon"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def water_float(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "water_float"
    knowledge = "Objects like apples, wood, and sponges are less dense than water and they will float in water. Many hollow things like empty bottles, balls, and balloons will also float. That's because air is less dense than water."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is in a swimming pool and he threw an object into water which sunk.",
            "When {name} was crossing a river, he threw an object into water which sunk.",

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could not be a wooden log.",
        ]

        false_hypotheses = [
            "The object could be a wooden log.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the object?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["balloon", "apple", "coin", "marble"],
            answers_list=[2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def chair_object(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "chair_object"
    knowledge = "Chairs can be made from wood, metal, or other strong materials, like stone or acrylic."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is building a chair for his school project using a strong material.",
            "{name} wanted a stool for his home and he asked the carpenter to use a strong material.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The material could be wood.",
        ]

        false_hypotheses = [
            "The material could be water.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the material?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["wood", "metal", "paper", "cloth"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def thermo_liquid(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "thermo_liquid"
    knowledge = "Mercury is one of the most familiar materials used in liquid thermometers. Other liquids, such as kerosene or ethanol, may also be used in thermometers. Water cannot be used in a liquid thermometer."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is working in a chemistry lab and studying the liquids that could be used in liquid thermometers and their properties.",
            "{name} is studying the properties of the liquids that could be used in liquid thermometers.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The liquid could be mercury.",
        ]

        false_hypotheses = [
            "The liquid could not be water.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the liquid?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["mercury", "ethanol", "kerosene", "water"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def fire_extinguish(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "fire_extinguish"
    knowledge = "Water or foam fire extinguishers can be used to extinguish Class A fire which is primarily composed of combustible substances like paper, wood, cloth, and plastics. Carbon dioxide fire extinguishers can be used to extinguish class B fires like those involving flammable liquids such as paraffin or petrol."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A fire broke in the kitchen. {name} is a fire fighter and has to pack a fire extinguisher based on the type of fire. {name} got the information that the fire was started because of wooden logs.",
            "A fire started due to wooden logs in the kitchen. {name} is a fire fighter and has to pack a fire extinguisher best suitable for the situation.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "Water could be used as the fire extinguisher in this case.",
        ]

        false_hypotheses = [
            "Carbondioxide fire extinguisher could be used in this case.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the extinguisher?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["water", "foam", "sand", "blanket"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def swim_animal(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "swim_animal"
    knowledge = "Camels, giraffes, porcupines, rhinos can't swim. Camels and giraffes are not exposed to such deep water during their lifetime due to their height and hence their physical adaptations were mainly focused on rest."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was learning about animal evolution and was trying to figure out how different land animals have special characteristics like swimming or increased height. He saw that a particular animal cannot swim at all and had a particularly long neck.",
            "{name} was reading a children's book and saw the picture of a particular animal that cannot swim and had a particularly long neck.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be giraffe.",
        ]

        false_hypotheses = [
            "The animal could be crocodile.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the animal?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["crocodile", "camel", "rhino", "giraffe"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def desert_and_plants(repetition_count):
    binary_instances = []
    mcq_instances = []
    category, subcategory = "non_numerical", "desert_and_plants"
    knowledge = "Cacti and Succulents can grow in desert regions where as plants like lotus, willow trees cannot grow in desert regions."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} visited the Sahara desert as part of his research expedition to study desert plants and their living conditions.",
            "In the trip to dubai, {name} went for a dessert safari and saw a lot of desert plants.",
        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)
        true_hypotheses = [
            "The plant could be cactus.",
        ]
        false_hypotheses = [
            "The plant could be lotus.",
        ]
        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )
        question_template = random.choice([
            "What could be the plant?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cactus", "lotus", "willow", "succulent"],
            answers_list=[0, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def cell_and_waves(repetition_count):
    binary_instances = []
    mcq_instances = []
    category, subcategory = "non_numerical", "cell_and_waves"
    knowledge = "Cell phones use radio waves to communicate with cell towers, and these waves have wavelengths of approximately 10-1000 m. Cell phone encodes the sounds of the caller's voice in microwaves by changing the frequency of the waves."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There is a cell phone company named after {name}. They have started a new communications lab for research and development where they made a prototype of cell phone communication with cell towers using certain waves.",
            "{name} proposed using a certain electromagnetic wave for a new cell phone communication line in under developed areas. "
        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)
        true_hypotheses = [
            "The waves could be radio waves.",
        ]
        false_hypotheses = [
            "The waves could be sound waves.",
        ]
        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )
        question_template = random.choice([
            "What could be the type of the waves?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["radio waves", "sound waves", "light waves"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def bullet_and_object(repetition_count):
    binary_instances = []
    mcq_instances = []
    category, subcategory = "non_numerical", "bullet_and_object"
    knowledge = "Gun powder is the propellant that provides the energy needed to force the bullet out of the barrel and into the target"
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a pyrotechnics expert who studies ballistics of bullets. For his experiment, he fires a bullet where a material is used to force the bullet out of the barrel.",
            "In a chemsitry class, {name} was told that a certain material can be used to force a bullet out of the barrel in a gun.",

        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)
        true_hypotheses = [
            "The material could be gun powder.",
        ]
        false_hypotheses = [
            "The material could be air.",
        ]
        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )
        question_template = random.choice([
            "What could be the material?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["gun powder", "oxygen", "nitrogen", "air"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def plant_and_photosynthesis(repetition_count):
    binary_instances = []
    mcq_instances = []
    category, subcategory = "non_numerical", "plant_and_photosynthesis"
    knowledge = "Photosynthesis is the process by which plants use sunlight, water, and carbon dioxide to create oxygen and energy in the form of sugar."
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is being taught photosynthesis in his biology class and is given a project to observe a plant for 5 days. He saw that some materials in its surroundings are being depleted as days go by.",
            "In a class, {name} was given a plant to observe for 5 days. He saw that some materials in its surroundings are being depleted as days go by.",
        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)
        true_hypotheses = [
            "The material could be water.",
        ]
        false_hypotheses = [
            "The material could be an insect.",
        ]
        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )
        question_template = random.choice([
            "What could be the material?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["water", "oxygen", "sun light", "plastic"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def covid_and_mask(repetition_count):
    binary_instances = []
    mcq_instances = []
    category, subcategory = "non_numerical", "covid_and_mask"
    knowledge = "High quality KN95, KF94, and N95 masks have the tightest fit and the best filtration to fight Covid. Cloth masks are also effective in filtering out small viral particles."
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "With the increase in covid cases due to many new variants, {name} has decided to take more precautions and use the best mask available.",
            "{name} was a medical student and he was given the task to observe a patient who is suffering from Covid-19. He saw that he was wearing a mask.",
        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)
        true_hypotheses = [
            "The mask could be N95.",
        ]
        false_hypotheses = [
            "The mask could be a cloth.",
        ]
        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )
        question_template = random.choice([
            "What could be the mask?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["N95", "paper", "flower", "leaf"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def reptile_and_habitat(repetition_count):
    binary_instances = []
    mcq_instances = []
    category, subcategory = "non_numerical", "reptile_and_habitat"
    knowledge = "Reptiles can live in land and water."
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} always wanted an animal as a gift. His father gifted him an animal that can live in land and water when he graduated from high school.",
            "In a zoo, {name} was saw an animal that can live in land and water.",
        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)
        true_hypotheses = [
            "The animal could be reptile.",
        ]
        false_hypotheses = [
            "The animal could be a crow.",
        ]
        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )
        question_template = random.choice([
            "What could be the species?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["reptile", "crow", "elephant", "cockroach"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


# if __name__ == "__main__":
#     repetition_count = 1
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = flash_point(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
