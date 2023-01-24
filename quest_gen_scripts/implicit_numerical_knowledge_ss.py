import util
import random
import pprint
import numpy as np


def dozen(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "dozen"
    knowledge = "A dozen has 12 items"

    given_value_start = 1
    given_value_end = 2

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a dozen of eggs and unfortunately some of the eggs are cracked.",
            "{name} is preparing dinner. He has a dozen of eggs and he cracked some eggs to prepare food."
        ])

        factor = 12
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be left with {hyp_value} non cracked eggs.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=3,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many eggs does {name} have such that it is not cracked?.",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def pair(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "pair"
    knowledge = "A pair has 2 items"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are more than {given_value} pair of dancers on the stage.",
            "For clicking a photograph in a gathering, more than {given_value} pairs gathered on the stage."
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} people on the stage.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=3,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many people could be on stage?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=3,
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


def grand(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "grand"
    knowledge = "A grand is equal to 1000 "

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The prize money for winning the dance competition is more than {given_value} grand dollars.",
            "For a weight lifting competition the prize money was more than {given_value} grand dollars."
        ])

        factor = 1000
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The prize money could be {hyp_value}.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=200,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "The prize money for winning the competition could be ?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=200,
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


def couple(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "couple"
    knowledge = "A couple has 2 items"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are more than {given_value} couples in a room.",
            "Mare than {given_value} couples were dancing in the room."
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} people in the room.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=3,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many people could be in the room?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=3,
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
#     repetition_count = 2
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = couple(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
