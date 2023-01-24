# coding=utf-8
import util
import random
import pprint
import numpy as np


def weight_and_mass(repetition_count):
    category, subcategory = "attribute_comparison", "weight_and_mass",
    knowledge = "Force exerted by gravity is directly proportional to the mass of an object."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 70

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is carrying two stones of different masses to throw it into the water. The minimum force required for the stone with higher mass is {given_value} units.",
            "{name} has to throw two different rocks into water. The force required to throw the heavier stone is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The minimum force that will be required for the other stone to throw it into the water could be {hyp_value} units.",

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
            "What could be the minimum force required to throw the other stone?",

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


def strain_and_stress(repetition_count):
    category, subcategory = "attribute_comparison", "strain_and_stress",
    knowledge = "The strain developed in an object is directly proportional to the stress applied."

    binary_instances = []
    mcq_instances = []
    given_value_start = 18
    given_value_end = 65

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to elongate two rubber bands. The stress applied to a rubber band that experienced more elongation is {given_value} units.",
            "{name} elongated two rubber bands. The stress applied to a rubber band that experienced more elongation is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Stress applied to the other rubber band could be {hyp_value} units.",

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
            "What could be the stress applied to the other rubber band?",

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


def strain_and_stress2(repetition_count):
    category, subcategory = "attribute_comparison", "strain_and_stress",
    knowledge = "The strain developed in an object is directly proportional to the stress applied."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} subjected two balls to stress where first ball was exerted with more stress. The strain developed in the first ball is {given_value} units.",
            "{name} subjected two balls with stress and more stress was applied to the first ball. The strain developed in the first ball is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Strain developed in the other ball could be {hyp_value} units.",

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
            "What could be the strain developed in the other ball?",

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


def stress_and_force(repetition_count):
    category, subcategory = "attribute_comparison", "stress_and_force",
    knowledge = "Stress is directly proportional to the force applied on an object."

    binary_instances = []
    mcq_instances = []
    given_value_start = 16
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} needed to crush two similar waste boxes for recycling them. The stress value for the box that is applied with more force is {given_value} units.",
            "{name} needed to crush two boxes and stress value for the box on which more force applied is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The value of stress for the other box could be {hyp_value} units.",

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
            "What could be the value of stress for the other box?",

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


def stress_and_force2(repetition_count):
    category, subcategory = "attribute_comparison", "stress_and_force",
    knowledge = "Stress is directly proportional to the force applied on an object."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} have two similar bottles where the stress applied to the first bottle is more than on the second bottle. The force exerted on the first bottle is {given_value} units.",
            "{name} has two same bottles where the stress applied to the first bottle is more than on the second bottle. The force exerted on the first bottle is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Force exerted on the other bottle could be {hyp_value} units.",

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
            "What could be the force exerted  on the other bottle?",

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


def rotation_angle_and_arc_length(repetition_count):
    category, subcategory = "attribute_comparison", "rotation_angle_and_arc_length",
    knowledge = "The angle enclosed by two points on a circle at the center is directly proportional to the length of the arc between those two points."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend ran on a circular ground. {name} ran more distance than his friend on the ground. The angle enclosed by the distance ran by {name} is {given_value} units.",
            "{name} and his friend ran on a circular ground and he ran more distance than his friend. The angle enclosed by {name} is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The angle enclosed by the distance ran by his friend could be {hyp_value} units.",

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
            "What could be the angle enclosed by the distance travelled by his friend?",

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


def rotation_angle_and_arc_length2(repetition_count):
    category, subcategory = "attribute_comparison", "rotation_angle_and_arc_length",
    knowledge = "The angle enclosed by two points on a circle at the center is directly proportional to the length of the arc between those two points."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There is a circular fence where it has two gates. The angle enclosed by first gate is more than the angle enclosed by the second gate at the center of the fence. The length of the first gate is {given_value} units.",
            "There is a circular fence with two gates. The angle enclosed by first gate by the center of the fence is more than the second gate. The length of the first gate is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The length of the other gate could be {hyp_value} units.",

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
            "What could be the length of the other gate?",

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


def tangential_velocity_and_distance(repetition_count):
    category, subcategory = "attribute_comparison", "tangential_velocity_and_distance",
    knowledge = "The tangential velocity is proportional to the distance from the center of rotation."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 65

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is his friend were travelling with the with same velocity but one on the inner side and other on the outer side of the circular road. The vehicle going on the outer side of the circular road has the tangential speed of {given_value} m/s.",
            "{name} was travelling on the inner side of a road while his friend was travelling on the outer side of the circular road. Both had same angular velocity. The vehicle going on the outer side of the circular road has the tangential speed of {given_value} m/s."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The tangential velocity of the other vehicle in the inner side of the circular road could be {hyp_value} m/s.",
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
            "What could be the tangential velocity of the vehicle going on the inner side of the circular road?",

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


def tangential_velocity_and_distance2(repetition_count):
    category, subcategory = "attribute_comparison", "tangential_velocity_and_distance",
    knowledge = "The tangential velocity is proportional to the distance from the center of rotation."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 55

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went on a ride in his car on two different circular roads with same velocity. The tangential velocity of the vehicle in the first circular road was more than on the other circular road. The radius of the first circular road is {given_value} units.",
            "{name} went on a car ride on two circular roads moving with same velocity on both of them. The tangential velocity of the vehicle in the first circular road was more. The radius of the first circular road is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The radius of the other circular road could be {hyp_value} units.",

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
            "What could be the radius of the other circular road?",

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


def centripetal_acceleration_and_radius(repetition_count):
    category, subcategory = "attribute_comparison", "centripetal_acceleration_and_radius",
    knowledge = "Centripetal acceleration is inversely proportional to radius keeping the velocity constant."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 70

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is planning to participate in a race event at an exhibition where participants need to make rounds on two different circular paths. {name} and his competitors' velocity was same. The centripetal acceleration for the smaller circular path is {given_value} units.",
            "{name} is participates in an event where they need to do rounds on two different circular paths. her speed was equal to his competitors . The centripetal acceleration for the smallest circular trajectory is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The centripetal acceleration for the other circular path could be {hyp_value} units.",
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
            "What could be the centripetal acceleration of the other circular path?",

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


def centripetal_acceleration_and_radius2(repetition_count):
    category, subcategory = "attribute_comparison", "centripetal_acceleration_and_radius",
    knowledge = "Centripetal acceleration is inversely proportional to radius keeping the velocity constant."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two objects were rotating around a pole in the circular path with same velocity. The centripetal acceleration of the first object is more than the second object. The radius of the circular path of the first object is {given_value} units.",
            "Two objects were rotating around a pole in the circular path with same velocity and the centripetal acceleration of the first object is more than the second object. The first object's radius is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The radius of the circular path for the other object could be {hyp_value} units.",

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
            "What could be the radius of the circular path for the other object?",

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


def centripetal_acceleration_and_velocity(repetition_count):
    category, subcategory = "attribute_comparison", "centripetal_acceleration_and_velocity",
    knowledge = "Centripetal acceleration is directly proportional to the velocity for a constant radius."

    binary_instances = []
    mcq_instances = []
    given_value_start = 14
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is organizing a bike event where two participant need to make rounds around a circular path. The centripetal acceleration for a bike with higher velocity is {given_value} units.",
            "{name} is organizing an event where two participants need to circle around a path. The bike with higher velocity has centripetal acceleration of {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The centripetal acceleration of the other bike could be {hyp_value} units.",

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
            "What could be the centripetal acceleration of the other bike?",

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


def centripetal_acceleration_and_velocity2(repetition_count):
    category, subcategory = "attribute_comparison", "centripetal_acceleration_and_velocity",
    knowledge = "Centripetal acceleration is directly proportional to the velocity for a constant radius."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            " {name} was rotating a ball that tied to a string. The centripetal acceleration for the ball for first case is more than that for the second case. The velocity of the ball rotating for the first case is {given_value} units.",
            " {name} was rotating a ball that tied to a string and later he changed the velocity of rotation that resulted in higher centripetal acceleration. The velocity of the ball rotating for the first case is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The velocity of the ball for the second case could be {hyp_value} units.",

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
            "What could be the velocity of the ball for the second case?",

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


def work_done_and_force(repetition_count):
    category, subcategory = "attribute_comparison", "work_done_and_force",
    knowledge = "The work done by a constant force is proportional to the force applied times the displacement of the object."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a mechanic and need to push two cars placed at the entrance gate of the garage to inside. {name} pushes the first car with much effort, the value of work done is {given_value} units.",
            "{name} has to push two cars. {name} pushes the first car with much effort, the value of work done is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The work done to move the second car could be {hyp_value} units.",

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
            "What could be the work done to move the other car?",

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


def potential_energy_and_spring(repetition_count):
    category, subcategory = "attribute_comparison", "potential_energy_and_spring",
    knowledge = "Elastic potential energy is directly proportional to the square of the change in length and the spring constant."

    binary_instances = []
    mcq_instances = []
    given_value_start = 14
    given_value_end = 58

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to elongate two similar rubber bands. {name} is curious to find the potential energy after the elongation. The value of the elastic potential energy stored in first rubber is {given_value} units.",
            "{name} elongated two similar rubber bands and was curious to find the potential energy of the band after the elongation. The value of the elastic potential energy stored in first rubber is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The elastic potential energy stored in another rubber band could be {hyp_value} units.",

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
            "What could be the elastic potential energy stored in the other rubber band?",

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


def potential_energy_and_spring2(repetition_count):
    category, subcategory = "attribute_comparison", "potential_energy_and_spring",
    knowledge = "Elastic potential energy is directly proportional to the square of the change in length and the spring constant."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 70

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two similar springs of same length were subjected to different forces and the potential energy developed in the first spring is more than the second spring. The change in the length of the first spring is {given_value} meters.",
            "Two springs were subjected to different forces and the potential energy developed in the first spring is more than the second. The change in the length of the first spring is {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The change in the length of the second spring could be {hyp_value} meters.",

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
            "What could be the change in the length for the second spring?",

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


def force_and_spring(repetition_count):
    category, subcategory = "attribute_comparison", "force_and_spring",
    knowledge = "The magnitude of the force required to change the length of a spring-like object is directly proportional to the spring constant and the displacement of the spring."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} visited Play Arena where a game involves jumping on the boxes that are attached with a similar type of spring at the bottom. On the first box {name} able to jump more. The amount of force {name} imposed to jump on the first spring box is {given_value} units.",
            "{name} is playing a game that involves jumping on the boxes attached with a spring at the bottom. On the first box {name} able to jump more and the amount of force {name} required to jump on the first spring box is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The force required to jump on the second spring could be {hyp_value} units.",

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
            "What could be the force required to jump on the other spring box?",

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


def force_and_spring2(repetition_count):
    category, subcategory = "attribute_comparison", "force_and_spring",
    knowledge = "The magnitude of the force required to change the length of a spring-like object is directly proportional to the spring constant and the displacement of the spring."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} stretched two similar rubber bands where the first rubber band is stretched with more force compared to the second one. The length of the first rubber band is {given_value} meters.",
            "{name} stretched two similar rubber bands where the second rubber band is stretched with less force compared to the first one. The length of the first rubber band is {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The length of the other rubber band could be {hyp_value} meters.",

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
            "What could be the length of the other rubber band?",

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


def pressure_and_area(repetition_count):
    category, subcategory = "attribute_comparison", "pressure_and_area",
    knowledge = "Pressure is inversely proportional to area."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 54

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to cut fruits with the two similar knives where it is difficult to cut using the first one. The area of this knife is {given_value} units.",
            "{name} is trying to cut fruits with the two similar knives. It is difficult to cut the fruit using the first one. The area of this knife is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The area of the other knife could be {hyp_value} units.",

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
            "What could be the area of the other knife?",

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


def pressure_and_area2(repetition_count):
    category, subcategory = "attribute_comparison", "pressure_and_area",
    knowledge = "Pressure is inversely proportional to area."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two boxes of different sizes were subjected to same force. The pressure on the smaller sized box is {given_value} units.",
            "Two boxes of different sizes were subjected to same force and the smaller sized box has a pressure of {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The pressure on the other box could be {hyp_value} units.",

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
            "What could be the pressure on the other box?",

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


def pressure_and_force(repetition_count):
    category, subcategory = "attribute_comparison", "pressure_and_force",
    knowledge = "Pressure is directly proportional to the force applied."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 65

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is blowing two balloons for a birthday party decoration where one of the balloons is inflated more. The pressure on that balloon is increased to {given_value} units.",
            "{name} is blowing two balloons for a birthday party where he blew the first one with more force. The pressure on that balloon is increased to {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The pressure on the other balloon could be {hyp_value} units.",

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
            "What could be the pressure developed on the other balloon?",

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


def pressure_and_force2(repetition_count):
    category, subcategory = "attribute_comparison", "pressure_and_force",
    knowledge = "Pressure is directly proportional to the force applied."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Two persons of different weight stepped on a ball where the pressure exerted by the first person is greater than the one exerted by the second person. The weight of the first person is {given_value} units.",
            "Two people of different weight stepped on a ball where the pressure exerted by the first person is greater than second person. The weight of the first person is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The weight of the other person could be {hyp_value} units.",

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
            "What could be the weight of the other person?",

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


def frequency_and_time(repetition_count):
    category, subcategory = "attribute_comparison", "frequency_and_time",
    knowledge = "Frequency is inversely proportional to time period."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is performing an experiment to measure the time period of waves produced by two different sources with different frequencies. The time period of the wave with higher frequency is {given_value} units.",
            "{name} is performing an experiment to measure the time period of the waves produced by two different sources with different frequencies. The time period of the wave more frequently is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The time period of the other sound wave could be {hyp_value} units.",

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
            "What could be the time period of the other wave?",

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


def frequency_and_time2(repetition_count):
    category, subcategory = "attribute_comparison", "frequency_and_time",
    knowledge = "Frequency is inversely proportional to time period."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} designed two sine waves with different time periods. The first wave time period is greater than the second wave. The frequency of the first wave is {given_value} units.",
            "{name} designed two Sine waves with different periods of time. The time period of first wave is greater than the second wave. The frequency of the first wave is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The frequency of the second wave could be {hyp_value} units.",

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
            "What could be the frequency of the output wave?",

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


def angle_and_length(repetition_count):
    category, subcategory = "attribute_comparison", "angle_and_length",
    knowledge = "The angles of a triangle are in same relative order as that of their opposite sides length in a triangle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 120

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is asked to draw a triangle where the angle opposite to the largest side of that triangle is {given_value} units.",
            "{name} drew a triangle where the angle opposite to the largest side of that triangle is {given_value} degrees.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The angle opposite to the other sides of the triangle could be {hyp_value} units.",

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
            "What could be the angle opposite to the other sides of that triangle?",

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


def angle_and_length2(repetition_count):
    category, subcategory = "attribute_comparison", "angle_and_length",
    knowledge = "The angles of a triangle are in same relative order as that of their opposite sides length in a triangle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The length of the side of a scalene triangle opposite to the largest angle enclosed is {given_value} meters.",
            "The length of the side of a scalene triangle opposite the larger angle enclosed is {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The length of the side opposite to the other angles enclosed inside the triangle could be {hyp_value} meters.",

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
            "What could be the length of the side opposite to the other enclosed angles of that triangle?",

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


def surface_tension_and_temperature(repetition_count):
    category, subcategory = "attribute_comparison", "surface_tension_and_temperature",
    knowledge = "Surface tension is inversely proportional to the temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was washing the clothes with soap and detergents and observed that the soap water did not soak well into the pores and soiled areas. So {name} changed the temperature of the water and was able to wash properly. The temperature of water in the first case is {given_value} units.",
            "{name} was washing the clothes with soap and observed that the clothes did not soak well with soap water. So {name} changed the temperature of the water and was able to wash properly. The temperature of water in the first case is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Temperature of the water in the second case could be {hyp_value} units.",

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
            "What could be the temperature of water for the second case?",

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


def surface_tension_and_temperature2(repetition_count):
    category, subcategory = "attribute_comparison", "surface_tension_and_temperature",
    knowledge = "Surface tension is inversely proportional to the temperature."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The surface tension of water was calculated at two different temperatures. The surface tension of water at the lower temperature is {given_value} units.",
            "Different temperatures are used as parameter for observing surface tension. The surface tension of water at the lower temperature is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Surface tension of the water at higher temperature could be {hyp_value} units.",

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
            "What could be the surface tension of the water at the higher temperature?",

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


def cholestrol_and_fat(repetition_count):
    category, subcategory = "attribute_comparison", "cholestrol_and_fat",
    knowledge = "Eating too much saturated fat or trans fats can result in unhealthy cholesterol levels."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 70

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was following a good healthy diet suggested by the doctor. The cholesterol level used to be {given_value} units. Due to some reasons, {name} started eating the outside food where his diet consists of deep fry items.",
            "{name} was following a good healthy diet and his cholesterol level used to be {given_value} units. Later, {name} started eating food where his diet consists of deep fry items.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The cholesterol level after the diet change could be {hyp_value} units.",

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
            "What could be the cholesterol level after the change in diet?",

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


def resistance_series_and_parallel(repetition_count):
    category, subcategory = "attribute_comparison", "resistance_series_and_parallel",
    knowledge = "A circuit with parallel connections has a smaller total resistance than the resistors connected in series."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} connected two circuits where the resistors are in series and in parallel respectively. The total value of resistance of the circuit when connected in series is {given_value} units.",
            "{name} connected two circuits where the resistors are in parallel and in series. The total resistance when connected in series is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The total resistance of the other connection could be {hyp_value} units.",

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
            "What could be the total resistance of the other connection of resistors?",

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


def water_boil_and_level(repetition_count):
    category, subcategory = "attribute_comparison", "water_boil_and_level",
    knowledge = "Water will convert into water vapour on boiling."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 70

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} boiled a glass of water to drink the hot water. The level of the water in the glass is {given_value} units. After boiling was done, she took the water into the glass.",
            "The level of the water in the glass is {given_value} units before boiling water.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The level of the water after boiling could be {hyp_value} units.",

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
            "What could be the level of the water after boiling?",

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


def absorption_and_concentration(repetition_count):
    category, subcategory = "attribute_comparison", "absorption_and_concentration",
    knowledge = "The absorbance is directly proportional to the concentration (c) of the solution of the sample used in the experiment."

    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 70

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} experimented with two same types of solutions but with different concentrations. The amount of light seen after passing through two solutions is more for the first solution. The concentration of the first solution is {given_value}.",
            "{name} experienced with two same types of solutions, but with different concentrations and the amount of light seen after passing through two solutions is more for the first solution and its concentration is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The  concentration of the other solution could be {hyp_value} units.",

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
            "What could be the concentration of other solution?",

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


def acid_and_PH(repetition_count):
    category, subcategory = "attribute_comparison", "acid_and_PH",
    knowledge = "The stronger the acid, and the lower the pH value."

    binary_instances = []
    mcq_instances = []
    given_value_start = 0
    given_value_end = 7

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment was to find the less acidic solution out of the given two solutions and use it for the chemical reaction. The PH value of the stronger acid used for a chemical reaction is {given_value} units.",
            "{name} has to find the acidity of two solutions and PH value of the stronger solution used for a chemical reaction is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "PH value of the other solution could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=1,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the PH value of the other solution?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=3,
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


def base_and_PH(repetition_count):
    category, subcategory = "attribute_comparison", "base_and_PH",
    knowledge = "The stronger the base, and the higher the pH value."

    binary_instances = []
    mcq_instances = []
    given_value_start = 7
    given_value_end = 14

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to identify the strong basic solution to neutralize strong acidic solution out of the two given solutions. The PH value of the used base is {given_value} units.",
            "{name} has to find the basicity of two solutions and PH value of the stronger solution used for a chemical reaction is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "PH value of the other base solution could be {hyp_value} units.",

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
            "What could be the Ph of the other solution?",

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


def height_and_oxygen(repetition_count):
    category, subcategory = "attribute_comparison", "height_and_oxygen",
    knowledge = "The effects of high altitude on humans decreases the saturation of oxyhemoglobin. "

    binary_instances = []
    mcq_instances = []
    given_value_start = 80
    given_value_end = 100

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is climbing a mountain where his saturation of oxyhemogobin before start is {given_value} units. {name} is facing some breathing issues.",
            "{name} is climbing a mountain where his saturation of oxyhemogobin at the base is {given_value} units. {name} is facing some breathing issues when he went to the top.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The saturation of oxyhemogoin could be {hyp_value} units.",

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
            "What could be the value of saturation of oxyhemoglobin?",

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


def power_bank_current(repetition_count):
    category, subcategory = "attribute_comparison", "power_bank_current",
    knowledge = " The higher the amperes of the output, the faster the device will charge."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to buy a power bank to charge the devices. {name} shortlisted two power banks where the one with fast charge have the output amperes as {given_value} units.",
            "{name} brought two power banks to charge his phone. He purchased the first one with fast charge have the output amperes as {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Amperes output of the second power bank could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=3,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the amperes of the other power bank?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=3,
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


def circumscribed_inscribed(repetition_count):
    category, subcategory = "attribute_comparison", "circumscribed_inscribed",
    knowledge = "Circumcircle of a polygon is a circle that passes through all the vertices of the polygon. An inscribed circle is the largest possible circle that can be drawn interior to a plane figure."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 60

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is doing a geometry exercise is to draw a polygon with both inscribed and circumscribed circles. {name} solved to get the radius of the inscribed circle as {given_value} units.",
            "{name} is drawing a polygon with both inscribed and circumscribed circles. The radius of the inscribed circle as {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Radius of the circumscribed circle of the polygon could be {hyp_value} units.",

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
            "What could be the radius of the circumscribed circle?",

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


def center_sector_angle(repetition_count):
    category, subcategory = "attribute_comparison", "center_sector_angle",
    knowledge = "The angle subtended by an arc of a circle at its center is greater than the angle it subtends anywhere on the circle's circumference."

    binary_instances = []
    mcq_instances = []
    given_value_start = 40
    given_value_end = 200

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s math exercise is to find the angle subtended by an arc of given length at the center of the circle and on the circle's circumference. The value of the angle subtended on the circumference is {given_value} units.",
            "The value of the angle subtended by an arc of given length at the center of the circle and on the circle's circumference is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The angle subtended by the arc at the center of the circle could be {hyp_value} units.",

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
            "What could be the angle subtended by the arc at the center of the circle?",

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


def frustum_of_cone_radius(repetition_count):
    category, subcategory = "attribute_comparison", "frustum_of_cone_radius",
    knowledge = "The frustum of a cone is the part of the cone with its base that is left after the cone is cut by a plane that is parallel to its base."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was eating a cone ice cream where he cut the chocolate part of cone shape at the sharp end. The radius of the circle at the top(base of the cone) is {given_value} units.",
            "{name} was eating an ice cream cone. The radius of the circle at the top (cone base) is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The radius of the base of the cone-shaped chocolate part could be {hyp_value} units.",

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
            "What could be the radius of the cone-shaped chocolate part?",

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


def monotonous_decrease(repetition_count):
    category, subcategory = "attribute_comparison", "monotonous_decrease",
    knowledge = "A function is called a monotonous decrease function if it is strictly decreasing."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s plotted a graph for the number of accidents that took place in the past one week. The graph came to be monotonously decreasing. The number of accidents on first day is {given_value} units.",
            "{name}'s plotted a graph for the number of accidents that were monotonously decreasing. The number of accidents on first day is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Number of accidents on the last day of the week could be {hyp_value} units.",

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
            "What could be the number of accidents recorded on the last day of the week?",

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


def monotonous_increase(repetition_count):
    category, subcategory = "attribute_comparison", "monotonous_increase",
    knowledge = "A function is called a monotonous increase function if it is strictly increasing."

    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} noted the heights of all the students in the class and made them stand according to their height. The height of the student standing at first place is {given_value} cm.",
            "{name} noted the heights of all the students who were standing according to increasing order of their height. The height of the student standing at first place is {given_value} cm."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Height of the student standing at the last could be {hyp_value} cm.",

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
            "What could be the height of the student standing in the last position?",

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


# knowledge work
def number_and_exponent(repetition_count):
    category, subcategory = "attribute_comparison", "number_and_exponent",
    knowledge = "Function with a number n(greater than or equal to 1) raised to a power x will have the (n^x) value proportional to the value x. The n^x value varies similar to the x, n^x increases as x increases and decreases as x decreases."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} want to mark the value of n^x for two values of x on the graph. {name} is calculating the n^x value for x1 and x2 where x1 is less than x2. The value of the function for x1 is {given_value} units.",
            "{name} want to mark the value of n^x for two values for x1 and x2 where x1 is less than x2. The value of the function for x1 is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The function value of the other input could be {hyp_value} units.",

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
            "What could be the function value for the other input value?",

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


def arithmetic_mean_and_geometric_mean(repetition_count):
    category, subcategory = "attribute_comparison", "airthmetic_mean_and_geometric_mean",
    knowledge = "Arithmetic mean is greater than or equal to Geometric mean."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 100

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was finding the geometric mean and arithmetic mean of a series in his exercise. The geometric mean is {given_value}.",
            "The geometric mean of a series is {given_value}.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The arithmetic mean of the series could be {hyp_value}.",

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
            "What could be the arithmetic mean of the series?",

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


def geometric_mean_and_harmonic_mean(repetition_count):
    category, subcategory = "attribute_comparison", "geometric_mean_and_harmonic_mean",
    knowledge = "Geometric mean is greater than or equal to Harmonic mean."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s maths exercise is to calculate the Geometric mean and harmonic mean of a given series. The geometric mean is {given_value}.",
            "The geometric mean of a series is {given_value}. "
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Harmonic mean of the series could be {hyp_value}.",

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
            "What could be the harmonic mean of the series?",

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


def arithmetic_mean_and_harmonic_mean(repetition_count):
    category, subcategory = "attribute_comparison", "arithmetic_mean_and_harmonic_mean",
    knowledge = "Arithmetic mean is greater than or equal to Harmonic mean."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 100

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was practicing mean problems for the mathematics exam. For a problem he calculated both harmonic and arithmetic mean. The harmonic mean of a series he solved is {given_value}.",
            "The harmonic mean of a series is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The arithmetic mean of the same series could be {hyp_value}.",

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
            "What could be the arithmetic mean of the series?",

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


def TIR_and_critical_angle(repetition_count):
    category, subcategory = "attribute_comparison", "TIR_and_critical_angle",
    knowledge = "When a light goes from a denser medium to a less dense medium, as the angle of incidence exceeds the critical angle, the ray reflects the denser medium. This process is called total internal reflection."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 90

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to observe the total internal reflection by incident light rays at an angle on the glass. The critical angle of this glass-air interface is {given_value} units.",
            "{name} wanted to observe the total internal reflection by the rays of light incident at an angle in the glass. The critical angle of this glass-air interface is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The angle of incidence of the light ray at the glass-air interface could be {hyp_value} units.",

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
            "What could be the angle of incidence of the light ray at the glass-air interface?",

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


def capacitors_series_and_parallel(repetition_count):
    category, subcategory = "attribute_comparison", "capacitors_series_and_parallel",
    knowledge = "Capacitors in parallel connections result in additive values while series connections result in diminished values."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} placed the capacitors in parallel to work with the AC driving voltage to allow more time for charging and discharging. {name} altered the arrangement of capacitors to charge and discharge quickly to maintain in open circuit mode. The capacitance of the circuit before altering is {given_value} units.",
            "{name} placed capacitors in parallel to work with the AC drive voltage to allow more time to charge and discharge. {name} modified the arrangement of the capacitors to charge and discharge quickly to keep in open circuit mode. The capacitance of the circuit before altering is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Capacitance of the circuit after the rearrangement of components could be {hyp_value} units.",

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
            "What could be the capacitance of the circuit after rearrangement?",

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


def low_pass_filter(repetition_count):
    category, subcategory = "attribute_comparison", "low_pass_filter",
    knowledge = "A low pass filter allows the signal that has a frequency below the cut-off frequency."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 90

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} have a meeting set with speaker systems where a low pass filter is required to direct the lower frequency bass signals to the larger bass speakers and reduce any high-frequency noise or “hiss” type distortion. The cutoff frequency for the filter used is {given_value} units.",
            "{name} has a set of meetings with speaker systems where a low pass filter is required to direct low frequency low signals to larger low speakers and reduce any high frequency noise. The cutoff frequency for the filter used is {given_value} units."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Frequency of the output signal that got filtered could be {hyp_value} units.",

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
            "What could be the frequency of the output signal?",

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


def high_pass_filter(repetition_count):
    category, subcategory = "attribute_comparison", "high_pass_filter",
    knowledge = "High pass filter is a filter which passes only those signals whose frequencies are higher than cutoff frequencies thereby attenuating signals of lower frequencies."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 90

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} need to design an amplifier in which the high-frequency signals are directed to the smaller speakers and reduce any low-frequency noise or rumble type distortion. The cutoff frequency for the high pass filter used is {given_value} units.",
            "{name} needs to design an amplifier in which high frequency signals are directed to smaller speakers and reduce any low frequency noise or direction type distortion. The cutoff frequency for the high pass filter used is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Frequency of the output signal that got filtered could be {hyp_value} units.",
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
            "What could be the frequency of the output signal?",

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


def cotton_and_water(repetition_count):
    category, subcategory = "attribute_comparison", "cotton_and_water",
    knowledge = "As cotton soaks up moisture, it becomes heavy and wet."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 150

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} made his donkey carry the cotton bags till the market. The weight of the cotton bags is {given_value} grams. It started to rain where the donkey was present and the cotton bags got wet.",
            "The weight of the cotton bags is {given_value} grams. It started to rain and the cotton bags got wet."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The weight of the cotton bags after getting wet could be {hyp_value} grams.",

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
            "What could be the weight of the cotton bags after getting wet?",

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


def valency_shell_electrons(repetition_count):
    category, subcategory = "attribute_comparison", "valency_shell_electrons",
    knowledge = "The conductivity of the atom depends on the number of electrons that are in the valence shell. Normally, a conductor has three or fewer valence electrons, an insulator has five or more valence electrons, and semiconductors usually have four valence electrons."

    binary_instances = []
    mcq_instances = []
    given_value_start = 5
    given_value_end = 8

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s task is to calculate the number of electrons present in the valence shell for two objects, an insulator and a conductor. The number of electrons in the valence shell of the insulator is {given_value} units.",
            "{name} has to calculate the number of electrons present in the valence shell for an insulator and a conductor. The number of electrons in the valence shell of the insulator is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Number of valency shell electrons of the other object could be {hyp_value} units.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=3,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the number of valence shell electrons of the other object?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=3,
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


def solenoid_coils(repetition_count):
    category, subcategory = "attribute_comparison", "solenoid_coils",
    knowledge = "The strength of the magnetic field around a solenoid is directly proportional to the number of turns on the coil."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was trying to generate a magnetic field using the solenoid. Initially, he made {given_value} number of turns of the coil. Later he changed the number of turns of the coil and observed that the magnetic field strength generated got increased.",
            "{name} was trying to generate a magnetic field using the solenoid. Initially, there were {given_value} turns of the coil. Later he changed the number of turns of the coil and observed that the magnetic field increased."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The number of turns of the coil in the second case could be {hyp_value} units.",

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
            "What could be the number of turns of the coil in the second case?",

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


def torque_and_radius(repetition_count):
    category, subcategory = "attribute_comparison", "height_and_potential_energy",
    knowledge = "Torque is directly proportional to the radius of rotation."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was spinning a ball with a stick in a circular direction. {name} took another stick where he felt more difficult to rotate. The length of the stick in the first case is {given_value} m.",
            "{name} was spinning a ball with a stick in a circular direction. He took another stick which required more energy to rotate. The length of the first stick is {given_value} m.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The length of the stick in the second case could be {hyp_value} m.",

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
            "What could be the length of the stick in the second case?",

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


def solenoid_and_current(repetition_count):
    category, subcategory = "attribute_comparison", "solenoid_and_current",
    knowledge = "The strength of the magnetic field around a solenoid is directly proportional to the current."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to create a controlled magnetic field using the solenoid to use as an electromagnet. {name} obtained two strengths by varying the current in which, for the second case, the strength is more. The current in the first case is {given_value} units.",
            "{name} wanted to create a controlled magnetic field using a solenoid. {name} varied the current and saw that the strength is more in second case. The current in the first case is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The current flow in the solenoid coil for the second case could be {hyp_value} units.",

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
            "What could be the current flowing in the coil of solenoid in the second case?",

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


def focal_length_and_power(repetition_count):
    category, subcategory = "attribute_comparison", "focal_length_and_power",
    knowledge = "The optical power of a lens is equal to the reciprocal of the focal length of the lens."

    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 54

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment is to work with the two lenses, provided their optical powers and observed the type of image being formed. The lens with more optical power has the focal length {given_value} cm.",
            "There are two lenses present and {name} knows their optical powers and observed the type of image being formed. The lens with higher optical power has the focal length {given_value} cm."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Focal length of the other lens could be {hyp_value} cm.",

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
            "What could be the focal length of the other lens?",

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


def focal_length_and_shot(repetition_count):
    category, subcategory = "attribute_comparison", "focal_length_and_shot",
    knowledge = "The shorter the focal length, the wider the angle of view and the greater the area captured. The longer the focal length, the smaller the angle and the larger the subject appears to be."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a photographer where he clicks pictures for the events and also shoots the wild photography. The focal length of the lens used to click the wide angle pictures for the events is {given_value} units.",
            "{name} is a photographer and the focal length of the lens used to click the wide angle pictures for the events is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Focal length of the other lens used for wild photography could be {hyp_value} units.",

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
            "What could be the focal length of the other lens used for wild photography?",

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


# doubt
def diode_and_cutoff(repetition_count):
    category, subcategory = "attribute_comparison", "diode_and_cutoff",
    knowledge = "In the forward bias condition, the current is directly proportional to the voltage."

    binary_instances = []
    mcq_instances = []
    given_value_start = 1
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is plotting a graph voltage vs. current for the p-n junction diode where the diode is in ON mode for all the values of voltages tested. The threshold voltage is {given_value} units.",
            "{name} is working on a relation of voltage and current for the p-n junction diode where the diode is in ON. The threshold voltage is {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The voltages used for the testing could be {hyp_value} units.",

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
            "What could be the voltages used for the testing?",

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


def power_bank_recharge(repetition_count):
    category, subcategory = "attribute_comparison", "power_bank_recharge",
    knowledge = "The higher the amperes of the input, the faster the power bank will recharge."

    binary_instances = []
    mcq_instances = []
    given_value_start = 5
    given_value_end = 25

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought two power banks with different specifications and tried to see the one that charges fast. The one charging fast has the input amperes as {given_value} units.",
            "{name} bought two power banks and wanted to see the one that charges fast. The one charging fast has the input amperes as {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The input amperes of the other power bank could be {hyp_value} units.",
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
            "What could be the input amperes of the other power bank?",

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


if __name__ == "__main__":
    repetition_count = 1
    binary_instances = []
    mcq_instances = []

    template_binary_instances, template_mcq_instances = solenoid_and_current(
        repetition_count)
    binary_instances += template_binary_instances
    mcq_instances += template_mcq_instances

    pprint.pprint(binary_instances)
    print("---------------")
    pprint.pprint(mcq_instances)
