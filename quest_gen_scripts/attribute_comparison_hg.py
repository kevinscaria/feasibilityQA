import util
import random
import pprint
import numpy as np


def momentum_and_velocity1(repetition_count):
    category, subcategory = "attribute_comparison", "momentum_and_velocity",
    knowledge = "Momentum is directly proportional to velocity."

    binary_instances = []
    mcq_instances = []
    given_value_start = 60
    given_value_end = 90

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to observe the relationship between momentum and velocity for two identical objects moving with different velocities. The faster object has a momentum of {given_value} units.",
            "{name}'s experiment is to observe the relationship between the momentum and speed for two objects that move with different speed.The objects are identical in nature. The quicker object has a momentum of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The momentum of slower object could be {hyp_value} units.",

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
            "What could be momentum of the slower object?",

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


def momentum_and_velocity2(repetition_count):
    category, subcategory = "attribute_comparison", "momentum_and_velocity",
    knowledge = "Momentum is directly proportional to velocity."

    binary_instances = []
    mcq_instances = []
    given_value_start = 600
    given_value_end = 900

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is working in a physics lab and he was assigned to observe the relationship between momentum and velocity for identical objects moving with different velocities. The slower object has a momentum of {given_value} units.",
            "{name}'s experiment is to observe the relationship between the momentum and speed for two objects that move with different speed.The objects are identical in nature. The quicker object has a momentum of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The momentum of faster object could be {hyp_value} units.",

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
            "What could be momentum of the faster object?",

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


def momentum_and_mass1(repetition_count):
    category, subcategory = "attribute_comparison", "momentum_and_mass",
    knowledge = "Momentum is directly proportional to mass."

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 100

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two different objects moving with same velocities. The heavier object has a momentum of {given_value} units.",
            "There are two objects moving with same velocities. The objects have different masses. The heavier object has a momentum of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The momentum of lighter object could be {hyp_value} units.",

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
            "What could be momentum of the lighter object?",

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


def momentum_and_mass2(repetition_count):
    category, subcategory = "attribute_comparison", "momentum_and_mass",
    knowledge = "Momentum is directly proportional to mass"

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 100

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two athletes running with same velocities. The lighter athlete has a momentum of {given_value} units.",
            "There are two athletes moving with same velocities. The athletes have different masses. The lighter athlete has a momentum of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The momentum of heavier athlete could be {hyp_value} units.",

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
            "What could be momentum of the heavier athlete?",

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


def kinetic_energy_and_speed1(repetition_count):
    category, subcategory = "attribute_comparison", "kinetic_energy_and_speed",
    knowledge = "Kinetic energy is directly proportional to speed."

    binary_instances = []
    mcq_instances = []
    given_value_start = 60
    given_value_end = 90

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls rolling down the mountain with different speeds. The faster ball has a kinetic energy of {given_value} units.",
            "There are two balls that rolled through the mountain with different speeds.The balls were identical in nature. The ball with more speed has a kinetic energy of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The kinetic energy of slower ball could be {hyp_value} units.",

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
            "What could be kinetic energy of the slower ball?",

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


def kinetic_energy_and_speed2(repetition_count):
    category, subcategory = "attribute_comparison", "kinetic_energy_and_speed",
    knowledge = "Kinetic energy is directly proportional to speed."

    binary_instances = []
    mcq_instances = []
    given_value_start = 60
    given_value_end = 90

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two identical balls rolling down the mountain with different speeds. The slower ball has a kinetic energy of {given_value} units.",
            "There are two balls that rolled through the mountain with different speeds.The balls were identical in nature. The ball with less speed has a kinetic energy of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The kinetic energy of slower ball could be {hyp_value} units.",

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
            "What could be kinetic energy of the faster ball?",

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


def kinetic_energy_and_mass1(repetition_count):
    category, subcategory = "attribute_comparison", "kinetic_energy_and_mass",
    knowledge = "Kinetic energy is directly proportional to mass."

    binary_instances = []
    mcq_instances = []
    given_value_start = 5000
    given_value_end = 10000

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There were two different cannon balls launched from a cannon during a battle in world war 2. Both cannon balls had the same speed but had different masses. The heavier cannon ball has a kinetic energy of {given_value} Joules.",
            "During a battle in World War II, there were two different cannon balls thrown from a cannon. Both cannon balls had different masses, but had the same speed. The cannon ball with more mass has a kinetic energy of {given_value} joules."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The kinetic energy of lighter cannon ball could be {hyp_value} units.",

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
            "What could be kinetic energy of the lighter cannon ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=1000,
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


def kinetic_energy_and_mass2(repetition_count):
    category, subcategory = "attribute_comparison", "kinetic_energy_and_mass",
    knowledge = "Kinetic energy is directly proportional to mass of the object."

    binary_instances = []
    mcq_instances = []
    given_value_start = 5000
    given_value_end = 10000

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There were two different cannon balls launched from a cannon during a battle in world war 2. Both cannon balls had the same speed but had different masses. The lighter cannon ball has a kinetic energy of {given_value} units.",
            "During a battle in World War II, there were two different cannon balls thrown from a cannon. Both cannon balls had different masses, but had the same speed. The cannon ball with less mass has a kinetic energy of {given_value} joules."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The kinetic energy of heavier cannon ball could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=1000,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be kinetic energy of the heavier cannon ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=1000,
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


def force_and_acceleration(repetition_count):
    category, subcategory = "attribute_comparison", "force_and_acceleration",
    knowledge = "Acceleration of an object is directly proportional to the force applied."

    binary_instances = []
    mcq_instances = []
    given_value_start = 700
    given_value_end = 900

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There is a bodybuilding championship going on and the contestants have to push identical objects to prove their strength. The winner is able to generate a larger force and is able to push the object with an acceleration of {given_value} units.",
            "There is a bodybuilding championship and contestants have to push identical objects to show their strength. The winner is capable of generating a larger force and is able to push the object with an acceleration of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The runner up pushed the object with lesser force. The acceleration of the object could be {hyp_value} units.",

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
            "What could be the acceleration of the object on which lesser force is applied?",

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


def force_and_acceleration2(repetition_count):
    category, subcategory = "attribute_comparison", "force_and_acceleration",
    knowledge = "Acceleration of an object is directly proportional to the force applied."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2000
    given_value_end = 3000

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There is a bodybuilding championship going on and the contestants have to push identical objects to prove their strength. The runner up is able to generate a smaller force and is able to push the object with an acceleration of {given_value} units.",
            "There is a bodybuilding championship and contestants have to push identical objects to show their strength. The runner-up is capable of generating a larger force and is able to push the object with an acceleration of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The winner pushed the object with greater force. The acceleration of the object could be {hyp_value} units.",

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
            "What could be the acceleration of the object on which higher force is applied?",

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


def force_and_acceleration3(repetition_count):
    category, subcategory = "attribute_comparison", "force_and_acceleration",
    knowledge = "Given the same force, an object with higher mass will have lower acceleration."

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 100

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is relocating to a new home and has to push different boxes to his room. There are two boxes. The first box contains books and is significantly heavy than the second box which contains pillows. The heavier box is pushed with an acceleration of {given_value} units.",
            "{name} is relocating to a new home and has to push two boxes to his room. The first box contains books and is significantly heavy than the second box containing pillows. The heavier box is pushed with an acceleration of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Acceleration of lighter box could be {hyp_value} units.",

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
            "What could be the acceleration of lighter box?",

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


def force_and_acceleration4(repetition_count):
    category, subcategory = "attribute_comparison", "force_and_acceleration",
    knowledge = "Given the same force, an object with higher mass will have lower acceleration."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 14

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is relocating to a new home and has to push different boxes to his room. There are two boxes. The first box contains books and is significantly heavy than the second box which contains pillows. Acceleration of the lighter box is {given_value} units.",
            "{name} is relocating to a new home and has to push two boxes to his room. The first box contains books and is significantly heavy than the second box containing pillows. The lighter box is pushed with an acceleration of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Acceleration of heavier box could be {hyp_value} units.",

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
            "What could be the acceleration of heavier box?",

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


def frequency_and_wavelength(repetition_count):
    category, subcategory = "attribute_comparison", "frequency and wavelength",
    knowledge = "Given two waves with same velocity, a wave with higher frequency will have lower wavelength."

    binary_instances = []
    mcq_instances = []
    given_value_start = 60000
    given_value_end = 90000

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two waves moving with same velocities and {name} has to find the relationship between their frequency and wavelength. Wavelength of the wave with higher frequency is {given_value} units.",
            "There are two waves that move with the same speeds and {name} has to find the relationship between its frequency and wavelength. The wavelength of the wave more frequency is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Wavelength of the wave with lower frequency could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=2000,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1000,
            scale=1000
        )

        question_template = random.choice([
            "What could be the wavelength of the wave with lower frequency?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=1000,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=100,
            scale=5
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def frequency_and_wavelength2(repetition_count):
    category, subcategory = "attribute_comparison", "frequency and wavelength",
    knowledge = "Given two waves with same velocity, the wave with higher frequency will have lower wavelength."

    binary_instances = []
    mcq_instances = []
    given_value_start = 60000
    given_value_end = 90000

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two waves moving with same velocities and {name} is assigned to find out the relationship between their frequency and wavelength. Frequency of the wave with lower wavelength is {given_value} units.",
            "There are two waves that move with the same speeds and {name} has to find the relationship between its frequency and wavelength. The wavelength of the wave with lower frequency is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Frequency of the wave with higher wavelength could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10000,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1000,
            scale=2000
        )

        question_template = random.choice([
            "What could be the frequency of the wave with lower wavelength?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=1000,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=100,
            scale=5
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )
    return binary_instances, mcq_instances


def sprint_race(repetition_count):
    category, subcategory = "attribute_comparison", "sprint_race",
    knowledge = "In a racing event, a person or a vehicle with least time to complete the event finishes first."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is participating in a race and he finishes the race in {given_value} seconds. He won the race.",
            "{name} is a racing driver of Formula 1 and he finished first in the race. The time taken by him to finish the race was {given_value} minutes."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Time taken by other athletes to finish the race could be {hyp_value} seconds.",
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
            "What could be the time taken by other athletes to finish the race?",

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


def f1_race(repetition_count):
    category, subcategory = "attribute_comparison", "f1_race",
    knowledge = "In a racing event, a person or a vehicle with least time to complete the event finishes first."

    binary_instances = []
    mcq_instances = []
    given_value_start = 150
    given_value_end = 200

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}' is a formula 1 race car driver and he came second in a race. The time taken by him to finish the race was {given_value} mins.",
            "{name} is a racing driver of Formula 1 and he finished second in the race. The time taken by him to finish the race was {given_value} minutes."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Time taken by the winner of the race to finish could be {hyp_value} mins.",
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
            "What could be the time taken by other f1 driver to finish the race?",

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


def floors_and_rooms(repetition_count):
    category, subcategory = "attribute_comparison", "floors_and_rooms",
    knowledge = "If two buildings have the same base area and room size, the building with more floors will have more rooms."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} visited NewYork and saw two building with the same base area. He was also told by his guide that the room dimensions of both buildings are same. One of the building is taller than the other and has {given_value} rooms.",
            "{name} visited Newyork and saw two buildings with the same base area. His guide also told him that the dimensions of the room of both buildings are equal. One of the buildings is taller than the other and has {given_value} rooms."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The shorter building could have {hyp_value} rooms.",

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
            "What could be the number of rooms in shorter building?",

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


def high_and_low_temp(repetition_count):
    category, subcategory = "attribute_comparison", "high_and_low_temp",
    knowledge = "Temperature of a place typically decreases with increase in altitude."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} visited a mountain which was extremely cold and was 8000 meters high. The temperature at the highest point of the mountain was {given_value} fahrenheit. Later, he climbed down the mountain where the temperature was significantly higher.",
            "{name} visited a mountain that was extremely cold and was 8000 meters high. The temperature was {given_value} Fahrenheit at the highest point of the mountain. Later, he went down to the mountain where the temperature was significantly higher."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The temperature at the base of the mountain could be {hyp_value} fahrenheit.",

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
            "What could be the temperature at the base of the mountain?",

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


def cooling_and_wind(repetition_count):
    category, subcategory = "attribute_comparison", "cooling_and_wind",
    knowledge = "Higher speed of wind will help in better evaporation."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has a wet towel and left it out to dry. {name} lives in a windy place and the wind speed was high. That day, the towel was dried at {given_value} minutes. Next day he kept his towel out to dry again when the wind speed was significantly lower.",
            "{name} has a wet towel and left it to dry. {name} lives in a windy place and the wind speed was high. That day, the towel dried at {given_value} minutes. The next day, he kept his towel to dry again when the wind speed was significantly lower."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The towel could have dried in {hyp_value} minutes.",

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
            "What could be the drying time of the towel ?",

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


def power_and_luminocity(repetition_count):
    category, subcategory = "attribute_comparison", "power_and_luminocity",
    knowledge = "Bulbs or lights with higher wattage will be brighter."

    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} purchased a bulb of {given_value} watts. He felt the bulb was too bright and purchased a new bulb that was dimmer.",
            "{name} bought a {given_value}-watt bulb. He felt the light bulb was too bright and bought a new light bulb that was dimmer."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The new bulb could be of {hyp_value} watts.",
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
            "What could be the wattage of the new bulb?",

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


def bus_capacity(repetition_count):
    category, subcategory = "attribute_comparison", "car_capacity",
    knowledge = "Bigger vehicles have more seating capacity."

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} purchased a bus with a capacity of {given_value} people. He later purchased a new bus with a higher capacity.",
            "{name} bought a bus with a capacity of {given_value} people. Later, he bought a new bus with a higher capacity."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The seating capacity of the new bus could be {hyp_value} people.",
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
            "What could be the seating capacity of the new bus?",

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

# if __name__ == "__main__":
#     repetition_count = 1
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = bus_capacity(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
