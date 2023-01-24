import util
import random
import pprint
import numpy as np


def battery_time1(repetition_count):
    category, subcategory = "attribute_comparison", "battery_time",
    knowledge = "Mobile on screen time is directly proportional to it's battery capacity."

    binary_instances = []
    mcq_instances = []
    given_value_start = 1000
    given_value_end = 7000

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is testing screen time of two mobiles. The mobile with higher on screen time has a battery of {given_value} mAh.",
            "{name} is doing screen time test of two tablets. The tablet with {given_value} mAh battery has higher on screen time. "
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Battery capacity of other device could be {hyp_value} mAh.",
        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=1000,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the battery capacity of other device?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=1000,
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


def battery_time2(repetition_count):
    category, subcategory = "attribute_comparison", "battery_time",
    knowledge = "Mobile on screen time is directly proportional to it's battery capacity."

    binary_instances = []
    mcq_instances = []
    given_value_start = 1000
    given_value_end = 7000

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is testing on screen time of two mobile. The mobile with lower on screen time has a battery of {given_value} mAh. ",
            "{name} is doing screen time test of two tablets. The tablet with {given_value} mAh battery has lower on screen time. "
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Battery capacity of the other device could be {hyp_value} mAh.",

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
            "What could be the battery capacity of other device?",

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


def vol_cuboid1(repetition_count):
    category, subcategory = "attribute_comparison", "vol_cube",
    knowledge = "Volume of large object is greater than volume of smaller object."

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 200

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "It was summer and {name} wanted to make ice for lemonade. He has two ice trays and fills water in the trays. The bigger ice tray was filled with {given_value} ml of water.",
            "{name} wanted to make some some ice for his soft drink. He fills water in two trays which he had. {given_value} ml of water was filled in larger ice tray."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of water that could be filled in the smaller ice tray could be {hyp_value} ml.",

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
            "What could be the volume of water filled in the smaller tray?",

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


def vol_cuboid2(repetition_count):
    category, subcategory = "attribute_comparison", "vol_cube",
    knowledge = "Volume of large cuboid is greater than volume of small cuboid."

    binary_instances = []
    mcq_instances = []
    given_value_start = 50
    given_value_end = 200

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "It was summer and {name} wanted to make ice. He has two ice trays and fills water in the trays. The smaller ice tray was filled with {given_value} ml of water.",
            "{name} wanted to make some some ice for his soft drink. He fills water in two trays which he had. {given_value} ml of water was filled in smaller ice tray."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Volume of water that could be filled in the bigger ice tray could be {hyp_value} ml.",

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
            "What could be the volume of water that could be needed to fill the smaller tray?",

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


def pendulum1(repetition_count):
    category, subcategory = "attribute_comparison", "pendulum",
    knowledge = "Time period of simple pendulum is directly proportional to it's length."

    binary_instances = []
    mcq_instances = []
    given_value_start = 5
    given_value_end = 15

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pendulum clocks in a room with different pendulum lengths. The time period of clock with larger pendulum is {given_value} seconds.",
            "{name} goes to buy two pendulum clocks of different pendulum lengths. {given_value} is the time period of the clock with a greater pendulum."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Time period of the pendulum with smaller length could be {hyp_value} seconds.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=3,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the time period of the pendulum with smaller length?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def pendulum2(repetition_count):
    category, subcategory = "attribute_comparison", "pendulum",
    knowledge = "Time period of simple pendulum is directly proportional to it's length."

    binary_instances = []
    mcq_instances = []
    given_value_start = 5
    given_value_end = 15

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two pendulum clocks in a room with different pendulum lengths. The time period of clock with smaller pendulum is {given_value} seconds.",
            "{name} goes to buy two pendulum clocks of different pendulum lengths. {given_value} is the time period of the clock with a smaller pendulum."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Time period of pendulum clock with larger length could be {hyp_value} seconds.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=3,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the time period of the larger pendulum clock?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def poster1(repetition_count):
    category, subcategory = "attribute_comparison", "poster",
    knowledge = "Printing of large poster requires more amount of ink as compared to printing of small posters."

    binary_instances = []
    mcq_instances = []
    given_value_start = 200
    given_value_end = 500

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} works in a printing press and has to print 2 posters. The bigger poster requires {given_value} ml of ink.",
            "A merketing comoany wants to get 2 posters of different sizes. {given_value} ml of ink is required for the bigger poster."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Amount of ink required for smaller poster could be {hyp_value} ml.",

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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the amount of ink required for the smaller poster?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
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


def poster2(repetition_count):
    category, subcategory = "attribute_comparison", "poster",
    knowledge = "Printing of large poster requires more amount of ink as compared to printing of small posters."

    binary_instances = []
    mcq_instances = []
    given_value_start = 200
    given_value_end = 500

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} works in a printing press and has to print 2 posters. The smaller poster requires {given_value} ml of ink.",
            "A merketing comoany wants to get 2 posters of different sizes. {given_value} ml of ink is required for the smaller poster."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Amount of ink required for larger poster could be {hyp_value} ml.",

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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the amount of ink required for the larger poster?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
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


def store_files1(repetition_count):
    category, subcategory = "attribute_comparison", "store_files",
    knowledge = "The number of files of equal sizes that can be stored is directly proportional to storage size."

    binary_instances = []
    mcq_instances = []
    given_value_start = 200
    given_value_end = 500

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two external hard drive of different capacity. It is known that each file is of the same size. He can fit {given_value} number of files in a hard drive of larger size.",
            "{name} bought two external USB drives of different capacity. It is known that each file is the same size. {given_value} is the file numbers which can be stored on a larger size USB drive."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Number of equal sized files which can be stored in smaller drive could be {hyp_value}.",

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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What number of equal sized files could be stored in smaller drive?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
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


def store_files2(repetition_count):
    category, subcategory = "attribute_comparison", "store_files",
    knowledge = "Number of files of same size, is directly proportional to storage size."

    binary_instances = []
    mcq_instances = []
    given_value_start = 200
    given_value_end = 500

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two external hard disks of different capacity. It is known that each file is of the same size. He can fit {given_value} number of files in hard disk of smaller size",
            "{name} bought two external USB drives of different capacity. It is known that each file is the same size. {given_value} is the file numbers which can be stored on a smller size USB drive."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Number of equal sized files which can be stored in larger drive could be {hyp_value}.",

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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What number of files could be stored in larger drive",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=50,
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


def eyes1(repetition_count):
    category, subcategory = "attribute_comparison", "eyes",
    knowledge = "People with higher power of spectacles have weak eyes as compared to people with low power of spectacles."

    binary_instances = []
    mcq_instances = []
    given_value_start = 1
    given_value_end = 7

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend wear spectacles because both of them have power. His eyes are more weaker as compared to his friend and wears spectacles of {given_value} power.",
            "{name} and his friend use spctacles because both of them have week eyes. He wears a spectacle of {given_value} power and his eyes are more debilitating compared to his friend's eyes."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "His friend could be wearing spectacles of {hyp_value} power.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=3,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the power of spectacles of his friend?"

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def eyes2(repetition_count):
    category, subcategory = "attribute_comparison", "eyes",
    knowledge = "People with high power of spectacles have weak eyes as compared to people with low power of spectacles."

    binary_instances = []
    mcq_instances = []
    given_value_start = 1
    given_value_end = 7

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend wear spectacles because both of them have power. His eyes are better in comparison to his friends power. He wears spectacles of {given_value} power.",
            "{name} and his friend use spctacles because both of them have week eyes. He wears a spectacle of {given_value} power and his eyes are much better as compared to his friend's eyes."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "His friend with weaker eyes might have spectacles of {hyp_value} power",

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
            "What could be the value of spectacles of higher power",

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


def tyre_size1(repetition_count):
    category, subcategory = "attribute_comparison", "tyre_size",
    knowledge = "A cycle with larger tyre size runs faster as compared to cycle with smaller tyre size."

    binary_instances = []
    mcq_instances = []
    given_value_start = 16
    given_value_end = 28

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend went on a bike trek. The bicycle that could go faster has {given_value} inch tyre size.",
            "{name} and his friend decided to race on cycle. The cycle with {given_value} inch tyre size could go much more fast"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The size of cycle that was slower could be {hyp_value} inches.",

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
            "What could be the size of the slower cycle?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=2,
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


def tyre_size2(repetition_count):
    category, subcategory = "attribute_comparison", "tyre_size",
    knowledge = "A cycle with larger tyre size runs faster as compared to cycle with smaller tyre size."

    binary_instances = []
    mcq_instances = []
    given_value_start = 16
    given_value_end = 28

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend went for a cycle racing contest. His cycle was faster and his friends cycle was slower. The slower cycle had a tyre size of {given_value} inch.",
            "{name} and his friend participates in a contest of cycle racing. His friend's cycle was slow as compared to his cycle. The slow cycle had tyre size of {given_value}"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The size of the faster cycle could be {hyp_value} inch.",

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
            "What could be the size of the faster cycle?",

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


def engine_power1(repetition_count):
    category, subcategory = "attribute_comparison", "engine_power",
    knowledge = "Bigger vehicles require more powerful engines as compared to small vehicles."

    binary_instances = []
    mcq_instances = []
    given_value_start = 400
    given_value_end = 1000

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has a truck and a car. The engine power of truck is {given_value} horsepower.",
            "{name} has a fire truck and a car. {given_value} horsepower is the power of the truck."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The engine power of his car could be {hyp_value} horsepower.",

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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the power of the car's engine?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=100,
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


def engine_power2(repetition_count):
    category, subcategory = "attribute_comparison", "engine_power",
    knowledge = "Big vehicles require more powerful engines as compared to small vehicle."

    binary_instances = []
    mcq_instances = []
    given_value_start = 400
    given_value_end = 1000

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has a truck and a car. The power of engine of car is {given_value} horsepower.",
            "{name} has a fire truck and a car. {given_value} horsepower is the power of the car."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The power of truck's engine could be {hyp_value} horsepower.",

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
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What can be the power of truck's engine?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=100,
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


def obj_weight1(repetition_count):
    category, subcategory = "attribute_comparison", "obj_weight",
    knowledge = "Objects with more weight tend to fall faster as compared to objects with less weight."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 200

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two balloons, one of them has air in it and one of them has water in it. Both the balloons were thrown at same time from same height and the balloon with water reaches the ground faster than the balloon with air. The weight of balloon with water is {given_value} grams ",
            "{name} performs an experiment on balloons. He takes two balloons,he fills one of them with air  and other one with water in it. He throws both the balloons at the same time from the same height and the balloon with water reaches the ground faster than the balloon with air. The weight of the balloon with water is {given_value} grams."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The weight of air balloon could be {hyp_value} grams.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=25,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What can be the weight of air balloon?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=25,
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


def obj_weight2(repetition_count):
    category, subcategory = "attribute_comparison", "obj_weight",
    knowledge = "Objects with more weight tend to fall faster as compared to objects with less weight."

    binary_instances = []
    mcq_instances = []
    given_value_start = 10
    given_value_end = 200

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two balloons, one of them has air in it and one of them has water in it. Both the balloons were thrown at same time from same height and the balloon with water reaches the ground faster than the balloon with air. The weight of balloon with air is {given_value} grams ",
            "{name} performs an experiment on balloons. He takes two balloons, he fills one of them with air  and other one with water in it. He throws both the balloons at the same time from the same height and the balloon with water reaches the ground faster than the balloon with air. The weight of the balloon with air is {given_value} grams."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The weight of water balloon could be {hyp_value} grams.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=25,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What can be the weight of water balloon?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=25,
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


def social_media1(repetition_count):
    category, subcategory = "attribute_comparison", "social_media",
    knowledge = "Number of daily active users in a social media platform is proportional to the popularity of the social media app."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2000
    given_value_end = 50000

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two social media platform, Fakebook and Chatsnap. Fakebook is more popular as compared to Chatsnap and the number of daily active users on Fakebook is {given_value}.",
            "{name} uses two social networking platforms, Fakebook and Chatsnap. Among the two he uses Fakebook, most of the social media users use Fakebook as it is more popular compared to ChatSnap. The number of daily active users in Fakebook is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The number of daily active users on Chatsnap could be {hyp_value}.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=360,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the number of daily active users on Chatsnap?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=360,
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


def social_media_2(repetition_count):
    category, subcategory = "attribute_comparison", "social_media",
    knowledge = "Number of daily active users in a social media platform is proportional to the popularity of the social media app."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2000
    given_value_end = 50000

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two social media platform, Fakebook and Chatsnap. Fakebook is more popular as compared to Chatsnap and the number of users on Chatsnap is {given_value}. ",
            "{name} uses two social networking platforms, Fakebook and Chatsnap. Among the two he uses Fakebook, most of the social media users use Fakebook as it is more popular compared to ChatSnap. The number of daily active users in Chatsnap is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The number of users on Fakebook could be {hyp_value}.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=360,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What can be the number of users on Fakebook?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=360,
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


def ohmslaw1(repetition_count):
    category, subcategory = "attribute_comparison", "ohms_law",
    knowledge = "Voltage is directly proportional to current."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two bulbs and in both the bulb sockets the voltage is different. The current in bulb with higher voltage is {given_value} A.",
            "There are two light bulbs and on both socket of the bulb, the voltage is different. {given_value} A is the current in bulb with higher voltage."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Current in the bulb with low voltage could be {hyp_value} A.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=2,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What can be the current in bulb with low voltage?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=2,
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


def ohmslaw2(repetition_count):
    category, subcategory = "attribute_comparison", "ohm_law",
    knowledge = "Voltage is directly proportional to current."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two bulbs, but both the bulb sockets have differenet voltages. The current in bulb with low voltage is {given_value} A.",
            "There are two light bulbs and on both socket of the bulb, the voltage is different. {given_value} A is the current in bulb with higher voltage."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The current in bulb with higher voltage could be {hyp_value} A.",

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
            "What could be the current in bulb with higher voltage?",

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


def ohmslaw3(repetition_count):
    category, subcategory = "attribute_comparison", "ohms_law",
    knowledge = "Voltage is directly proportional to resistance."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two electrical circuits which {name} is experimenting. Among both the circuits, one of them has higher voltage applied. The circuit with higher voltage has resistance of {given_value} ohms.",
            "{name} performs an experiments on two circuits. Between the two circuits, one of them has a higher voltage applied. {given_value} is the resistance of the circuit with a higher voltage."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The resistance value in circuit with low voltage is {hyp_value} ohms",

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
            "What could be the resistance in circuit with low voltage?",

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


def ohmslaw4(repetition_count):
    category, subcategory = "attribute_comparison", "ohm_4",
    knowledge = "Voltage is directly proportional to resistance."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two electrical circuits which {name} is experimenting. He has to find out which circuit has higher resistance. Among both the circuits, one of them has high voltage as compared to others. The circuit with low voltage has resistance of {given_value} ohms.",
            "{name} performs an experiments on two circuits. Between the two circuits, one of them has a higher voltage applied. {given_value} is the resistance of the circuit with a lower voltage."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The resistance value in circuit with high voltage is {hyp_value} ohms.",

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
            "What could be the resistance in the circuit with high voltage?",

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


def heat_length1(repetition_count):
    category, subcategory = "attribute_comparison", "heat_length",
    knowledge = "A  expansion in length is directly proportional to the amount of heat."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} works for a construction firm, he noticed that there were two equal sized iron rods of same length. One of the iron rod was heated and its length increased as compared to the other rod. The length of the rod subjcted to heat became {given_value} metres.",
            "{name} works for a construction company, noticed that there were two iron rods of equal size of the same length. One of the iron rods was heated and its length increased compared to the other rod. The length of the subjugated bar heat became {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The length of rod which was not heated could be {hyp_value} metres.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=3,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the length of non heated rod?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def heat_length2(repetition_count):
    category, subcategory = "attribute_comparison", "heat_length",
    knowledge = "Length is directly proportional to the amount of heat."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} works for a construction firm, he noticed that there were two iron rods of same length. One of the iron rod was heated and its length increased as compared to the other rod. The length of shorter rod is {given_value} metres.",
            "{name} works for a construction company, noticed that there were two iron rods of equal size of the same length. One of the iron rods was heated and its length increased compared to the other rod. {given_value} meters is the length of the shorter rod."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The length of rod which was subjected to heat could be {hyp_value} metres.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=3,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the length of heated rod?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def refraction1(repetition_count):
    category, subcategory = "attribute_comparison", "refraction",
    knowledge = "Refractive index is inversely proportional to speed of light."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two transparent sheets with different refractive index. Speed of light in the sheet with lower refractive index is {given_value}.",
            "There are two transparent windows which have different refractive index. The speed of light on the window with a lower refractive index is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Speed of light in the other transparent object could be {hyp_value}.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=2,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the speed of light in the other transparent object?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def refraction2(repetition_count):
    category, subcategory = "attribute_comparison", "refraction",
    knowledge = "Refractive index is inversely proportional to speed of light."

    binary_instances = []
    mcq_instances = []
    given_value_start = 2
    given_value_end = 20

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "There are two transparent sheets with different refractive index. Speed of Light from sheet with less refractive index is more as compared to other sheet. Refractive index of sheet with more speed of light is {given_value}.",
            "{name} performs an experiment on two transparent windows with different refractive index. The speed of light from window with less refractive index is more compared to another window. The refractive index of the window with more light speed is {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "Refractive index of transparent object when speed of light is lesser could be {hyp_value}",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=2,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What can be the refractive index of object with lesser speed of light?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def bad_tyre(repetition_count):
    category, subcategory = "attribute_comparison", "bad_tyre",
    knowledge = "Condition of tyre is inversely proportional to distance travelled by the tyre."

    binary_instances = []
    mcq_instances = []
    given_value_start = 210
    given_value_end = 500

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two tyres, the first tyre that is in worse condition than the other and has travelled {given_value} miles.",
            "{name} has two tyres of bicycle, one of them has travelled {given_value} miles and is which is in worse condition than the other ."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The distance travelled by the other tyre could be {hyp_value} miles.",

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
            "What could be the distance travelled by the other tyre?",

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


def bad_tyre_2(repetition_count):
    category, subcategory = "attribute_comparison", "bad_tyre_2",
    knowledge = "Condition of tyres is inversely proportional to distance travelled by the tyre."

    binary_instances = []
    mcq_instances = []
    given_value_start = 200
    given_value_end = 500

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two tyres, the first tyre is in better condition than the first and has travelled {given_value} miles.",
            "{name} has two tyres of bicycle, one of them has travelled {given_value} miles and is which is in better condition than the other ."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The distance travelled by the other tyre could be {hyp_value}.",

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
            "What could be the distance travelled by the other tyre?",

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


def internet_speed(repetition_count):
    category, subcategory = "attribute_comparison", "internet_speed",
    knowledge = "Quality of video which can be buffered is directly proportional to internet speed."

    binary_instances = []
    mcq_instances = []
    given_value_start = 150
    given_value_end = 500

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two internet connections. From first internet connection, the video streaming was in better quality than the other. The internet speed of the first connction is {given_value} MB per sec.",
            "{name} has two different mobile phones and both of them have two different connections to the Internet. From the first Internet connection, the video transmission was of better quality than the other. {given_value} MB per sec is the the speed of first internet connection."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The internet speed of the other connection could be {hyp_value}.",

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
            "What could be the speed of the other internet connection?",

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


def internet_speed_2(repetition_count):
    category, subcategory = "attribute_comparison", "internet_speed_2",
    knowledge = "Quality of video feed is directly proportional to high internet speed."

    binary_instances = []
    mcq_instances = []
    given_value_start = 150
    given_value_end = 500

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has two internet connections. From first internet connection, the video streaming was in worse quality than the other. The internet speed of the second connection is {given_value} MB per sec.",
            "{name} has two different mobile phones and both of them have two different connections to the Internet. From the first Internet connection, the video transmission was of better quality than the other. {given_value} MB per sec is the the speed of second internet connection."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The internet speed of the other connection could be {hyp_value}.",

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
            "What could be the speed of the other internet connection??",

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


def workout_calories_2(repetition_count):
    category, subcategory = "attribute_comparison", "workout_calories_2",
    knowledge = "More minutes of workout is directly proportional to more calories burnt."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 120
    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend went to gym for a workout. The calories burnt by him is more than the his friend, The number of minutes his friend worked out is {given_value}.",
            "{name} worksout along with his friend. He burns less calories as compared to his friend. {given_value} is the number of minutes for which his friend works out."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} minutes could be the duration for which he worked out.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=2,
            more_is_correct_flag=True,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the duration for which he works out?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
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


def workout_calories(repetition_count):
    category, subcategory = "attribute_comparison", "workout_calories",
    knowledge = "More minutes of workout is directly proportional to more calories burnt."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 120

    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friend went to gym for a workout. The calories burnt by him is less than the calories burnt by his friend. The number of minutes he worked out is {given_value}.",
            "{name} worksout along with his friend. He burns less calories as compared to his friend. {given_value} is the number of minutes for which he works out."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "{hyp_value} minutes could be the duration for which his friend worked out.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=2,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the duration for which his friend worked out?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=2,
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


def amount_of_food(repetition_count):
    category, subcategory = "attribute_comparison", "amount_of_food",
    knowledge = "Amount of food required is directly proportional to the number of people."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50
    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} invited guests on two consecutive days. On both days he cooked same amount of food but the food on first day was insufficient. The number of people came on that day was {given_value}.",
            "{name} started a canteen two days a week. On both days he cookd the same amount of food, but the food the first day was not sufficient for all the people came to his canteen. The number of people came on that day was {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The number of people came on the second day could be {hyp_value}.",

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
            "What could be the number of people came on the other day?",

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


def amount_of_food_2(repetition_count):
    category, subcategory = "attribute_comparison", "amount_of_food_2",
    knowledge = "Amount of food required to feed is directly proportional to the number of people."

    binary_instances = []
    mcq_instances = []
    given_value_start = 20
    given_value_end = 50
    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} invited guests on two consecutive days. On both days he cooked same amount of food but the food on first day was sufficient but on 2nd day it was not. The number of people came on the second day was {given_value}.",
            "{name} started a canteen two days a week. On both days he cookd the same amount of food, but the food the first day was not sufficient for all the people came to his canteen. The number of people came on scond day was {given_value}."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The number of people came on the first day could be {hyp_value}.",

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
            "What could be the number of people came on the first day?",

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


def length_of_wire(repetition_count):
    category, subcategory = "attribute_comparison", "length_of_wire",
    knowledge = "Amount of material required is directly proportional to the length of wire."

    binary_instances = []
    mcq_instances = []
    given_value_start = 5
    given_value_end = 15
    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is making two wires of same thickness from copper. The amount of copper used in first wire was more than the other wire. The length of that wire is {given_value} metre.",
            "{name} is making two wires of the same aluminium thickness. The amount of aluminium used in the first wire was more than the other wire. The length of that wire is {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The length of other wire could be {hyp_value} metres.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=2,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the length of the other wire?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=2,
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


def length_of_wire_2(repetition_count):
    category, subcategory = "attribute_comparison", "length_of_wire_2",
    knowledge = "Amount of material required is directly proportional to the length of wire."

    binary_instances = []
    mcq_instances = []
    given_value_start = 5
    given_value_end = 15
    for i in range(repetition_count):
        # *******Template 1

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is making two wires of same thickness from copper. The amount of copper used in first wire was less than the other wire. The length of the other wire is {given_value} metre.",
            "{name} is making two wires of the same aluminium thickness. The amount of aluminium used in the first wire was less than the other wire. The length of other wire is {given_value} meters."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        given_value = random.randint(given_value_start, given_value_end)
        premise = premise_template.format(name=name, given_value=given_value)

        hypothesis_template = random.choice([
            "The length of the first wire could be {hyp_value} metres.",

        ])

        binary_instances += util.create_all_scenarios_for_binary_classification_task(
            category,
            subcategory,
            knowledge,
            premise,
            hypothesis_template,
            name,
            given_value,
            diff=2,
            more_is_correct_flag=False,
            equal_is_correct_flag=False,
            negative_options_possible=False,
            round_to=1,
            scale=1
        )

        question_template = random.choice([
            "What could be the length of the first wire?",

        ])
        question_text = question_template.format(name=name)
        question = util.generate_question(
            question_text=question_text, given_value=given_value,
            diff=2,
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


# if __name__ == "__main__":
#     repetition_count = 1
#     binary_instances = []
#     mcq_instances = []
#
#     template_binary_instances, template_mcq_instances = battery_time2(
#         repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
