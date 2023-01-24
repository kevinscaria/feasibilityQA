import util
import random
import pprint
import numpy as np


def height_with_time(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "change_with_time", "height"
    knowledge = "Height does not decrease with time"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s height is {given_value} inches today.",
            "{name}  went to clinic today, where he was asked to meausre hise height. So his height was {given_value} inches.",
            "Today {name} is {given_value} inches tall.",
            "{name} went to his physician for general checkup today, and got his height checked. It was {given_value} inches."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(15, 30)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} could have been {hyp_value} inches tall last year.",
            "{name} could have been {hyp_value} inches tall on his last birthday.",

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
            "What could have been {name}'s height last year ?",

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


def height_with_time2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "change_with_time", "height"
    knowledge = "Height does not decrease with time"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s height is {given_value} inches today.",
            "{name}  went to clinic today, where he was asked to meausre hise height. So his height was {given_value} inches.",
            "Today {name} is {given_value} inches tall.",
            "{name} went to his physician for general checkup today, and got his height checked. It was {given_value} inches."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(15, 30)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 3
        hypothesis_template = random.choice([
            "{name} could be {hyp_value} inches tall next year."
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
            "What could be {name}'s height next year ?",

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


def height_with_time3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "change_with_time", "height"
    knowledge = "Height does not decrease with time"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s height is {given_value} inches today.",
            "{name}  went to clinic today, where he was asked to meausre hise height. So his height was {given_value} inches.",
            "Today {name} is {given_value} inches tall.",
            "{name} went to his physician for general checkup today, and got his height checked. It was {given_value} inches."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(15, 30)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} could have been {hyp_value} inches tall last year.",
            "{name} could have been {hyp_value} inches tall on his last birthday.",

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
            "What could have been {name}'s height last year ?",

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


def height_with_time4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "change_with_time", "height"
    knowledge = "Height does not decrease with time"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s height is {given_value} inches today.",
            "{name}  went to clinic today, where he was asked to meausre hise height. So his height was {given_value} inches.",
            "Today {name} is {given_value} inches tall.",
            "{name} went to his physician for general checkup today, and got his height checked. It was {given_value} inches."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(15, 30)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 3
        hypothesis_template = random.choice([
            "{name} could be {hyp_value} inches tall next year."
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
            "What could be {name}'s height next year ?",

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


def price_with_time(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 300
    given_value_end = 800

    category, subcategory = "change_with_time", "price"
    knowledge = "Selling price of an object decreases with time"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a phone at a price of {given_value} dollars last year.",
            "There was a sale on mobile phones last year. {name} went to buy a phone from that sale last year which costed him {given_value} dollars."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} can possibly sell that used phone at a price of {hyp_value} dollars next year.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=250,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=50,
            scale=1
        )

        question_template = random.choice([
            "At what price {name} can possibly sell the used phone next year?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=250,
            more_is_correct_flag=False,
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


# if __name__ == "__main__":
#     repetition_count = 1
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = price_with_time(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
