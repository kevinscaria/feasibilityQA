import util
import random
import pprint
import numpy as np


def elongation_and_tensile_strength1(repetition_count):
    category, subcategory = "attribute_comparison", "elongation_and_tensile_strength",
    knowledge = "Elongation is inversely proportional to the tensile strength."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} conducted a survey on train accidents due to elongation of railway tracks where he observed that the elongation of metals change with tensile strength of metals. The elongation of the metal with higher tensile strength is {given_value} units.",
            "{name} had two iron rods with different tensile strengths. The elongation of the metal with higher tensile strength is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Elongation of could be {hyp_value} units.",

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
            "What could be the elongation of the other metal?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def elongation_and_tensile_strength2(repetition_count):
    category, subcategory = "attribute_comparison", "elongation_and_tensile_strength",
    knowledge = "Elongation is inversely proportional to the tensile strength."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} conducted a survey on train accidents due to elongation of railway tracks where he observed that the elongation of metals change with tensile strength of metals. The tensile strength of the metal with more elongation is {given_value} units.",
            "{name} had two iron bars of different lengths. The tensile strewngth of the metal with more elongation was {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Tensile strength of the other metal could be {hyp_value} units.",

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
            "What could be the tensile strength of the other metal?",

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


def elongation_and_tensile_strength3(repetition_count):
    category, subcategory = "attribute_comparison", "elongation_and_tensile_strength",
    knowledge = "Elongation is inversely proportional to the tensile strength."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} conducted a survey on train accidents due to elongation of railway tracks where he observed that the elongation of metals change with tensile strength of metals. The elongation of the metal with lower tensile strength is {given_value} units.",
            "{name} had two iron rods with different tensile strengths. The elongation of the metal with lower tensile strength is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Elongation of other metal could be {hyp_value} units.",

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
            "What could be the elongation of the other metal?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def elongation_and_tensile_strength4(repetition_count):
    category, subcategory = "attribute_comparison", "elongation_and_tensile_strength",
    knowledge = "Elongation is inversely proportional to the tensile strength."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} conducted a survey on train accidents due to elongation of railway tracks where he observed that the elongation of metals change with tensile strength of metals. The tensile strength of the metal with less elongation is {given_value} units.",
            "{name} had two iron bars of different lengths. The tensile strewngth of the metal with more elongation was {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Tensile strength of the other metal could be {hyp_value} units.",

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
            "What could be the tensile strength of the other metal?",

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


def flash_point_and_flammability1(repetition_count):
    category, subcategory = "attribute_comparison", "flash_point_and_flammability",
    knowledge = "Liquids with lower flash points ignite easier."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 250

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a forensic department officer who was appointed to check out the fire accident scene. As part of the case, he is checking how the flash point and flammability of two liquids vary. The flash point of the liquid with higher flammability is {given_value} units.",
            "{name} was conducting a survey on the fire accident scene. He identified two liquids. Further analysis showed the flash point of the liquid with higher flammability is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Flash point of the other liquid could be {hyp_value} units.",

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
            "What could be the flash point of the other liquid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def flash_point_and_flammability2(repetition_count):
    category, subcategory = "attribute_comparison", "flash_point_and_flammability",
    knowledge = "Liquids with lower flash points ignite easier."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a forensic department officer who was appointed to check out the fire accident scene. As part of the case, he is checking how the flash point and flammability of two liquids vary. The flash point of the liquid with lower flammability is {given_value} units.",
            "{name} was conducting a survey on the fire accident scene. He identified two liquids. Further analysis showed the flash point of the liquid with lower flammability is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Flash point of the other liquid could be {hyp_value} units.",

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
            "What could be the flash point of the other liquid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def pressure_and_volume1(repetition_count):
    category, subcategory = "attribute_comparison", "pressure_and_volume",
    knowledge = "The volume of an ideal gas is inversely proportional to the pressure of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to understand the ideal gas laws between two gases to use it in the working of air bags. The volume of the gas with higher pressure is {given_value} units.",
            "To identify optimal gases to be used in airbags, {name} was pressure testing it with two gases. The volume of gas with higher pressure is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of the other gas could be {hyp_value} units.",

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
            "What could be the volume of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def pressure_and_volume2(repetition_count):
    category, subcategory = "attribute_comparison", "pressure_and_volume",
    knowledge = "The volume of an ideal gas is inversely proportional to the pressure of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 65

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to understand the ideal gas laws between two gases to use it in the working of air bags. The pressure of the gas with higher volume is {given_value} units.",
            "To identify optimal gases to be used in airbags, {name} was volume testing it with two gases. The pressure of gas with lower volume is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Pressure of the other gas could be {hyp_value} units.",

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
            "What could be the pressure of the other gas?",

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


def pressure_and_volume3(repetition_count):
    category, subcategory = "attribute_comparison", "pressure_and_volume",
    knowledge = "The volume of an ideal gas is inversely proportional to the pressure of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 45

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to understand the ideal gas laws between two gases to use it in the working of air bags. The volume of the gas with lower pressure is {given_value} units.",
            "To identify optimal gases to be used in airbags, {name} was pressure testing it with two gases. The volume of gas with lower pressure is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of the other gas could be {hyp_value} units.",

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
            "What could be the volume of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def pressure_and_volume4(repetition_count):
    category, subcategory = "attribute_comparison", "pressure_and_volume",
    knowledge = "The volume of an ideal gas is inversely proportional to the pressure of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to understand the ideal gas laws between two gases to use it in the working of air bags. The pressure of the gas with lower volume is {given_value} units.",
            "To identify optimal gases to be used in airbags, {name} was pressure testing it with two gases. The volume of gas with higher pressure is {given_value} units."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Pressure of the other gas could be {hyp_value} units.",

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
            "What could be the pressure of the other gas?",

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


def viscosity_and_temperature1(repetition_count):
    category, subcategory = "attribute_comparison", "viscosity_and_temperature",
    knowledge = "The viscosity of liquids decreases rapidly with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Manufacturing equipment requires appropriate lubrication to run smoothly. {name} is a new joinee and is asked to make a report on two liquids to understand their viscocity with change in temperature. The viscosity of the liquid with higher temperature is {given_value} units.",
            "To identify the best lubricant for the manufacturing equipment, {name} was testing it with two liquids. The viscosity of the liquid with higher temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Viscosity of the other liquid could be {hyp_value} units.",

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
            "What could be the viscosity of the other liquid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def viscosity_and_temperature2(repetition_count):
    category, subcategory = "attribute_comparison", "viscosity_and_temperature",
    knowledge = "The viscosity of liquids decreases rapidly with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Manufacturing equipment requires appropriate lubrication to run smoothly. {name} is a new joinee and is asked to make a report on two liquids to understand their viscocity with change in temperature. The temperature of the liquid with higher viscosity is {given_value} units.",
            "To identify the best lubricant for the manufacturing equipment, {name} was testing it with two liquids. The temperature of the liquid with higher viscosity is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other liquid could be {hyp_value} units.",

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
            "What could be the temperature of the other liquid?",

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


def viscosity_and_temperature3(repetition_count):
    category, subcategory = "attribute_comparison", "viscosity_and_temperature",
    knowledge = "The viscosity of liquids decreases rapidly with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Manufacturing equipment requires appropriate lubrication to run smoothly. {name} is a new joinee and is asked to make a report on two liquids to understand their viscocity with change in temperature. The viscosity of the liquid with lower temperature is {given_value} units.",
            "To identify the best lubricant for the manufacturing equipment, {name} was testing it with two liquids. The viscosity of the liquid with lower temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Viscosity of the other liquid could be {hyp_value} units.",

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
            "What could be the viscosity of the other liquid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def viscosity_and_temperature4(repetition_count):
    category, subcategory = "attribute_comparison", "viscosity_and_temperature",
    knowledge = "The viscosity of liquids decreases rapidly with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Manufacturing equipment requires appropriate lubrication to run smoothly. {name} is a new joinee and is asked to make a report on two liquids to understand their viscocity with change in temperature. The temperature of the liquid with lower viscosity is {given_value} units.",
            "To identify the best lubricant for the manufacturing equipment, {name} was testing it with two liquids. The temperature of the liquid with lower viscosity is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other gas could be {hyp_value} units.",

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
            "What could be the temperature of the other liquid?",

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


def viscosity_and_temperature_gas1(repetition_count):
    category, subcategory = "attribute_comparison", "viscosity_and_temperature_gas",
    knowledge = "The viscosity of gases increases with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 18
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The viscosity of gases played an important role in the historical development of the kinetic theory of gases. {name} is very intrigued by this development and wants to try it on own, how two gases viscocity change with temperature. The viscosity of the gas with higher temperature is {given_value} units.",
            "To understand the effect of viscosity on the kinetic theory of gases, {name} was testing it with two gases. The viscosity of the gas with higher temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Viscosity of the other gas could be {hyp_value} units.",
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
            "What could be the viscosity of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def viscosity_and_temperature_gas2(repetition_count):
    category, subcategory = "attribute_comparison", "viscosity_and_temperature_gas",
    knowledge = "The viscosity of gases increases with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 90

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The viscosity of gases played an important role in the historical development of the kinetic theory of gases. {name} is very intrigued by this development and wants to try it on own, how two gases viscocity change with temperature. The temperature of the gas with higher viscosity is {given_value} units.",
            "To understand the effect of viscosity on the kinetic theory of gases, {name} was testing it with two gases. The temperature of the gas with higher viscosity is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other gas could be {hyp_value} units.",

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
            "What could be the temperature of the other gas?",

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


def viscosity_and_temperature_gas3(repetition_count):
    category, subcategory = "attribute_comparison", "viscosity_and_temperature_gas",
    knowledge = "The viscosity of gases increases with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 8
    given_value_end = 59

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The viscosity of gases played an important role in the historical development of the kinetic theory of gases. {name} is very intrigued by this development and wants to try it on own, how two gases viscocity change with temperature. The viscosity of the gas with lower temperature is {given_value} units.",
            "To understand the effect of viscosity on the kinetic theory of gases, {name} was testing it with two gases. The viscosity of the gas with lower temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Viscosity of the other gas could be {hyp_value} units.",

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
            "What could be the viscosity of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def viscosity_and_temperature_gas4(repetition_count):
    category, subcategory = "attribute_comparison", "viscosity_and_temperature_gas",
    knowledge = "The viscosity of gases increases with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 100

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The viscosity of gases played an important role in the historical development of the kinetic theory of gases. {name} is very intrigued by this development and wants to try it on own, how two gases viscocity change with temperature. The temperature of the gas with lower viscosity is {given_value} units.",
            "To understand the effect of viscosity on the kinetic theory of gases, {name} was testing it with two gases. The temperature of the gas with lower viscosity is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other gas could be {hyp_value} units.",

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
            "What could be the temperature of the other gas?",

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


def wetting_and_contact_angle1(repetition_count):
    category, subcategory = "attribute_comparison", "wetting_and_contact_angle",
    knowledge = "Small contact angles correspond to high wettability."

    binary_instances = []
    mcq_instances = []
    given_value_start = 5
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is working in a car repair shop where wettability is used to prevent corrosion with two different liquids. He found that the effectiveness of two liquids is different and is verifying the change by comparing their contact angles and wettability. The contact angle of the liquid with higher wettability is {given_value} degrees.",
            "To verify the effectiveness of two liquids, {name} was comparing their contact angles and wettability. The contact angle of the liquid with higher wettability is {given_value} degrees."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Contact angle of the other liquid could be {hyp_value} degrees.",

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
            "What could be the contact angle of the other liquid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def wetting_and_contact_angle2(repetition_count):
    category, subcategory = "attribute_comparison", "wetting_and_contact_angle",
    knowledge = "Small contact angles correspond to high wettability."

    binary_instances = []
    mcq_instances = []
    given_value_start = 8
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is working in a car repair shop where wettability is used to prevent corrosion with two different liquids. He found that the effectiveness of two liquids is different and is verifying the change by comparing their contact angles and wettability. The contact angle of the liquid with lower wettability is {given_value} degrees.",
            "To verify the effectiveness of two liquids, {name} was comparing their contact angles and wettability. The contact angle of the liquid with lower wettability is {given_value} degrees."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Contact angle of the other liquid could be {hyp_value} degrees.",

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
            "What could be the contact angle of the other liquid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def surface_tension_and_temperature1(repetition_count):
    category, subcategory = "attribute_comparison", "surface_tension_and_temperature",
    knowledge = "Surface tension decreases when the temperature increases."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 35

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is washing clothes using water in two different temperatures and found that efficiency of water increased by lowering the surface tension which is how they resist external force with change in temperature. The surface tension of the liquid with higher temperature is {given_value} units.",
            "{name} wanted to wash clothes quicker as he had an important meeting coming up. So he decides to test the effect of surface tension of water in different temperatures. The surface tension of liquid with higher temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Surface tension of the other water could be {hyp_value} units.",

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
            "What could be the surface tension of the other water?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def surface_tension_and_temperature2(repetition_count):
    category, subcategory = "attribute_comparison", "surface_tension_and_temperature",
    knowledge = "Surface tension decreases when the temperature increases"

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 45

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is washing clothes using water in two different temperature and found that efficiency of water in cleaning by lowering the surface tension which is how they resist external force with change in temperature. The temperature of the liquid with higher surface tension is {given_value} units.",
            "{name} wanted to wash clothes quicker as he had an important meeting coming up. So he decides to test the effect of surface tension of water in different temperatures. The temperature of liquid with surface tension is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other water could be {hyp_value} units.",

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
            "What could be the temperature of the other water?",

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


def surface_tension_and_temperature3(repetition_count):
    category, subcategory = "attribute_comparison", "surface_tension_and_temperature",
    knowledge = "Surface tension decreases when the temperature increases."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 36

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is washing clothes using water in different temperatures and found that efficiency of water increased by lowering the surface tension which is how they resist external force with change in temperature. The surface tension of the liquid with lower temperature is {given_value} units.",
            "{name} wanted to wash clothes quicker as he had an important meeting coming up. So he decides to test the effect of surface tension of water in different temperatures. The surface tension of liquid with lower temperature is {given_value} units."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Surface tension of the other water could be {hyp_value} units.",

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
            "What could be the surface tension of the other water?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def surface_tension_and_temperature4(repetition_count):
    category, subcategory = "attribute_comparison", "surface_tension_and_temperature",
    knowledge = "Surface tension decreases when the temperature increases."

    binary_instances = []
    mcq_instances = []
    given_value_start = 14
    given_value_end = 46

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is washing clothes using two different temperature water and found that efficiency of water in cleaning by lowering the surface tension which is how they resist external force with change in temperature. The temperature of the liquid with lower surface tension is {given_value} units.",
            "{name} wanted to wash clothes quicker as he had an important meeting coming up. So he decides to test the effect of surface tension of water in different temperatures. The temperature of liquid with lower surface tension is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the water with higher surface tension could be {hyp_value} units.",

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
            "What could be the temperature of the other water?",

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


def entropy_and_pressure1(repetition_count):
    category, subcategory = "attribute_comparison", "entropy_and_pressure",
    knowledge = "The entropy of a system decreases with an increase in pressure."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 40

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is studying the entropy of a system with altering pressure. The pressure of the system when entropy of the system is high is {given_value} Pa.",
            "{name} wanted to study the effect of pressure on entropy of a system. The pressure of the system when entropy of the system is high is {given_value} Pa."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Pressure of the other system could be {hyp_value} Pa.",

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
            "What could be the pressure of the other system?",

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


def entropy_and_pressure2(repetition_count):
    category, subcategory = "attribute_comparison", "entropy_and_pressure",
    knowledge = "The entropy of a system decreases with an increase in pressure."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 40

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is studying the entropy of a system with altering pressure. The pressure of the system when entropy of the system is low is {given_value} Pa",
            "{name} wanted to study the effect of pressure on entropy of a system. The pressure of the system when entropy of the system is low is {given_value} Pa."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Pressure of the system when entropy is high could be {hyp_value} Pa.",

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
            "What could be the pressure of the system when entropy is high?",

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


def entropy_and_volume1(repetition_count):
    category, subcategory = "attribute_comparison", "entropy_and_volume",
    knowledge = "An increase in volume will increase the entropy."

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 100

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is studying the entropy of a system with altering volume. The volume of the system when entropy of the system is high is {given_value} units",
            "{name} wanted to study the effect of volume on entropy of a system. The volume of the system when entropy of the system is high is {given_value} Pa."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of the other system could be {hyp_value} units.",

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
            "What could be the volume of the other system?",

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


def entropy_and_volume2(repetition_count):
    category, subcategory = "attribute_comparison", "entropy_and_volume",
    knowledge = "An increase in volume will increase the entropy."

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 100

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is studying the entropy of a system with altering volume. The volume of the system when entropy of the system is low is {given_value} units.",
            "{name} wanted to study the effect of volume on entropy of a system. The volume of the system when entropy of the system is low is {given_value} Pa."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of the other system could be {hyp_value} units.",

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
            "What could be the volume of the other system?",

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


def diffusion_and_mass1(repetition_count):
    category, subcategory = "attribute_comparison", "diffusion_and_mass",
    knowledge = "The rate of diffusion is inversely proportional to the molar mass."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 100

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is studying the graham's law by filling containers with two different gases of different masses. The rate of diffusion of gas when mass is higher is {given_value} units.",
            "{name} as part of his assignment was given a problem about Graham's law. The question stated that the rate of diffusion of gas with higher molar mass is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Rate of diffusion of the other gas could be {hyp_value} units.",

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
            "What could be the rate of diffusion of other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def diffusion_and_mass2(repetition_count):
    category, subcategory = "attribute_comparison", "diffusion_and_mass",
    knowledge = "The rate of diffusion is inversely proportional to the molar mass."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 90

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is studying the graham's law by filling containers with different mass of gases. The molar mass of gas with higher rate of diffusion is {given_value} units.",
            "{name} as part of his assignment was given a problem about Graham's law. The question stated that the molar mass of gas with higher rate of diffusion is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Molar mass of the other gas could be {hyp_value} units.",

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
            "What could be the molar mass of the other gas?",

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


def diffusion_and_mass3(repetition_count):
    category, subcategory = "attribute_comparison", "diffusion_and_mass",
    knowledge = "The rate of diffusion is inversely proportional to the molar mass."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 100

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is studying the graham's law by filling containers with different gases of different masses. The rate of diffusion of gas when mass is lower is {given_value} units.",
            "{name} as part of his assignment was given a problem about Graham's law. The question stated that the rate of diffusion of gas with lower molar mass is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Rate of diffusion of the other gas could be {hyp_value} units.",

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
            "What could be the rate of diffusion of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def diffusion_and_mass4(repetition_count):
    category, subcategory = "attribute_comparison", "diffusion_and_mass",
    knowledge = "The rate of diffusion is inversely proportional to the molar mass."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is studying the graham's law by filling containers with different mass of gases. The molar mass of gas with lower rate of diffusion is {given_value} units.",
            "{name} as part of his assignment was given a problem about Graham's law. The question stated that the molar mass of gas with lower rate of diffusion is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Molar mass of the other gas could be {hyp_value} units.",

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
            "What could be the molar mass of the other gas?",

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


def pitch_and_amplitude1(repetition_count):
    category, subcategory = "attribute_comparison", "pitch_and_amplitude",
    knowledge = "The pitch of the sound is directly proportional to the frequency of the sound."

    binary_instances = []
    mcq_instances = []
    given_value_start = 200
    given_value_end = 600

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is working in an auditorium and is testing the pitch of sound at two different frequencies. The pitch of sound when frequency is higher is {given_value} Hertz.",
            "{name} is testing the pitch of sound waves at different frequencies as part of the physics lab exam. The pitch of the sound wave when frequency is higher is {given_value} Hz."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Pitch of the other sound could be {hyp_value} Hertz.",

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
            "What could be the pitch of the other sound?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def pitch_and_amplitude2(repetition_count):
    category, subcategory = "attribute_comparison", "pitch_and_amplitude",
    knowledge = "The pitch of the sound is directly proportional to the frequency of the sound."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is working in an auditorium and is testing the pitch of sound at two different frequencies. The frequency of sound when pitch is higher is {given_value} Hertz.",
            "{name} is testing the pitch of sound waves at different frequencies as part of the physics lab exam. The frequency of the sound wave when pitch is higher is {given_value} Hz."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Frequency of the other sound could be {hyp_value} Hertz.",

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
            "What could be the frequency of the other sound?",

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


def pitch_and_amplitude3(repetition_count):
    category, subcategory = "attribute_comparison", "pitch_and_amplitude",
    knowledge = "The pitch of the sound is directly proportional to the frequency of the sound."

    binary_instances = []
    mcq_instances = []
    given_value_start = 200
    given_value_end = 600

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is working in an auditorium and is testing the pitch of sound at two different frequencies. The pitch of sound when frequency is lower is {given_value} Hertz.",
            "{name} is testing the pitch of sound waves at different frequencies as part of the physics lab exam. The pitch of the sound wave when frequency is lower is {given_value} Hz."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Pitch of the other sound could be {hyp_value} Hertz.",

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
            "What could be the pitch of the other sound?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def pitch_and_amplitude4(repetition_count):
    category, subcategory = "attribute_comparison", "pitch_and_amplitude",
    knowledge = "The pitch of the sound is directly proportional to the frequency of the sound."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is working in an auditorium and is testing the pitch of sound. The Frequency of sound when pitch is lower is {given_value} Hertz.",
            "{name} is testing the pitch of sound waves at different frequencies as part of the physics lab exam. The frequency of the sound wave when pitch is lower is {given_value} Hz."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Frequency of the other sound could be {hyp_value} Hertz.",

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
            "What could be the frequency of the other sound?",

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


def effusion_and_velocity1(repetition_count):
    category, subcategory = "attribute_comparison", "effusion_and_velocity",
    knowledge = "The rate of effusion is directly proportional to velocity of particles."

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 100

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} brought a balloon from a birthday party and observed loss of gas inside a balloon over time. So he wants to understand the reason behind this effusion and has taken balloons with two different effusion rates and velocities. The rate of effusion of gas from the balloon when the velocity of gas particles is higher is {given_value} units.",
            "The two balloon's filled with different gases was bought by {name} for his friends party , but it was losing pressure. He noted that the rate of effusion of gas from the balloon with a gas with higher velocity is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Rate of effusion of gas from the other baloon could be {hyp_value} units.",

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
            "What could be the rate of effusion of gas from the other balloon?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def effusion_and_velocity2(repetition_count):
    category, subcategory = "attribute_comparison", "effusion_and_velocity",
    knowledge = "The rate of effusion is directly proportional to velocity of particles."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} brought a balloon from a birthday party and observed loss of gas inside a balloon over time. So he wants to understand the reason behind this effusion and has taken balloons with two different effusion rates and velocities. The velocity of the gas particles when the rate of effusion of gas from the balloon is higher is {given_value} units.",
            "The two balloon's filled with different gases was bought by {name} for his friends party , but it was losing pressure. He noted that the velocity of gas from the balloon with higher rate of effusion is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Velocity of gas particles of the other balloon could be {hyp_value} units.",

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
            "What could be the velocity of the gas with lower rate of effusion?",

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


def effusion_and_velocity3(repetition_count):
    category, subcategory = "attribute_comparison", "effusion_and_velocity",
    knowledge = "The rate of effusion is directly proportional to velocity of particles."

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 100

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} brought a balloon from a birthday party and observed loss of gas inside a balloon over time. So he wants to understand the reason behind this effusion and has taken balloons with two different effusion rates and velocities. The rate of effusion of gas from the balloon when the velocity of gas particles is lower is {given_value} units.",
            "The two balloon's filled with different gases was bought by {name} for his friends party , but it was losing pressure. He noted that the rate of effusion of gas from the balloon with a gas with lower velocity is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Rate of effusion of gas from the other baloon could be {hyp_value} units.",

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
            "What could be the rate of effusion of gas from the other balloon?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def effusion_and_velocity4(repetition_count):
    category, subcategory = "attribute_comparison", "effusion_and_velocity",
    knowledge = "The rate of effusion is directly proportional to velocity of particles."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 55

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} brought a balloon from a birthday party and observed loss of gas inside a balloon over time. So he wants to understand the reason behind this effusion and has taken balloons with two different effusion rates and velocities. The velocity of the gas particles when the rate of effusion of gas from the balloon is lower is {given_value} units.",
            "The two balloon's filled with different gases was bought by {name} for his friends party , but it was losing pressure. He noted that the velocity of gas from the balloon with lower rate of effusion is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Velocity of gas particles of the other balloon could be {hyp_value} units.",

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
            "What could be the velocity of the gas of the other balloon?",

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


def buoyant_and_density1(repetition_count):
    category, subcategory = "attribute_comparison", "buoyant_and_density",
    knowledge = "Buoyant force is directly proportional to the density of the fluid in which an object is immersed."

    binary_instances = []
    mcq_instances = []
    given_value_start = 18
    given_value_end = 55

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is sailing on a boat and was intriugued to study how boat floats on water as part of which he observed the changes in buoyant force and density on two fluids. The buoyant force exerted when density is higher is {given_value} units.",
            "{name} was oil painting and he accidentally dropped his brushes. Two of the brushes fell in a bowl of oil and a bowl of paint kept nearby. The buoyant force exerted on the brush when the density was higher is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Buoyant force exerted by other fluid could be {hyp_value} units.",

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
            "What could be the buoyant force exerted by other fluid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def buoyant_and_density2(repetition_count):
    category, subcategory = "attribute_comparison", "buoyant_and_density",
    knowledge = "Buoyant force is directly proportional to the density of the fluid in which an object is immersed."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 500

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is sailing on a boat and was intrugued to study how boat floats on water as part of which he observed the changes in buoyant force and density on two fluids. The density when buoyant force exerted is higher is {given_value} units.",
            "{name} was oil painting and he accidentally dropped his brushes. Two of the brushes fell in a bowl of oil and a bowl of paint kept nearby. The density of the liquid when the force exerted was higher is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Density of other fluid could be {hyp_value} units.",

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


def buoyant_and_density3(repetition_count):
    category, subcategory = "attribute_comparison", "buoyant_and_density",
    knowledge = "Buoyant force is directly proportional to the density of the fluid in which an object is immersed."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is sailing on a boat and was intriugued to study how boat floats on water as part of which he observed the changes in buoyant force and density on two fluids. The buoyant force exerted when density is lower is {given_value} units.",
            "{name} was oil painting and he accidentally dropped his brushes. Two of the brushes fell in a bowl of oil and a bowl of paint kept nearby. The buoyant force exerted on the brush when the density was lower is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Buoyant force when density is higher could be {hyp_value} units.",

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
            "What could be the buoyant force of the other liquid?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def buoyant_and_density4(repetition_count):
    category, subcategory = "attribute_comparison", "buoyant_and_density",
    knowledge = "Buoyant force is directly proportional to the density of the fluid in which an object is immersed."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 500

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is sailing on a boat and was intrugued to study how boat floats on water as part of which he observed the changes in buoyant force and density on two fluids. The density when buoyant force is lower is {given_value} units.",
            "{name} was oil painting and he accidentally dropped his brushes. Two of the brushes fell in a bowl of oil and a bowl of paint kept nearby. The density of the liquid when the force exerted was lower is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Density of other fluid could be {hyp_value} units.",

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
            "What could be the density of the other liquid?",

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


def compressibility_and_temperature1(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_temperature",
    knowledge = "Compressibility factor is inversely proportional to temperature at constant pressure and density of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at fire extinguisher manufacturing company. {name} is asked to learn and observe how the compressibility factor changes at two different temperature for two identical gases. So {name} compared the compressibility factor and temperature of both the gases to understand the same. The compressibility factor with higher temperature is {given_value} units.",
            "{name} is a student at a college and he is asked to observe how the compressibility factor changes at two different temperature for two identical gases. So {name} compared the compressibility factor and temperature of both the gases to understand the same. The compressibility factor of gas with higher temperature is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Compressibility factor of the other gas could be {hyp_value} units.",

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
            "What could be the compressibility factor of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_temperature2(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_temperature",
    knowledge = "Compressibility factor is inversely proportional to temperature at constant pressure and density of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different temperature for two identical gases. So {name} compared the compressibility factor and temperature of both the gases to understand the same. The temperature with higher compressibility factor is {given_value} K.",
            "{name} is a student at a college and he is asked to observe how the compressibility factor changes at two different temperature for two identical gases. So {name} compared the compressibility factor and temperature of both the gases to understand the same. The temperature of gas with higher compressibility factor is {given_value} K.",

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other gas could be {hyp_value} K.",

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
            "What could be the temperature of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_temperature3(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_temperature",
    knowledge = "Compressibility factor is inversely proportional to temperature at constant pressure and density of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at fire extinguisher manufacturing company. {name} is asked to learn and observe how the compressibility factor changes at two different temperature of two identical gases. So {name} compared the compressibility factor and temperature of both the gases to understand the same. The compressibility factor with lower temperature is {given_value} units.",
            "{name} is a student at a college and he is asked to observe how the compressibility factor changes at two different temperature for two identical gases. So {name} compared the compressibility factor and temperature of both the gases to understand the same. The compressibility factor of gas with lower temperature is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Compressibility factor of the other gas could be {hyp_value} units.",

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
            "What could be the compressibility factor of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_temperature4(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_temperature",
    knowledge = "Compressibility factor is inversely proportional to temperature at constant pressure and density of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different temperature of two identical gases. So {name} compared the compressibility factor and temperature of both the gases to understand the same. The temperature with lower compressibility factor is {given_value} K.",
            "{name} is a student at a college and he is asked to observe how the compressibility factor changes at two different temperature for two identical gases. So {name} compared the compressibility factor and temperature of both the gases to understand the same. The temperature of gas with lower compressibility factor is {given_value} K.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other gas could be {hyp_value} K.",

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
            "What could be the temperature of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_density1(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_density",
    knowledge = "Compressibility factor is inversely proportional to density at constant pressure and temperature of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 60

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different density of two identical gases to know how fairly large mass of a gas can be put in a small metal cylinder by compression. So {name} compared the compressibility factor and density of both the gases to understand the same. The compressibility factor of the gas with higher density is {given_value} units.",
            "{name} wants to store two gases in separate containers. To determine the amount of gas that can be stored in the containers, he needs to understand the relation between the compressibility factor and density of gas. The compressibility factor of gas with higher density is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Compressibility factor of the other gas could be {hyp_value} units.",

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
            "What could be the compressibility factor of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_density2(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_density",
    knowledge = "Compressibility factor is inversely proportional to density at constant pressure and temperature of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at Fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different density of two identical gases to know how fairly large mass of a gas can be put in a small metal cylinder by compression. So {name} compared the compressibility factor and density of both the gases to understand the same. The density of the gas with higher compressibility factor is {given_value} units.",
            "{name} wants to store two gases in separate containers. To determine the amount of gas that can be stored in the containers, he needs to understand the relation between the compressibility factor and density of gas. The density of gas with higher compressibility factor is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Density of the other gas could be {hyp_value} units.",

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
            "What could be the density of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_density3(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_density",
    knowledge = "Compressibility factor is inversely proportional to density at constant pressure and temperature of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 58

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different density of two identical gases to know how fairly large mass of a gas can be put in a small metal cylinder by compression. So {name} compared the compressibility factor and density of both the gases to understand the same. The compressibility factor with lower density is {given_value} units.",
            "{name} wants to store two gases in separate containers. To determine the amount of gas that can be stored in the containers, he needs to understand the relation between the compressibility factor and density of gas. The compressibility factor of gas with lower density is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Compressibility factor of the other gas could be {hyp_value} units.",

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
            "What could be the compressibility factor of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_density4(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_density",
    knowledge = "Compressibility factor is inversely proportional to density at constant pressure and temperature of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 14
    given_value_end = 65

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at Fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different density of two identical gases to know how fairly large mass of a gas can be put in a small metal cylinder by compression. So {name} compared the compressibility factor and density of both the gases to understand the same. The density of the gas with lower compressibility factor is {given_value} units.",
            "{name} wants to store two gases in separate containers. To determine the amount of gas that can be stored in the containers, he needs to understand the relation between the compressibility factor and density of gas. The density of the gas with lower compressibility factor is {given_value} K.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Density of the other gas could be {hyp_value} units.",

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
            "What could be the density of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_pressure1(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_pressure",
    knowledge = "Compressibility factor is directly proportional to pressure at constant density and temperature of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different pressure of the gas of two identical gases to know how fairly large mass of a gas can be put in a small metal cylinder by compression. So {name} compared the compressibility factor and pressure of both the gases to understand the same. The compressibility factor of the gas with higher pressure is {given_value} units.",
            "{name} knows that the if more pressure is applied gases can be stored in containers. He was assigned to develop the process of storing two gases in metal containers. The compressibility factor of the gas on which higher pressure had to be applied is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Compressibility factor of the other gas could be {hyp_value} units.",

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
            "What could be the compressibility factor of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_pressure2(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_pressure",
    knowledge = "Compressibility factor is directly proportional to pressure at constant density and temperature of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 500

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at Fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different pressure of two identical gases. So {name} compared the compressibility factor and pressure of both the gases to understand the same. The pressure with higher compressibility factor is {given_value} Pa.",
            "{name} knows that the if more pressure is applied gases can be stored in containers. He was assigned to develop the process of storing two gases in metal containers. The pressure that had to be applied on the gas with higher compressibility factor is {given_value} Pa."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Pressure of the other gas could be {hyp_value} Pa.",

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
            "What could be the pressure of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_pressure3(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_pressure",
    knowledge = "Compressibility factor is directly proportional to pressure at constant density and temperature of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different pressure of two identical gases. So {name} compared the compressibility factor and pressure of both the gases to understand the same. The compressibility factor with lower pressure is {given_value} units.",
            "{name} knows that the if more pressure is applied gases can be stored in containers. He was assigned to develop the process of storing two gases in metal containers. The compressibility factor of the gas on which lower pressure had to be applied is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Compressibility factor of the other gas could be {hyp_value} units.",

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
            "What could be the compressibility factor of the other gas?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def compressibility_and_pressure4(repetition_count):
    category, subcategory = "attribute_comparison", "compressibility_and_pressure",
    knowledge = "Compressibility factor is directly proportional to pressure at constant density and temperature of the gas."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 500

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an employee at Fire extinguisher manufacturing industry. {name} is asked to learn and observe how the compressibility factor changes at two different pressure of two identical gases. So {name} compared the compressibility factor and pressure of both the gases to understand the same. The pressure with lower compressibility factor is {given_value} Pa.",
            "{name} knows that the if more pressure is applied gases can be stored in containers. He was assigned to develop the process of storing two gases in metal containers. The pressure that had to be applied on the gas with lower compressibility factor is {given_value} Pa."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Pressure of the other gas could be {hyp_value} Pa.",

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
            "What could be the pressure of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def diffusion_and_temperature1(repetition_count):
    category, subcategory = "attribute_comparison", "diffusion_and_mass",
    knowledge = "At higher temperatures, the rate at which fluid particles will diffuse is faster than at lower temperatures."

    binary_instances = []
    mcq_instances = []
    given_value_start = 13
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} loves drinking tea. He noticed that, when tea bags are dipped in hot water, the diffusion of tea particles was found to be different at two different temperature of hot water. The rate of diffusion when temperature is higher is {given_value} units.",
            "{name} and his friend heated two bowls of water to make coffee. They noticed that the sugar cubes dissolved at different rates in both bowls. The rate of diffusion of sugar with water in the bowl at higher temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Rate of diffusion in the other bowl of water could be {hyp_value} units.",

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
            "What could be the rate of diffusion in the other bowl of water?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def diffusion_and_temperature2(repetition_count):
    category, subcategory = "attribute_comparison", "diffusion_and_temperature",
    knowledge = "At higher temperatures, the rate at which fluid particles will diffuse is faster than at lower temperatures."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 500

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} loves drinking tea. He noticed that, when tea bags are dipped in hot water, the diffusion of tea particles was found to be different at two different temperature of hot water. The temperature at higher rate of diffusion is {given_value} K.",
            "{name} and his friend heated two bowls of water to make coffee. They noticed that the sugar cubes dissolved at different rates in both bowls. The temperature of the water bowl in which the sugar cubes diffused quickly with water is {given_value} K."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other water could be {hyp_value} K.",

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
            "What could be the temperature of the other water?",

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


def diffusion_and_temperature3(repetition_count):
    category, subcategory = "attribute_comparison", "diffusion_and_mass",
    knowledge = "At higher temperatures, the rate at which fluid particles will diffuse is faster than at lower temperatures."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} loves drinking tea. He noticed that, when tea bags are dipped in hot water, the diffusion of tea particles was found to be different at two different temperature of hot water. The rate of diffusion when temperature is lower is {given_value} units.",
            "{name} and his friend heated two bowls of water to make coffee. They noticed that the sugar cubes dissolved at different rates in both bowls. The rate of diffusion of sugar with water in the bowl at lower temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Rate of diffusion of the other water could be {hyp_value} units.",

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
            "What could be the rate of diffusion of the other water?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def diffusion_and_temperature4(repetition_count):
    category, subcategory = "attribute_comparison", "diffusion_and_temperature",
    knowledge = "At higher temperatures, the rate at which fluid particles will diffuse is faster than at lower temperatures."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 500

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} loves drinking tea. He noticed that, when tea bags are dipped in hot water, the diffusion of tea particles was found to be different at two different temperature of hot water. The temperature at lower rate of diffusion is {given_value} K.",
            "{name} and his friend heated two bowls of water to make coffee. They noticed that the sugar cubes dissolved at different rates in both bowls. The temperature of the water bowl in which the sugar cubes diffused slowly with water is {given_value} K."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other water could be {hyp_value} K.",

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
            "What could be the temperature of the other water?",

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


def precipitation_and_temperature1(repetition_count):
    category, subcategory = "attribute_comparison", "precipitation_and_temperature",
    knowledge = "Precipitation is directly proportional to average temperature at earth's surface."

    binary_instances = []
    mcq_instances = []
    given_value_start = 0
    given_value_end = 100

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Precipitation can have a negative impact on life. If too much rain or snowmelt (water from melted snow) occurs at one time, it can lead to flooding. {name} is the geologist investigating it and found the cause for change in precipitation is temperature by taking two different scenarios. The precipitation in the scenario with higher surface temperature is {given_value} mm per hour.",
            "{name} who is a geologist is investigating the cause of change in precipitation by creating two scenario simulations. In one scenario, the precipitation with higher surface temperature is {given_value} mm per hour."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Precipitation in the other scenario could be {hyp_value} mm per hour.",

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
            "What could be the precipitation at lower surface temperature?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def precipitation_and_temperature2(repetition_count):
    category, subcategory = "attribute_comparison", "precipitation_and_temperature",
    knowledge = "Precipitation is directly proportional to average temperature at earth's surface."

    binary_instances = []
    mcq_instances = []
    given_value_start = 120
    given_value_end = 540

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Precipitation can have a negative impact on life. If too much rain or snowmelt (water from melted snow) occurs at one time, it can lead to flooding. {name} is the geologist investigating it and found the cause for change in precipitation is temperature by taking two different scenarios. The surface temperature in the scenario with higher precipitation is {given_value} K.",
            "{name} who is a geologist is investigating the cause of change in precipitation by creating two scenario simulations. In one scenario, the surface temperature when the precipitation was high is {given_value} mm per hour."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Surface temperature in the other scenario could be {hyp_value} K.",

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
            "What could be the temperature in the other case?",

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


def precipitation_and_temperature3(repetition_count):
    category, subcategory = "attribute_comparison", "precipitation_and_temperature",
    knowledge = "Precipitaion is directly proportional to average temperature at earth's surface."

    binary_instances = []
    mcq_instances = []
    given_value_start = 0
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Precipitation can have a negative impact on life. If too much rain or snowmelt occurs at one time, it can lead to flooding. {name} is the geologist investigating it and found the cause for change in precipitation is temperature by taking two different scenarios. The precipitation in the scenario at lower surface temperature is {given_value} mm per hour.",
            "{name} who is a geologist is investigating the cause of change in precipitation by creating two scenario simulations. In one scenario, the precipitation with lower surface temperature is {given_value} mm per hour."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Precipitation in the other case could be {hyp_value} mm per hour.",

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
            "What could be the precipitation at higher surface temperature?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def precipitation_and_temperature4(repetition_count):
    category, subcategory = "attribute_comparison", "precipitation_and_temperature",
    knowledge = "Precipitation is directly proportional to average temperature at earth's surface."

    binary_instances = []
    mcq_instances = []
    given_value_start = 120
    given_value_end = 540

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Precipitation can have a negative impact on life. If too much rain or snowmelt occurs at one time, it can lead to flooding. {name} is the geologist investigating it and found the cause for change in precipitation is temperature by taking two different scenarios of precipitation. The surface temperature in a scenario with lower precipitation is {given_value} K.",
            "{name} who is a geologist is investigating the cause of change in precipitation by creating two scenario simulations. In one scenario, the surface temperature when the precipitation was low is {given_value} mm per hour."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Surface temperature in other scenario could be {hyp_value} K.",

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
            "What could be the temperature in other case?",

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


def humidity_and_temperature1(repetition_count):
    category, subcategory = "attribute_comparison", "humidity_and_temperature",
    knowledge = "Relative humidity is inversely proportional to temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was giving his physics exam and was asked relative humidity at two different temperature. It was given in the question that the relative humidity at higher temperature is {given_value} units.",
            "In a physics test that {name} recently took, it was given in the question that the relative humidity at higher temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The relative humidity at lower temperature could be {hyp_value} units.",

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
            "What could be the relative humidity at other temperatures?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def humidity_and_temperature2(repetition_count):
    category, subcategory = "attribute_comparison", "humidity_and_temperature",
    knowledge = "Relative humidity is inversely proportional to temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 120
    given_value_end = 480

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend were living in two cities with different weather conditions such as temperature and relative humidity. The temperature at the city with higher relative humidity is {given_value} K.",
            "The cities where {name} and his friend lives have different weather conditions. The temperature of the city with higher relative humidity is {given_value} K."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other city could be {hyp_value} K.",

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
            "What could be the relative humidty of the other city?",

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


def humidity_and_temperature3(repetition_count):
    category, subcategory = "attribute_comparison", "humidity_and_temperature",
    knowledge = "Relative humidity is inversely proportional to temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 14
    given_value_end = 70

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was giving his physics exam and was aksed relative humidity at two different temperature. It was given in the question that the relative humidity at lower temperature is {given_value} units.",
            "In a physics test that {name} recently took, it was given in the question that the relative humidity at lower temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The relative humidity at higher temperature could be {hyp_value} units.",

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
            "What could be the relative humidity at the other temperature?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def humidity_and_temperature4(repetition_count):
    category, subcategory = "attribute_comparison", "humidity_and_temperature",
    knowledge = "Relative humidity is inversely proportional to temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 120
    given_value_end = 480

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend were living in two cities with different weather conditions such as temperature and relative humidity. The temperature at the city with lower relative humidity is {given_value} K.",
            "The cities where {name} and his friend lives have different weather conditions. The temperature of the city with lower relative humidity is {given_value} K."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other city could be {hyp_value} units.",

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
            "What could be the relative humidty of the other city?",

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


def heat_and_area1(repetition_count):
    category, subcategory = "attribute_comparison", "heat_and_area",
    knowledge = "The rate of heat transfer is directly proportional to the surface area through which the heat is being conducted."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 80

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is having a back ache. He bought two heating pads with different surface area to warm his muscles and he found the heat transfer to be different. The rate of heat transfer with the heating pad with higher surface area is {given_value} units.",
            "There are two heating pads that {name} has and they have different surface areas. Rate of heat transfer of the heating pad with higher surface area is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Rate of heat transfer of the other heating pad could be {hyp_value} units.",

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
            "What could be the rate of heat transfer of the other heating pad?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def heat_and_area2(repetition_count):
    category, subcategory = "attribute_comparison", "heat_and_area",
    knowledge = "The rate of heat transfer is directly proportional to the surface area through which the heat is being conducted."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is having a back ache. He bought two heating pads with different heat transfer rate to warm his muscles and he found the heat transfer to be different. The surface area of the heating pad with higher rate of heat transfer is {given_value} units.",
            "There are two heating pads that {name} has and they have different surface areas. The surfcae area of the heating pad with higher rate of heat transfer is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Surface area of the other heating pad could be {hyp_value} units.",

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
            "What could be the surface area of the other pad?",

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


def heat_and_area3(repetition_count):
    category, subcategory = "attribute_comparison", "heat_and_area",
    knowledge = "The rate of heat transfer is directly proportional to the surface area through which the heat is being conducted."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 55

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is having a back ache. He bought two heating pads with different surface area to warm his muscles and he found the heat transfer to be different. The rate of heat transfer with the heating pad with lower surface area is {given_value} units.",
            "There are two heating pads that {name} has and they have different surface areas. Rate of heat transfer of the heating pad with lower surface area is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Rate of heat transfer of the other heating pad could be {hyp_value} units.",

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
            "What could be the rate of heat transfer with the other heating pad?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def heat_and_area4(repetition_count):
    category, subcategory = "attribute_comparison", "heat_and_area",
    knowledge = "The rate of heat transfer is directly proportional to the surface area through which the heat is being conducted."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is having a back ache. He bought two heating pads with different heat transfer rate to warm his muscles and he found the heat transfer to be different. The surface area of the heating pad with lower rate of heat transfer is {given_value} units.",
            "There are two heating pads that {name} has and they have different surface areas. The surfcae area of the heating pad with lower rate of heat transfer is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Surface area of the heating pad with higher rate of heat trasnfer could be {hyp_value} units.",

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
            "What could be the surface area of the other heating pad?",

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


def toughness_and_thickness1(repetition_count):
    category, subcategory = "attribute_comparison", "toughness_and_thickness",
    knowledge = "The critical fracture toughness decreases when thickness of specimens increases."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a glass smith. One day he observed that there was a crack in the glasses, and he also observed that the crack propogation was different in two different thickness of two glasses. The fracture toughness at higher thickness is {given_value} units.",
            "There are two glasses that {name} has and they have different thickness. The fracture toughness at higher thickness is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Fracture toughness of the other glass could be {hyp_value} units.",

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
            "What could be the fracture toughness of the other glass?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def toughness_and_thickness2(repetition_count):
    category, subcategory = "attribute_comparison", "toughness_and_thickness",
    knowledge = "The critical fracture toughness decreases when thickness of specimens increases."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a glass smith. One day he observed that there was a crack in the glasses, and he also observed that the crack propogation was different in two different thickness of two glasses. The thickness of the glass with higher fracture toughness is {given_value} units.",
            "There are two glasses that {name} has and they have different thickness. The thickness of the glass with higher fracture toughness is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Thickness of the other could be {hyp_value} units.",

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
            "What could be the thickness of the other glass?",

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


def toughness_and_thickness3(repetition_count):
    category, subcategory = "attribute_comparison", "toughness_and_thickness",
    knowledge = "The critical fracture toughness decreases when thickness of specimens increases."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a glass smith. One day he observed that there was a crack in the glasses, and he also observed that the crack propogation was different in two different thickness of two glasses. The fracture toughness at lower thickness is {given_value} units.",
            "There are two glasses that {name} has and they have different thickness. The fracture toughness at lower thickness is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Fracture toughness of the other glass could be {hyp_value} units.",

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
            "What could be the fracture toughness of the other glass?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def toughness_and_thickness4(repetition_count):
    category, subcategory = "attribute_comparison", "toughness_and_thickness",
    knowledge = "The critical fracture toughness decreases when thickness of specimens increases."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a glass smith. One day he observed that there was a crack in the glasses, and he also observed that the crack propogation was different in two different thickness of two glasses. The thickness of the glass with lower fracture toughness is {given_value} units.",
            "There are two glasses that {name} has and they have different thickness. The thickness of the glass with lower fracture toughness is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Thickness of the other glass could be {hyp_value} units.",

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
            "What could be the thickness of the other glass?",

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


def solubility_and_solid1(repetition_count):
    category, subcategory = "attribute_comparison", "solubility_and_solid",
    knowledge = "The solubility of a solid in water increases with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two student were dehydrated in {name}'s class. {name} gave the students a solution with salt dissolved in water at two different temperatures. The solubility in solution at higher temperature is {given_value} units.",
            "{name} wanted to dissolve salt in water at two different temperatures. The solubility in solution at higher temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Solubility in other solution could be {hyp_value} units.",
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
            "What could be the solubility in other solution?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def solubility_and_solid2(repetition_count):
    category, subcategory = "attribute_comparison", "solubility_and_solid",
    knowledge = "The solubility of a solid in water increases with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 120
    given_value_end = 480

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two student were dehydrated in {name}'s class. {name} gave the students a solution with salt dissolved in water at two different temperatures. At temperature {given_value} K, the solubility was higher.",
            "{name} wanted to dissolve salt in water at two different temperatures. At temperature {given_value} K, the solubility was higher."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The temperature of the other solution could be {hyp_value} K.",

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
            "What could be the temperature of the other solution?",

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


def solubility_and_solid3(repetition_count):
    category, subcategory = "attribute_comparison", "solubility_and_solid",
    knowledge = "The solubility of a solid in water increases with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two student were dehydrated in {name}'s class. {name} gave the students a solution with salt dissolved in water at two different temperatures. The solubility in solution at lower temperature is {given_value} units.",
            "{name} wanted to dissolve salt in water at two different temperatures. The solubility in solution at lower temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Solubility in other solution could be {hyp_value} units.",

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
            "What could be the solubility in other solution?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def solubility_and_solid4(repetition_count):
    category, subcategory = "attribute_comparison", "solubility_and_solid",
    knowledge = "The solubility of a solid in water increases with an increase in temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 120
    given_value_end = 480

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two student were dehydrated in {name}'s class. {name} gave the students a solution with salt dissolved in water at two different temperatures. At temperature {given_value} K, the solubility was lower.",
            "{name} wanted to dissolve salt in water at two different temperatures. At temperature {given_value} K, the solubility was lower."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The temperature of the other solution could be {hyp_value} K.",

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
            "What could be the temperature of other solution?",

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


def solubility_and_gas1(repetition_count):
    category, subcategory = "attribute_comparison", "solubility_and_gas",
    knowledge = "The solubility of the gas in a solvent is inversely proportional to temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "To understand the phenomenon of how dissolved oxygen in water is important to the survival of fish, {name} is studying the solubility of gas at two different temperature. The solubility of gas at higher temperature is {given_value} units.",
            "{name} wanted to know the solubility of two gases at two different temperature. The solubility of gas at higher temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Solubility of other gas could be {hyp_value} units.",

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
            "What could be the solubility of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def solubility_and_gas2(repetition_count):
    category, subcategory = "attribute_comparison", "solubility_and_gas",
    knowledge = "The solubility of the gas in a solvent is inversely proportional to temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 120
    given_value_end = 480

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "To understand the phenomenon of how dissolved oxygen in water is important to the survival of fish, {name} is studying the solubility of two gases at two different temperature. The temperature of a gas was {given_value} K when the solubility is higher.",
            "{name} wanted to know the solubility of two different gases at two different temperature. The temperature of a gas was {given_value} K when the solubility is higher."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other gas could be {hyp_value} K.",

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
            "What could be the temperature of the other gas?",

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


def solubility_and_gas3(repetition_count):
    category, subcategory = "attribute_comparison", "solubility_and_gas",
    knowledge = "The solubility of the gas in a solvent is inversely proportional to temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "To understand the phenomenon of how dissolved oxygen in water is important to the survival of fish, {name} is studying the solubility of two gases at two different temperature. The solubility of a gas at lower temperature is {given_value} units.",
            "{name} wanted to know the solubility of two different gases at two different temperature. The solubility of a gas at lower temperature is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Solubility of other gas could be {hyp_value} units.",

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
            "What could be the solubility of the other gas?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text,
            given_value=given_value,
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


def solubility_and_gas4(repetition_count):
    category, subcategory = "attribute_comparison", "solubility_and_gas",
    knowledge = "The solubility of the gas in a solvent is inversely proportional to temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "To understand the phenomenon of how dissolved oxygen in water is important to the survival of fish, {name} is studying the solubility of two gases at two different temperature. The temperature of a gas was {given_value} K when the solubility is lower.",
            "{name} wanted to know the solubility of two different gases at two different temperature. The temperature of a gas was {given_value} K when the solubility is higher."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the other gas could be {hyp_value} K.",

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
            "What could be the temperature of other gas?",

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

# if __name__ == "__main__":
#     repetition_count = 1
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = compressibility_and_temperature2(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
