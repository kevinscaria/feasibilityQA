import util
import random
import pprint
import numpy as np


def speed_and_distance1(repetition_count):
    category, subcategory = "attribute_comparison", "speed_and_distance",
    knowledge = "distance covered is directly proportional to speed"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A bike and a car travelling in a straight line. Car is moving faster than bike with {given_value} miles/hour.",
            "A truck and a bike were travelling on a straight road. Truck was moving faster than bike with {given_value} miles/hour."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Speed of the bike could be {hyp_value} miles/hour.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the speed of the bike ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 2
def speed_and_distance2(repetition_count):
    category, subcategory = "attribute_comparison", "speed_and_distance",
    knowledge = "distance covered is directly proportional to speed"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A bike and a car travelling in a straight line. The distance covered by the car which is moving faster is {given_value} miles.",
            "A bike and a bus were going on a straight freeway. Distance covered by the bus is {given_value} miles. The bike was moving slower than the bus"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Distance covered by the bike could be {hyp_value} miles.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the distance covered by the bike ?",
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 3
def speed_and_time1(repetition_count):
    category, subcategory = "attribute_comparison", "speed_and_time",
    knowledge = "Time taken is inversely proportional to speed"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A bike and a car travelled equal distance in a straight line. The taken taken by the car which is moving faster is {given_value} minutes.",
            "Two colleague going were going to office. One of the person was travelling using bike and the other person was using car. The car which was moving faster took {given_value} minutes to reach to the office."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Time taken by the bike could be {hyp_value} minutes.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the time taken by the bike ?",
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 4
def speed_and_time2(repetition_count):
    category, subcategory = "attribute_comparison", "speed_and_time",
    knowledge = "Time taken is inversely proportional to speed"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A bike and a car travelled equal distance in a straight line. The speed of the car which took less time to travel is {given_value} miles/hour.",
            "Two colleague going were going to office. One of the person was travelling using bike and the other person was using city bus. The bus which took less time was travelling with the speed of {given_value} minutes to reach to the office."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Speed of the bike could be {hyp_value} miles/hour.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the speed of the bike ?",
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 5
def density_and_height_submerged1(repetition_count):
    category, subcategory = "attribute_comparison", "density_and_height_submerged",
    knowledge = "Submerged height of a floating object is directly proportional to density"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 60  # unit in kg/m3

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two objects floating on water have different densities. Object with higher density has submerged to a height of {given_value} meters.",
            "{name} saw two objects floating on the water. One of the object that had higher density was submerged {given_value} meters in the water."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Submerged height of the other object could be {hyp_value} meters.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the submerged height of the other object ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 6
def density_and_height_submerged2(repetition_count):
    category, subcategory = "attribute_comparison", "density_and_height_submerged",
    knowledge = "Submerged height of a floating object is directly proportional to density"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 60  # unit in kg/m3

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two objects floating on water have different densities. Object which sunk more in the water has density of {given_value} units",
            "{name} saw two objects floating on the water. One of the object that was submerged more in the water had density of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Density of the other object could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the density of the other object ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 7
def density_and_volume1(repetition_count):
    category, subcategory = "attribute_comparison", "density_and_volume",
    knowledge = "Density is inversely proportional to the volume"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two similar balls have same mass but different volumes. Volume of the ball with higher density is {given_value} units.",
            "{name} was playing with two balls that had same mass but different volumes. Volume of the ball with higher density is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of the other ball could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of the other ball ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 8
def density_and_volume2(repetition_count):
    category, subcategory = "attribute_comparison", "density_and_volume",
    knowledge = "Density is inversely proportional to the volume"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two similar balls have same mass but different volumes. Density of the ball with lower volume is {given_value} units.",
            "{name} was playing with two balls that had same mass but different volumes. Density of the ball with lower volume is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Density of the other ball could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the density of the other ball ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 9
def cylinder_bottle_volume1(repetition_count):
    category, subcategory = "attribute_comparison", "cylinder_and_volume",
    knowledge = "Volume of the cylinder is directly proportional to radius."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s has two cylindrical shaped bottles with same height. Volume of the bottle having larger radius is {given_value} units.",
            "{name}'s is distributing two water bottles at an event. Bottles are in cylindrical shape. Volume of the bottle having larger radius is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of the other bottle could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of the other bottle ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 10
def cylinder_bottle_volume2(repetition_count):
    category, subcategory = "attribute_comparison", "cylinder_and_volume",
    knowledge = "Volume of the cylinder is directly proportional to radius."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 40

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s has two cylindrical shaped bottles with same height. Radius of the bottle having lower volume is {given_value} meters.",
            "{name}'s is distributing two water bottles at an event. Bottles are in cylindrical shape. Radius of the bottle having lower volume is {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Radius of the other bottle could be {hyp_value} meters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the radius of the other bottle ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 11
def cylinder_bottle_volume3(repetition_count):
    category, subcategory = "attribute_comparison", "cylinder_and_volume",
    knowledge = "Volume of the cylinder is directly proportional to height."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 40

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s has two cylindrical shaped bottles with same radius. Height of the bottle having larger volume is {given_value} meters.",
            "{name} is filling two cylindrical shaped bottles at home. Both the bottles have same base area but different heights. One of the bottle which filled more water had height of {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Height of the other bottle could be {hyp_value} meters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the height of the other bottle ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# 11
def cylinder_bottle_volume4(repetition_count):
    category, subcategory = "attribute_comparison", "cylinder_and_volume",
    knowledge = "Volume of the cylinder is directly proportional to height."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 40

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s has two cylindrical shaped bottles with same radius. Volume of the bottle having less height is {given_value} units.",
            "{name} is filling two cylindrical shaped bottles at home. Both the bottles have same base area but different heights. One of the bottle which had less height of filled {given_value} units of water."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of the other bottle could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of the other bottle?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bottle_volume_water1(repetition_count):
    category, subcategory = "attribute_comparison", "water_and_volume",
    knowledge = "Larger volume holds lager amount of water."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 54

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s has two cylindrical shaped bottles. A bottle with higher volume holds {given_value} units of water.",
            "{name}'s is filling two bottles which are in a cylindrical shape. One of the bottles that had greater volume was filled with {given_value} units of water."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Amount of water in other bottle could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the amount of water in other bottle ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bottle_volume_water2(repetition_count):
    category, subcategory = "attribute_comparison", "water_and_volume",
    knowledge = "Larger volume holds lager amount of water."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 54

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s has two cylindrical shaped bottles. The bottle holding less amount of water has volume {given_value} units.",
            "{name}'s is filling two bottles which are in a cylindrical shape. One of the bottles that was filled with less water had volume of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of other bottle could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of the other bottle ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bottle_weight_water1(repetition_count):
    category, subcategory = "attribute_comparison", "weight_and_volume",
    knowledge = "Larger amount of water have more weight."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 54

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s has two identical cylindrical shaped bottles. The bottle holding less amount of water has {given_value} kg weight.",
            "{name}'s is filling two bottles which are in a cylindrical shape. One of the bottles that have less water weighs {given_value} kg."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Weight of other bottle could be {hyp_value} kg.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the weight of the other bottle ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bottle_weight_water2(repetition_count):
    category, subcategory = "attribute_comparison", "weight_and_volume",
    knowledge = "Larger amount of water have more weight."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 54

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s has two identical cylindrical shaped bottles. The bottle having higher weight has {given_value} units of water.",
            "{name}'s is filling two bottles which are in a cylindrical shape. One of the bottles that have more weight is filled with {given_value} units of water."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Amount of water in the other bottle could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the amount of water in other bottle ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def density_and_mass1(repetition_count):
    category, subcategory = "attribute_comparison", "density_and_mass",
    knowledge = "Density is directly proportional to the mass"

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two similar rods. Mass of rod with higher density is {given_value} units.",
            "{name} works at company which manufactures rods for construction. He has two similar rods to be transported. The mass of the rod with a higher density is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Mass of the other rod could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the mass of the other rod ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def density_and_mass2(repetition_count):
    category, subcategory = "attribute_comparison", "density_and_mass",
    knowledge = "Density is directly proportional to the mass"

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two similar rods. Density of rod with lower mass is {given_value} units.",
            "{name} works at company which manufactures rods for construction. He has two similar rods to be transported. Density of the rod with a lower weight is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Density of the other rod could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the density of the other rod ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def thickness_and_pages1(repetition_count):
    category, subcategory = "attribute_comparison", "thickness_and_pages",
    knowledge = "Number of pages in book is directly proportional to the the thickness of the book"

    binary_instances = []
    mcq_instances = []
    given_value_start = 80
    given_value_end = 300

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two 8th grade books: Physics and Chemistry. Physics book with higher thickness has {given_value} pages.",
            "{name} is preparing for his exam. He is trying to estimate how many pages he has to read from book for courses Chemistry and History. History book with higher thickness has {given_value} pages."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Number of pages in Chemistry book could be {hyp_value}.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the number of pages in Chemistry book ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def thickness_and_pages2(repetition_count):
    category, subcategory = "attribute_comparison", "thickness_and_pages",
    knowledge = "Number of pages in book is directly proportional to the the thickness of the book"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two books: Physics and Chemistry. {name} is reading book Chemistry that has a thickness of {given_value} units. It has has less number of pages than Physics book.",
            "{name} is preparing for his exam. He is trying to estimate how many pages he has to read from book for courses Physics and History. History book with less number of pages have thickness of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Thickness of Physics book could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the thickness of Physics book ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def thickness_and_weight1(repetition_count):
    category, subcategory = "attribute_comparison", "thickness_and_weight",
    knowledge = "Weight of book is directly proportional to the the thickness of the book"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 40

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two books: Physics and Chemistry. {name} is carrying heavier book which is Physics and it is {given_value} units thick.",
            "{name} is preparing for his exam for courses Chemistry and Arts. He decided to study in library instead of home. While preparing the bag he noticed that Arts book with thickness {given_value} units is heavier."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Thickness of Chemistry book could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the thickness of Chemistry book ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def thickness_and_weight2(repetition_count):
    category, subcategory = "attribute_comparison", "thickness_and_weight",
    knowledge = "Weight of book is directly proportional to the the thickness of the book"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 30

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two books: Physics and Chemistry. {name} is carrying thinner book which is Physics and has {given_value} units of weight.",
            "{name} is preparing for his exam for courses Chemistry and Arts. He decided to study in library instead of home. While preparing the bag he noticed that Arts book with less thickness weighs {given_value} units."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Weight of Chemistry book could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the weight of Chemistry book ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def radius_and_circumference1(repetition_count):
    category, subcategory = "attribute_comparison", "radius_and_circumference",
    knowledge = "Length of fence for circular garden is directly proportional to radius"

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to fence two circular shaped gardens. One garden having larger radius requires {given_value} length of fence.",
            "{name}'s friend Tom, suggested him to install a new fence to his two circular shaped gardens because Tom found some broken fence wires. {name} required {given_value} length of fence for garden with larger radius."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Length of the fence required for other garden could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the length of the fence required for other garden ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def radius_and_circumference2(repetition_count):
    category, subcategory = "attribute_comparison", "radius_and_circumference",
    knowledge = "Length of fence for circular garden is directly proportional to radius"

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to fence two circular shaped gardens. One garden that requires less fencing wire is having radius of {given_value} units.",
            "{name}'s friend Tom, suggested him to install a new fence to his two circular shaped gardens because Tom found some broken fence wires. {name} required less fencing wire for a garden having a radius of {given_value} units."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Radius of the other garden could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the radius for the other garden ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def refrigerator_and_food1(repetition_count):
    category, subcategory = "attribute_comparison", "refrigerator_and_food",
    knowledge = "Larger refrigerator occupies more food"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 40

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two unique refrigerators have different sizes. Larger refrigerator occupies {given_value} volume of food.",
            "{name} wants to buys a refrigerator that could accommodate more food. {name} went to shop to buy a refrigerator. {name} was confused among two refrigerator having different sizes. The larger refrigerator could occupy {given_value} volume of food."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The Volume of food the other refrigerator could occupy could be {hyp_value}.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of food that the other refrigerator can contain?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def gravity_and_masses1(repetition_count):
    category, subcategory = "attribute_comparison", "gravity_and_masses",
    knowledge = "Gravitational force is directly proportional to mass"

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 80

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two asteroids have different masses and are at the same distance from Earth. Gravitational pull from Earth to the heavier asteroid is {given_value} units.",
            "{name} saw on news that there are two asteroids near earth. These asteroid may hit the ground because of gravitational pull from earth. The two asteroids have different masses and are equally apart from the Earth. The gravitational pull of the Earth to the heaviest asteroid is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Gravitational pull from Earth to the other asteroid could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the gravitational pull from Earth to the other asteroid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def gravity_and_masses2(repetition_count):
    category, subcategory = "attribute_comparison", "gravity_and_masses",
    knowledge = "Gravitational force is directly proportional to mass"

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 80

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two asteroids have different masses and are at the same distance from Earth. Mass of the asteroid having less gravitational pull from Earth is {given_value} units.",
            "{name} saw on news that there are two asteroids near earth. These asteroid may hit the ground because of gravitational pull from earth. The two asteroids have different masses and are equally apart from the Earth. The asteroid which experienced less gravitational pull has mass of {given_value} units."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Mass of the other asteroid could be {hyp_value}.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the mass of the other asteroid ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def gravity_and_distance1(repetition_count):
    category, subcategory = "attribute_comparison", "gravity_and_distance",
    knowledge = "Gravitational force is inversely proportional to the distance"

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 80

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two identical asteroids are some distance away from earth. An asteroid having less gravitational pull from earth is {given_value} units of distance away.",
            "{name} is astrophysicist, he is observing two identical asteroid that are some distance away from our planet. An asteroid that is {given_value} units of distance away, have less gravitational pull from earth."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The other asteroid could be {hyp_value} distance away.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the distance of the other asteroid from Earth?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def gravity_and_distance2(repetition_count):
    category, subcategory = "attribute_comparison", "gravity_and_distance",
    knowledge = "Gravitational force is inversely proportional to distance"

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 80

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two identical asteroids are some distance away from Earth. The asteroid closer to Earth is having gravitational pull of {given_value} units.",
            "{name} is astrophysicist, he is observing two identical asteroid that are some distance away from our planet. An asteroid that is closer to the earth, have gravitational pull of {given_value} units from earth."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Gravitational pull for the other asteroid could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the gravitational pull for the other asteroid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def triangle_side_sum(repetition_count):
    category, subcategory = "attribute_comparison", "triangle_side_sum",
    knowledge = "Sum of any two side of triangle is greater than the third side"

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 80

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to fence his triangular shaped garden. {name} fenced two sides of the garden with {given_value} length of fencing wire.",
            "In a triangular shaped garden, total fencing wire used for two sides of the garden is {given_value}"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Length of the wire required for third side of garden could be {hyp_value} meters.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the length of the wire required for the third side of the garden?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def water_flow_volume1(repetition_count):
    category, subcategory = "attribute_comparison", "flow_rate_and_volume",
    knowledge = "Volume filled is directly proportional to flow rate"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical pipes which are filling water to their respective container. Container which is filled more have a pipe with a flow rate of {given_value} units.",
            "{name} is filling his two water tank. Each tank is being filled by two identical pipes. The water tank that is filled more is being filled by a pipe with flow rate of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Flow rate of other pipe could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=4,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the flow rate of other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=4,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def water_flow_volume2(repetition_count):
    category, subcategory = "attribute_comparison", "flow_rate_and_volume",
    knowledge = "Volume filled is directly proportional to flow rate"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical pipes which are filling water to their respective container. Container which is filled less have a pipe with a flow rate of {given_value} units.",
            "{name} is filling his two water tank. Each tank is being filled by two identical pipes. The water tank that is filled less is being filled by a pipe with flow rate of {given_value} units."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Flow rate of other pipe could be {hyp_value} units.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=4,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the flow rate of other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=4,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def water_flow_volume3(repetition_count):
    category, subcategory = "attribute_comparison", "flow_rate_and_volume",
    knowledge = "Volume filled is directly proportional to flow rate"

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical pipes which are filling water to their respective container. Pipe with a higher flow rate has filled {given_value} liters of water.",
            "{name} is filling his two water tank. Each tank is being filled by their respective pipe. Both the pipes are identical. Pipe with higher flow rate has filled its respective tank with {given_value} liters of water."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Water filled by other pipe could be {hyp_value} liters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of water filled by other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def water_flow_volume4(repetition_count):
    category, subcategory = "attribute_comparison", "flow_rate_and_volume",
    knowledge = "Volume filled is directly proportional to flow rate"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical pipes which are filling water to their respective container. Pipe with a lower flow rate has filled {given_value} liters of water.",
            "{name} is filling his two water tank. Each tank is being filled by their respective pipe. Both the pipes are identical. Pipe with lower flow rate has filled its respective tank with {given_value} liters of water."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Water filled by other pipe could be {hyp_value} liters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of water filled by other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def volume_radius1(repetition_count):
    category, subcategory = "attribute_comparison", "radius_and_volume",
    knowledge = "Volume filled is directly proportional to radius of the pipe"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pipes, both have same speed of water flowing through it. Pipe with a larger radius has filled {given_value} liters of water into the well.",
            "A professor is explaining to his students how water filled in a container is related to dimensions of the pipe. Professor used two pipes filling their respective well experiment to explain. He set the same velocity of flowing water to the pipe. The pipe with a larger radius has filled {given_value} liters of water into the well."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Water filled by other pipe could be {hyp_value} liters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of water filled by other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def volume_radius2(repetition_count):
    category, subcategory = "attribute_comparison", "radius_and_volume",
    knowledge = "Volume filled is directly proportional to radius of the pipe"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pipes, both have same speed of water flowing through it. Pipe with a smaller radius has filled {given_value} liters of water into the well.",
            "A professor is explaining to his students how water filled in a container is related to dimensions of the pipe. Professor used two pipes filling their respective well experiment to explain. He set the same velocity of flowing water to the pipe and started observing water filled in the wells at a particular time. The pipe with a smaller radius has filled {given_value} liters of water into the well."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Water filled by other pipe could be {hyp_value} liters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of water filled by other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def volume_area1(repetition_count):
    category, subcategory = "attribute_comparison", "area_and_volume",
    knowledge = "Volume filled is directly proportional to area of the pipe"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pipes, both have same speed of water flowing through it. Pipe with a smaller area has filled {given_value} liters of water into the well.",
            "A professor is explaining to his students how water filled in a container is related to dimensions of the pipe. Professor used two pipes filling their respective well experiment to explain. He set the same velocity of flowing water to the pipe and started observing water filled in the wells at a particular time. The pipe with a smaller area has filled {given_value} liters of water into the well."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Water filled by other pipe could be {hyp_value} liters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=8,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of water filled by other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=8,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def volume_area2(repetition_count):
    category, subcategory = "attribute_comparison", "area_and_volume",
    knowledge = "Volume filled is directly proportional to area of the pipe"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pipes, both have same speed of water flowing through it. Pipe with a larger area has filled {given_value} liters of water into the well.",
            "A professor is explaining to his students how water filled in a container is related to dimensions of the pipe. Professor used two pipes filling their respective well experiment to explain. He set the same velocity of flowing water to the pipe and started observing water filled in the wells at a particular time. The pipe with a larger area has filled {given_value} liters of water into the well."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Water filled by other pipe could be {hyp_value} liters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of water filled by other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def flow_rate_time1(repetition_count):
    category, subcategory = "attribute_comparison", "flow_rate_and_time",
    knowledge = "Time taken to fill the container is inversely proportional flow rate."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pipes, each has filled container of equal capacity. Pipe with a higher flow rate has filled the container in {given_value} minutes.",
            "{name} his filling two identical water tanks. Both water tanks have equal capacity to hold the water. One of the water tanks was filled in {given_value} minutes. This water tanks was being filled by a pipe that had a higher flow rate."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Time taken by other pipe could be {hyp_value} minutes.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=4,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the time taken by other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=4,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def flow_rate_time2(repetition_count):
    category, subcategory = "attribute_comparison", "flow_rate_and_time",
    knowledge = "Time taken to fill the container is inversely proportional flow rate."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pipes, each has filled container of equal capacity. Pipe with a less flow rate has filled the container in {given_value} minutes.",
            "{name} his filling two identical water tanks. Both water tanks have equal capacity to hold the water. One of the water tanks was filled in {given_value} minutes. This water tanks was being filled by a pipe that had a lower flow rate."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Time taken by other pipe could be {hyp_value} minutes.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the time taken by other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def flow_rate_time3(repetition_count):
    category, subcategory = "attribute_comparison", "flow_rate_and_time",
    knowledge = "Time taken to fill the container is inversely proportional flow rate."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pipes, each has filled container of equal capacity. A pipe which took less time to fill has a flow rate of {given_value} liter/minute.",
            "{name} his filling two identical water tanks. Both water tanks have equal capacity to hold the water. One of the water tanks took less time to fill. This water tanks was being filled by a pipe that had a flow rate of {given_value} liter/minute."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Flow rate of other pipe could be {hyp_value} liter/minute.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the flow rate of the other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def flow_rate_time4(repetition_count):
    category, subcategory = "attribute_comparison", "flow_rate_and_time",
    knowledge = "Time taken to fill the container is inversely proportional flow rate."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pipes, each has filled container of equal capacity. A pipe which took more time to fill has a flow rate of {given_value} liter/minute.",
            "{name} his filling two identical water tanks. Both water tanks have equal capacity to hold the water. One of the water tanks took more time to fill. This water tanks was being filled by a pipe that had a flow rate of {given_value} liter/minute."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Flow rate of other pipe could be {hyp_value} liter/minute.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the flow rate of the other pipe ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def ball_speed_height1(repetition_count):
    category, subcategory = "attribute_comparison", "speed_height",
    knowledge = "Speed of the ball near the ground is directly proportional to the height from which the ball is dropped."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls, each has been dropped from a certain height. A ball which is dropped from higher height has a speed {given_value} meter/second near ground.",
            "{name} is experimenting and he is using two identical balls, each has been fall from a certain height. A ball that falls from the highest height has a speed of {given_value} meters/second near the ground."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Speed of the other ball could be {hyp_value} meter/second.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the speed of the other ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def ball_speed_height2(repetition_count):
    category, subcategory = "attribute_comparison", "ball_speed_height",
    knowledge = "Speed of the ball near the ground is directly proportional to the height from which the ball is dropped."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls, each has been dropped from a certain height. A ball which is dropped from lower height has a speed {given_value} meter/second near the ground.",
            "In an experiment, two identical balls has been dropped from a certain height. A ball that falls from the lowest height has a speed of {given_value} meter/second near the ground."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Speed of the other ball could be {hyp_value} meter/second.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the speed of the other ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def ball_speed_height3(repetition_count):
    category, subcategory = "attribute_comparison", "ball_speed_height",
    knowledge = "Speed of the ball near the ground is directly proportional to the height from which the ball is dropped."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls, each has been dropped from a certain height. A ball that has a higher speed near the ground is dropped from height {given_value} meters.",
            "{name} dropped two identical balls from different height. A ball that has a higher speed near the ground falls from {given_value} meters high."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Height from which the other ball could have been dropped is {hyp_value} meters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the height from which the other ball could have been dropped?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def ball_speed_height4(repetition_count):
    category, subcategory = "attribute_comparison", "ball_speed_height",
    knowledge = "Speed of the ball near the ground is directly proportional to the height from which the ball is dropped."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls, each has been dropped from a certain height. A ball that has a lower speed near the ground is dropped from height {given_value} meters.",
            "{name} and his brother were observing how speed is related to the height from which it is dropped. They dropped two identical balls from different height. A ball that has a lower speed near the ground is dropped from a {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Height from which the other ball could have been dropped is {hyp_value} meters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=8,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the height from which the other ball could have been dropped?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=8,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def ball_time_height1(repetition_count):
    category, subcategory = "attribute_comparison", "ball_time_height",
    knowledge = "Time taken by the ball to hit the ground is directly proportional to the height from which the ball is dropped."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls, each has been dropped from a certain height. A ball which took more time to hit the ground is dropped from a height {given_value} meters.",
            "{name} and his brother were observing how time taken is related to the height from which it is dropped. They dropped the balls from different height. A ball that took more time to reach the ground is dropped from a {given_value} meters."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Height from which the other ball could have been dropped is {hyp_value} meters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the height from which the other ball could have been dropped?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def ball_time_height2(repetition_count):
    category, subcategory = "attribute_comparison", "ball_time_height",
    knowledge = "Time taken by the ball to hit the ground is directly proportional to the height from which the ball is dropped."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls, each has been dropped from a certain height. A ball which took less time to hit the ground is dropped from a height {given_value} meters.",
            "{name} and his brother were observing how time taken is related to the height from which it is dropped. They dropped the balls from different height. A ball that took less time to reach the ground is dropped from a {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Height from which the other ball could have been dropped is {hyp_value} meters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the height from which the other ball could have been dropped?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def ball_time_height3(repetition_count):
    category, subcategory = "attribute_comparison", "ball_time_height",
    knowledge = "Time taken by the ball to hit the ground is directly proportional to the height from which the ball is dropped."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls, each has been dropped from a certain height. A ball which was dropped from a higher height took {given_value} seconds time to hit the ground.",
            "{name} and his brother were observing how time taken is related to the height from which it is dropped. They dropped the balls from different height. A ball that was dropped from a higher height took {given_value} seconds to reach the ground."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Time taken by the other ball to hit the ground could be {hyp_value} seconds.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=4,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the height from which the other ball could have been dropped?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=4,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def ball_time_height4(repetition_count):
    category, subcategory = "attribute_comparison", "ball_time_height",
    knowledge = "Time taken by the ball to hit the ground is directly proportional to the height from which the ball is dropped."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls, each has been dropped from a certain height. A ball which was dropped from a lower height took {given_value} seconds time to hit the ground.",
            "{name} and his brother were observing how time taken is related to the height from which it is dropped. They dropped the balls from different height. A ball that was dropped from a lower height took {given_value} seconds to reach the ground."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Time taken by the other ball to hit the ground could be {hyp_value} seconds.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=4,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the height from which the other ball could have been dropped?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=4,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wall_area_paint1(repetition_count):
    category, subcategory = "attribute_comparison", "area_paint_wall",
    knowledge = "Volume of paint required is directly proportional to area of the wall."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is painting two walls in the room. A wall that has a larger area required {given_value} volume of paint.",
            "A restaurant hired a painter to paint two walls in the dining hall. The name of the painter is {name}. The painter painted the wall with larger surface area and it required {given_value} volume of paint."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of paint {name} requires to paint the other wall could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=4,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of paint {name} requires to paint the other wall?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=4,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wall_area_paint2(repetition_count):
    category, subcategory = "attribute_comparison", "area_paint_wall",
    knowledge = "Volume of paint required is directly proportional to area of the wall."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is painting two walls in the room. A wall that has a smaller area required {given_value} volume of paint.",
            "A restaurant hired a painter to paint two walls in the dining hall. The name of the painter is {name}. The painter painted the wall with less surface area using {given_value} volume of paint."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of paint {name} requires to paint the other wall could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=4,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of paint {name} requires to paint the other wall?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=4,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wall_width_paint1(repetition_count):
    category, subcategory = "attribute_comparison", "width_paint_wall",
    knowledge = "Volume of paint required is directly proportional to width of the wall."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to repaint his apartment. {name} is painting two walls in the living room in which a wall that has a larger width required {given_value} volume of paint.",
            "A restaurant hired a painter to paint two walls in the dining hall. The name of the painter is {name}. The painter painted the wall with larger width which required {given_value} volume of paint."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of paint {name} requires to paint the other wall in the living room could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of paint {name} requires to paint the other wall?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wall_width_paint2(repetition_count):
    category, subcategory = "attribute_comparison", "width_paint_wall",
    knowledge = "Volume of paint required is directly proportional to height of the wall."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 40

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to repaint his apartment. {name} is painting two walls in the living room in which a wall that less wider required {given_value} volume of paint.",
            "A restaurant hired a painter to paint two walls in the dining hall. The name of the painter is {name}. The painter painted the wall which is less wide which required {given_value} volume of paint."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of paint {name} requires to paint the other wall could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of paint {name} requires to paint the other wall?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wall_height_paint1(repetition_count):
    category, subcategory = "attribute_comparison", "height_paint_wall",
    knowledge = "Volume of paint required is directly proportional to height of the wall."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is painting two walls in the garage, both walls are equally wide. A wall that has a larger height required {given_value} volume of paint.",
            "{name} recently started his part time job as a painter. {name} was being called to his customer's apartment to repaint the two walls in the master bedroom. Both walls have equal width but different heights. A wall that has a larger height required {given_value} volume of paint."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of paint {name} requires to paint the other wall could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of paint {name} requires to paint the other wall?",
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wall_height_paint2(repetition_count):
    category, subcategory = "attribute_comparison", "height_paint_wall",
    knowledge = "Volume of paint required is directly proportional to height of the wall."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is painting two walls in the garage, both walls are equally wide. A wall that has a less height required {given_value} volume of paint.",
            "{name} recently started his part time job as a painter. {name} was being called to his customer's apartment to repaint the two walls in the master bedroom. Both walls have equal width but different height. A wall that has a less height required {given_value} volume of paint."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of paint {name} requires to paint the other wall could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=8,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of paint {name} requires to paint the other wall?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=8,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wall_paint_cost1(repetition_count):
    category, subcategory = "attribute_comparison", "cost_paint_wall",
    knowledge = "Cost of paint is directly proportional to volume required to paint."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 110

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is painting his two walls in bedroom. {name} expenses depends on the amount of paint used. The cost to paint a wall that required larger volume is {given_value} dollars.",
            "{name} recently started his part time job as a painter. {name} was being called to his customer's apartment to repaint the walls in the master bedroom. {name} is trying to calculate the cost of painting. The cost to paint a wall that required larger volume of paint is {given_value} dollars."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The cost {name} requires to paint the other wall could be {hyp_value} dollars.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the cost of paint {name} requires to paint the other wall?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wall_paint_cost2(repetition_count):
    category, subcategory = "attribute_comparison", "cost_paint_wall",
    knowledge = "Cost of paint is directly proportional to volume required to paint."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 110

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is painting his two walls in bedroom. {name} expenses depends on the amount of paint used. The cost to paint a wall that required less volume is {given_value} dollars.",
            "{name} recently started his part time job as a painter. {name} was being called to his customer's apartment to repaint the walls in the master bedroom. {name} is trying to calculate the cost of painting. The cost to paint a wall that required less volume of paint is {given_value} dollars."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The cost {name} requires to paint the other wall could be {hyp_value} dollars.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the cost of paint {name} requires to paint the other wall?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def students_classroom1(repetition_count):
    category, subcategory = "attribute_comparison", "students_classroom",
    knowledge = "Number of students that can be occupied is directly proportional to the classroom size."

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 160

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two classrooms available for the History course. The classroom that is larger in size can accommodate maximum of {given_value} students.",
            "{name} is scheduling the classroom and timing for the Statistics course. There are two classrooms available for this course. The bigger classroom amongst both can accommodate a maximum of {given_value} students."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The maximum number of students other classroom could accommodate is {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the maximum number of students another classroom would accommodate?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def students_classroom2(repetition_count):
    category, subcategory = "attribute_comparison", "students_classroom",
    knowledge = "Maximum Number of students that can be occupied is directly proportional to the classroom size."

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 160

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two classrooms available for the Literature course. The classroom that is smaller in size can accommodate maximum of {given_value} students.",
            "{name} is scheduling the classroom and timing for the Statistics course. There are two classrooms available for this course. The smaller classroom amongst both can accommodate a maximum of {given_value} students."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The maximum number of students other classroom could accommodate is {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the maximum number of students another classroom could accommodate?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cab_driver_earn1(repetition_count):
    category, subcategory = "attribute_comparison", "cab_driver_earn",
    knowledge = "A cab driver's earning is directly proportional to number of trips he makes."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a cab driver in Tempe city and drove a cab for two days. The earnings he made on a day in which he had more number trips are {given_value} dollars.",
            "{name}'s brother recently started driving taxi to support his family financially. He drove a taxi for two days. The profits he made on a day in which he had more trips are {given_value} dollars."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The earnings {name} could have made on the other day is {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the earnings {name} could have made on the other day?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cab_driver_earn2(repetition_count):
    category, subcategory = "attribute_comparison", "cab_driver_earn",
    knowledge = "A cab driver's earning is directly proportional to number of trips he makes."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a cab driver in Tempe city and drove a cab for two days. The earnings he made on a day in which he had less number trips are {given_value} dollars.",
            "{name}'s brother recently started driving taxi to support his family financially. He drove a taxi for two days. The profits he made on a day in which he had comparatively less trips are {given_value} dollars."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The earnings {name} could have made on the other day is {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the earnings {name} could have made on the other day?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def electricity_bill_power1(repetition_count):
    category, subcategory = "attribute_comparison", "electricity_bill_power",
    knowledge = "Electricity bill amount is directly proportional to power usage."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 150

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has paid the electricity bill for months May and June. The month May had higher power usage amounting electricity bill to {given_value} dollars.",
            "{name} is managing the bill payment for an apartment building. He paid the electricity bill for two months May and June. In month May the apartment had higher power usage amounting the electricity bill to {given_value} dollars."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The electricity bill amount {name} paid for month June could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the electricity bill amount {name} could have paid for month June?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def electricity_bill_power2(repetition_count):
    category, subcategory = "attribute_comparison", "electricity_bill_power",
    knowledge = "Electricity bill amount is directly proportional to power usage."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 150

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has paid the electricity bill for months May and June. The month May had lower power usage amounting electricity bill to {given_value} dollars.",
            "{name} is managing the bill payment for an apartment building. He paid the electricity bill for two months May and June. In month May the apartment had lower power usage amounting the electricity bill to {given_value} dollars."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The electricity bill amount {name} paid for month June could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the electricity bill amount {name} could have paid for month June?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def electricity_bill_power3(repetition_count):
    category, subcategory = "attribute_comparison", "electricity_bill_power",
    knowledge = "Electricity bill amount is directly proportional to power usage."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 150

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has paid the electricity bill for months May and June. The month May had higher electricity bill amount with power usage of {given_value} watts.",
            "{name} is managing the bill payment for an apartment building. He paid the electricity bill for two months May and June. In month May the apartment had higher electricity bill by usage of {given_value} watts of power."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The power usage of month June could be {hyp_value} watts.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the power usage of month June?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def electricity_bill_power4(repetition_count):
    category, subcategory = "attribute_comparison", "electricity_bill_power",
    knowledge = "Electricity bill amount is directly proportional to power usage."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 150

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has paid the electricity bill for months May and June. The month May had lower electricity bill amount with power usage of {given_value} watts.",
            "{name} is managing the bill payment for an apartment building. He paid the electricity bill for two months May and June. In month May the apartment had lower electricity bill by usage of {given_value} watts of power."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The power usage of month June could be {hyp_value} watts.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the power usage of month June?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def sheet_pages1(repetition_count):
    category, subcategory = "attribute_comparison", "sheet_pages",
    knowledge = "Number of pages made is directly proportional to the area of sheet."

    binary_instances = []
    mcq_instances = []
    given_value_start = 80
    given_value_end = 250

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A paper company is making A4 sized papers by cutting two big sheet of paper. Number of papers prepared from a larger sheet is {given_value}.",
            "{name} is trying to get a rough estimate of how many A4 sized papers can be made from a large sheet of paper. He has two large big of paper. Number of papers prepared from a larger sheet is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Number of A4 sized papers created from other sheet could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the number of pages created by the other sheet?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def sheet_pages2(repetition_count):
    category, subcategory = "attribute_comparison", "sheet_pages",
    knowledge = "Number of pages made is directly proportional to the area of sheet."

    binary_instances = []
    mcq_instances = []
    given_value_start = 80
    given_value_end = 250

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A paper company is making A4 sized papers by cutting two big sheet of paper. Number of papers prepared from a smaller sheet is {given_value}.",
            "{name} is trying to get a rough estimate of how many A4 sized papers can be made from a large sheet of paper. He has two large big of paper. Number of papers prepared from a smaller sheet is {given_value}."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Number of A4 sized papers created from other sheet could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the number of pages created by the other sheet?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_distance1(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_distance",
    knowledge = "Horizontal distance travelled by cannon ball is directly proportional to the muzzle velocity, if fired at 45 degree projection angle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two cannons fired two identical cannon balls. The cannon ball having higher muzzle velocity travelled {given_value} meters.",
            "{name} was wondering how cannons were used before in the war. He was experimenting with two cannons in testing zone to obeserve the distance covered by cannon balls. Two cannons shot two identical cannon balls. The cannon ball that has a greater muzzle velocity covered distance of {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Distance travelled by the other cannon ball could be {hyp_value} meters.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the distance travelled by the other cannon ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_distance2(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_distance",
    knowledge = "Horizontal distance travelled by cannon ball is directly proportional to the muzzle velocity, if fired at 45 degree projection angle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two cannon fired two identical cannon balls. The cannon ball having lower muzzle velocity travelled {given_value} meters.",
            "{name} was wondering how cannons were used before in the war. He was experimenting with two cannons in testing zone to obeserve the distance covered by cannon balls. Two cannons shot two identical cannon balls. The cannon ball that has a lower muzzle velocity covered distance of {given_value} meters."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Distance travelled by the other cannon ball could be {hyp_value} meters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the distance travelled by the other cannon ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_distance3(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_distance",
    knowledge = "Horizontal distance travelled by cannon ball is directly proportional to the muzzle velocity, if fired at 45 degree projection angle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 250

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was in a defense research project and was testing two different cannons and they fired two identical cannon ball. The cannon ball which travelled more distance have muzzle velocity of {given_value} meter/second.",
            "{name} was wondering how cannons were used before in the war. He was experimenting with two cannons in testing zone to obeserve the distance covered by cannon balls. Two cannons shot two identical cannon balls. The cannon ball that covered more distance have muzzle velocity of {given_value} meter/seconds."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Muzzle velocity of the other cannon ball could be {hyp_value} meter/second.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the muzzle velocity of the other cannon ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_distance4(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_distance",
    knowledge = "Horizontal distance travelled by cannon ball is directly proportional to the muzzle velocity, if fired at 45 degree projection angle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 250

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was in a defense research project and was testing two different cannons and they fired two identical cannon ball. The cannon ball which travelled less distance have muzzle velocity of {given_value} meter/second.",
            "{name} was wondering how cannons were used before in the war. He was experimenting with two cannons in testing zone to obeserve the distance covered by cannon balls. Two cannons shot two identical cannon balls. The cannon ball that covered less distance have muzzle velocity of {given_value} meter/seconds."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Muzzle velocity of the other cannon ball could be {hyp_value} meter/second.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the muzzle velocity of the other cannon ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_height1(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_height",
    knowledge = "The maximum height reached by the ball is directly proportional to the initial velocity at which it is thrown if fired at 45 degrees of projection angle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his brother are throwing two identical balls in an upward direction at 45 degree of projection angle. {name}'s ball which reached at higher height had initial velocity of {given_value} meter/second.",
            "{name} and his brother are playing with two identical balls. Both were trying to throw the ball as high as possible. Both of the balls are thrown at 45 degree of projection angle.{name} threw a ball that reached a higher height had an initial speed of {given_value} meter/second."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Initial velocity of the ball thrown by {name}'s brother could be {hyp_value} meter/second.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the initial velocity of the ball thrown by {name}'s brother?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_height2(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_height",
    knowledge = "Maximum height reached by the ball is directly proportional to the initial velocity at which it is thrown if fired at 45 degrees of projection angle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his brother are throwing two identical balls in an upward direction at 45 degree of projection angle. {name}'s ball which reached at lower height had initial velocity of {given_value} meter/second.",
            "{name} and his brother are playing with two identical balls. Both were trying to throw the ball as high as possible, the balls were thrown at 45 degree of projection angle. {name} threw a ball that reached a lower height had an initial speed of {given_value} meter/second."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Initial velocity of the ball thrown by {name}'s brother could be {hyp_value} meter/second.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the initial velocity of the ball thrown by {name}'s brother?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_height3(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_height",
    knowledge = "Maximum height reached by the ball is directly proportional to the initial velocity at which it is thrown if fired at 45 degrees of projection angle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his brother are throwing two identical ball in an upward direction at 45 degree of projection angle. The {name}'s ball which was thrown with higher initial velocity reached height of {given_value} meters.",
            "{name} and his brother are playing with two identical balls. Both were trying to throw the ball as high as possible, the balls were thrown at 45 degree of projection angle. {name} threw a ball with higher initial velocity that reached height of {given_value} meter."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Maximum height reached by the ball thrown by {name}'s brother could be {hyp_value} meters.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the maximum height reached by the ball thrown by {name}'s brother?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_height4(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_height",
    knowledge = "Maximum height reached by the ball is directly proportional to the initial velocity at which it is thrown if fired at 45 degrees of projection angle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his brother are throwing two identical balls at 45 degree of projection angle. {name}'s ball which was thrown with lower initial velocity reached height of {given_value} meters.",
            "{name} and his brother are playing with two identical balls. Both were trying to throw the ball as high as possible, the balls were thrown at 45 degree of projection angle. {name} threw a ball with lower initial velocity that reached height of {given_value} meters."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Maximum height reached by the ball thrown by {name}'s brother could be {hyp_value} meters.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the maximum height reached by the ball thrown by {name}'s brother?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_angle_height1(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_angle_height",
    knowledge = "Maximum height reached by an object is directly proportional to the projectile angle at which it is thrown if the initial velocity is constant."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his sister are trying to pick mangoes from a tree by throwing stones. Both have same muscle power to throw a stone. {name} threw stone with higher projection angle and reached a height of {given_value} meters.",
            "{name} and his sister are trying to pick some oranges from a tree. Since they are not able to reach to height of the oranges, they decided to throw stone to make orange fall on the ground. Both have same muscle power to throw a stone. {name} threw a stone with a greater angle of projection and reached a height of {given_value} meters."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Maximum height reached by the stone thrown by {name}'s sister could be {hyp_value} meters.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the maximum height reached by the stone thrown by {name}'s sister?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_angle_height2(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_angle_height",
    knowledge = "Maximum height reached by an object is directly proportional to the projectile angle at which it is thrown if the initial velocity is constant."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his sister are trying to pick mangoes from a tree by throwing stones. {name} threw stone with lower projection angle reached height of {given_value} meters.",
            "{name} and his sister are trying to pick some oranges from a tree. Since they are not able to reach to height of the oranges, they decided to throw stone to make orange fall on the ground. Both have same muscle power to throw a stone. {name} threw a stone with a lower angle of projection and reached a height of {given_value} meters."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Maximum height reached by the stone thrown by {name}'s sister could be {hyp_value} meters.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the maximum height reached by the stone thrown by {name}'s sister?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_angle_height3(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_angle_height",
    knowledge = "Maximum height reached by an object is directly proportional to the projectile angle at which it is thrown if the initial velocity is constant."

    binary_instances = []
    mcq_instances = []
    given_value_start = 6
    given_value_end = 85

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his sister are trying to pick mangoes from a tree by throwing stones. {name} threw a stone that reached higher height had projection angle of {given_value} degrees.",
            "{name} and his sister are trying to pick some oranges from a tree. Since they are not able to reach to height of the oranges, they decided to throw stone to make orange fall on the ground. Both have same muscle power to throw a stone. {name} threw a stone that reached higher height had projection angle of {given_value} degrees."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Maximum projection angle from which the stone is thrown by {name}'s sister could be {hyp_value} degrees.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the maximum projection angle from which the stone is thrown by {name}'s sister?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def projectile_angle_height4(repetition_count):
    category, subcategory = "attribute_comparison", "projectile_angle_height",
    knowledge = "Maximum height reached by an object is directly proportional to the projectile angle at which it is thrown if the initial velocity is constant."

    binary_instances = []
    mcq_instances = []
    given_value_start = 6
    given_value_end = 85

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his sister are trying to pick mangoes from a tree by throwing stones. {name} threw stone that reached lower height had projection angle of {given_value} degrees.",
            "{name} and his sister are trying to pick some oranges from a tree. Since they are not able to reach to height of the oranges, they decided to throw stone to make orange fall on the ground. Both have same muscle power to throw a stone. {name} threw a stone that reached lower height had projection angle of {given_value} degrees."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Maximum projection angle from which the stone is thrown by {name}'s sister could be {hyp_value} degrees.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the maximum projection angle from which the stone is thrown by {name}'s sister?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
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
#     template_binary_instances, template_mcq_instances = projectile_distance2(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
