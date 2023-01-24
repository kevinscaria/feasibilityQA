import util
import random
import pprint
import numpy as np


def height_and_potential_energy(repetition_count):
    category, subcategory = "attribute_comparison", "height_and_potential_energy",
    knowledge = "Potential energy is directly proportional to the height"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between potential energy and height using two identical balls. The height of the ball with higher potential energy is {given_value} units.",
            "{name} learns about the relation of potential energy and height. {given_value} units is the height of ball which has higher potential energy."
        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Height of the other ball could be {hyp_value} units.",

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
            "What could be the height of the other ball ?",

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


def height_and_potential_energy2(repetition_count):
    category, subcategory = "attribute_comparison", "height_and_potential_energy",
    knowledge = "Potential energy is directly proportional to the height"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between potential energy and height of two identical balls. The potential energy of the ball at higher height is {given_value} units.",
            "{name} learns about the relation of potential energy and height. {given_value} units is the potential energy of the ball at higher height."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Potential energy of the other ball could be {hyp_value} units.",

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
            "What could be the potential energy of the other ball?",

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


def height_and_potential_energy3(repetition_count):
    category, subcategory = "attribute_comparison", "height_and_potential_energy",
    knowledge = "Potential energy is directly proportional to the height"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between potential energy and height of two balls. The height of the ball with lower potential energy is {given_value} units.",
            "{name} learns about the relation of potential energy and height. {given_value} units is the height of ball which has lower potential energy."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Height of the other ball could be {hyp_value} units.",

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
            "What could be the height of the other ball?",

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


def height_and_potential_energy4(repetition_count):
    category, subcategory = "attribute_comparison", "height_and_potential_energy",
    knowledge = "Potential energy is directly proportional to the height"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 4

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between potential energy and height of two identical balls. The potential energy of the ball at lower height is {given_value} units.",
            "{name} learns about the relation of potential energy and height. {given_value} units is the potential energy of ball which has lower height."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Potential energy of the other ball could be {hyp_value} units.",

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
            "What could be the potential energy of the other ball?",

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


def length_and_resistance(repetition_count):
    category, subcategory = "attribute_comparison", "length_and_resistance",
    knowledge = "Resistance is directly proportional to the length of the metalic wire"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between resistance and length using two similar wires of different lengths. The length of the wire with higher resistance is {given_value} units.",
            "{name} experiment is to observe the relationship between the resistance and the area using two similar cables from different length. The cable area with greater resistance is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "Length of the other wire could be {hyp_value} units.",

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
            "What could be the length of the other wire?",

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


def length_and_resistance2(repetition_count):
    category, subcategory = "attribute_comparison", "length_and_resistance",
    knowledge = "Resistance is directly proportional to the length of the metalic wire"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between resistance and length using two similar wires of different lengths. The resistance of the wire with higher length is {given_value} units.",
            "{name} experiment is to observe the relationship between the resistance and the length using two similar cables from different length. The cable resistance with greater length is {given_value} units"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "Resistance of the other wire could be {hyp_value} units.",

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
            "What could be the resistance of the other wire?",

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


def length_and_resistance3(repetition_count):
    category, subcategory = "attribute_comparison", "length_and_resistance",
    knowledge = "Resistance is directly proportional to the length of the metalic wire"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 3

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between resistance and length of two wires. The length of the wire with lower resistance is {given_value} units.",
            "{name} experiment is to observe the relationship between the resistance and the length using two cables. The cable length with lower resistance is {given_value} units"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "Length of the other wire could be {hyp_value} units.",

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
            "What could be the length of the other wire?",

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


def length_and_resistance4(repetition_count):
    category, subcategory = "attribute_comparison", "length_and_resistance",
    knowledge = "Resistance is directly proportional to the length of the metalic wire"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 4

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between resistance and length using two similar wires of different lengths. The resistance of the wire with lower length is {given_value} units.",
            "{name} experiment is to observe the relationship between the resistance and the length using two similar cables from different length. The cable resistance with lower length is {given_value} units"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Resistance of the other wire could be {hyp_value} units.",

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
            "What could be the resistance of the other wire?",

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


def area_and_resistance(repetition_count):
    category, subcategory = "attribute_comparison", "area_and_resistance",
    knowledge = "Resistance is inversely proportional to the area of the metalic wire"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between resistance and area using two similar wires of different areas. The area of the wire with larger resistance is {given_value} units.",
            "{name} learns about the relation of resistance and area using two wires which are similar with different areas. {given_value} units is the area of wire which has larger resistance."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Area of the other wire could be {hyp_value} units.",

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
            "What could be the area of the other wire?",

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


def area_and_resistance2(repetition_count):
    category, subcategory = "attribute_comparison", "area_and_resistance",
    knowledge = "Resistance is inversely proportional to the area of the metalic wire"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between resistance and area using two similar wires of different areas. The resistance of the wire with larger area is {given_value} units.",
            "{name} learns about the relation of resistance and area using two wires which are similar with different areas. {given_value} units is the resistance of wire which has larger area."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "Resistance of the other wire could be {hyp_value} units.",

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
            "What could be the resistance of the other wire?",

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


def area_and_resistance3(repetition_count):
    category, subcategory = "attribute_comparison", "area_and_resistance",
    knowledge = "Resistance is inversely proportional to the area of the metalic wire"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 3

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between resistance and area of two wires. The area of the wire with smaller resistance is {given_value} units.",
            "{name} learns about the relation of resistance and area using two wires. {given_value} units is the area of wire which has smaller resistance."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Area of the other wire could be {hyp_value} units.",

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
            "What could be the area of the other wire?",

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


def area_and_resistance4(repetition_count):
    category, subcategory = "attribute_comparison", "area_and_resistance",
    knowledge = "Resistance is inversely proportional to the area of the metalic wire"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 4

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between resistance and area using two similar wires of different areas. The resistance of the wire with smaller area is {given_value} units.",
            "{name} learns about the relation of resistance and area using two similar wires of different areas. {given_value} units is the resistance of wire which has smaller area."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Resistance of the other wire could be {hyp_value} units.",

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
            "What could be the resistance of the other wire?",

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


def momentum_and_velocity(repetition_count):
    return [], []


def kinetic_energy_and_speed(repetition_count):
    return [], []


def gravity_and_weight(repetition_count):
    return [], []


def force_and_acceleration(repetition_count):
    return [], []


def frequency_and_direction(repetition_count):
    return [], []


def weight_and_gravity(repetition_count):
    category, subcategory = "attribute_comparison", "weight_and_gravity",
    knowledge = "weight is directly proportional to the gravity"

    binary_instances = []
    mcq_instances = []
    given_value_start = 60
    given_value_end = 90

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an astronaut and is visiting another planet that has lower gravity. {name}'s weight on that planet is {given_value} units.",
            "{name} compares the gravity of earth and gravity of another planet. He figures out that the pther planet has lower gravity. {name} calculates that his weight on that planet will be {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name}'s weight on Earth could be {hyp_value} units.",

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
            scale=5
        )

        question_template = random.choice([
            "What could be {name}'s weight on Earth?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=5
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def weight_and_gravity2(repetition_count):
    category, subcategory = "attribute_comparison", "weight_and_gravity",
    knowledge = "weight is directly proportional to the gravity"

    binary_instances = []
    mcq_instances = []
    given_value_start = 60
    given_value_end = 90

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an astronaut and is visiting another planet that has lower gravity. {name}'s weight on Earth is {given_value} units.",
            "{name} compares the gravity of earth and gravity of another planet. He figures out that the pther planet has lower gravity. {name}'s weight on earth is {given_value}"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name}'s weight on the other planet could be {hyp_value} units.",

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
            scale=5
        )

        question_template = random.choice([
            "What could be {name}'s weight on that planet?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=5
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def table_height_and_object(repetition_count):
    category, subcategory = "attribute_comparison", "table_height_and_object",
    knowledge = "Only a shorter object can be kept under a table"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has a table of height {given_value} units and a cabinet that fits under the table.",
            "{name} went to buy a cabinet which we wanted to fit under his table whose height is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Height of the cabinet could be {hyp_value} units.",

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
            "What could be the height of the cabinet?",

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


def direct_comparison(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "Smaller planet has a smaller radius in comparison to a larger planet"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Planet A is smaller in radius that planet B. The radius of planet B is {given_value} units.",
            "Radius of planet A is smaller than that of planet B. {given_value} units is the radius of planet B"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Radius of planet A could be {hyp_value} units.",

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
            "What could be the radius of planet A?",

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


def direct_comparison2(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "Smaller planet has a smaller radius in comparison to a larger planet"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Planet A is bigger in radius that planet B. The radius of planet B is {given_value} units.",
            "Radius of planet A is bigger than that of planet B. {given_value} units is the radius of planet B"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Radius of planet A could be {hyp_value} units.",

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
            "What could be the radius of planet A?",

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


def direct_comparison3(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "Smaller planet has a smaller radius in comparison to a larger planet"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 3

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Planet A is smaller in radius that planet B. The radius of planet A is {given_value} units.",
            "{name} studied about two planets A and B. {given_value} units is the radius of planet A and is smaller in radius than planet B."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "Radius of planet B could be {hyp_value} units.",

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
            "What could be the radius of planet B?",

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


def direct_comparison4(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "Smaller planet has a smaller radius in comparison to a larger planet"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Planet A is bigger in radius that planet B. The radius of planet A is {given_value} units.",
            "{name} studied about two planets A and B. {given_value} units is the radius of planet A and is bigger in radius than planet B."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "Radius of planet B could be {hyp_value} units.",

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
            "What could be the radius of planet B?",

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


def direct_comparison5(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "More weight implies an object is heavier"

    binary_instances = []
    mcq_instances = []
    given_value_start = 25
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought two cans and while loading them into a truck, {name} felt that the first can is heavier than the second. The weight of the first can is {given_value} units.",
            "{name} has two cans. The first can is heavier than the second can. The weight of first can is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Weight of the second can could be {hyp_value} units.",

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
            scale=3
        )

        question_template = random.choice([
            "What could be the weight of the second can?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def direct_comparison6(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "More weight implies an object is heavier"

    binary_instances = []
    mcq_instances = []
    given_value_start = 25
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought two cans and while loading them into a truck, {name} felt that the second can is heavier than the first. The weight of the first can is {given_value} units.",
            "{name} has two cans. The second can is heavier than the first can. The weight of first can is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Weight of the second can could be {hyp_value} units.",

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
            "What could be the weight of second can?",

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


def direct_comparison7(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "More weight implies an object is heavier"

    binary_instances = []
    mcq_instances = []
    given_value_start = 25
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 3

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought two cans and while loading them into a truck, {name} felt that the first can is heavier than the second. The weight of the second can is {given_value} units.",
            "{name} has two cans. The first can is heavier than the second can. The weight of second can is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "Weight of the first can could be {hyp_value} units.",

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
            "What could be the weight of the first can?",

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


def direct_comparison8(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "More weight implies an object is heavier"

    binary_instances = []
    mcq_instances = []
    given_value_start = 25
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought two cans and while loading them into a truck, {name} felt that the first can is lighter than the second. The weight of the second can is {given_value} units.",
            "{name} has two cans. The first can is lighter than the second can. The weight of second can is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "Weight of the first can could be {hyp_value} units.",

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
            "What could be the weight of the first can?",

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


def direct_comparison9(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "Less number implies that an object has lesser count"

    binary_instances = []
    mcq_instances = []
    given_value_start = 25
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are {given_value} schools in a village and lesser number of hospitals.",
            "The number of schools in a village is lesser than the number of hospitals. The number of schools is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The number of hospitals in the village could be {hyp_value}.",

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
            "What could be the number of hospitals in the village?",

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


def direct_comparison10(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "Bigger library can accomodate more books"

    binary_instances = []
    mcq_instances = []
    given_value_start = 25
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A library can accommodate {given_value} books. There is a bigger library nearby.",
            "There is a bigger library nearby. The library can accommodate {given_value} books."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The capacity of the bigger library could be {hyp_value}.",

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
            "What could be the capacity of the bigger library?",

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


def direct_comparison11(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "Cheaper thing costs less money"

    binary_instances = []
    mcq_instances = []
    given_value_start = 25
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to buy a ring for this wife. The cost of one ring is {given_value} thousand dollars but he bought the other ring as it was cheaper.",
            "{name} went to a shop to buy a ring for his wife. He had low budget, so instead of a ring whose cost was {given_value} thousand dollars he bought a ring which was cheaper than the other ring."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The cost of the ring that {name} bought could be {hyp_value} thousand dollars.",

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
            "What could be the cost of the ring that {name} bought?",

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


def direct_comparison12(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "Expensive thing costs more money"

    binary_instances = []
    mcq_instances = []
    given_value_start = 25
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to buy a ring for this wife. The cost of one ring is {given_value} thousand dollars but he bought the other ring but it was more expensive.",
            "{name} went to a shop to buy a ring for his wife. He had very high budget, so instead of a ring whose cost was {given_value} thousand dollars he bought a ring which was expensive than the other ring."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The cost of the ring that {name} bought could be {hyp_value} thousand dollars.",

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
            "What could be the cost of the ring that {name} bought?",

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


def direct_comparison13(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "Larger duration means more time"

    binary_instances = []
    mcq_instances = []
    given_value_start = 25
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} took {given_value} minutes to finish the homework. His friend Jamie is weak in studies. Jamie took longer to finish the homework.",
            "{name} is driving to his school and takes {given_value} minutes to reach, but his friend Jamie was driving slow and took more time to reach the school"
        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Jamie could have taken {hyp_value} minutes.",

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
            "How many minutes could Jamie have taken?",

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


def direct_comparison14(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "bigger circle has larger area"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} drew a circle of area {given_value} sq units. Then, his friend Nancy drew a circle of larger radius around it.",
            "{name} and his Nancy's both drew a cricle on a paper. {name}'s circle area was {given_value} sq units and his friend Nancy drew a cricle with larger radius around it."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Area of Nancy's circle could be {hyp_value} sq units.",

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
            "What could be the radius of Nancy's circle?",

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


def direct_comparison15(repetition_count):
    category, subcategory = "attribute_comparison", "direct_comparison",
    knowledge = "smaller circle has smaller area"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} drew a circle of area {given_value} sq units. Then, his friend Nancy drew a circle of within it.",
            "{name} and his Nancy's both drew a cricle on a paper. {name}'s circle area was {given_value} sq units and his friend Nancy drew a cricle within that circle."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Area of Nancy's circle could be {hyp_value} sq units.",

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
            "What could be the radius of Nancy's circle?",

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


def portion_pizza(repetition_count):
    category, subcategory = "attribute_comparison", "portion",
    knowledge = "A portion of an object is less than the whole object"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A pizza has {given_value} units of calories. {name} ate a portion of this pizza.",
            "{name} like to eat a lot of junk food. One day, he went out to eat junk food with his friends which had {given_value} units of calories."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have consumed {hyp_value} units calories.",

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
            "How many calories {name} could have consumed?",

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


def portion_pizza2(repetition_count):
    category, subcategory = "attribute_comparison", "portion",
    knowledge = "A portion of an object is less than the whole object"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A pizza slice has {given_value} units of calories. {name} ate several such slices.",
            "{name} like to eat a lot of junk food. One day, he went out to eat burgers with his friends which had {given_value} units of calories in one burger, and he ate several such burgers."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have consumed {hyp_value} units calories.",

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
            "How many calories {name} could have consumed?",

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


def portion_count(repetition_count):
    category, subcategory = "attribute_comparison", "portion",
    knowledge = "A portion of an object is less than the whole object"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a basket of apples that had {given_value} apples.",
            "{name} got himeself a basket of fruits, in which {given_value} apples were there."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} can eat {hyp_value} apples from that basket.",

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
            "How many apples can {name} eat from that basket?",

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


def portion_count2(repetition_count):
    category, subcategory = "attribute_comparison", "portion",
    knowledge = "A portion of an object is less than the whole object"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} broke a glass window of weight {given_value} pounds into several pieces.",
            "{name} was playing cricket along with his friend with a heavy weighted ball, unfortunately they broke a glass which was of {given_value} pounds."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Weight of a broken piece could be {hyp_value} pounds.",

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
            "What could be the weight of a broken piece?",

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

        # *******Template 3

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} broke a glass window into several pieces. Weight of a broken piece is {given_value} pounds",
            "{name} was playing cricket along with his friend with a heavy weighted ball, unfortunately they broke a glass which was of {given_value} pounds."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Weight of the unbroken window could be {hyp_value} pounds.",

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
            "What could be the weight of the unbroken window?",

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


def portion_count3(repetition_count):
    category, subcategory = "attribute_comparison", "portion",
    knowledge = "A portion of an object is less than the whole object"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 3

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} broke a glass window into several pieces. Weight of a broken piece is {given_value} pounds",
            "{name} while playing cricket aimed his shot at a window and broke that window into several pieces. Weight of one of the broken piece is {given_value} pounds."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Weight of the unbroken window could be {hyp_value} pounds.",


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
            "What could be the weight of the unbroken window?",

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


def gift_wrapper(repetition_count):
    category, subcategory = "attribute_comparison", "gift_wrapper",
    knowledge = "Gift wrapper needs to be of larger area than the object it needs to wrap"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is buying a gift for a friend. The gift box has an area of {given_value} units {name} wants to buy a wrapper for this box.",
            "{name} has to wrap a box of area {given_value} units so he buys a wrapper for this box."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "A wrapper that can completely wrap this box could be of area {hyp_value} units.",

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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the area of the wrapper that can completely wrap the box?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def gift_wrapper2(repetition_count):
    category, subcategory = "attribute_comparison", "gift_wrapper",
    knowledge = "Gift wrapper needs to be of larger area than the object it needs to wrap"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to wrap a gift box for a friend. The wrapper has an area of {given_value} units.",
            "{name} has to wrap a box. The wrapper has an area of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "This wrapper can be used to completely wrap a box of area {hyp_value} units.",

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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the area of the box that this wrapper can completely wrap?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def gift_wrapper3(repetition_count):

    category, subcategory = "attribute_comparison", "cover",
    knowledge = "Cloth needs to be of larger area than the object it needs to cover"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A marble has an area of {given_value} units. It need to be covered with a piece of cloth to be protected from rain.",
            "{name} has to cover marble of area {given_value} units. He wants to cover the marbel with cloth in order to protect it from rain."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "A cloth of area {hyp_value} units can completely cover the marble.",
            "It can be completely covered by a cloth of area {hyp_value} units.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the area of the cloth that can completely cover the marble?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def portion_price(repetition_count):
    category, subcategory = "attribute_comparison", "portion",
    knowledge = "Price of a component of an object is less than the whole object"

    binary_instances = []
    mcq_instances = []
    given_value_start = 101
    given_value_end = 120

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} recently bought a TV remote at a price of {given_value} dollars. {name} is thinking of buying a new TV now.",
            "{name} bought a TV and a remote for that TV. He got the remote at the price of {given_value} dollars."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} can get the TV at a price of {hyp_value} dollars.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=400,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=100,
            scale=1
        )

        question_template = random.choice([
            "At what price can {name} get a new TV?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=400,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=100,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def water_cotton(repetition_count):
    category, subcategory = "attribute_comparison", "water_and_cotton",
    knowledge = "Water is heavier than cotton"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two boxes of same dimensions. {name} filled one box with water and the other box with cotton. The weight of the box with water is {given_value} pounds.",
            "{name} fills one box with cotton and a box pof same size with water. The box with water weighted {given_value} pounds."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Weight of the cotton box could be {hyp_value} pounds.",

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
            scale=5
        )

        question_template = random.choice([
            "What could be the weight of the cotton box?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=5
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def water_cotton2(repetition_count):
    category, subcategory = "attribute_comparison", "water_and_cotton",
    knowledge = "Water is heavier than cotton"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two boxes of same dimensions. {name} filled one box with water and the other box with cotton. The weight of the box with cotton is {given_value} pounds.",
            "{name} fills one box with cotton and a box pof same size with water. The box with cotton weighted {given_value} pounds."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Weight of the water box could be {hyp_value} pounds.",

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
            scale=5
        )

        question_template = random.choice([
            "What could be the weight of the water box?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=5
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def at_least(repetition_count):
    category, subcategory = "attribute_comparison", "at_least",
    knowledge = "If each member contributes at least 1 then total would be more than the number of contributors"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} hosted a birthday party in which {given_value} people came. Each person gave at least 1 gift to {name}.",
            "{name} and his wife threw an anniversary party to their family and friends. A total of {given_value} people came to their party who also brought atleast 1 gift."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Total number of gifts could be {hyp_value}.",

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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the total number of gifts?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def at_least2(repetition_count):
    category, subcategory = "attribute_comparison", "at_least",
    knowledge = "If each member contributes at least 1 then total would be more than the number of contributors"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} hosted a birthday party in which {given_value} people came. Only a few people brought a gift and none of them gave more than one gift.",
            "{name} and his wife threw an anniversary party to their family and friends. A total of {given_value} people came to their party but only few of them brought atleast a gift and none of them brought more than one gift."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Total number of gifts could be {hyp_value}.",

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
            "What could be the total number of gifts?",

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

        # *******Template 3

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is hosting a birthday party in which {given_value} people are expected to come. {name} wants to buy at least 1 chocolate for each person.",
            "{name} and his wife threw an anniversary party to their family and friends. A total of {given_value} people were invited to their party. {name} wanted to buy atleast 1 chocolate for each person."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} can buy a total of {hyp_value} chocolates.",

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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the total number of chocolates {name} can buy?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def at_least3(repetition_count):
    category, subcategory = "attribute_comparison", "at_least",
    knowledge = "If each member contributes at least 1 then total would be more than the number of contributors"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 3

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is hosting a birthday party in which {given_value} people are expected to come. {name} wants to buy at least 1 chocolate for each person.",
            "{name} and his wife threw an anniversary party to their family and friends. A total of {given_value} people were invited to their party. {name} wanted to buy atleast 1 chocolate for each person."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} can buy a total of {hyp_value} chocolates.",

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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the total number of chocolates {name} can buy?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def train_and_walking(repetition_count):
    category, subcategory = "attribute_comparison", "train_and_walking",
    knowledge = "Train is a faster way of travelling than walking"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 40

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s office is at a large distance from his home. One day {name} travelled via train and reached in {given_value} minutes.",
            "{name} went to his office by train. It takes {given_value} minutes to reach the office by train."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Next day {name} decided to walk to the office. It can take {hyp_value} minutes to reach the office.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=15,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "Next day {name} decided to walk to the office. How much time can it take to reach the office?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=15,
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


def train_and_walking2(repetition_count):
    category, subcategory = "attribute_comparison", "train_and_walking",
    knowledge = "Train is a faster way of travelling than walking"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 40

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s office is at a large distance from his home. One day {name} walked and reached in {given_value} minutes.",
            "The distance of {name}'s home and office is large. One day he missed his train so he walked to the office and it took him {given_value} minutes to reach the office."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Next day {name}  took the train to the office. It can take {hyp_value} minutes to reach the office.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=15,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "Next day {name} took the train to the office. How much time can it take to reach the office?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=15,
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


def train_and_plane(repetition_count):
    category, subcategory = "attribute_comparison", "train_and_plane",
    knowledge = "Plane is a faster way of travelling than train"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 40

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s home country is at a large distance from USA. Last year {name} travelled via train and reached in {given_value} hours.",
            "{name} lives far away from USA. Every year he visits USA. One time he travelled by train because their were no flight tickets. It took him {given_value} hours to reach by train."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "This year {name} decided to take plane to go back home. It can take {hyp_value} hours to reach the home.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=15,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "This year {name} decided to take plane to go back home. How many hours it can take to reach the home?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=15,
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


def train_and_plane2(repetition_count):
    category, subcategory = "attribute_comparison", "train_and_plane",
    knowledge = "Plane is a faster way of travelling than train"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 40

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s home country is at a large distance from USA. Last year {name} travelled via plane and reached in {given_value} hours.",
            "{name} lives far away from USA. Every year he visits USA. One time he travelled by plane. It took him {given_value} hours to reach by plane."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "This year {name} decided to take train to go back home. It can take {hyp_value} hours to reach the home.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=15,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "This year {name} decided to take train to go back home. How many hours it can take to reach the home?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=15,
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


def train_and_plane3(repetition_count):
    category, subcategory = "attribute_comparison", "train_and_plane",
    knowledge = "Plane is a faster way of travelling than train"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 40

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A train covers {given_value} miles in some time.",
            "{name} travelled to his aunt's place. He uses train to reach there. train covers the distance of {given_value} miles in some time."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "A plane can cover {hyp_value} miles in the same time.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=15,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=5
        )

        question_template = random.choice([
            "How many miles the plane can cover in the same time?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=15,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def train_and_plane4(repetition_count):
    category, subcategory = "attribute_comparison", "train_and_plane",
    knowledge = "Plane is a faster way of travelling than train"

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 40

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A plane covers {given_value} miles in some time.",
            "{name} travelled to his aunt's place. He uses plane to reach there. Plane covers the distance of {given_value} miles in some time."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "A train can cover {hyp_value} miles in the same time.",


        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=15,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=5
        )

        question_template = random.choice([
            "How many miles a train can cover in the same time?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=15,
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


def elephant_size(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "elephant_size"
    knowledge = "Elephant is huge in comparison to size of a human"

    given_value_start = 1
    given_value_end = 3

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A room has just enough space to fit in {given_value} humans",
            "{given_value} humans can be fitted in a room up to the full capacity of the room."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{hyp_value} elephants can fit in that room.",
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
            scale=5
        )

        question_template = random.choice([
            "How many elephants can fit in that room?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=5
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def race(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "race"
    knowledge = "Race winner takes the least time to finish the race"

    given_value_start = 10
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two boys competed in a race. The winner finished the race in {given_value} minutes.",
            "{name} and some other boy were competing against each other in a bicycle race. {name} finished the race in {given_value} and won the race."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The other boy could have taken {hyp_value} minutes to finish the race.",
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
            "How many minutes the other boy could have taken to finish the race?",

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


def race2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "race"
    knowledge = "Race winner takes the least time to finish the race"

    given_value_start = 10
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two boys competed in a race. The loser finished the race in {given_value} minutes.",
            "{name} and some other boy were competing against each other in a bicycle race. {name} finished the race in {given_value} and lost the race."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The other boy could have taken {hyp_value} minutes to finish the race.",
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
            "How many minutes the other boy could have taken to finish the race?",

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


def distance(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "distance"
    knowledge = "It takes more time to cover larger distance than shorter distance"

    given_value_start = 12
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two girls who walk at the same speed study in the same school. The girl who stays closer to the school takes {given_value} minutes to travel from home to school.",
            "Two girls study in same school. Then speed of walikng of both the girls is same.One of the girsl stays near the school, so she takes {given_value} minutes to travel from home to school."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The other girl could take {hyp_value} minutes to travel from her home to school.",
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
            "How many minutes can the other girl take to travel from home to school?",

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


def distance2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "distance"
    knowledge = "It takes more time to cover larger distance than shorter distance"

    given_value_start = 12
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two girls who walk at the same speed study in the same school. The girl who stays farther from the school takes {given_value} minutes to travel from home to school.",
            "Two girls study in same school. Then speed of walikng of both the girls is same. One of the girsl stays farther from the school, so she takes {given_value} minutes to travel from home to school"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The other girl could take {hyp_value} minutes to travel from her home to school.",
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
            "How many minutes can the other girl take to travel from home to school?",

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


def distance3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "distance"
    knowledge = "It takes more time to cover larger distance than shorter distance"

    given_value_start = 12
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 3

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} recently shifted closer to his school. It used to take him {given_value} minutes to travel from his previous home to shcool.",
            "{name} recently bought a new house, because his other house was far from his school, so he bought a house which was closer to his school. From his previous house he used to take {given_value} minutes to travel to his school"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Now, it could take {name} {hyp_value} minutes to travel from home to school.",
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
            "How many minutes it could take {name} to travel from home to school?",

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


def distance4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "distance"
    knowledge = "It takes more time to cover larger distance than shorter distance"

    given_value_start = 12
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} recently shifted farther from his school. It used to take him {given_value} minutes to travel from his previous home to shcool.",
            "{name} recently bought a new house, farther from his school, so he bought a house which was closer to his school. From his previous house he used to take {given_value} minutes to travel to his school"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Now, it could take {name} {hyp_value} minutes to travel from home to school.",
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
            "How many minutes it could take {name} to travel from home to school?",

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


def distance5(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "distance"
    knowledge = "It takes more time to cover larger distance than shorter distance"

    given_value_start = 12
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 5

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two girls who walk at the same speed study in the same school. The girl who takes more time to travel from home to school stays {given_value} meters away from school.",
            "Two girls study in same school. The speed of walikng of both the girls is same. One of the girl takes more time to travel from home to school lives {given_value} metres away from school."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The other girl could be staying {hyp_value} meters from school.",
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
            "How many meters away from the school can the other girl be staying?",

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


def distance6(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "distance"
    knowledge = "It takes more time to cover larger distance than shorter distance"

    given_value_start = 12
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 6

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two girls who walk at the same speed study in the same school. The girl who takes less time to travel from home to school stays {given_value} meters away from school.",
            "Two girls study in same school. The speed of walikng of both the girls is same. One of the girl takes less time to travel from home to school lives {given_value} metres away from school."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The other girl could take {hyp_value} minutes to travel from her home to school.",
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
            "How many minutes can the other girl take to travel from home to school?",

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


def age(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "age"
    knowledge = "Son's age would be less than that of the father"

    given_value_start = 51
    given_value_end = 80

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is {given_value} years old.",
            "{name}'s son has to write his age and {name}'s age in a form given in school. But his son is unaware of {name}'s age so {name} tells his son that his age is {given_value} years old."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name}'s son could be {hyp_value} years old.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=50,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=25
        )

        question_template = random.choice([
            "How old could {name}'s son be?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=25
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def age2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "age"
    knowledge = "Son's age would be less than that of the father"

    given_value_start = 26
    given_value_end = 31

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is {given_value} years old.",
            "{name}has to write his age and his father's age in a school form. {name} write's {given_value} years as his age."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name}'s father could be {hyp_value} years old.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=50,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=25
        )

        question_template = random.choice([
            "How old could {name}'s son be?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=25
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def age3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "age"
    knowledge = "Elder person has more age than a younger person"

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s elder sister is {given_value} years old.",
            "{name} has a sister who is older than him, the age of his sister is {given_value} years old.",
            "{name}'s elder brother is {given_value} years old.",
            "{name} has a brother who is older than him, the age of his brother is {given_value} years old.",
            "{name}'s elder cousin is {given_value} years old.",
            "{name} has a cousin who is older than him, the age of his cousin is {given_value} years old."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be {hyp_value} years old.",
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
            "How old could {name} be?",

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


def age4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "age"
    knowledge = "Elder person has more age than a younger person"

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s younger sister is {given_value} years old.",
            "{name} has a sister who is younger than him, the age of his sister is {given_value} years old.",
            "{name}'s younger brother is {given_value} years old.",
            "{name} has a brother who is younger than him, the age of his brother is {given_value} years old.",
            "{name}'s younger cousin is {given_value} years old.",
            "{name} has a cousin who is younger than him, the age of his cousin is {given_value} years old."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be {hyp_value} years old.",
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
            "How old could {name} be?",

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


def width(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "width"
    knowledge = "Width of the house would be equal or more than that of a room of that house"

    given_value_start = 10
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The width of a {name}'s room is {given_value} units.",
            "{name} recently bought a new house, in which the width of master bedroom was {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The width of {name}'s entire house could be {hyp_value} units.",

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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the width of {name}'s entire house?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def width2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "width"
    knowledge = "Width of the room would be equal or less than that of the entire house"

    given_value_start = 10
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The width of {name}'s house is {given_value} units.",
            "{name} recently bought a new house whose width was {given_value} units."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The width of {name}'s room in that house could be {hyp_value} units.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the width of {name}'s room in that house?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def family(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "family"
    knowledge = "Family consists of all the members"

    given_value_start = 1
    given_value_end = 5

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} sons and a few daughters.",
            "{name} is a person, who is father of  few daughters and {given_value} sons."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name}'s could be having {hyp_value} kids.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=9,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )

        question_template = random.choice([
            "What could be the number of {name}'s kids?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=9,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def literate(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "literate"
    knowledge = "Total members is sum of literate and illiterate"

    given_value_start = 400
    given_value_end = 600

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A village has {given_value} literate and few illiterates",
            "There are many people in a village. Out of all the population, few of them are illitrates, and the rest {given_value} are literate."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The population of the village could be {hyp_value}.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=200,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=50
        )

        question_template = random.choice([
            "What could be the number of {name}'s kids?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=200,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=50
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def electric_bill(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "electric_bill"
    knowledge = "Electric bill of two houses combined is more than that of an individual house"

    given_value_start = 400
    given_value_end = 600

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s electric bill for this month is {given_value} dollars. {name} has to pay electric bill of his brother's home also.",
            "{name} pays electric bill for his house and his brother's house every month. His bill for this month was {given_value} dollars."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The combined electric bill could be {hyp_value} dollars.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=200,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=50
        )

        question_template = random.choice([
            "What could be the combined electric bill?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=200,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=50
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def passing(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "passing"
    knowledge = "Students who pass an exam can not be more than the number of students who gave the exam"

    given_value_start = 40
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{given_value} students appeared for the exam.",
            "Government of USA conducted an exam, in which {given_value} students appeared."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} could pass that exam.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=100,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the number of students who pass that exam?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=100,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def school(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "school"
    knowledge = "Number of government run schools can not be more than the total number of schools."

    given_value_start = 40
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In the capital city, there are a total of {given_value} schools.",
            "{name} lives in a city where {given_value} is the total number of schools."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} government-run schools in the city.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the number of government run schools in the city?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def price(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "price"
    knowledge = "Price of a branded watch would be more than a regular watch"

    given_value_start = 400
    given_value_end = 600

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The price of a branded watch is {given_value}. {name} decided to buy a regular watch.",
            "{name} bought a very expensive watch from his first salary whose cost was {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The price of a regular watch could be {hyp_value} dollars.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=300,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=50
        )

        question_template = random.choice([
            "What could be the price of a regular watch?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=300,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=50
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def price2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "price"
    knowledge = "Price of a branded watch would be more than a regular watch"

    given_value_start = 400
    given_value_end = 600

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The price of a regular watch is {given_value}. {name} decided to buy a branded watch.",
            "{name} is a rich person, so instead of buying a regular watch of {given_value} he bought a branded watch."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The price of a branded watch could be {hyp_value} dollars.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=300,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=50
        )

        question_template = random.choice([
            "What could be the price of a branded watch?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=300,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=50
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def teaching(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "teaching"
    knowledge = "Total staff is more than the teaching staff in a school"

    given_value_start = 40
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are {given_value} teachers in a school and a few administrative people.",
            "{name} is the owner of a school. In his staff, he has {given_value} teachers and some peopl who work for administration."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The total staff of the school could be {hyp_value} dollars.",
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
            "What could be the total staff of the school?",

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


def speed_ticket(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "speed_ticket"
    knowledge = "One gets a speed ticket if he exceeds the speed limit"

    given_value_start = 40
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} goes on a road trip to Vegas and at night he got pulled over by a Sheriff and received a speed ticket for exceeding the limit of {given_value}.",
            "{name} was late for his office, so he exceeded the speed limit of {given_value}. He was stopped by cops and was given a ticket for over speeding by cops."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could be driving at a speed of {hyp_value}.",
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
            "What could be his possible speed?",

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


def force_same_direction(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "force_same_direction"
    knowledge = "If force is applied in the same direction it increases the speed of cart"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is pushing a cart. He is managing to push the cart a speed of {given_value} units. Then, his friend starts to apply force with him in the same direction.",
            "{name} pushes a cart with speed of {given_value}, then after sometime his friend starts helping him, and applies the force in same direction as {name} is applying."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "They could manage to push the cart at a speed of {hyp_value}.",
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
            "What could be the speed of the cart now?",

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


def force_opposite_direction(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "force_opposite_direction"
    knowledge = "If force is applied in the opposite direction it decreases the speed of cart"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is pushing a cart. He is managing to push the cart a speed of {given_value} units. Then, his friend starts to apply force in the opposite direction.",
            "{name} pushes a cart with speed of {given_value}, then after sometime his friend starts helping him, and applies the force in opposite direction as {name} is applying."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "They could manage to push the cart at a speed of {hyp_value}.",
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
            "What could be the speed of the cart now?",

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


def rafting_downstream(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "rafting_downstream"
    knowledge = "speed of the downstream river adds to the speed of the raft"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is rowing a boat. The speed of the boat in still water is {given_value}. Now, {name} starts to go downstream.",
            "{name} participates in a boat racing competition. He first rows the boat in still water with a speed of {given_value} and then starts to go downstream."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The overall speed of the raft could be {hyp_value} units in downstream.",
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
            "What could be the overall speed of the raft in downstream?",

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


def rafting_downstream2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "rafting_downstream"
    knowledge = "speed of the downstream river adds to the speed of the raft"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is rowing a boat. The time taken to cross the river in still water is {given_value} minutes. While coming back {name} goes downstream.",
            "{name} participates in a boat racing competition. He first rows the boat in still water and takes {given_value} minutes to corss and then while coming back starts going downstream."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The time taken to come back could be {hyp_value} units in downstream.",
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
            "What could be the time taken to come back in downstream?",

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


def rafting_upstream(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "rafting_upstream"
    knowledge = "speed of the upstream river reduces the speed of the raft"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is rowing a boat. The speed of the boat in still water is {given_value}. Now, {name} starts to go upstream.",
            "{name} participates in a boat racing competition. He first rows the boat in still water with a speed of {given_value} and then starts to go upstream."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The overall speed of the raft could be {hyp_value} units in upstream.",
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
            "What could be the overall speed of the raft in upstream?",

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


def rafting_upstream2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "rafting_upstream"
    knowledge = "speed of the upstream river reduces the speed of the raft"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is rowing a boat. The time taken to cross the river in still water is {given_value} minutes. While coming back {name} starts to go upstream.",
            "{name} participates in a boat racing competition. He first rows the boat in still water and takes {given_value} minutes to corss and then while coming back starts going upstream."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The time taken to come back could be {hyp_value} units in upstream.",
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
            "What could be the time taken to come back in upstream?",

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


def legal_age(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "legal_age"
    knowledge = "One is allowed to join the tournament if they satisfy the age criteria"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The maximum age to play a tennis tournament is {given_value} years. {name} was allowed to play this tournament.",
            "The maximum age to play a table-tennis tournament is {given_value} years. {name} was allowed to play this tournament."
            "The maximum age to play a badminton tournament is {given_value} years. {name} was allowed to play this tournament.",
            "The maximum age to play a lawn-tennis tournament is {given_value} years. {name} was allowed to play this tournament."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be {hyp_value} years old.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be his age?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def legal_age2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "legal_age"
    knowledge = "One is allowed to join the tournament if they satisfy the age criteria"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The maximum age to play a tennis tournament is {given_value} years. {name} was not allowed to play this tournament due to age criteria.",
            "The maximum age to play a lawn-tennis tournament is {given_value} years. {name} was not allowed to play this tournament due to age criteria."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be {hyp_value} years old.",
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
            "What could be his age?",

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


def legal_age3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "legal_age"
    knowledge = "One is allowed to join the tournament if they satisfy the age criteria"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The minimum age to play a tennis tournament is {given_value} years. {name} was allowed to play this tournament due to age criteria.",
            "The minimum age to play a lawn-tennis tournament is {given_value} years. {name} was allowed to play this tournament due to age criteria."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be {hyp_value} years old.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be his age?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def legal_age4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "legal_age"
    knowledge = "One is allowed to join the tournament if they satisfy the age criteria"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The minimum age to play a tennis tournament is {given_value} years. {name} was not allowed to play this tournament due to age criteria.",
            "The minimum age to play a table-tennis tournament is {given_value} years. {name} was not allowed to play this tournament due to age criteria."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be {hyp_value} years old.",
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
            "What could be his age?",

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


def density(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "density"
    knowledge = "A liquid with lesser density floats on another liquid"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Density of a liquid is {given_value} units. It floats on another liquid.",
            "{name} has two different liquids in a flask. One of them floats over the other liquid has density of {given_value} units"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Density of the other liquid could be {hyp_value} units.",
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
            "What could be the density of the other liquid?",

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


def density2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "density"
    knowledge = "A liquid with lesser density floats on another liquid"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Density of a liquid is {given_value} units. Another liquid floats on this liquid.",
            "{name} has two different liquids in a flask.Density of one of them is {given_value} units on which another liquid floats"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Density of the other liquid could be {hyp_value} units.",
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
            "What could be the density of the other liquid?",

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


def gravity(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "gravity"
    knowledge = "Gravitational pull decreases as the distance from Earth increases"

    given_value_start = 5
    given_value_end = 9

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The gravitational pull 1000 units above the Earth's surface is {given_value}. ",
            "{given_value} is the gravitational pull 1000 units above the Earth's surface. "
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Gravitational pull 6000 units above the Earth's surface could be {hyp_value}.",
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
            "What could be the gravitational pull 6000 units above the Earth's surface?",

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


def gravity2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "gravity"
    knowledge = "Gravitational pull decreases as the distance from Earth increases"

    given_value_start = 5
    given_value_end = 8

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The gravitational pull 1000 units above the Earth's surface is {given_value}. ",
            "{given_value} is the gravitational pull 1000 units above the Earth's surface."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Gravitational pull 600 units above the Earth's surface could be {hyp_value}.",
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
            "What could be the gravitational pull 6000 units above the Earth's surface?",

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


def account_balance(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "account_balance"
    knowledge = "One can not withdraw more money than the amount in their bank account"

    given_value_start = 500
    given_value_end = 800

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars in his account. He wants to buy a bike.",
            "{name} wants to buy a sports car. He has {given_value} dollars in his bank account."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The cost of the vehicle is {hyp_value}. {name} could buy the vehicle from his account.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=250,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=50,
            scale=50
        )

        question_template = random.choice([
            "At what cost could {name} buy the vehicle from his account?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=250,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=50,
            scale=50
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def account_balance2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "account_balance"
    knowledge = "One can not withdraw more money than the amount in their bank account"

    given_value_start = 500
    given_value_end = 800

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Cost of a bike is {given_value} dollars. {name} wants to buy this bike.",
            "{name} wants to buy a sports car which has cost of {given_value} dollars."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} has {hyp_value} dollars in his account. {name} could buy the vehicle from his account.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=250,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=50,
            scale=50
        )

        question_template = random.choice([
            "How much money {name} could have to buy the vehicle from his account?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=250,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=50,
            scale=50
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def hotel_capacity(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "hotel_capacity"
    knowledge = "Occupants can not exceed the capcity of a hotel"

    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The hotel Grand can accommodate {given_value} customers at once.",
            "A new hotel Grand was inaugrated. in that hotel, a total of {given_value} customers can be accomodated at once."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "On Monday, {hyp_value} customers could be residing in the hotel.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=50,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many customers could be residing in the hotel on Monday?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def sound_limit(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "sound_limit"
    knowledge = "A music system can not produce sound more than its limit"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A music system's volume ranges from 0 to {given_value} units.",
            "Maximum volume of a music system is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} bought this system and played it in his party. He could have played the music at a volume of {hyp_value} units",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "{name} bought this system and played it in his party. At what volume he could have played the music?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def sound_limit2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "sound_limit"
    knowledge = "A music system can not produce sound more than its limit"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a music system and played it at a volume of {given_value} units.",
            "{name} was listening to music in his music system at {given_value} units volume."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The maximum volume of this system could be {hyp_value} units.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the maximum volume of this system?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def temperature(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "temperature"
    knowledge = "An instrument can not measure values beyond its limit"

    given_value_start = 50
    given_value_end = 80

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "An instrument can measure temperature till {given_value} units.",
            "{name} bought an instrument which measures temprature. The upper range of temprature which can be meaured with that instrument is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "In the month of June, it became extremely hot and the temperature reached {hyp_value} units. The instrument could measure this temperature.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "In the month of June, it became extremely hot. What temperature can this instrument measure?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
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

#     template_binary_instances, template_mcq_instances = account_balance(
#         repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
