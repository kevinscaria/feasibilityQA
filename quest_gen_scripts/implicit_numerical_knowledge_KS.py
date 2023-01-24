import util
import random
import pprint
import numpy as np


def geometry1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "circumference_and_radius"
    knowledge = "Circumference of a circle is 44/7 times the radius of the circle."

    given_value_start = 15
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has his final exams today. In the maths paper, it was told the radius of a circle is {given_value} units.",
            "In the mathematics exam, one of the questions that was present in {name}'s paper was from geomery. It was given that the radius of a circle is {given_value} units.",
        ])

        factor = 44 / 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "In {name}'s test, the circumference of the circle could have been {hyp_value} units."
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value * factor),
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could have been the circumference of the circle that was mentioned in {name}'s test?"
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


def geometry2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "circumference_and_radius"
    knowledge = "Diameter of a circle is 7/22 times the circumference of the circle."

    given_value_start = 15
    given_value_end = 30

    for i in range(repetition_count):
        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has his maths paper today. In one of the questions, it was told the circumference of a circle is {given_value} units.",
            "In the mathematics exam, one of the questions that was present in {name}'s paper was from geomery. It was given that the circumference of a circle is {given_value} units.",
        ])

        factor = 22 / 7
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "In {name}'s test, the diameter of the circle could have been {hyp_value} units."
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value / factor),
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could have been the diameter of the circle that was mentioned in {name}'s test?"
        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value / factor),
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


def man_hours1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "man_hours"
    knowledge = "An employee works for 8 hours per day."

    given_value_start = 20
    given_value_end = 25

    for i in range(repetition_count):
        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a developer and he works for {given_value} days every month.",
            "As part of his job, {name} works for {given_value} days every month.",
        ])

        factor = 8
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The number of hours {name} works could be {hyp_value} hours in a month."
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value * factor),
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could have been the number of hours that {name} works in a month?"
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


def man_hours2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "circumference_and_radius"
    knowledge = "There are four sides in a square."

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):
        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a mason and it takes {given_value} hours to fence a side of a square plot.",
            "To fence the side of a square plot, {name} the mason took {given_value} hours to finish the job."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The number of hours {name} could take {hyp_value} to complete fencing the square plot."
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value * factor),
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could have been the number of hours that {name} works in a month?"
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


def man_hours3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "circumference_and_radius"
    knowledge = "It takes 28 days to cure concrete cube."

    given_value_start = 10
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a builder and has to cure {given_value} concrete cubes.",
            "The builder {name} has to cure {given_value} concrete cubes."
        ])

        factor = 28
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "If at a time only one concrete cube can be cured, {name} could take {hyp_value} days to complete curing."
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value * factor),
            diff=5,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could have been the number of days that {name} could need to complete curing if at a time only one concrete cube can be cured?"
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


def teeth(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numericalSG", "teeth"
    knowledge = "A normal adult has approx 32 teeth."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to the dentist for a regular check up. The dentist told him that 30 of his teeth are fine, rest of them have cavity in it.",
            "{name} went to the dentist where the dentist told him that 30 teeth are fine and there was plaque in the rest."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have cavity in 2 teeth.",
        ]

        false_hypotheses = [
            "He could have cavity in 6 teeth.",
        ]

        binary_instances += util.direct_create_data_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            true_hypotheses,
            false_hypotheses,
        )

        question_template = random.choice([
            "What could be the number of teeth he has cavity in?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=[50, 4, 6, 2],
            answers_list=[3],
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

#     template_binary_instances, template_mcq_instances = man_hours3(
#         repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances

#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
