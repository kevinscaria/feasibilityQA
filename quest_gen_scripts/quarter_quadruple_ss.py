import util
import random
import pprint
import numpy as np


def quarter1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "quarter"
    knowledge = "Quarter means one by four"

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and spent more than quarter of this amount buying burgers.",
            "{name} borrowed {given_value} dollars from his friend to buy some food. He spent more than a quarter of this amount to buy burgers."
        ])

        factor = 0.25
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have spent {hyp_value} dollars on burgers",
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
            "How many dollars {name} could have spent on burgers ?",

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


def quarter2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "quarter"
    knowledge = "Quarter means one by four"

    given_value_start = 20
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and spent more than quarter of this amount buying burgers.",
            "{name} borrowed {given_value} dollars from his friend to buy some food. He spent more than a quarter of this amount to buy burgers."

        ])

        factor = 0.25
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be left with {hyp_value} dollars after spending on burgers.",
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
            "How many dollars could be left with {name} after spending on burgers?",

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


def quarter3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "Quarter"
    knowledge = "Quarter means one by four"

    given_value_start = 10
    given_value_end = 30

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} ate {given_value} chocolates and his brother then ate more than quarter of this amount of chocolate.",
            "{name}'s father brought {given_value} chocolates from the shop. {name}'s brother ate more than a quarter of the chocolates brought by his father. "
        ])

        factor = 0.25
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name}'s brother could have eaten {hyp_value} chocolates.",
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
            "How many chocolates {name}'s brother could have eaten ?",

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


def percent1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "percent"
    knowledge = "25% means quarter"

    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and spent more than 25% of this amount buying burgers.",
            "{name} borrowed {given_value} dollars from his friend to buy some food. He spent more than 25% of this amount to buy burgers."

        ])

        factor = 0.25
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have spent {hyp_value} dollars on burgers",
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
            "How many dollars {name} could have spent on burgers ?",

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
    knowledge = "25% percent means quarter"

    given_value_start = 10
    given_value_end = 50

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and spent more than 25% of this amount buying burgers.",
            "{name} borrowed {given_value} dollars from his friend to buy some food. He spent more than 25% of this amount to buy burgers."

        ])

        factor = 0.25
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be left with {hyp_value} dollars after spending on burgers.",
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
            "How many dollars could be left with {name} after spending on burgers?",

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


def quadruple1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "quadruple"
    knowledge = "Quadruple means four times"

    given_value_start = 1
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} burgers and bought french fries more than quadruple of this amount.",
            "{name} had ordered {given_value} pizzas. And he bought french fries more than quadruple amount of pizzas that were delivered before."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have {hyp_value} french fries.",
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
            "How many french fries {name} could have bought ?",

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


def quadruple2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "quadruple"
    knowledge = "Quadruple means four times"

    given_value_start = 5
    given_value_end = 20

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and spent more than quadruple of this amount buying burgers after borrowing some money from his friend.",
            "{name} spent {given_value} on buying chocolates and spent more than quadruple of this amount buying burgers."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have spent {hyp_value} dollars on burgers.",
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
            "How many dollars {name} could have spent on burgers ?",

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


def quadruple3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "quadruple"
    knowledge = "Quadruple means four times"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} have {given_value} chocolates and {name}'s sister bought more than quadruple of these chocolates.",
            "Since {name} was not happy with {given_value} chocolates, his sister bought more than quadruple of these chocolates."
        ])

        factor = 4
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name}'s sister could have bought {hyp_value} of chocolates.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=2,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many chocolates {name}'s sister could have bought?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=2,
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


def triple1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "triple"
    knowledge = "Triple means three times"

    given_value_start = 1
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} pens and bought pencils more than triple of this amount.",
            "{name} had {given_value} pens. Because of bad quality of ink, {name} went shopping and bought pencils more than the triple amount of pen he had earlier."
        ])

        factor = 3
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have {hyp_value} pencils.",
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
            "How many pencils {name} could have bought ?",

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


def triple2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "triple"
    knowledge = "Triple means three times"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and spent more than triple of this amount buying pens after borrowing more money from his friend.",
            "{name} recently started his graduate program at ASU. He already spent {given_value} dollars buying pencils. To be prepared he bought pens and spent more than the triple amount of dollars he spent to buy pencils."

        ])

        factor = 3
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have spent {hyp_value} dollars on pens.",
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
            "How many dollars {name} could have spent on pens ?",

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


def triple3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "implicit_numerical_knowledge", "triple"
    knowledge = "triple means three times"

    given_value_start = 2
    given_value_end = 10

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} have {given_value} chocolates and {name}'s sister bought more than triple of these chocolates.",
            "Since {name} was not happy with {given_value} chocolates, his sister bought more than triple of these chocolates."
        ])

        factor = 3
        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.choice(
            [i for i in range(given_value_start, given_value_end, 2)])
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name}'s sister could have bought {hyp_value} chocolates.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            int(given_value*factor),
            diff=2,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many chocolates {name}'s sister could have bought?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=int(given_value * factor),
            diff=2,
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
#     repetition_count = 1
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = triple2(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
