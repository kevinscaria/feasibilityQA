import util
import random
import pprint
import numpy as np


def age_with_time1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "change_with_time", "age"
    knowledge = "Age increases with time"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s age is {given_value} years old today.",
            "Today {name} is {given_value} years old.",
            "Today, while filling the application form {name} filled the age field with {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(15, 30)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have been {hyp_value} years old last year.",
            "{name} could have been {hyp_value} years old on his last birthday.",
            "While filling the application form last year, {name} could have written {hyp_value} in the age field."

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
            "What could have been {name}'s age last year ?",

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


def age_with_time2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "change_with_time", "age"
    knowledge = "Age increases with time"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s age is {given_value} years old today.",
            "Today {name} is {given_value} years old.",
            "Today, while filling the application form {name} filled the age field with {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(15, 30)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be {hyp_value} years old next year.",
            "{name} could be {hyp_value} years old on his next birthday.",
            "When filling the application form next year, {name} could write {hyp_value} in the age field."

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
            "What could have been {name}'s age next year ?",

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


def foot_with_time1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "change_with_time", "foot_length"
    knowledge = "Foot length increases with time"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s feet length is {given_value} cm today.",
            "{name} went shopping to buy new pair of shoes. His foot length is {given_value} cm when measured at the store."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(15, 30)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have {hyp_value} cm foot length last year.",
            "He could have bought a pair of shoes of foot length {hyp_value} cm last year."
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
            "What could have been {name}'s foot length last year ?",

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


def foot_with_time2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "change_with_time", "foot_length"
    knowledge = "Foot length increases with time"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s feet length is {given_value} cm today.",
            "{name} went shopping to buy new pair of shoes. His foot length is {given_value} cm when measured at the store."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(15, 30)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have {hyp_value} cm foot length next year.",
            "He could have bought a pair of shoes of foot length {hyp_value} cm last year."
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
            "What could have been {name}'s foot length next year ?",

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


# if __name__ == "__main__":
#     repetition_count = 1
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = foot_with_time2(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
