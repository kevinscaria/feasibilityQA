import util
import random
import pprint
import numpy as np


def flying_object(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "flying_object"
    knowledge = "A human cannot fly but other objects like birds, plane and football can."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was playing in the ground and he saw an object flying from the window.",
            "{name} was playing on the floor and saw a flying object from the window."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could not have been another human being.",
        ]

        false_hypotheses = [
            "The object could have been another human being.",
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
            "What could be flying object ?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["human", "bird", "plane", "football"],
            answers_list=[1, 2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def lock_and_key(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "lock_and_key"
    knowledge = "A key can be used to open a lock. Any other object cannot open the lock."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is trying to open a lock in front of him and he was able to open the lock with that object.",
            "{name} attempted to open a door lock for his house and could open the lock with that object."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could be a key.",
        ]

        false_hypotheses = [
            "The object could be a banana.",
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
            "What could be the object from which the lock was opened?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["door", "fruit", "key", "none of these"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def phone_and_charge(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "phone_and_charge"
    knowledge = "A phone's battery can typically last for one day of two days with continuous usage. The battery cannot last for 1 week or more time."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has been using an electronic appliance without charging it for 1 month continuously.",
            "{name} has been using an electronic device. He is using it without charging it for 1 month continuously."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The electronic appliance could not be a mobile phone. ",
        ]

        false_hypotheses = [
            "The electronic appliance could be a mobile phone.",
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
            "What could be the electronic appliance?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["mobile phone", "car", "laptop", "none of these"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def car_and_wheels(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "car_and_wheels"
    knowledge = "A car runs on four wheels. Any other object moving with less number of wheels is not a car. Bicycle moves on two wheels."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw an object moving on the road from his window. The object was moving on two wheels.",
            "{name} was sitting by his window and saw an object moving on the road. The object was moving on two wheels."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could not be a car. ",
        ]

        false_hypotheses = [
            "The object could be a car.",
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
            "What could be the object?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["bicycle", "car", "truck", "none of these"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bicycle_and_wheels(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "bicycle_and_wheels"
    knowledge = "A bicycle runs on two wheels. Any other object moving with less number of wheels is not a bicycle."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw an object moving on the road from his window. The object was moving on two wheels.",
            "{name} was sitting by his window and saw an object moving on the road. The object was moving on two wheels."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could be a bicycle. ",
        ]

        false_hypotheses = [
            "The object could be a car.",
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
            "What could not be the object?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["bicycle", "car", "truck", "rocket"],
            answers_list=[1, 2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def moving_and_flying_objects(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "moving_and_flying_objects"
    knowledge = "Vehicles like car and bicycle run on the ground. Vehicles like plane and rockets fly in the air."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw an object moving on the ground from his window.",
            "{name} saw an object from his window that moved on the ground."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The vehicle could be a bicycle. ",
        ]

        false_hypotheses = [
            "The vehicle could be a rocket.",
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
            "What could be the vehicle?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["bicycle", "car", "truck", "rocket"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def moving_and_flying_objects2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "moving_and_flying_objects"
    knowledge = "Vehicles like car and bicycle run on the ground. Vehicles like plane and rockets fly in the air."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw a vehicle flying when he visited a space station.",
            "{name} went to a space station. He went to the station by a vehicle."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The vehicle could be a rocket. ",
        ]

        false_hypotheses = [
            "The vehicle could be a bicycle.",
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
            "What could be the vehicle?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["bicycle", "car", "truck", "rocket"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cars_and_trains(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "cars_and_trains"
    knowledge = "Vehicles like car and bicycle run on the ground. Vehicle like train run on rails."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw a vehicle travelling on rails from his window.",
            "{name} was sitting in front of his window and saw a vehicle that traveled in rails."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The vehicle could be a train. ",
        ]

        false_hypotheses = [
            "The vehicle could be a car.",
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
            "What could be the vehicle?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["bicycle", "car", "truck", "train"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cars_and_boats(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "cars_and_boats"
    knowledge = "Vehicles like car and bicycle run on the ground. Vehicle like boats run on water."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw a vehicle travelling in an ocean while visiting a beach.",
            "{name} was visiting a beach and saw a vehicle traveling in the ocean."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The vehicle could be a boat. ",
        ]

        false_hypotheses = [
            "The vehicle could be a car.",
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
            "What could be the vehicle?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["boat", "car", "truck", "train"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cars_and_rockets(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "cars_and_rockets"
    knowledge = "Vehicles like car and bicycle run on the ground. Vehicles like space shuttle travel in space."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} in an astronaut is going to a moon on a vehicle.",
            "{name} saw a vehicle traveling in an ocean while visiting a beach."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The vehicle could be a space shuttle. ",
        ]

        false_hypotheses = [
            "The vehicle could be a car.",
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
            "What could be the vehicle?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["boat", "space shuttle", "truck", "train"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cars_and_submarines(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "cars_and_submarines"
    knowledge = "Vehicles like car and bicycle run on the ground. Vehicles like submarine travel under water."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} in a scuba diver and saw a vehicle moving under water.",
            "{name} saw a vehicle that moved underwater while scuba diving in the ocean."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The vehicle could be a submarine. ",
        ]

        false_hypotheses = [
            "The vehicle could be a car.",
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
            "What could be the vehicle?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["boat", "submarine", "truck", "train"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def fish_and_cow(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "fish_and_cow"
    knowledge = "Animals like fish, whale and sharks swim under water."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} in a scuba diver and saw an animal moving under water towards him.",
            "{name} saw an animal moving under water towards him while scuba diving in the ocean."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be a shark. ",
        ]

        false_hypotheses = [
            "The animal could be a cow.",
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
            "What could be the animal?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cow", "shark", "whale", "fish"],
            answers_list=[1, 2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def fish_and_animals(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "fish_and_animals"
    knowledge = "Animals like fish, whale and sharks swim under water. Animals like cow, horses and buffaloes stay on land. "

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a farmer and saw an animal running on the farm.",
            "{name} saw an animal running on the farm."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be a horse. ",
        ]

        false_hypotheses = [
            "The animal could be a shark.",
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
            "What could be the animal?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cow", "shark", "horse", "fish"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def domestic_and_wild_animals(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "domestic_and_wild_animals"
    knowledge = "Animals like lion, tiger, bear and panther are wild animals. They are found in forest. Animals like cow, horses and buffaloes stay on farm animals. They are not found in forest. "

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was going on an expedition to a wildlife preserve forest. He saw a wild animal there.",
            "{name} was going on an expedition to a national forest and saw a wild animal there."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be a Lion. ",
        ]

        false_hypotheses = [
            "The animal could be a cow.",
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
            "What could be the animal ?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cow", "Lion", "Tiger", "Bear"],
            answers_list=[1, 2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bear_height(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "bear_height"
    knowledge = "Black bears are about two metres tall. "

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was going on an expedition to a wildlife preserve forest. He saw a wild animal there whose height was about 2 meters",
            "{name} was going to spend an expedition to a forest of wildlife preserves. He saw a wild animal there whose height was about 2 meters away."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be a Black bear. ",
        ]

        false_hypotheses = [
            "The animal could be a rat.",
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
            "What could be the animal ?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["rat", "cockroach", "Black Bear", "cat"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def carnivore_herbivore(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "carnivore_herbivore"
    knowledge = "Animals like Lion, Tiger, Bear Eat other animals are called Carnivores. Animals like cow, buffalo, sheep, deer eat grass and are called herbivore. Carnivores eat herbivores. "

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was going on an expedition to a wildlife preserve forest. He saw a wild animal hunting and eating another animal.",
            "{name} went to an expedition to a preserve forest. He saw a wild animal hunting and eating another animal."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The wild animal could be a Lion. ",
        ]

        false_hypotheses = [
            "The wild animal could be a cow.",
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
            "What could be the wild animal ?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Lion", "Tiger", "Bear", "Deer"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def dragonflies_wings(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "dragonflies_wings"
    knowledge = "Dragonflies have 4 wings."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was an entomologist and was moving through a rainforest for a study. He saw an insect with 4 wings fluttering nearby.",
            "{name} was an entomologist and saw an insect with 4 wings fluttering nearby while moving through a rainforest for a study."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The insect could have been a dragonfly.",
        ]

        false_hypotheses = [
            "The insect could have been a mosquito.",
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
            "What could be the electronic appliance?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["dog", "peacock", "hen", "dragonfly"],
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

#     template_binary_instances, template_mcq_instances = car_and_wheels(
#         repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances

#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
