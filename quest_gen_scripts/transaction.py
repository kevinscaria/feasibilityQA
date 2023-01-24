import util
import random
import pprint


def crates(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "transaction", "crates"
    knowledge = "When some items are transferred to others their quantity at the initial place decreases"

    for i in range(repetition_count):

        premise_template = [
            "{name1} initially had {given_value1} crates and {name2} had {given_value2} crates. A few crates were transferred from {name1} to {name2}.",
            "There are crates of fruits at {name1}  and {name2}. {name1} had {given_value1} crates of fruits and {name2} had {given_value2} crates of fruits. There was a requirement of some crates at {name2}, so some of crates were sent from {name1} to {name2}."
        ]
        premise_template = premise_template[i % len(premise_template)]

        from_name1_to_name2 = True
        name = random.choice([
            {
                "name1": "Dock A",
                "name2": "Dock B",
            }
        ])
        given_value = {
            "given_value1": random.randint(15, 30),
            "given_value2": random.randint(15, 30),
        }
        premise = premise_template.format(
            name1=name["name1"], name2=name["name2"], given_value1=given_value["given_value1"], given_value2=given_value["given_value2"])

        hypothesis_template = random.choice([
            "{name} can now have {hyp_value} crates.",

        ])

        binary_instances += util.for_transaction_create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            from_name1_to_name2=from_name1_to_name2,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What can be the number of crates at {name}?",

        ])
        question_text = question_template
        mcq_instances += util.for_transaction_generate_question(
            category,
            subcategory,
            knowledge,
            premise,
            question_text=question_text, name=name, given_value=given_value,
            diff=10,
            from_name1_to_name2=from_name1_to_name2,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

    return binary_instances, mcq_instances


def crates2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "transaction", "crates"
    knowledge = "When some items are transferred to others their quantity at the initial place decreases"

    for i in range(repetition_count):

        premise_template = [
            "{name1} initially had {given_value1} crates and {name2} had {given_value2} crates. A few crates were transferred from {name2} to {name1}.",
            "There are crates of fruits at {name1}  and {name2}. {name1} had {given_value1} crates of fruits and {name2} had {given_value2} crates of fruits. There was a requirement of some crates at {name1}, so some of crates were sent from {name2} to {name1}."
        ]
        premise_template = premise_template[i % len(premise_template)]

        from_name1_to_name2 = False
        name = random.choice([
            {
                "name1": "Dock A",
                "name2": "Dock B",
            }
        ])
        given_value = {
            "given_value1": random.randint(15, 30),
            "given_value2": random.randint(15, 30),
        }
        premise = premise_template.format(
            name1=name["name1"], name2=name["name2"], given_value1=given_value["given_value1"], given_value2=given_value["given_value2"])

        hypothesis_template = random.choice([
            "{name} can now have {hyp_value} crates.",

        ])

        binary_instances += util.for_transaction_create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=10,
            from_name1_to_name2=from_name1_to_name2,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What can be the number of crates at {name}?",

        ])
        question_text = question_template
        mcq_instances += util.for_transaction_generate_question(
            category,
            subcategory,
            knowledge,
            premise,
            question_text=question_text, name=name, given_value=given_value,
            diff=10,
            from_name1_to_name2=from_name1_to_name2,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

    return binary_instances, mcq_instances


def money(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "transaction", "money"
    knowledge = "When some money is transferred to others money with the giver decreases"

    for i in range(repetition_count):

        premise_template = [
            "{name1} had {given_value1} dollars initially and gave some money to {name2} who initially had {given_value2} dollars."
            "{name1} had a friend {name2}. {name2} wanted to buy something but only had {given_value2} dollars with her which was not sufficient, so {name1} who had initially {given_value1} dollars gave {name2} some money."
        ]
        premise_template = premise_template[i % len(premise_template)]

        from_name1_to_name2 = True
        name = random.choice([
            {
                "name1": random.choice(util.male_names),
                "name2": random.choice(util.female_names),
            }
        ])
        given_value = {
            "given_value1": random.randint(100, 200),
            "given_value2": random.randint(50, 90),
        }
        premise = premise_template.format(
            name1=name["name1"], name2=name["name2"], given_value1=given_value["given_value1"], given_value2=given_value["given_value2"])

        hypothesis_template = random.choice([
            "{name} could be having {hyp_value} dollars now.",

        ])

        binary_instances += util.for_transaction_create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=40,
            from_name1_to_name2=from_name1_to_name2,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )

        question_template = random.choice([
            "What could be the amount of money with {name} now?",

        ])
        question_text = question_template
        mcq_instances += util.for_transaction_generate_question(
            category,
            subcategory,
            knowledge,
            premise,
            question_text=question_text, name=name, given_value=given_value,
            diff=40,
            from_name1_to_name2=from_name1_to_name2,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )

    return binary_instances, mcq_instances


def money2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "transaction", "money"
    knowledge = "When some money is transferred to others money with the giver decreases"

    for i in range(repetition_count):

        premise_template = [
            "{name1} had {given_value1} dollars initially and took some money from {name2} who initially had {given_value2} dollars."
            "{name1} had a friend {name2}. {name1} wanted to buy something but only had {given_value1} dollars with her which was not sufficient, so {name2} who had initially {given_value2} dollars gave {name1} some money"
        ]
        premise_template = premise_template[i % len(premise_template)]

        from_name1_to_name2 = False
        name = random.choice([
            {
                "name1": random.choice(util.male_names),
                "name2": random.choice(util.female_names),
            }
        ])
        given_value = {
            "given_value1": random.randint(50, 100),
            "given_value2": random.randint(150, 250),
        }
        premise = premise_template.format(
            name1=name["name1"], name2=name["name2"], given_value1=given_value["given_value1"], given_value2=given_value["given_value2"])

        hypothesis_template = random.choice([
            "{name} could be having {hyp_value} dollars now.",

        ])

        binary_instances += util.for_transaction_create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=40,
            from_name1_to_name2=from_name1_to_name2,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )

        question_template = random.choice([
            "What could be the amount of money with {name} now?",

        ])
        question_text = question_template
        mcq_instances += util.for_transaction_generate_question(
            category,
            subcategory,
            knowledge,
            premise,
            question_text=question_text, name=name, given_value=given_value,
            diff=40,
            from_name1_to_name2=from_name1_to_name2,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=10,
            scale=1
        )

    return binary_instances, mcq_instances


# if __name__ == "__main__":
#     repetition_count = 1
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = money2(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
