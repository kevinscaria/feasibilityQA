import util
import random
import pprint
import numpy as np


def working_days(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "working_days"
    knowledge = "A week has 5 working days"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} goes to the office on all working days. He has been going to the office for at least {given_value} weeks.",
            "{name} recently joined the ACB company and has been going to the office for at least {given_value} weeks on all working days."
        ])

        factor = 5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have gone for {hyp_value} days.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many days {name} could have gone to the office?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
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


def working_days2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "working_days"
    knowledge = "A week has 5 working days"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} goes to the office on all working days. He has been going to the office for less than {given_value} weeks.",
            "{name} recently joined the ACB company and has been going to the office for less than {given_value} weeks on all working days."

        ])

        factor = 5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have gone for {hyp_value} days.",
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
            "How many days {name} could have gone to the office?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
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


def working_days3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "working_days"
    knowledge = "A week has 5 working days"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} goes to the office on all working days. He has been going to the office for more than {given_value} weeks.",
            "{name} recently joined the ACB company and has been going to the office for more than {given_value} weeks on all working days."

        ])

        factor = 5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have gone for {hyp_value} days.",
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
            "How many days {name} could have gone to the office?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
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


def days_in_week(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "working_days"
    knowledge = "A week has 7 days"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} goes to the office on all days of a week. He has been going to the office for at least {given_value} weeks.",
            "{name} recently joined the ACB company and has been going to the office for at least {given_value} weeks on all days."
        ])

        factor = 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have gone for {hyp_value} days.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many days {name} could have gone to the office?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
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


def days_in_week2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "working_days"
    knowledge = "A week has 7 days"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} goes to the office on all days of a week. He has been going to the office for less than {given_value} weeks.",
            "{name} recently joined the ACB company and has been going to the office for less than {given_value} weeks on all days."
        ])

        factor = 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have gone for {hyp_value} days.",
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
            "How many days {name} could have gone to the office?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
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


def days_in_week3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "working_days"
    knowledge = "A week has 7 days"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} goes to the office on all days of a week. He has been going to the office for more than {given_value} weeks.",
            "{name} recently joined the ACB company and has been going to the office for more than {given_value} weeks on all days."
        ])

        factor = 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have gone for {hyp_value} days.",
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
            "How many days {name} could have gone to the office?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
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


def days_in_week4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "working_days"
    knowledge = "A week has 7 days"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} gym membership will expire exactly after {given_value} weeks. He will be going on a vacation for a few days in that period.",
            "{name} was sick and was unable to gym for a few days. Unfortunately, his gym membership will be expiring exactly after {given_value} weeks."
        ])

        factor = 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could visit to the gym for {hyp_value} days.",
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
            "How many days could {name} go to the gym?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
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


def thumb_in_hand(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "thumb_in_hand"
    knowledge = "A human usually has two hands each having one thumb"

    given_value_start = 20
    given_value_end = 80

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a meeting, all the attendees scanned the thumb of both their hands. There were at least {given_value} scans done.",
            "For security purpose, a company have the policy to scan thumbs of employers. In a business meeting, all the member's thumbs were scanned, and there were at least {given_value} scans."
        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} people could have attended the meeting.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many people could have attended the meeting?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def thumb_in_hand2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "thumb_in_hand"
    knowledge = "A human usually has two hands each having one thumb"

    given_value_start = 20
    given_value_end = 80

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a meeting, all the attendees scanned the thumb of both their hands. There were less than {given_value} scans done.",
            "For security purpose, a company have the policy to scan thumbs of employers. In a business meeting, all the member's thumbs were scanned, and there were less than {given_value} scans."
        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} people could have attended the meeting.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many people could have attended the meeting?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def chess(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "chess"
    knowledge = "In chess, there are 4 knights, 4 bishops, 4 rooks."

    given_value_start = 6
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought more than {given_value} chess games.",
            "{name} received more than {given_value} chess games as gift."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have {hyp_value} knights in total.",
            "{name} could have {hyp_value} bishops in total.",
            "{name} could have {hyp_value} rooks in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "How many knights {name} could have in total?",
            "How many bishops {name} could have in total?",
            "How many rooks {name} could have in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def chess2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "chess"
    knowledge = "In chess, there are 4 knights, 4 bishops, and 4 rooks; 2 of black and 2 of white"

    given_value_start = 6
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought more than {given_value} chess games.",
            "{name} received more than {given_value} chess games as gift."
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have {hyp_value} white knights in total.",
            "{name} could have {hyp_value} white bishops in total.",
            "{name} could have {hyp_value} white rooks in total.",
            "{name} could have {hyp_value} black knights in total.",
            "{name} could have {hyp_value} black bishops in total.",
            "{name} could have {hyp_value} black rooks in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many white knights {name} could have in total?",
            "How many white bishops {name} could have in total?",
            "How many while rooks {name} could have in total?",
            "How many black knights {name} could have in total?",
            "How many black bishops {name} could have in total?",
            "How many black rooks {name} could have in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def chess3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "chess"
    knowledge = "In chess, there are 16 pawns, 8 of black and 8 of white"

    given_value_start = 6
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought more than {given_value} chess games.",
            "{name} received more than {given_value} chess games as gift."
        ])

        factor = 8
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have {hyp_value} white pawns in total.",
            "{name} could have {hyp_value} black pawns in total.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many white pawns {name} could have in total?",
            "How many black pawns {name} could have in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def chess4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "chess"
    knowledge = "In chess, there are 32 white squares and 32 black squares"

    given_value_start = 32
    given_value_end = 33

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} started painting all the white squares of a chess board with pink color.",
            "{name} started painting all the black squares of a chess board with green color.",
        ])

        factor = 1
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "In an hour, {name} could have painted {hyp_value} squares.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "In an hour, how many squares {name} could have painted?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def chess5(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "chess"
    knowledge = "A chess board has 64 squares"

    given_value_start = 64
    given_value_end = 65

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} started painting all the squares of a chess board with pink color.",
            "{name} got bored playing chess and started painting all the squares with green color."
        ])

        factor = 1
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "In an hour, {name} could have painted {hyp_value} squares.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "In an hour, how many squares {name} could have painted?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def square(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "square"
    knowledge = "A square has four sides of equal length"

    given_value_start = 6
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to fence his square garden of side length {given_value} units using wires.",
            "To protect the square garden of side length {given_value} units from invaders, {name} fenced his garden with wires."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "A wire of length {hyp_value} units could suffice for fencing the garden completely.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What length wire could be used to completely fence the garden?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def square2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "square"
    knowledge = "A square has four sides of equal length"

    given_value_start = 50
    given_value_end = 100

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to make a square using a thread. He has a thread of length {given_value} units.",
            "{name} is making a square shaped frame with ribbon. He has ribbon of length {given_value} units."
        ])

        factor = 0.25
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could make the square of side length {hyp_value} units.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the side length of the square?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


# def square2(repetition_count):
#     binary_instances = []
#     mcq_instances = []
#
#     category, subcategory = "implicit_numerical_knowledge", "square"
#     knowledge = "Area of a square is side multiplied by side."
#
#     given_value_start = 6
#     given_value_end = 20
#
#     for i in range(repetition_count):
#         # *******Template 1
#
#         premise_template = np.random.choice(size=repetition_count, replace=False, a=[
#             "{name} wants to paint a square board of side length {given_value}.",
#         ])
#
#         premise_template = premise_template[i % len(premise_template)];name = random.choice(util.male_names)
#         given_value = random.randint(given_value_start, given_value_end)
#         factor = given_value
#
#         premise = premise_template.format(name=name, given_value=given_value)
#
#         hypothesis_template = random.choice([
#             "A paint box that can cover {hyp_value} sq. units of area could be used to completely paint the board.",
#
#         ])
#         binary_instances += util.create_all_scenarios_for_binary_classification_task(
#             category,
#             subcategory,
#             knowledge,
#             premise,
#             hypothesis_template,
#             name,
#             int(given_value*factor),
#             diff=6,
#             more_is_correct_flag=True,
#             equal_is_correct_flag=True,
#             negative_options_possible=False,
#             round_to=1,
#             scale=1
#         )
#
#     return binary_instances, mcq_instances


def square3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "square"
    knowledge = "A square has four sides of equal length"

    given_value_start = 6
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to fence some portion of his square garden of side length {given_value} units using wires.",
            "To protect the square garden of side length {given_value} units from invaders, {name} fenced some of the uncovered sides of his garden with wires."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "A wire of length {hyp_value} units could result in no wastage.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What length wire could be used for fencing some portion without wastage?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def square4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "square"
    knowledge = "A square has four sides of equal length"

    given_value_start = 6
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to fence some portion of his square garden of side length {given_value} units using wires.",
            "To protect the square garden of side length {given_value} units from invaders, {name} fenced some of the uncovered sides of his garden with wires."

        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "A wire of length {hyp_value} units could result in some wastage.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What length wire could be used for fencing with wastage?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def triangle(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "triangle"
    knowledge = "An equilateral triangle has three sides of equal length"

    given_value_start = 6
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to fence his garden which is in the shape of an equilateral triangle of side length {given_value} units.",
            "{name} was hired to fence an equilateral triangle of side length {given_value} units."
        ])

        factor = 3
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "A wire of length {hyp_value} units could suffice for fencing the garden completely.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What length wire could be used to completely fence the garden?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def bike_tires(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "bike_tires"
    knowledge = "A bike has 2 tires"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a parking lot, there are more than {given_value} bikes. {name} needs to test air in all the tires of the bikes.",
            "In a mechanic shop, more than {given_value} bike arrived to repair their tires. {name} was assigned to do these repairs by his manager at the shop."

        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Total number of tires that {name} needs to test could be {hyp_value}.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many tires {name} could be required to test?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def car_wheels(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "car_wheels"
    knowledge = "A car has 4 wheels"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a parking lot, there are more than {given_value} cars. {name} needs to test air in all the wheels of the cars.",
            "In a mechanic shop, more than {given_value} cars arrived to repair their tires. {name} was assigned to do these repairs by his manager at the shop."

        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Total number of wheels that {name} needs to test could be {hyp_value}.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=8,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "How many tires {name} could be required to test?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=8,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def car_wheels2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "car_wheels"
    knowledge = "A car has 4 wheels"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a repairing workshop, {given_value} cars are tested daily. {name} and his co-worker test air in all the wheels of the cars.",
            "{name} works at car showroom. He daily tests the air pressure of all wheels present in the showroom and there are {given_value} cars present in the showroom."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Total number of wheels that {name} tested could be {hyp_value}.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "How many tires {name} could have tested?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=8,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def olympics(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "olympics"
    knowledge = "In Olympics, medals are awarded to three winners of each sport"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "This time, more than {given_value} sports were organized on the first day of Olympics.",
            "In last year's sports competition at school, there were more than {given_value} sports were organized.",
        ])

        factor = 3
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "A total of {hyp_value} medals could have been given to the winners.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )

        question_template = random.choice([
            "How many medals could have been given to the winners in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=12,
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


def buying(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "buying"
    knowledge = "One needs equal or more money than the price of item to buy it"

    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and he wants to buy a toy each for his two kids. The two toys are of equal price.",
            "{name} went shopping to buy some toys. He has {given_value} dollars and wants to buy two different toys of equal price."

        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could buy both the toys if the price of each toy is {hyp_value} dollars.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )

        question_template = random.choice([
            "What could be the price of a toy if {name} managed to buy them?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def buying2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "buying"
    knowledge = "One can not afford a thing if they have lesser money than its cost"

    given_value_start = 100
    given_value_end = 200

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and he wants to buy a toy each for his two kids. The two toys are of equal price.",
            "{name} went shopping to buy some toys. He has {given_value} dollars and wants to buy two different toys of equal price."

        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could not buy both the toys if the price of each toy is {hyp_value} dollars.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )

        question_template = random.choice([
            "What could have been the price of a toy if {name} failed to buy them?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=12,
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


def dogs(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "dogs"
    knowledge = "Dogs have 4 legs"

    given_value_start = 5
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has recently brought a more than {given_value} dogs to his home. He wants to buy a shoe for each leg of his dogs.",
            "{name} wants to gift shoes for his friend's dogs. His friend recently brought more than {given_value} dogs."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could buy {hyp_value} shoes for his dogs.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "How many shoes could he buy for his dogs?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def animals(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "animals"
    knowledge = "Dogs, cats, cows have 4 legs"

    given_value_start = 5
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} animals. Some are dogs, a few are cats, and remaining are cows. He took all his animals to a doctor and got all their legs tested. The doctor also tested a few other animals that day.",
            "{name} works at a vet. He tested more than {given_value} animal's legs today. The animals tested by {name} includes dogs, cows, and cats."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The doctor could have tested {hyp_value} legs that day.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "How many legs could the doctor have tested?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def decade(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "decade"
    knowledge = "A decade has 10 years"

    given_value_start = 2
    given_value_end = 5

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has been in politics for over {given_value} decades.",
            "John's son {name} has been in politics for {given_value} decades now."
        ])

        factor = 10
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have spent {hyp_value} years in politics.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=8,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many years could {name} have spent in politics?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=8,
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


def dice(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "dice"
    knowledge = "A dice has 6 faces"

    given_value_start = 2
    given_value_end = 5

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} painted all faces of more than {given_value} dice.",
            "{name} is making art by just using many dice. He painted {given_value} dice with different colors."
        ])

        factor = 6
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have painted {hyp_value} faces in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many faces {name} could have painted?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def dice2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "dice"
    knowledge = "A dice has 6 faces"

    given_value_start = 2
    given_value_end = 5

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} painted all faces of less than {given_value} dice.",
            "{name} is making art by just using many dice. He painted less than {given_value} dice with different colors and left the remaining dice untouched."

        ])

        factor = 6
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have painted {hyp_value} faces in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many faces {name} could have painted?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def dice3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "dice"
    knowledge = "A dice has 6 faces"

    given_value_start = 2
    given_value_end = 5

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} painted all faces of at least {given_value} dice.",
            "{name} is making art by just using many dice. He painted at least {given_value} dice with different colors and left the remaining dice untouched."
        ])

        factor = 6
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have painted {hyp_value} faces in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many faces {name} could have painted?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=12,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def dice4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "dice"
    knowledge = "A dice has 6 faces"

    given_value_start = 2
    given_value_end = 5

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend were asked to paint all faces of {given_value} dice. Both of them worked hard and finished the work in 2 hours.",
            "{name} and his brother bought {given_value} dice from the shop. They started painting all faces of dice with blue."
        ])

        factor = 6
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have painted {hyp_value} faces in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many faces {name} could have painted?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value*factor),
            diff=12,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def rainbow(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "rainbow"
    knowledge = "Rainbow has severn colors"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought at least {given_value} shirts of each color of the rainbow.",
            "{name} went shopping during sale season to grab the best deals on clothes. He bought at least {given_value} shirts of each color of the rainbow."
        ])

        factor = 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have bought {hyp_value} shirts in total.",
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
            "How many shirts {name} could have bought in total?",

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


def arms(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "arms"
    knowledge = "A human has 2 arms"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a sports meeting, more than {given_value} sportsmen were present. All of them given a band for both their hands.",
            "In boxing workshop, more than {given_value} candidates came. Before starting the session, the mentor {name} distributed bands for both of their hands."
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} bands could have been given in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many bands could have been given in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def eyes(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "eyes"
    knowledge = "A human has 2 eyes"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a health checkup, more than {given_value} healthy people were present. Eye drops were put in both eyes of all attendees.",
            "In annual health check up at school, the doctor put eye drops in both of eyes of {given_value} students present."
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Eye drops could have been put in {hyp_value} eyes in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "In how many eyes, dropus could have been put in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def eyes2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "eyes"
    knowledge = "A human has 2 eyes"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a health checkup, {given_value} healthy people were present. Eye drops were put in both eyes of all attendees. A few drops also got spilled on the floor.",
            "In annual health check up at school, the doctor put eye drops in both of eyes of {given_value} students present at school. While doing so, the doctor spilled some of the eye drops on the floor."
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} eye drops could have been used up in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many eye drops could have been used up in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bones(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "bones"
    knowledge = "A human body has 206 bones"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a medical student. He is studying each bone of the human body for at least {given_value} hours.",
            "{name} is studying for his exam. The only topic that is left to study is bones in the human body. To learn about a single bone, {name} spends at least {given_value} hours."
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could finish studying all the bones in {hyp_value} hours.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many hours could {name} takes to study all the bones of the human body?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bones2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "bones"
    knowledge = "A human body has 206 bones"

    given_value_start = 206
    given_value_end = 207

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In an accident, a few of {name}'s bones broke.",
            "{name} is a doctor, and is currently aiding one of the patients who has fractured a few bones in an accident."
        ])

        factor = 1
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} bones could be in the perfect state.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "How many hours could {name} takes to study all the bones of the human body?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def dimes(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "dimes"
    knowledge = "10 dimes make 1 dollar"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is collecting only dimes. He could not manage to collect {given_value} dollars from these dimes.",
            "{name} many dimes in his wallet and he accidentally fell his wallet on the street. Because of traffic, he was not able to collect {given_value} dollars from these dimes."
        ])

        factor = 10
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could have collected {hyp_value} dimes.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many dimes could {name} have collected?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def dimes2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "quarter"
    knowledge = "1 dime is 10 cents"

    given_value_start = 5
    given_value_end = 15

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} found {given_value} dimes and a few cents in his piggy bank.",
            "While walking on the street, {name} found {given_value} dimes and a few cents lying on the curb."
        ])

        factor = 10
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could have found coins worth {hyp_value} cents.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "What worth of coins could {name} have found?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def quarter(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "quarter"
    knowledge = "4 quarters make 1 dollar"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is collecting only quarters. He could not manage to collect {given_value} dollars from these quarters.",
            "{name} is collecting donation for underprivileged students. He only accepts quarters in the donation and failed to collect {given_value} dollars."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could have collected {hyp_value} quarters.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many quarters could {name} have collected?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def quarter2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "quarter"
    knowledge = "1 quarter is 25 cents"

    given_value_start = 5
    given_value_end = 15

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} found {given_value} quarters and a few cents in his piggy bank.",
            "While walking on the street, {name} found {given_value} quarters and a few cents lying on the curb."

        ])

        factor = 25
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could have found coins worth {hyp_value} cents.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "What worth of coins could {name} have found?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cards(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "cards"
    knowledge = "In a deck of cards, there are 52 cards"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought {given_value} decks of cards and started tearing them.",
            "While playing with friends, {name} got angry tore cards from {given_value} decks."
        ])

        factor = 52
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could tear {hyp_value} cards in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many cards could {name} tear?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
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


def cards2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "cards"
    knowledge = "In a deck of cards, there are 26 black cards and 26 red cards"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought {given_value} decks of cards and started tearing all the red cards.",
            "{name} bought {given_value} decks of cards and started tearing all the black cards.",
        ])

        factor = 26
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could tear {hyp_value} cards in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many cards could {name} tear?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
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


def cards3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "cards"
    knowledge = "In a deck of cards, there are 12 face cards"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought {given_value} decks of cards and started tearing all the face cards.",
            "While playing with friends, {name} got angry tore all the face cards from {given_value} decks."

        ])

        factor = 12
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could tear {hyp_value} cards in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many cards could {name} tear?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
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


def cards4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "cards"
    knowledge = "In a deck of cards, there are 6 black face cards and 6 red face cards"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought {given_value} decks of cards and started tearing all the red face cards.",
            "{name} bought {given_value} decks of cards and started tearing all the black face cards.",
        ])

        factor = 6
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could tear {hyp_value} cards in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many cards could {name} tear?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
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


def cards5(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "cards"
    knowledge = "In a deck of cards, there are 52 cards"

    given_value_start = 52
    given_value_end = 53

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friends played a card game. At the end of the game, {name} had majority of the cards.",
            "{name} is playing a card game with his friend in which who has the highest number of cards wins. {name} won against his friend in this game."
        ])

        factor = 1
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could be having {hyp_value} cards.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many cards could he be having?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def cards6(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "cards"
    knowledge = "In a deck of cards, there are 52 cards"

    given_value_start = 2
    given_value_end = 4

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought {given_value} decks of cards but lost a few cards from all the decks",
            "While cleaning the room, {name} found that he lost few cards from all his {given_value} decks."
        ])

        factor = 52
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could be having {hyp_value} cards in total now.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "How many cards could he be having now?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cards7(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "cards"
    knowledge = "In a deck of cards, there are 52 cards"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought {given_value} decks of cards and stole a few cards from his friend's collection",
            "{name} went to shop to buy {given_value} card decks. The shopkeeper misheard and gave him card decks more than what he asked for."
        ])

        factor = 52
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could be having {hyp_value} cards in total now.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "How many cards could he be having now?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cards8(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "cards"
    knowledge = "In a deck of cards, there are 52 cards out of which 12 are face cards"

    given_value_start = 48
    given_value_end = 49

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} had a deck of cards. On his last trip to Vegas, he lost all the face cards and a few other cards.",
            "{name}'s friend borrowed his deck of cards. When returned, {name} found out that there are no face cards and few other cards were missing from the deck."
        ])

        factor = 1
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could be having {hyp_value} cards in total now.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "How many cards could he be having now?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cards9(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "cards"
    knowledge = "In a deck of cards, there are 52 cards out of which 26 are black"

    given_value_start = 26
    given_value_end = 27

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} had a deck of cards. On his last trip to Vegas, he lost all the black cards and a few other cards.",
            "{name} had a deck of cards. On his last trip to Vegas, he lost all the red cards and a few other cards.",
        ])

        factor = 1
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could be having {hyp_value} cards in total now.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "How many cards could he be having now?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def continents(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "continents"
    knowledge = "There are 7 continents in the world"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an Asian and visited all the other continents at least {given_value} times in the last 5 years.",
            "{name} and his wife are Asian. They travel to all the other continents every year. It has been at least {given_value} years since they started traveling."
        ])

        factor = 6
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could have travelled {hyp_value} times",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many trips in total {name} could have made?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def continents2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "continents"
    knowledge = "There are 7 continents in the world"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has written at least {given_value} research articles on each continent of the world.",
            "{name} is a news reporter and writes international articles. He has written at least {given_value} news articles on each continent."
        ])

        factor = 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "He could have written {hyp_value} articles in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many articles {name} could have written in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def continents3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "continents"
    knowledge = "There are 7 continents in the world"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A funding organization is allocating at least {given_value} million dollars for each continent for healthcare.",
            "During COVID-19 pandemic, a healthcare organization helped all continent by funding at least {given_value} million dollars."
        ])

        factor = 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The organization's budget could be {hyp_value} million dollars in total.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the budget of the organization in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def continents4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "continents"
    knowledge = "There are 7 continents in the world"

    given_value_start = 6
    given_value_end = 7

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an Asian and is planning to visit all the other continents in the next 5 years.",
            "{name} is an Asian and a news reporter. He decided to visit all the other continents for his research. He planned this research to be complete in the next 5 years."
        ])

        factor = 1
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "After 2 years, {name} could visit {hyp_value} continents excluding Asia.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many continents (excluding Asia) he could visit after 2 years?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=3,
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


def bunch(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "bunch"
    knowledge = "A bunch has 12 items"

    given_value_start = 1
    given_value_end = 2

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a bunch of bananas and ate a few.",
            "{name} have a bunch of bananas and he gave some of them to his friend Tom."
        ])

        factor = 12
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be left with {hyp_value} bananas.",
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
            "How many bananas are left with {name}?",

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


def legs(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "legs"
    knowledge = "A human usually has 2 legs"

    given_value_start = 20
    given_value_end = 40

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Everyone takes off their shoes outside the temple. There were at least {given_value} shoes",
            "Today {name} went to temple with his father for the first time. He noticed people leave their shoes outside the temple. And there were at least {given_value} shoes outside the temple."
        ])

        factor = 0.5
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "In total, there could be {hyp_value} people in the temple.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many people could be there in the temple in total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def time(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "time"
    knowledge = "There are 60 minutes in an hour"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has an exam tomorrow. He studied for {given_value} hours and a few minutes.",
            "{name} is preparing for his mathematics exam. He has been studying for {given_value} hours and a few minutes to complete the syllabus."
        ])

        factor = 60
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "In total, he could have studied for {hyp_value} minutes.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "For how many minutes {name} could have studied?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def days_in_week5(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "days_in_week"
    knowledge = "There are 7 days in a week"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} played computer games for at least {given_value} hours daily for a week",
            "{name} is training for his soccer match. He has been playing soccer for at least {given_value} hours daily for a week now."
        ])

        factor = 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "In that week, he could have played for {hyp_value} hours.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "For how many hours {name} could have played in the entire week?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
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


def days_in_month(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "days_in_month"
    knowledge = "There are 31 days in January"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} played computer games for at least {given_value} hours daily in the month of January.",
            "{name} is training for his soccer match. He has been playing soccer for at least {given_value} hours daily in January."

        ])

        factor = 31
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "In January, he could have played for {hyp_value} hours.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "For how many hours {name} could have played in the entire month of January?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
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


def days_in_month2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "days_in_month"
    knowledge = "There are 30 days in April"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} played computer games for at least {given_value} hours daily in the month of April.",
            "{name} is training for his soccer match. He has been playing soccer for at least {given_value} hours daily in April."

        ])

        factor = 30
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "In April, he could have played for {hyp_value} hours.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "For how many hours {name} could have played in the entire month of April?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
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

# RECHECK


def dice5(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "dice"
    knowledge = "Values in a regular dice range from 1 to 6"

    given_value_start = 2
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} rolled {given_value} regular dice and calculated the sum on all dice.",
            "{name} rolled {given_value} regular dice and calculated the sum on all dice.",
        ])

        factor = 6
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could get {hyp_value}.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could have been his total?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def century(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "century"
    knowledge = "A century has 100 years"

    given_value_start = 20
    given_value_end = 60

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The price of a property in increasing by at least {given_value} dollars every year.",
            "The price of a property in decreasing by at least {given_value} dollars every year.",
        ])

        factor = 100
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The price could have changed by {hyp_value} dollars after a century.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=500,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=50,
            scale=1
        )

        question_template = random.choice([
            "By how much the price could have changed after a century?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=500,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=50,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def alphabet(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "alphabet"
    knowledge = "English alphabet has 26 letters"

    given_value_start = 4
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is preparing for GRE. He plans to spend no more than {given_value} hours reading words for each letter.",
            "{name} is preparing for CAT and plans to spend no more than {given_value} hours reading words for each letter.",
        ])

        factor = 26
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could finish his preparation in {hyp_value} hours if he sticks to his plan.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "In how many hours can {name} finish his preparation if he sticks to his plan?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def alphabet2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "alphabet"
    knowledge = "English alphabet has 26 letters"

    given_value_start = 4
    given_value_end = 10

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A baby is learning to write. He takes at least {given_value} minutes to master writing a letter.",
            "A baby is learning to write and takes at least {given_value} minutes to write a letter.",
        ])

        factor = 26
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The baby can master all the letter of the english alphabet in {hyp_value} minutes.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=10,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "In how many minutes can the baby master all the letters?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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

##########################################################################################################


def alphabet3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "alphabet"
    knowledge = "English alphabet has 26 letters"

    given_value_start = 20
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A school has a section corresponding to each letter of the english alphabet. Each section has {given_value} students. A few more students will join the school tomorrow.",
            "A school has a section corresponding to each letter of the english alphabet. Each section has {given_value} students. A few more students will join the school tomorrow.",
        ])

        factor = 26
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The strength of the school tomorrow could be {hyp_value} students.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "What could be the strength of the school tomorrow?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def alphabet4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "alphabet"
    knowledge = "English alphabet has 26 letters"

    given_value_start = 20
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A school has a section corresponding to each letter of the english alphabet. Each section has {given_value} students. A few more students will leave the school tomorrow.",
            "A school has a section corresponding to each letter of the english alphabet. Each section has {given_value} students. A few more students will leave the school tomorrow.",
        ])

        factor = 26
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The strength of the school tomorrow could be {hyp_value} students.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )

        question_template = random.choice([
            "What could be the strength of the school tomorrow?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=20,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=4
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def alphabet5(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "alphabet"
    knowledge = "English alphabet has 26 letters"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A school has a section corresponding to each letter of the english alphabet. Each section has {given_value} students. At least one student will join each group tomorrow",
            "A school has a section corresponding to each letter of the english alphabet. Each section has {given_value} students. At least one student will join each group tomorrow",
        ])

        factor = 26
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The strength of the school tomorrow could be {hyp_value} students.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=52,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=26
        )

        question_template = random.choice([
            "What could be the strength of the school tomorrow?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=52,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=26
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def alphabet6(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "alphabet"
    knowledge = "English alphabet has 26 letters"

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A school has a section corresponding to each letter of the english alphabet. Each section has {given_value} students. At least one student will leave each group tomorrow",
            "A school has a section corresponding to each letter of the english alphabet. Each section has {given_value} students. At least one student will leave each group tomorrow",
        ])

        factor = 26
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The strength of the school tomorrow could be {hyp_value} students.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=52,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=26
        )

        question_template = random.choice([
            "What could be the strength of the school tomorrow?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=52,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=26
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def alphabet7(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "alphabet"
    knowledge = "English alphabet has 5 vowels"

    given_value_start = 5
    given_value_end = 6

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Teacher asked the students to write words in which each vowel appears at least once.",
            "Teacher asked the students to write words in which each vowel appears at least once.",
        ])

        factor = 1
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "One such word could be of length {hyp_value} characters.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=4,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the length of one such word?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=4,
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


def soccer(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "soccer"
    knowledge = "There are 11 players in a team of soccer"

    given_value_start = 11
    given_value_end = 12

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A new jersey was sent to the players of a soccer team. Some of them did not get the jersey.",
            "A new jersey was sent to the players of a soccer team. Some of them did not get the jersey.",
        ])

        factor = 1
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} players could have received the jersey.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=4,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many players could have received the jersey?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def soccer2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "soccer"
    knowledge = "There are 11 players in a team of soccer and a game has 2 teams"

    given_value_start = 11
    given_value_end = 12

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A new jersey was sent to the players of both teams of a soccer game. Some of them did not get the jersey.",
            "A new jersey was sent to the players of both teams of a soccer game. Some of them did not get the jersey.",
        ])

        factor = 2
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} players could have received the jersey.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=4,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many players could have received the jersey?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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


def days_in_week6(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "days_in_week"
    knowledge = "A week has 7 days"

    given_value_start = 2
    given_value_end = 5

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A Spain soccer player scored at least {given_value} goals in every match. He played a match every day for a week.",
            "A Spain soccer player scored at least {given_value} goals in every match. He played a match every day for a week.",
        ])

        factor = 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have scored a total of {hyp_value} goals in that week.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many goals {name} could have scored in that week?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
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

#     template_binary_instances, template_mcq_instances = days_in_week6(
#         repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances

#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
