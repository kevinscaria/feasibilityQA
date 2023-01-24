import util
import random
import pprint
import numpy as np


def half(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "half"
    knowledge = "Half means one by two"

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} borrowed a loan of {given_value} thousand dollars and spent more than half in just setting up new infrastructure.",
            "{name} spent {given_value} years in a finance company and then spent more than half this time in a technology company.",
        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have spent {hyp_value} thousand dollars on just infrastructure",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many thousand dollars {name} could have spent on infrastructure?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def half2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "half"
    knowledge = "Half means one by two"

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} borrowed a loan of {given_value} thousand dollars and spent more than half in just setting up new infrastructure.",
            "{name} spent {given_value} years in a finance company and then spent more than half this time in a technology company.",
        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be left with {hyp_value} thousand dollars after spending on infrastructure.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many thousand dollars could be left with {name} after spending on infrastructure?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def half3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "half"
    knowledge = "Half means one by two"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} spent {given_value} years in a finance company and then spent more than half this time in a technology company.",
            "{name} borrowed a loan of {given_value} thousand dollars and spent more than half in just setting up new infrastructure.",
        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have spent {hyp_value} years in the technology company.",
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
            "How many years {name} could have spent in the technological company?",

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


def percent(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "percent"
    knowledge = "50% means half"

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} borrowed a loan of {given_value} thousand dollars and spent more than 50% of it in just setting up new infrastructure.",
            "{name} spent {given_value} years in a finance company and then spent more than 50% this time in a technology company.",
        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have spent {hyp_value} thousand dollars on just infrastructure",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many thousand dollars {name} could have spent on infrastructure?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def percent2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "percent"
    knowledge = "50% percent means half"

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} borrowed a loan of {given_value} thousand dollars and spent more than 50% of it in just setting up new infrastructure.",
            "{name} spent {given_value} years in a finance company and then spent more than 50% this time in a technology company.",
        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be left with {hyp_value} thousand dollars after spending on infrastructure.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=5,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many thousand dollars could be left with {name} after spending on infrastructure?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def double(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "double"
    knowledge = "Double means two times"

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} borrowed a loan of {given_value} thousand dollars from state bank and borrowed more than double this amount from his father.",
            "{name} borrowed a loan of {given_value} thousand dollars from state bank and borrowed more than double this amount from his mother.",
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have borrowed {hyp_value} thousand dollars from his father.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many thousand dollars {name} could have borrowed from his father?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def double2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "double"
    knowledge = "Double means two times"

    given_value_start = 5
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} spent {given_value} years in a finance company and then spent more than double this time in a technology company.",
            "{name} spent {given_value} years in a finance company and then spent more than double this time in a software company.",
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have spent {hyp_value} years in the technology company.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many years {name} could have spent in the technological company?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def double3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "double"
    knowledge = "Double means two times"

    given_value_start = 500
    given_value_end = 1000

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} scored {given_value} runs last year and this year he has scored more than double these runs.",
            "{name} scored {given_value} runs last year and this year he has scored more than double these runs.",
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have scored {hyp_value} runs this year.",
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
            round_to=50,
            scale=1
        )

        question_template = random.choice([
            "How many runs {name} could have scored this year?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=200,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=50,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def double4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "double"
    knowledge = "Double means two times"

    given_value_start = 500
    given_value_end = 1000

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Last year {given_value} people voted for the college election and this year the vote count was more than double the last time.",
            "This year the number of people who voted was more than double the last time. Last time the vote count was just {given_value}.",

        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} people could have voted this year.",
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
            round_to=50,
            scale=1
        )

        question_template = random.choice([
            "How many people could have voted this year?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=200,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=50,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def double5(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "double"
    knowledge = "Double means two times"

    given_value_start = 500
    given_value_end = 1000

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "This year the number of people who joined the company was more than double the last time. Last time only {given_value} people joined.",
            "Last year {given_value} people joined the company and this year the number of people who joined was more than double the last time.",

        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} people could have joined this year.",
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
            round_to=10,
            scale=1
        )

        question_template = random.choice([
            "How many people could have joined this year?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=200,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=10,
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

#     template_binary_instances, template_mcq_instances = double5(
#         repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances

#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
