import util
import random
import pprint
import numpy as np


def integers_and_whole_numbers(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "integers_and_whole_numbers"
    knowledge = "whole numbers are either positive or zero and integers can be positive negative or zero."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a kindergarten student and his test is to identify the type of numbers written in his notebook. The number present in front of him is a negative number.",
            "{name} wants to identify the type of numbers written in his notebook. The number in front of him is a negative number."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The number could be an integer.",
        ]

        false_hypotheses = [
            "The number could a whole number.",
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
            "What could be the type of the numeral?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["integer", "natural number",
                          "whole number", "none of these"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def natural_and_whole_numbers(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "natural_and_whole_numbers"
    knowledge = "Whole numbers are either positive or zero and natural numbers are only positive."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a kindergarten student and his test is to identify the type of numbers written in his notebook. The number present in front of him is zero.",
            "{name}'s test is to identify the type of numbers written in his notebook. The number in front of him is zero."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The number could be a whole number.",
        ]

        false_hypotheses = [
            "The number could be a natural number.",
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
            "What could be the type of the numeral?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["integer", "natural number",
                          "whole number", "none of these"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def rational_and_irrational_numbers1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "rational_and_irrational_numbers"
    knowledge = "Any number that can be represented in the form of a fraction is a rational number. Irrational numbers like square root of 2,3 or pi are non recurring and non repeating decimals."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a middle school student and learning about how to calculate perimeter of a circle. He identified the number pi in the formula.",
            "{name} identified the number pi while calculating perimeter of a circle."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The number could an irrational number.",
        ]

        false_hypotheses = [
            "The number could be a rational number.",
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
            "What could be the type of the numeral ?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["irrational number", "natural number",
                          "whole number", "none of these"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def rational_and_irrational_numbers2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "rational_and_irrational_numbers2"
    knowledge = "Any number that can be represented in the form of a fraction is a rational number. Irrational numbers like square root of 2,3 or pi are non recurring and non repeating decimals."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is learning about how to calculate perimeter of a circle. He wanted to use the value of pi but the teacher told him to use quotient of 22 divided by 7. He named its quotient to be approximate pi.",
            "{name} wanted to use the value of pi for calculating area of a circle but the teacher told him to use quotient of 22 divided by 7. He named its quotient to be approximate pi."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "Approximate pi could be a rational number.",
        ]

        false_hypotheses = [
            "Approximate pi could be an irrational number.",
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
            "What could be the type of the numeral?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["irrational number", "rational number",
                          "whole number", "none of these"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def real_and_imaginary_numbers(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "real_and_imaginary_numbers"
    knowledge = "Any number that can be represented on the real number line is a real number. Some number like square root of -1 cannot be represented on the number line and are called imaginary numbers."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is curious math student and learning about number line. He asked his teacher where he can mark the square root of -2 in the line. The teacher answered that the number cannot be represented on the real number line. ",
            "{name} asked his teacher where he can mark the square root of -2 in the line. The teacher answered that the it cannot be represented on the real number line. "
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "Approximate pi could be a rational number.",
        ]

        false_hypotheses = [
            "Approximate pi could be an irrational number.",
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
            "What could be the type of the numeral?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["irrational number", "rational number",
                          "whole number", "none of these"],
            answers_list=[1],
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
#     template_binary_instances, template_mcq_instances = flying_objects(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
