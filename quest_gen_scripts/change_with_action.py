import util
import random
import pprint
import numpy as np


def selling(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 500

    category, subcategory = "change_with_action", "selling"
    knowledge = "Selling something reduces its quantity"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} organized a garage sale yesterday. {name} sold a total of {given_value} items at a minimum price of 1 USD each.",
            "{name} organized a sale and sold a total of {given_value} items at a minimum price of 1 USD each.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} could have made {hyp_value} money in the garage sale.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=40,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )

        question_template = random.choice([
            "How much money {name} could have made from the garage sale?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=40,
            more_is_correct_flag=True,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def selling2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 500

    category, subcategory = "change_with_action", "selling"
    knowledge = "Selling something reduces its quantity"

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} organized a garage sale yesterday. {name} sold a total of {given_value} items at a maximum price of 1 USD each.",
            "{name} organized a sale and sold a total of {given_value} items at a maximum price of 1 USD each.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have made {hyp_value} money in the garage sale.",

        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=40,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )

        question_template = random.choice([
            "How much money {name} could have made from the garage sale?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=40,
            more_is_correct_flag=False,
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def selling3(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 300
    given_value_end = 800

    category, subcategory = "change_with_action", "selling"
    knowledge = "Selling price of an object decreases if its broken"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a phone at a price of {given_value} dollars and it fell on the ground breaking its screen.",
            "{name} purchased a phone for {given_value} dollars and its screen broke as it fell on the ground.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "{name} can possibly sell that phone at a price of {hyp_value} dollars.",

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
            "At what price {name} can possibly sell the broken phone?",

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


def selling4(repetition_count):
    binary_instances = []
    mcq_instances = []

    given_value_start = 300
    given_value_end = 800

    category, subcategory = "change_with_action", "selling"
    knowledge = "Selling price of an object decreases if discount is given"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a phone at a discounted price of {given_value} dollars.",
            "{name} purchased a phone for {given_value} dollars. The phone price was discounted.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The original price of the phone could be {hyp_value} dollars.",

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
            round_to=25,
            scale=1
        )

        question_template = random.choice([
            "What could have been the original price of that phone?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=100,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=25,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def selling5(repetition_count):
    binary_instances = []
    mcq_instances = []

    given_value_start = 300
    given_value_end = 800

    category, subcategory = "change_with_action", "selling"
    knowledge = "Selling price of an object decreases if discount is given"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a phone at a discounted price of {given_value} dollars.",
            "{name} purchased a phone for {given_value} dollars. The phone price was discounted.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The original price of the phone could be {hyp_value} dollars.",

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
            round_to=25,
            scale=1
        )

        question_template = random.choice([
            "What could have been the original price of that phone?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=100,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=25,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def selling6(repetition_count):
    binary_instances = []
    mcq_instances = []

    given_value_start = 300
    given_value_end = 800

    category, subcategory = "change_with_action", "selling"
    knowledge = "Selling price of an object decreases if discount is given"

    for i in range(repetition_count):
        # *******Template 2

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a phone at a discounted price. The phone's price before discount was {given_value} dollars.",
            "There is a phone whose price before discount was {given_value} dollars. {name} brought that phone in a sale.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        # ----Scenario 1
        hypothesis_template = random.choice([
            "The discounted price of the phone could be {hyp_value} dollars.",

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
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=25,
            scale=1
        )

        question_template = random.choice([
            "What could be the discounted price of that phone?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=70,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=25,
            scale=1
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def profit_loss(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 300

    category, subcategory = "change_with_action", "profit_loss"
    knowledge = "For making profit the selling price need to be higher than cost price"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a mobile manufacturer. His cost price of making a mobile is {given_value} dollars.",
            "{name} is a mobile manufacturer and manufactures mobiles by {given_value} dollars per unit.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "If he wants to make a profit then he can sell the mobile at {hyp_value} dollars.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=50,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )

        question_template = random.choice([
            "At what price can {name} sell a mobile in order to make profit?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
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


def profit_loss2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 100
    given_value_end = 300

    category, subcategory = "change_with_action", "profit_loss"
    knowledge = "For making loss the selling price need to be lower than cost price"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a mobile manufacturer. His cost price of making a mobile is {given_value} dollars.",
            "{name} is a mobile manufacturer and manufactures mobiles by {given_value} dollars per unit."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "If he makes a loss then he could be selling the mobile at {hyp_value} dollars.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=50,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )

        question_template = random.choice([
            "At what price could {name} be selling a mobile if he is making a loss?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
            more_is_correct_flag=False,
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


def adding_components(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    category, subcategory = "change_with_action", "adding_components"
    knowledge = "Adding components increases the weight of the whole"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has a bag with weight of {given_value} units. {name} adds a ball to this bag.",
            "{name} is carrying a bag whose weight is {given_value} units. {name} adds a ball to this bag.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The weight of the bag could be {hyp_value} units now.",
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
            "What could be the weight of the bag now?",

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


def adding_components2(repetition_count):
    binary_instances = []
    mcq_instances = []

    # Template 2
    given_value_start = 100
    given_value_end = 200

    category, subcategory = "change_with_action", "adding_components"
    knowledge = "Adding components increases the electricity bill"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Last month {name}'s electricity consumption was {given_value} units. This month {name} has installed 2 air conditioners.",
            "{name}'s electricity consumption was {given_value} units for last month. This month {name} has installed 2 air conditioners.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name}'s electricity consumption this month could be {hyp_value} units.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=50,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=10,
            scale=10
        )

        question_template = random.choice([
            "What could be {name}'s electricity consumption this month?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=10,
            scale=10
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def removing_components(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    category, subcategory = "change_with_action", "removing_components"
    knowledge = "Removing something decreases the weight of the whole"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has a bag with weight of {given_value} units. {name} removes a ball from this bag.",
            "{name} is carrying a bag whose weight is {given_value} units. {name} removes a ball to this bag.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The weight of the bag could be {hyp_value} units now.",
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
            "What could be the weight of the bag now?",

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


def temperature_change(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 30

    category, subcategory = "change_with_action", "temperature_change"
    knowledge = "On turning on the heater temperature increases"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Temperature of the room is {given_value} units. {name} turned on the heater.",
            "Temperature of the room was {given_value} units before turning on the heater."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The temperature after an hour could be {hyp_value} units.",
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
            "What could be the temperature after an hour?",

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


def temperature_change2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 12
    given_value_end = 30

    # Template 2
    category, subcategory = "change_with_action", "temperature_change"
    knowledge = "On turning on the cooler temperature decreases"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Temperature of the room is {given_value} units. {name} turned on the cooler.",
            "Temperature of the room was {given_value} units before turning on AC."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The temperature after an hour could be {hyp_value} units.",
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
            "What could be the temperature after an hour?",

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


def broken_components(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 20

    category, subcategory = "change_with_action", "broken_components"
    knowledge = "If some items break then lesser number of unbroken items are left"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was bringing {given_value} eggs from the supermarket. He dropped his bag and a few eggs broke.",
            "{name} went to the market and brought {given_value} eggs. He dropped his bag and a few eggs broke."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} unbroken eggs could be remaining in his bag.",
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
            "How many unbroken eggs could be remaining in his bag?",

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


def broken_components2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 20

    # Template 2
    category, subcategory = "change_with_action", "broken_components"
    knowledge = "If some items break then lesser number of unbroken items are left"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} installed {given_value} bulbs in the room. After an year, some of them stopped working.",
            "{name} had {given_value} bulbs in his room and after a few months, some of them stopped working.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Now, {hyp_value} bulbs can be in a working condition.",
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
            scale=2
        )

        question_template = random.choice([
            "How many bulbs can be in a working condition now?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=5,
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


def marks(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 90

    category, subcategory = "change_with_action", "marks"
    knowledge = "For getting full marks in an exam, you meed to answer all the questions correctly"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a student and appeared for an exam. The exam was of {given_value} marks. He answered a few questions incorrectly.",
            "{name} appeared for an exam that was of {given_value} marks. He answered a few questions incorrectly.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} can get {hyp_value} marks.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How marks he can possibly get?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def marks_2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "marks"
    knowledge = "One can get marks only for the questions they attempted"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} attempted questions of {given_value} marks only in an exam of 100 marks.",
            "{name} appeared in an exam of 100 marks and attempted questions for {given_value} marks.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} can get {hyp_value} marks.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many marks he can possibly get?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def marks_3(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "marks"
    knowledge = "Highest marks are the maximum marks among all students"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In {name}'s class, the highest marks are {given_value}.",
            "In {name}'s class, the maximum marks are {given_value}.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have scored {hyp_value} marks.",
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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many marks {name} could have scored?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def marks_4(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 60

    category, subcategory = "change_with_action", "marks"
    knowledge = "Lowest marks are the minimum marks among all students"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In {name}'s class, the lowest marks are {given_value}.",
            "In {name}'s class, the least marks are {given_value}.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could have scored {hyp_value} marks.",
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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many marks {name} could have scored?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def family_size(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 10

    category, subcategory = "change_with_action", "family_size"
    knowledge = "A family consists of gents, ladies, and kids"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A family has {given_value} gents and a few ladies.",
            "A family has a few ladies and {given_value} gents."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The size of this family could be {hyp_value}.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "What could be the size of this family?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def balance(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 10

    category, subcategory = "change_with_action", "balance"
    knowledge = "After spending one is left with lesser money"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} earns {given_value} thousand dollars and spends some money on his food and other essentials.",
            "{name} annual income is {given_value} thousand dollars and spends some money on his food and other essentials.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be left with {hyp_value} thousand dollars.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=2
        )

        question_template = random.choice([
            "What could be the amount of remaining money with {name}?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
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


def boys_and_girls(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "boys_and_girls"
    knowledge = "There will equal or less number of boys than the total number of students"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are {given_value} students in a class.",
            "The number of students in a class is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} boys in this class.",
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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many boys can be there in this class?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def boys_and_girls2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "boys_and_girls"
    knowledge = "There will equal or less number of girls than the total number of students"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are {given_value} students in a class.",
            "The number of students in a class is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} girls in this class.",
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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many girls can be there in this class?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def boys_and_girls3(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "boys_and_girls"
    knowledge = "There will equal or more number of students than the number of boys or girls"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are {given_value} boys in a class.",
            "There are {given_value} girls in a class.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} total students in this class.",
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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many total students can be there in this class?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def boys_and_girls4(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 50

    category, subcategory = "change_with_action", "boys_and_girls"
    knowledge = "Total number of students is sum of number of boys and girls"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are {given_value} boys in a class and a few girls.",
            "There are a few girls in a class and {given_value} boys."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} total students in this class.",
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
            scale=2
        )

        question_template = random.choice([
            "How many total students can be there in this class?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
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


def boys_and_girls5(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "boys_and_girls"
    knowledge = "Count of people would be less if some are absent"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are {given_value} students in a class and some of them are absent today.",
            "The strength of the class is {given_value} students and some of them are absent today."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} total students present in the class today.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many total students can be present in this class today?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def families(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "families"
    knowledge = "Number of poor families would be less than the total number of families"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are {given_value} families in a village and some of them are rich.",
            "There are some rich families in a village of {given_value} families."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} poor families in the village.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many poor families can be in the village?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def animals(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 15
    given_value_end = 50

    category, subcategory = "change_with_action", "animals"
    knowledge = "Total number of animals is sum of all types of animals"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{given_value} goats and a few cows are grazing in the field.",
            "Few cows and a {given_value} goats are grazing in the field."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} total animals in this field.",
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
            scale=2
        )

        question_template = random.choice([
            "How many total animals can be there in this field?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=10,
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


def subtraction(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "subtraction"
    knowledge = "Subtracting a positive number from a value results in a smaller value"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A positive number was subtracted from {given_value}.",
            "There is number {given_value} and a positive value is subtracted from it."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The result could be {hyp_value}.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the result?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def addition(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "addition"
    knowledge = "Adding a positive number from a value results in a larger value"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A positive number was added to {given_value}.",
            "There is number {given_value} and a positive value is added to it."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The result could be {hyp_value}.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the result?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def subtraction2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "subtraction"
    knowledge = "Subtracting a negative number from a value results in a larger value"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A negative number was subtracted from {given_value}.",
            "There is number {given_value} and a negative value is subtracted from it."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The result could be {hyp_value}.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the result?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def addition2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "addition"
    knowledge = "Adding a negative number from a value results in a smaller value"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A negative number was added to {given_value}.",
            "There is number {given_value} and a negative number is added to it."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The result could be {hyp_value}.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the result?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def addition3(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "addition"
    knowledge = "Adding a positive number from a value results in a larger value"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The sum of two positive numbers is {given_value}.",
            "{given_value} is the sum of two positive numbers.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "One of the numbers could be {hyp_value}.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be one of the numbers?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def buying(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "buying"
    knowledge = "If the shopkeeper returns some money then the bill would be less than the amount of money you gave to the shopkeeper"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} gave {given_value} dollars to the shopkeeper to buy a book. The shopkeeper returned some money to {name}.",
            "{name} went to a shop to buy a book and gave {given_value} dollars to him. The shopkeeper returned some money to {name}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The cost of book could be {hyp_value}.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the cost of the book?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def buying2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "buying"
    knowledge = "If the shopkeeper asks for more money then the bill would be more than the amount of money you initially gave to the shopkeeper"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} bought a book initially gave {given_value} to the shopkeeper. The shopkeeper asked for more money for the book.",
            "{name} went to a shop to buy a book and gave {given_value} dollars to him. The shopkeeper returned some money to {name}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The cost of book could be {hyp_value}.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the cost of the book?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def hunting(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 40

    category, subcategory = "change_with_action", "hunting"
    knowledge = "Hunting reduces the number of birds"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There were {given_value} birds on a tree. Hunters fired at them and killed some of them.",
            "There were {given_value} birds on a tree some of them were killed by a hunter."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "There could be {hyp_value} birds remaining.",
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
            "How many birds could be remaining?",

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


def breaking(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 40

    category, subcategory = "change_with_action", "breaking"
    knowledge = "Breaking an object reduces its length"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} had a rope of length {given_value} units. He broke that into multiple parts.",
            "{name} had a rope of length {given_value} units and he cut it into multiple parts."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Length of a part could be {hyp_value} units.",
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
            "What could be the length of a part?",

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


def breaking2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 40

    category, subcategory = "change_with_action", "breaking"
    knowledge = "Breaking an object reduces its length"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} had a rope and he broke that into multiple parts. Length of a part was {given_value} units.",
            "{name} had a rope of length {given_value} units and he cut it into multiple parts."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Length of whole rope could be {hyp_value} units.",
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
            "What could be the length of whole rope?",

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


def teaching(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 6
    given_value_end = 10

    category, subcategory = "change_with_action", "teaching"
    knowledge = "In a school that teacher multiple subjects, time devoted to one subject would be less than the time students spend in school"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} spends {given_value} hours in the school and studies multiple subjects.",
            "{name} studies multiple subjects and spends {given_value} hours in the school."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could spend {hyp_value} on studying Maths.",
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
            "How many hours can {name} spend in studying Maths?",

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


def teaching2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 6
    given_value_end = 10

    category, subcategory = "change_with_action", "teaching"
    knowledge = "In a school that teacher multiple subjects, time devoted to one subject would be less than the time students spend in school"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a week, {name} spends {given_value} hours in studying Maths and studies multiple subjects.",
            "{name} studies Maths and other subjects for a total of {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could spend {hyp_value} on studying in total.",
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
            "How many hours can {name} spend in studying in total?",

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


def passing(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 30
    given_value_end = 60

    category, subcategory = "change_with_action", "passing"
    knowledge = "Number of total students is more or equal than the number of passed students"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In an exam, {given_value} students passed while a few failed.",
            "In an exam, a few students failed while {given_value} students passed."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} students could have appeared for the exam.",
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
            "How many hours can {name} spend in studying in total?",

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


def moving_components(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    category, subcategory = "change_with_action", "moving_components"
    knowledge = "When things are transported, their initial quantity reduces"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A dock had {given_value} crates initially and then a few crates were transported to a ship.",
            "A dock had {given_value} crates and then some creates were shipped off.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The dock now has {hyp_value} crates.",
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
            "What could be the number of crates in the dock now?",

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


def moving_components2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    category, subcategory = "change_with_action", "moving_components"
    knowledge = "Number of items that can be moved is less than or equal to the total number of items present"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A dock in California has {given_value} crates and another dock in New York has 34 crates.",
            "A dock in New York has 34 crates and another dock in California has {given_value} crates."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} crates can be moved from the California dock.",
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
            equal_is_correct_flag=True,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How many crates can be moved the California dock?",

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


def moving_components3(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    category, subcategory = "change_with_action", "moving_components"
    knowledge = "When a few items are moved away the number of items that remain is less than the total number of items initially present"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A dock in California had {given_value} crates and a few crates have been transferred to the dock in New York.",
            "A dock in New York has 34 crates and another dock in California has {given_value} crates."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} crates could be remaining at the California dock now.",
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
            "How many crates could be remaining at the California dock now?",

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


def money(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 50

    category, subcategory = "change_with_action", "money"
    knowledge = "When one lends money they are left with lesser money"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and he lends some money to his friend.",
            "{name} lends some money to his friend. He initially had {given_value} dollars."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} dollars could be remaining money with {name}.",
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
            "How much money could be remaining with {name} now?",

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


def money2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 80

    category, subcategory = "change_with_action", "money"
    knowledge = "When one borrows money they have money"

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has {given_value} dollars and he borrows some money from his friends.",
            "{name} borrows some money from his friend. He initially had {given_value} dollars."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} dollars could be amount of money with {name} now.",
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
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "How much money could be with {name} now?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def cut_items(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 7
    given_value_end = 15

    category, subcategory = "change_with_action", "cut_items"
    knowledge = "When something is cut the number of pieces increases"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} had {given_value} apples and he cut some of them into pieces.",
            "{name} cut some apples into pieces. He initially had {given_value} apples.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be having {hyp_value} pieces now.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )

        question_template = random.choice([
            "How much pieces {name} could be having?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
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


def cut_items2(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 7
    given_value_end = 15

    category, subcategory = "change_with_action", "cut_items"
    knowledge = "When something is eaten its quantity reduces"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} had {given_value} apples and he shared some of them with his sister.",
            "{name} had {given_value} apples and he ate a few in the breakfast.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{name} could be having {hyp_value} apples now.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )

        question_template = random.choice([
            "How much apples {name} could be having now?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
            more_is_correct_flag=False,
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


def stretching(repetition_count):
    binary_instances = []
    mcq_instances = []
    given_value_start = 7
    given_value_end = 15

    category, subcategory = "change_with_action", "stretching"
    knowledge = "When something is stretched its length increases"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} had a elastic belt whose size was {given_value} units. He stretched it.",
            "{name} had a elastic belt whose size was {given_value} units and he stretched it."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The size of the belt could be {hyp_value} units after stretching.",
        ])
        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=6,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=3
        )

        question_template = random.choice([
            "What could be the size of the belt after stretching?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=6,
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


# if __name__ == "__main__":
#     repetition_count = 1
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = cut_items(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
