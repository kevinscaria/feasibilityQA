import util
import random
import pprint
import numpy as np


def traffic_sense1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "traffic_sense"
    knowledge = "Vehicle should start at green light, halt at red lights, and slow down at yellow lights."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was driving to his university and he saw a signal and stopped his car.",
            "When cycling to his office {name} saw a signal and stopped his bike.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The signal was showing red light.",
        ]

        false_hypotheses = [
            "The signal was showing yellow light.",
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
            "Which color light was flashed by the signal?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Red", "Green", "Yellow", "Blue"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def traffic_sense2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "traffic_sense"
    knowledge = "Vehicle should start at green light, halt at red lights, and slow down at yellow lights."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "When {name} was motorbiking to his office he saw a signal and slowed down his bike.",
            "When {name} was riding his bike to go pick his friend up, he reached a signal and slowed down his bike.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The signal was showing yellow light.",
        ]

        false_hypotheses = [
            "The signal was showing green light.",
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
            "What was the color that was flashed by the signal?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Red", "Green", "Yellow", "Blue"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def traffic_sense3(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "traffic_sense"
    knowledge = "Vehicle should start at green light, halt at red lights, and slow down at yellow lights."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "On a monday morning, {name} was travelling to the airport. The bus was halted in the signal and when the color of the signal changed, the bus started moving.",
            "{name} was off for a vacation and travelling to the airport. The bus which was halted in the signal satrted moving when the color of the signal changed.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The color of the signal now is green.",
        ]

        false_hypotheses = [
            "The color of the signal now is yellow.",
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
            "Which color did the signal light change to?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Red", "Green", "Yellow", "Blue"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def traffic_sense4(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "traffic_sense"
    knowledge = "Vehicle should start at green light, halt at red lights, and slow down at yellow lights."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was driving to pick up his mom, was waiting in the signal. After a couple of seconds the signal changed to green.",
            "{name} was waiting in the signal in his car. Few seconds later the signal changed to yellow.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The driver should now start driving.",
        ]

        false_hypotheses = [
            "The driver should wait for the signal to change again to another color.",
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
            "Since the color of the signal changed to green, what should the driver do?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Halt", "Move", "Sleep", "Drive"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def traffic_sense5(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "traffic_sense"
    knowledge = "Vehicle should start at green light, halt at red lights, and slow down at yellow lights."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was riding his bike to go pick his friend up. He reached a signal and he saw the signal was red.",
            "When {name} reached a signal on his way to meet his friend, he saw the signal was red."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The driver should halt at the signal.",
        ]

        false_hypotheses = [
            "The driver should drive faster.",
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
            "Since the color of the signal changed to red, what should the driver do?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Halt", "Move", "Sleep", "Drive"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def traffic_sense6(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "traffic_sense"
    knowledge = "Vehicle should start at green light, halt at red lights, and slow down at yellow lights"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was using the bus to reach his office. The bus saw a yellow signal on the way.",
            "{name} was riding his bike to go pick his friend up. He saw a yellow signal on the way.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The driver should slow down at the signal",
        ]

        false_hypotheses = [
            "The driver should drive faster.",
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
            "Since the color of the signal changed to red, what should the driver do?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Halt", "Move", "Slow down", "Drive"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def nature_sense1(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "nature_sense"
    knowledge = "Insects have six legs."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was an entomology major. In his mid term exam he was asked the number of legs that an insect has.",
            "In a biology mid term exams, {name} was asked the number of legs an insect has."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The candidate wrote the answer as six.",
        ]

        false_hypotheses = [
            "The candidate wrote the answer as five.",
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
            "What could be the answer wrote by the candidate in his mid term exams?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["6", "16", "9", "5"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def nature_sense2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "nature_sense"
    knowledge = "Female gender in mammals give birth to young ones."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was taken to a farm as part of his field trip. In the farm he witnessed the birth of a calf.",
            "In a field trip to a farm, {name} witnessed the birth of a calf."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The calf was delivered by a cow.",
        ]

        false_hypotheses = [
            "The calf was delivered by a bull.",
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
            "Which animal could have given birth to the calf?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Bull", "Ox", "Cow", "drake"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def jumping_power(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "jumping_power"
    knowledge = "Humans can jump to a limited distance."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was running and he came across a small ditch and he decided to jump",
            "When {name} came across a ditch along the path he was running, he decided to jump."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He will land across the ditch.",
        ]

        false_hypotheses = [
            "He will land in another city.",
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
            "Where will {name} land after he jumps?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Across the ditch", "Another city",
                          "Another planet", "Another country"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def running_speed(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "running_speed"
    knowledge = "Humans cannot run faster than motor vehicles in its maximum speed."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was running through a busy road and an object went ahead of him.",
            "When {name} was jogging through a busy road, an object overtook him."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could have been a car.",
        ]

        false_hypotheses = [
            "The object could have been an ant.",
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
            "What was the object that crossed {name} when he was running?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Train", "Bike", "Ant", "Car"],
            answers_list=[0, 1, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def train_travel1(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "train_travel"
    knowledge = "Passengers should arrive at the railway station before the train leaves."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was planning a vacation and he decided to travel the entire east coast through train. His boarding time was 12:00 PM and he sucessfully boarded the train.",
            "{name} was eager for his vacation trip and decided to travel via train. He succesfully boarded the train which was scheduled to leave at 12:00 PM."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have arrived at the station before 12:00 PM.",
        ]

        false_hypotheses = [
            "He could have arrived at the station after 12:00 PM.",
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
            "When could {name} have arrived at the railway station?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Before the boarding time",
                          "After the boarding time", "One day after the boarding time", "None"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def train_travel2(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "train_travel"
    knowledge = "Passengers should arrive at the railway station before the train leaves."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} couldn't go for his vacation. The boarding time was 12:30 PM, but he missed his train.",
            "{name} was disappointed as he could not board the train which was scheduled to depart at 12:30 for his vacation due to some last minute change in schedule."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have arrived at the station after 12:30 PM.",
        ]

        false_hypotheses = [
            "He could have arrived at the station before 12:30 PM.",
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
            "When could {name} have arrived at the railway station?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Before the boarding time",
                          "After the boarding time", "One day after the boarding time", "None"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def time_knowledge(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "time_knowledge"
    knowledge = "New movies can be watched after the release date."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "The latest superhero moving was releasing on 28th February 2022. {name} was a super fan of the superhero and wished to see the movie.",
            "{name} wanted to watch a documentary on pollution. However, the release date for the documentary was 3rd March 2020."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have watched the movie on 2nd March 2022.",
        ]

        false_hypotheses = [
            "He could have watched the movie on 3rd February 2022.",
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
            "When could {name} have arrived at the railway station?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["28th February 2022", "1st January 2022",
                          "2nd March 2022", "3rd February 2022"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def screwdriver(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "screwdriver"
    knowledge = "Screwdriver is required to unwind or wind a screw."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was fixing a device and he needed to open the screws at the back of the device.",
            "To open the device for repairs, {name} needed to unscrew a component in the device."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have used a screwdriver to open the screws.",
        ]

        false_hypotheses = [
            "He could have used a hammer to open the screws.",
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
            "What could have been used by {name} to open the screws?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Screwdriver", "Hammer", "Bulb", "Laptop"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def voice_and_distance(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "voice_and_distance"
    knowledge = "Human voice can be heard only upto a limited distance."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to play with his friend. So he shouted his friend's name so that his friend could hear him and come to play.",
            "{name} called out his friend's name loudly to invite him over to the ground to play a match of cricket."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "His friend could have been in the same house.",
        ]

        false_hypotheses = [
            "His friend could have been in another city.",
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
            "Where could {name}'s friend be residing?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Same house", "Same building",
                          "Another city", "Another country"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def profession_knowledge1(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "profession_knowledge"
    knowledge = "Teacher is the person who teaches students skills."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to learn a new subject. So he went to a person to learn the subject.",
            "Fed up with his current job, {name} wanted to upskill and wanted to learn a new skill to get a better job. He went to a person to learn the new skill."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The person could have been a teacher.",
        ]

        false_hypotheses = [
            "The person could have been musician.",
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
            "Who could have been the person who taught {name} the subject?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Doctor", "Teacher",
                          "Maid", "Musician"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def profession_knowledge2(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "profession_knowledge"
    knowledge = "Carpenter is the person who makes furniture."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to build a door. He hires a person to get this work done.",
            "The main door in {name}'s house was broken and needed repairs. So he hired a person to repair the door."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The person could have been a carpenter.",
        ]

        false_hypotheses = [
            "The person could have been a chef.",
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
            "Who could have been the person that {name} hired to do this job?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Doctor", "Teacher",
                          "Chef", "Carpenter"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def light_and_brightness(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "light_and_brightness"
    knowledge = "Illuminating devices/objects can generate light."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was watching TV when there was a major power cut. He finds an object that generated light in the dark.",
            "There was a power cut and {name} needed to find an object that generated light in the dark."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could have been a candle.",
        ]

        false_hypotheses = [
            "The object could have been a eraser.",
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
            "What could be the object used by {name} to generate light?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Candle", "Emergency lamp",
                          "Pen", "Pencil"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def food_and_protein(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "food_and_protein"
    knowledge = "Non vegetarian food is rich in proteins."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a recent blood test, {name} realised that he was having deficiency of proteins. Since he did not want to use protein supplements, he went and bought an item from a store.",
            "{name} was having protein deficiency. He went to a store and bought an item from the store."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The item could have been fish.",
        ]

        false_hypotheses = [
            "The item could have been a laptop.",
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
            "What could be the item that was purchased by {name} to increase is protein levels naturally?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Fish", "Sugar",
                          "Water", "Salt"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def good_credit(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "good_credit"
    knowledge = "Prompt repayment of credit build credit score."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Last Friday, {name} turned 30. He planned to buy a house and realised he had bas credit score.",
            "{name} was planning to buy a house and realised he had bad credit score."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He should pay credit before due date to improve credit score.",
        ]

        false_hypotheses = [
            "He should pay credit after due date to improve credit score.",
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
            "When should {name} pay his due amount to increase the credit score?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Before due date", "One month after due date",
                          "One year after due date", "Don't repay"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def free_right(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "diving_height"
    knowledge = "Incoming traffic need not wait for signal to turn right on a free right."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "On his way to work, {name} saw a lot of cars turning right without waiting for the signal.",
            "Several cars were turning right without waiting for the signal when {name} was on his fway to work."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The cars were on a free right road.",
        ]

        false_hypotheses = [
            "The cars were on a free left road.",
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
            "What type of signal did {name} encounter on the way to his work?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Free right", "Free left",
                          "U Turn", "Red light"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def diving_knowledge(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "diving_height"
    knowledge = "Diving in shallow pools can cause serious injury."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} recently visited an aquatic theme park. He saw people bathing in a swimming pool. However he did not see anyone diving.",
            "When {name} visited a water park, he noticed that no one was diving into the pool."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "This could be because the pool was shallow.",
        ]

        false_hypotheses = [
            "This could be because the pool was deep.",
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
            "Why was no one diving into the pool that {name} visited in the park?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Shallow pool", "Deep pool",
                          "Shark infested", "None"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def perpetual_machines(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "perpetual_machines"
    knowledge = "Perpetual machines is not possible."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} purchased a fan that rotates on an axis. He rotated the fan using his hands.",
            "{name} rotated the blades of a fan using his hands that was fixed on an axis."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The machine will stop rotating in few moments.",
        ]

        false_hypotheses = [
            "The machine will never stop rotating.",
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
            "What could happen to the fan that was rotated by {name} using his hands?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Stop rotating eventuallys", "Keep rotating permanently",
                          "Stop immediately", "None"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def heat_uses(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "heat_uses"
    knowledge = "Heat is required to dry clothes."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to dry his laundry load.",
            "Since last week was very hectic, {name} wanted to do his laundry and dry it in the weekend."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could dry the load outside on a hot sunny afternoon.",
        ]

        false_hypotheses = [
            "He could dry the load oustide on a rainy day.",
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
            "What could be done by {name} to dry his laundry load?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Dry on a hot afternoon", "Dry on a rainy day",
                          "Use a dryer", "None"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def food_knowledge(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "spices_and_food"
    knowledge = "Spices such as cardamom, coriander etc. are required to add flavour to Indian gravies."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was hosting his friend's family for dinner. So he was preparing a traditional Indian dish. However after tasting it he found the dish to be bland.",
            "{name} was preparing a traditional Indian dish to treat his in laws. When he tried out a small piece of the dish he found it to be bland."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could add coriander to add flavour to the dish.",
        ]

        false_hypotheses = [
            "He could add corn flour to add flavour to the dish.",
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
            "What could be done by {name} to add flavour to the dish?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["coriander", "corn flour", "cilantro", "oil"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def eye_wear(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "spices_and_food"
    knowledge = "Wearing sunglass is a good way to protect eyes from harsh sunlight."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was out jogging on a trail. It was a sunny day and he used an item from his backpack to cover his eyes from the sun.",
            "To cover his eyes from the hot sun, {name} used an item from his backpack when he was out jogging on a trail."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The item could have been sunglasses.",
        ]

        false_hypotheses = [
            "The item could have been a T-shirt.",
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
            "What could be the item used by {name} to protect his eyes from the sun?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["sunglasses", "shades", "T-shirt", "water bottle"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def domestic_animals1(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "domestic_animals"
    knowledge = "Domesticated animals are animals that have been selectively bred and genetically adapted over generations to live alongside humans."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friends visited a nearby farm. He saw an animal ploughing the farm.",
            "An animal was ploughing the farm that {name} and his friends visited.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been bull.",
        ]

        false_hypotheses = [
            "The animal could have been a lion.",
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
            "What could be the animal that {name} saw in the farm ploughing?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["leopard", "lion", "bull", "ox"],
            answers_list=[2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def domestic_animals2(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "domestic_animals"
    knowledge = "Domesticated animals are animals that have been selectively bred and genetically adapted over generations to live alongside humans."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to meet his grand parents who lived on a ranch in the suburbs. He saw that there an animal pulling a cart.",
            "An animal was pulling a cart in the ranch in the suburbs that {name} went to.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been horse.",
        ]

        false_hypotheses = [
            "The animal could have been a zebra.",
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
            "What could be the animal that {name} saw which was pulling the cart?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["zebra", "giraffe", "horse", "bullock"],
            answers_list=[2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def domestic_animals3(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "domestic_animals"
    knowledge = "Wool yielding animals with thick fur rearing is done to extract wool."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} won a gift coupon to stay at a ranch. The owner of the ranch showed that majority of his business was from rearing an animal which was used to extract wool.",
            "Rearing an animal that is used to extract wool is the main business of the ranch owner {name}",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been sheep.",
        ]

        false_hypotheses = [
            "The animal could have been a cobra.",
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
            "What could be the animal that {name} saw which was used to extract wool?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cobra", "yak", "sheep", "horse"],
            answers_list=[1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def domestic_animals4(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "domestic_animals"
    knowledge = "Dairy cattle are used to extract milk."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In his recent trip to a milk production factory, {name} saw that the factory had a huge farm filled with one type of animal.",
            "A milk producing factory had a huge farm filled with one type of animal that {name} went to visit.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been cow.",
        ]

        false_hypotheses = [
            "The animal could have been a giraffe.",
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
            "What could be the animal that {name} saw which was used to extract milk?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cow", "lion", "zebra", "python"],
            answers_list=[1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def domestic_animals5(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "domestic_animals"
    knowledge = "Honey bees create honey."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s favourite bread spread was honey. So he asked his mother how is honey made?. She replied that honey is made from an animal which was used to extract honey.",
            "In an environmental science class, {name} was told honey is made by rearing an animal that creates honey nectar.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been honey bee.",
        ]

        false_hypotheses = [
            "The animal could have been a house fly.",
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
            "What could be the animal that creates honey?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["house fly", "wasp", "bee", "sea lion"],
            answers_list=[1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wild_animals1(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "wild_animals"
    knowledge = "A wild animal finds its own food, shelter, water and all its other needs in a specific natural habitat."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was watching the geographic channel. The narrator was speaking about an animal that lives in the wild and hunts animals for it food.",
            "In a documentary, {name} was told that an animal lives in the wild and hunts animals for it food.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been leopard.",
        ]

        false_hypotheses = [
            "The animal could have been a cow.",
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
            "What could be the animal that was shown in the channel that {name} was watching?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["lion", "leopard", "cow", "penguin"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wild_animals2(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "wild_animals"
    knowledge = "Only wild animals are found in wildlife sanctuaries."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friends visited a famous wildlife sanctuary. They were sitting inside a caged vehicle and saw an animal approaching them.",
            "When {name} and his friends visited a wildlife national park, they saw an animal approaching them.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been lioness.",
        ]

        false_hypotheses = [
            "The item could have been a cow.",
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
            "What could be the animal that was approching the vehicle that {name} was sitting in?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Lion", "Elephant", "Cow", "Pet dog"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def celebrities(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "celebrities"
    knowledge = "Famous people have huge fan following."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was dining at a hotel when he suddenly saw several diners and photographers running behind a person to get his autograph and photographs.",
            "When {name} was walking at a mall, he saw several diners and photographers running behind a person to get his autograph and photographs.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The person could have been an actor.",
        ]

        false_hypotheses = [
            "The person could have been a valet.",
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
            "Who could have been the person that {name} saw in the hotel?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Actor", "Football player", "Valet", "Waiter"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def amphibians(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "amphibians"
    knowledge = "Amphibians are animals that can live on both land and water."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} as part of his school lecture learnt that an animal can live on both land and water.",
            "In a documentary, {name} was told that an animal can live on both land and water.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been a frog.",
        ]

        false_hypotheses = [
            "The animal could have been an elephant.",
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
            "Who could have been the animal that {name} learnt about?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Turtle", "Frog", "Cow", "Dog"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def desserts(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "amphibians"
    knowledge = "Desserts are sweet foods that are usually eaten after a meal."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to a dinner in a 5 star hotel and ordered a 3 course meal. At the end of the meal, he saw a dessert that was served to him.",
            "After the meal, {name} was offered a complimentary dessert which was served to him.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The taste of the dessert is sweet.",
        ]

        false_hypotheses = [
            "The taste of the dessert is salty.",
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
            "Who could have been the taste of the dessert that {name} ate?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Sweet", "salty", "Cow", "Dog"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def clothing_knowledge(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "amphibians"
    knowledge = "People wear clothes with fleece in colder climates."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "Last christmas {name} went to a switzerland for a trip with his girl friend. The weather was sub zero and they packed an item specially for such temperature.",
            "In a trip to Nepal, {name}, the weather was extremeley cold and {name} packed an item to handle such harsh climate."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The item that was packed could be a thick sweater.",
        ]

        false_hypotheses = [
            "The item that was packed could be a sleeveless shirt.",
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
            "Who could have been the item packed by {name} specially for the cold?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Sweater", "T Shirt", "Jacket", "Vests"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def shoe_sizes(repetition_count):

    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "amphibians"
    knowledge = "One cannot wear shoes that are smaller than their feet."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} had an interview to attend. So he told his partner to purchase shoes for him on their way back home. However, when {name} tried to wear it, he could not fit.",
            "To attend a party that {name} was invited to, he could not wear his new shoes when he tried to put it on."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The shoe could be smaller in size.",
        ]

        false_hypotheses = [
            "The shoe could be larger in size.",
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
            "Who could have been the issue faced by {name} with his shoe?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Larger size", "Smaller size", "Torn", "None"],
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

#     template_binary_instances, template_mcq_instances = shoe_sizes(
#         repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances

#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
