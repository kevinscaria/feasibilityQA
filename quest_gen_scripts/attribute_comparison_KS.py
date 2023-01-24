import util
import random
import pprint
import numpy as np


def vehicle_in_garage_less_than_spots(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "vehicle_and_garage"
    knowledge = "Number of vehicles in garage can not be more than the total number of spots in the garage."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A parking garage has {given_value} spots.",
            "{given_value} spots are there in a parking lot.",
        ])
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(150, 300)
        premise = premise_template.format(given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The parking garage could accommodate {hyp_value} cars.",
            "{hyp_value} cars could be present in the garage.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=5,
            scale=1
        )

        question_template = random.choice([
            "How many cars can this garage accommodate?"
        ])
        question_text = question_template
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=5,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def num_parking_spots_more_than_num_cars(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "vehicle_and_garage"
    knowledge = "Number of parking spots is at least the number of cars parked in the area."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The parking lot owned by {name} had {given_value} cars parked at 1 pm.",
            "{given_value} cars were parked in the parking lot owned by {name} at 1 pm.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 200)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The parking garage could be having {hyp_value} spots."
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=5,
            scale=1
        )

        question_template = random.choice([
            "How many spots could the parking garage have?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=5,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cup_and_water(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "cup_and_water"
    knowledge = "The volume of water cannot be more than the volume of cup."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s is holding a single {given_value} ml cup of water.",
            "The cup of water held by {name} is {given_value} ml.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 500)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} could drink {hyp_value} ml of water in from that cup."
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=5,
            scale=1
        )

        question_template = random.choice([
            "How much water can {name} drink from that cup?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=5,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def water_and_cup(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "cup_and_water"
    knowledge = "The volume of liquid a cup can hold can not be more than its capacity."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to transfer {given_value} ml of juice from a bottle to a cup.",
            "{name} bought a packet of juice containing {given_value} ml of juice. He wanted to transfer it to a cup.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 500)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} could use a {hyp_value} ml cup of for this."
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=5,
            scale=1
        )

        question_template = random.choice([
            "What could be the volume of the cup to be used by {name}?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=5,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def patients_less_than_number_beds(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "patients_less_than_number_beds", "patients_and_beds"
    knowledge = "The number of patients that can be accommodated can not be more than the number of beds in a hospital."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A local hospital has {given_value} beds available.",
            "In a town, there are {given_value} beds available in the hospital.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(15, 30)
        premise = premise_template.format(given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The hospital can accommodate {hyp_value} patients."
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
            "How many patients can be accommodated in the hospital?"
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


def winning_team_score_more_than_losing_team(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "winning_and_losing_team"
    knowledge = "Winning team scores more than losing team."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The winning team scored {given_value} points in the match.",
            "In the recent high school soccer game, the away team won the match and scored {given_value} points.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(15, 30)
        premise = premise_template.format(given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The losing team could have scored {hyp_value} points in that match."
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
            "How many points could have been scored by the losing team?"
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


def losing_team_score_less_than_winning_team(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "winning_and_losing_team"
    knowledge = "Losing team scores less than winning team."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The losing team scored {given_value} points in the match.",
            "In the recent soccer game, the losing team scored {given_value} points.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(15, 30)
        premise = premise_template.format(given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The winning team could have scored {hyp_value} points in that match."
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
            "How many points could have been scored by the winning team?"
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


def weight_comparison1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "weight"
    knowledge = "Heavy person has more weight than a light person."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is heavier than his friend and is {given_value} pounds.",
            "{name} and his friend recently went a fair. They went to a stall to weigh themselves. {name} who is heavier than his friend weighed {given_value} pounds.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(130, 200)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s friend could weigh {hyp_value} pounds."
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
            "What could be the weight of his friend?"
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


def weight_comparison2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "weight"
    knowledge = "Light person has lesser weight than heavy person."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is less heavier than his friend and is {given_value} pounds.",
            "{name} and his friend recently went a fair. They went to a stall to weigh themselves. {name} who is less heavier than his friend weighed {given_value} pounds.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(130, 200)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s friend could weigh {hyp_value} pounds."
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
            "What could be the weight of his friend?"
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


def sport_throwing1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "throwing_sport"
    knowledge = "In throwing sports, winner throws the object farthest."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In the recent tournament, {name} was the winner who threw the Javelin {given_value} meters.",
            "{name} was a winner in the recent shotput tournament. He threw the shotput ball {given_value} meters.",

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(50, 90)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The runner up in the recent tournament could have thrown in for {hyp_value} meters."
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
            "How far could the third place player have thrown the object?"
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


def sport_throwing2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "throwing_sport"
    knowledge = "In throwing sports, winner throws the object farthest."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In the recent athletics game, {name} was the runner up and threw the ball {given_value} meters far.",
            "{name} was a runner up in the recent shotput tournament. He threw the shotput ball {given_value} meters far.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(5, 10)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The winner in that tournament could have thrown the ball {hyp_value} meters far."
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
            "How far could the winner player have thrown the ball?"
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


def sport_lifting1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "lifting_sport"
    knowledge = "In lifting sports, the winner lifts the heaviest object among the competitors."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "This year's state weight lifting championship witnessed {name} emerging as the winner who lifted {given_value} kgs.",
            "In the recent heavy weight lifting tournament, {name} was the winner who lifted {given_value} kgs.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 150)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The player who came second in that tournament could have lifted {hyp_value} kgs."
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
            "What could have been the weight that was lifted by the third place winner?"
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


def sport_lifting2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "lifting_sport"
    knowledge = "In lifting sports, the winner lifts the heaviest object among the competitors."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "In a weight lifting tournament, {name} was the runner up who lifted {given_value} kgs.",
            "This year's state heavy weight championship witnessed {name} emerging as the runner up who lifted {given_value} kgs.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 180)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The winner in that tournament could have lifted {hyp_value} kgs."
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
            "What could have been the weight lifted by the winner?"
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


def subset_is_smaller_than_set1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "subset_vs_set"
    knowledge = "Size of set can never be smaller to the size of subset."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "There are {given_value} red balls and few white balls in the bag.",
            "In a small bag, there are {given_value} blue balls and few green balls.",

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 180)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The total number of balls in the bag could be {hyp_value}."
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
            "How many balls could be in the bag?"
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


def subset_is_smaller_than_set2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "subset_vs_set"
    knowledge = "A subset can not be bigger than the set."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "There are {given_value} balls in the bag. Some balls are red and some are blue.",
            "In a small bag, there are {given_value} balls. Some of them are green and the rest are red."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 180)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The total number of red balls in the bag could be {hyp_value}."
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
            "How many red balls could be in the bag?"
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


def marks_comparisons1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "marks_comparisons"
    knowledge = "To pass an exam, you need to get at least passing marks."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} passed an exam where the passing score was {given_value}.",
            "{name} cleared the toughest exam in his country to become a revenue officer. It was an impressive feat because the passing marks was {given_value}.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(70, 83)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} could have scored {hyp_value} marks in that exam."
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
            "How many marks could have been scored by {name} in the exam?"
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


def marks_comparisons2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "marks_comparisons"
    knowledge = "To pass an exam, you need to get at least passing marks."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} secured {given_value} marks in the final test and passed.",
            "{name} in the civil services test this year scored {given_value} marks. He was very proud of himself as he cleared the cut off score.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(70, 83)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The passing marks for {name}'s test could have been {hyp_value}."
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
            "What could have been the passing marks for {name}'s test?"
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


def marks_comparisons3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "marks_comparisons"
    knowledge = "If one does not score at least the passing marks they fail."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} secured {given_value} marks in the final test and failed.",
            "{name} in the civil services test this year scored {given_value} marks. He was disappointed as he could not clear the cut off score.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(70, 83)
        premise = premise_template.format(
            name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The passing marks for {name}'s test could have been {hyp_value}."
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
            "What could have been the passing marks for {name}'s test?"
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


def speed_and_time1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "speed_and_time"
    knowledge = "Faster body takes lesser time to travel."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} is travelling at the rate of {given_value} mph and reaches the destination in 2 hours. His friend started from the same place and reached an hour late.",
            "{name}'s friend started from {name}'s home and reached the destination an hour late. However, {name} who started at the same time and was travelling at the rate of {given_value} mph reached the destination in 2 hours.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(60, 100)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The speed at which {name}'s friend was travelling could have been {hyp_value} mph."
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
            "What could have been the speed at which {name}'s friend was travelling?"
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


def speed_and_time2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "speed_and_time"
    knowledge = "Slower body takes more time to travel."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} reached to the office at the rate of {given_value} mph, 30 minutes later than his brother who started from the same home at the same time.",
            "{name} arrived at the hotel at a rate of {given_value} mph, one hour later than his brother who started from the same house at the same time."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(60, 100)
        premise = premise_template.format(
            name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The speed at which {name}'s brother travelled could have been {hyp_value} mph."
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
            "What could have been the speed at which {name}'s brother was travelling?"
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


def addition_knowledge1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "addition_knowledge"
    knowledge = "The sum of two operands is greater than or equal to the largest operand."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "In a game of cricket, the winning team scored {given_value} runs.",
            "The recent football match witnessed the winning team scoring {given_value} runs."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(80, 130)
        premise = premise_template.format(
            given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The total number of runs scored by both teams could have been {hyp_value}."
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=60,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could have been the total runs scored by both teams?"
        ])
        question_text = question_template
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=60,
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


def addition_knowledge2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "addition_knowledge"
    knowledge = "The operands are smaller than the sum of operands."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} has a barrel of oil and his friend has another barrel which is smaller than {name}'s barrel. The contents of both were emptied to a container and the total volume of oil in that was {given_value} units.",
            "{name} purchased a barrel of wine and his friend has another barrel that is smaller than the barrel that {name} had. Both containers were poured into a bigger barrel and the total volume of wine is now {given_value} units."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(50, 100)
        premise = premise_template.format(name=name,
                                          given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The volume of liquid in {name}'s barrel could have been {hyp_value}."
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
            "What could have been the volume of liquid in {name}'s barrel?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=60,
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


def subtraction_knowledge(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "subtraction_knowledge"
    knowledge = "The difference of two positive operands is smaller than or equal to the largest positive operand."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "A class has more boys than girls. The difference between the number of boys and girls is {given_value}.",
            "A bus that was taking a few students toa  field trip had more number of boys than girls. The number of  boys were {given_value} more than the number of girls."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(10, 15)
        premise = premise_template.format(
            given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The total number of boys in the could be {hyp_value}."
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
            "What could be the total number of boys?"
        ])
        question_text = question_template
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


def tallest_knowledge(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "tallest_knowledge"
    knowledge = "There is nothing taller than the tallest object."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "The tower built by {name}'s company is the tallest building in the city and it will stand {given_value} meters tall.",
            "{name}'s friend lives in the tallest building in the city and it is {given_value} meters high.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(80, 100)
        premise = premise_template.format(name=name,
                                          given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "A nearby shop could be {hyp_value} meters tall."
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
            "What could be the height of a nearby shop?"
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


def shortest_knowledge(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "shortest_knowledge"
    knowledge = "There is nothing shorter than the shortest object."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} is the shortest among his friends group and is {given_value} cms tall.",
            "In his friend's circle, {name} is the shortest and is {given_value} cms tall.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(150, 170)
        premise = premise_template.format(name=name,
                                          given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s friend's height could be {hyp_value} cms."
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
            "What could be the height of {name}'s friend?"
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


def heaviest_knowledge(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "heaviest_knowledge"
    knowledge = "There is nothing heavier than the heaviest object."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "Among a group of friends, {name} is the heaviest and is {given_value} kgs.",
            "{name} and his friends went for a weight loss session. {name} who is the heaviest was {given_value} kgs.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(80, 110)
        premise = premise_template.format(name=name,
                                          given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s friend's weight could be {hyp_value} kgs."
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
            "What could be the weight of {name}'s friend?"
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


def topper_is_highest_scorer1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "education_performance"
    knowledge = "Topper of a class is the best performer in an exam."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} was the topper in the physics quiz and scored {given_value} marks.",
            "In the chemistry test, {name} was the topper and got {given_value} marks.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(90, 100)
        premise = premise_template.format(name=name,
                                          given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s classmate could have scored {hyp_value} marks in the same test."
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
            "What could be the marks scored by {name}'s classmate in the same test?"
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


def topper_is_highest_scorer2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "education_performance"
    knowledge = "There is no student scoring more than the topper of a class."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} scored {given_value} marks in a maths test.",
            "In the chemistry test, {name} scored {given_value} marks.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(80, 90)
        premise = premise_template.format(name=name,
                                          given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s classmate who was the topper could have scored {hyp_value} marks in the same test."
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
            "What could be the marks scored by {name}'s classmate who was the topper in the same test?"
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
    knowledge = "Legal age to vote is 18 years in India"

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} is a citizen of India and he recently cast his first vote in the national election.",
            "{name} is an Indian citizen and recently cast his first vote in the national assembly election."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(18, 19)
        premise = premise_template.format(name=name)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} is {hyp_value} years old when he casted the vote."
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=7,
            scale=1
        )

        question_template = random.choice([
            "What could be the age of {name} when he casted the vote?"
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


def relations_siblings(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "sibling_relationship"
    knowledge = "Elder sibling is older than younger sibling."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name}'s elder brother recenetly turned {given_value} years old this year.",
            "{name}'s older brother recently turned {given_value} this year."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(18, 50)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The age of {name} is {hyp_value} years old."
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the age of {name} this year?"
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


def percentile_logic(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "percentile_logic"
    knowledge = "Higher percentile means more people scored lower than you."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "In a competitive exam for B-Schools, {name} scored 73 percentile and had {given_value} people scoring lesser than him.",
            "{name} scored 80 percentile in the engineering entrance exam. He was relieved that{given_value} people scored lesser than him and he had a shot of getting a good university."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(3000, 8000)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s friend whose percentile was higher than {name} had {hyp_value} candidates scoring lesser than him."
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
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "If {name}'s friend whose percentile was higher than {name}, how many candidates scored lesser than him."
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=100,
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


def geometry_rectangles1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "geometry_rectangles"
    knowledge = "Length is always greater than width in a rectangle."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} visited a rectangular park in the middle of new york city. The park is {given_value} metres wide.",
            "When {name} visited New York, he wanted to visit the rectangular park owned by his friend.The park was sophisticated and was {given_value} meters wide."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 200)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The park visited by {name} has {hyp_value} metres length."
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
            "What could be the length of the park visited by {name}?"
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


def geometry_rectangles2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "geometry_rectangles"
    knowledge = "Width is always lesser than length in a rectangle."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "In {name}'s recent trip, he visited a park which was rectangular in shape. The park was {given_value} metres in length.",
            "On the recent field trip {name} visited a rectangular park which was {given_value} meters long."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 200)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The park visited by {name} has {hyp_value} metres width."
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
            "What could be the width of the park visited by {name}?"
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


def size_to_weight_knowledge(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "size_to_weight"
    knowledge = "Bigger car is heavier than smaller car."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} recently bought an SUV which is bigger than his friend's sedan and weighed around {given_value} lb.",
            "{name} invited his friend to go on a drive on his new SUV, since it was bigger than his friends car and could accomodate more people. However, the car was heavy and weighed {given_value} lb and the mileage was poor."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(4800, 5500)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s friends sedan weighed {hyp_value} lb."
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
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=100,
            scale=1
        )

        question_template = random.choice([
            "What could be the weight of the {name}'s friends sedan?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=1000,
            more_is_correct_flag=False,
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


def height_is_proportional_to_pressure_head1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "height_and_pressure"
    knowledge = "Height is directly proportional to pressure head."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name}'s house recently installed a water tank and the pressure head generated is {given_value} m.",
            "The  pressure head generated by a water tank that was installed by {name} was {given_value}m."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(50, 100)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s friend's house which is higher than {name}'s house also installed a water tank and the pressure head generated is {hyp_value} m."
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
            "What could be the pressure generated by the water tank installed at {name}'s friend's house which is higher than {name}'s house?"
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


def height_is_proportional_to_pressure_head2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "height_and_pressure"
    knowledge = "Height is directly proportional to pressure head."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name}'s house recently installed a water tank and the pressure head generated is {given_value} m.",
            "The  pressure head generated by a water tank that was installed by {name} was {given_value}m."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(50, 100)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name}'s friend's house which is lower than {name}'s house also installed a water tank and the pressure head generated is {hyp_value} m."
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
            "What could be the pressure generated by the water tank installed at {name}'s friend's house which is lower than {name}'s house?"
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


def volume_knowledge1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "volume_and_height"
    knowledge = "Volume is directly proportional to height when base area is constant."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name}'s house recently installed a rectangular water tank and his friends' house also installed a bigger water tank with the same base dimensions. The height of the {name}'s water tank is {given_value} m.",
            "{name}'s recently installed a rectangular septic tank along with his friend to get a larger discount on installation. His friend however installed a bigger septic tank with the same base dimensions. The height of the {name}'s septic tank is {given_value} m."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(50, 100)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The height of {name}'s friend's tank can be {hyp_value} m."
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
            "What could be the height of the tank installed by {name}'s friend?"
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


def volume_knowledge2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "volume_and_height"
    knowledge = "Volume is directly proportional to height when base area is constant."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name}'s neighbour installed a swimming pool. So, {name} installed a smaller swimming pool as well with the same base area. The height of the {name}'s neighbours swimming pool is {given_value} m.",
            "{name}'s friend and {name} installed a swimming pool together. {name}'s swimming pool was smaller but with the same base area. The height of the {name}'s friend's swimming pool is {given_value} m.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(3, 10)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The height of {name}'s swimming pool can be {hyp_value} m."
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
            "What could be the height of the swimming pool installed by {name}?"
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


def volume_knowledge3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "volume_and_base_area "
    knowledge = "Volume is directly proportional to base area when height is constant."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} and his neighbour fitted a water tank of same height. {name}'s water tank is larger than his neighbours. The base area of {name}'s water tank is {given_value} units.",
            "{name} and his friend installed a septic tank of same height. {name}'s septic tank is larger than his friend's. The base area of {name}'s septic tank is {given_value} units.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(3, 10)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The base area of {name}'s neighbours tank can be {hyp_value} m."
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
            "What could be the base area of the tank installed by {name}?"
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


def volume_knowledge4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "volume_and_base_area "
    knowledge = "Volume is directly proportional to base area when height is constant."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} and his neighbour fitted a swimming pool of same height. {name}'s swimming pool is smaller than his neighbours. The base area of {name}'s swimming pool is {given_value} units.",
            "{name} and his friend fitted a swimming pool of same height. The base area of {name}'s swimming pool is {given_value} units and is smaller than his friend."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(3, 10)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The base area of {name}'s neighbours swimming pool can be {hyp_value} m."
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
            "What could be the base area of the water tank installed by {name}?"
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


def work_done(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "work_done "
    knowledge = "Work done is proportional to rate of work done when time is constant."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} and his friend were building a wall and both of them worked for 25 days. Their manager told that {name} worked more in the time duration and was paid more. {name} built the wall at the rate of {given_value} metre per day.",

            "The project manager told that {name} worked more than his friend to complete the construction of the wall in the given time duration and thus was paid more. {name} built the wall at the rate of {given_value} metre per day.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(5, 10)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The rate at which {name}'s friend built the wall could be {hyp_value} metre per day."
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=2,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the rate at which {name}'s friend constructed the wall?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=2,
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


def temperature1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "temperature_and_weather "
    knowledge = "Hotter weather means higher temperature."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} lives in Texas which is more hotter than where his friend stays which is in San Diego. The temperature in Texas is {given_value} celsius.",
            "{name} lives in Chennai which is more hotter than Delhi where his friend stays. The temperature in Chennai is {given_value} celsius.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(35, 50)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The temperature where {name}'s friend lives could be {hyp_value} celsius."
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
            "What could be the temperature in the city where {name}'s friend stays?"
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


def temperature2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "temperature_and_weather "
    knowledge = "Colder weather means lower temperature."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name}'s job is in a far more colder place than where his friend stays. The temperature yesterday dropped to {given_value} celsius in the city where {name} lives.",
            "The recent posting for {name} was in a much colder place than where his friend stays. The temperature yesterday was {given_value} celsius in the city where {name} was posted to."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(100, 150)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The temperature where {name}'s friend lives could be {hyp_value} celsius."
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
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the temperature in the city where {name}'s friend stays?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def taller1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "height_comparison "
    knowledge = "Taller means more higher."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} is taller than his friend. {name} is {given_value} cms tall."
            "{name} is {given_value} cms tall and is taller than his friend."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(150, 190)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The height of {name}'s friend is {hyp_value} cms."
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
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the height of {name}'s friend?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def taller2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "height_comparison "
    knowledge = "Shorter means less higher."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} is shorter than his friend. {name} is {given_value} cms tall."
            "{name} is {given_value} cms tall and is shorten than his friend."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(150, 190)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The height of {name}'s friend is {hyp_value} cms."
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
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the height of {name}'s friend?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def flight_schedule1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "schedule_and_time "
    knowledge = "Passengers should arrive at the airport before the departure time."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} has to board a flight to Singapore at {given_value} o'clock and was able to succesfully catch the flight from JFK airport.",
            "{name} has a business trip to New Delhi at {given_value} o'clock. He boarded the flight from Mumbai airport."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(6, 12)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} could have arrived at the airport at {hyp_value} o'clock."
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
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the time when {name} arrived at the airport?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=3,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def flight_schedule2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "schedule_and_time "
    knowledge = "Passengers should arrive at the airport before the departure time."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} has to board a flight to Singapore at {given_value} o'clock and missed his flight from Los Angeles airport.",
            "{name} has a business trip to New Delhi at {given_value} o'clock. He could not board the flight from Mumbai airport as he missed the flight."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(6, 12)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} could have arrived at the airport at {hyp_value} o'clock."
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
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the time when {name} arrived at the airport?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=3,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=True,
            round_to=1,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def anatomy_knowledge(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "attribute_comparison", "anatomy_knowledge "
    knowledge = "A baby has more bones than a human."

    for i in range(repetition_count):

        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, a=[
            "{name} attended a biology seminar where he learnt that an adult human has {given_value} bones.",
            "{name}'s kid saw a book which displayed that a human adult has 206 bones."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)

        given_value = random.randint(206, 206)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The number of bones in a baby could be {hyp_value}.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=94,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=True,
            round_to=10,
            scale=1
        )

        question_template = random.choice([
            "What could be the number of bones in an infant?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=94,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=True,
            round_to=10,
            scale=1
        )

        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


# if __name__ == "__main__":
#     repetition_count = 2
#     binary_instances = []
#     mcq_instances = []

#     template_binary_instances, template_mcq_instances = vehicle_in_garage_less_than_spots(
#         repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances

#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
