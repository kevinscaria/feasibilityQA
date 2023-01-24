import util
import random
import pprint
import numpy as np


def swimming(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "swimming"
    knowledge = "A person should learn swimming to not drown."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to a pool along with his friends. When he went to the pool, he didn't drown.",
            "{name} fell into a pool in his society but he didn't drown"
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have known swimming.",
        ]

        false_hypotheses = [
            "He could not have known swimming.",
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
            "What could be the skill due to which he didn't drown?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Skating", "Swimming", "Cooking", "Flying"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def animals_cant_fly(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "animals_cant_fly"
    knowledge = "Birds can fly but animals can't fly."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to a pet store to buy a pet. After thinking a lot he wanted a pet that could fly.",
            "{name} bought a pet for himeself that could fly."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The pet could have been a Parrot.",
        ]

        false_hypotheses = [
            "The pet could have been a Tiger.",
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
            "What could be the pet that he bought?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cat", "dog", "rat", "parrot"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def citrus_fruit(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "citrus_fruit"
    knowledge = "Grapes is a type of citrus fruit."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has deficiency of vitamin C. Doctor suggests him to consume more amount of vitamin C, So he goes to the supermarket to get his supplements with fruits.",
            "{name}'s doctor suggested him to consume more amount of vitamin C because of dificiency of vitamin c in his body and suggests to buy some fruits which are full of vitamin C."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have bought a grape fruit.",
        ]

        false_hypotheses = [
            "He could have bought a mango.",
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
            "What could be the fruit?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Jackfruit", "Apricot", "Grape fruit", "Mango"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def size_of_moon_sun(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "Size_of_moon_sun"
    knowledge = "Sun is the largest body and Earth is the fifth largest body in the solar system."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an astronomy major student. His assignment was to identify a body larger than Earth in the Solar System.",
            "{name} studies about the solar system for his science project. He has to identify a body that is bigger than earth in the solar system."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The body could have been Sun.",
        ]

        false_hypotheses = [
            "The body could have been Mercury.",
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
            "What could be the body?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Sun", "Jupyter", "Pluto", "Mercury"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def vegetables_and_fruits(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "vegetables_and_fruits"
    knowledge = "Fruits are seed-bearing structures developed from ovary of plant whereas vegetables are plant parts such as roots, leaves and stems."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} goes to a farm and sees an item growing on a tree. He cuts it open and he finds seeds in it.",
            "{name} is a farm owner, one day he saw an item on one of the tree, after cutting that item he finds seeds in it."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The item could have been a mango.",
        ]

        false_hypotheses = [
            "The item could have been a carrot.",
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
            "What could the item be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Carrot", "Mango", "Banana", "Potato"],
            answers_list=[1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def shortest_month(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "shortest_month"
    knowledge = "February is the shortest month of the year."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was short on cash and was eagerly waiting for his salary. He was relived because the current month was the shortest month of the year.",
            "{name}'s birthday comes in the current month. It is the shortest month out of all the twelve months."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The current month could be February.",
        ]

        false_hypotheses = [
            "The current month could be March.",
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
            "Which could be the current month?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["January", "February", "December", "November"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cause_of_fire(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "cause_of_fire"
    knowledge = "Gas leakage leads to fire."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s house caught fire when he was not at home. When he claimed for the insurance, the insurance company later told the reason for the fire.",
            "{name}'s house burned down when he was not at home. Later he got to know the reason of the fire after he claimed for insurance"
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The reason could have been a gas leak.",
        ]

        false_hypotheses = [
            "The reason could have been loud music.",
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
            "What could have been the reason given by the insurance company?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Gas leak", "Loud music", "exercise", "None"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def colour_change(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "colour_change"
    knowledge = "Mixing colours creates new colours. Red and yellow colour mix to form orange."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a painter and checked his paintbox and found that the container holding orange was empty. So he mixes the red colour with another colour.",
            "{name} mixed red colour with some other colour to get orange colour"
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The other colour could have been yellow.",
        ]

        false_hypotheses = [
            "The other colour could have been blue.",
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
            "Which could be the other colour?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Yellow", "Black", "Blue", "Pink"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def kangaroo(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "kangaroo"
    knowledge = "Kangaroo is effectively a five legged animal."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went on a trip to Australia. He was eager to see the five legged animal that is famous in Australia.",
            "{name} studied about a five-legged animal that is famous in Australia."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been a Kangaroo.",
        ]

        false_hypotheses = [
            "The animal could have been a Giraffe.",
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
            "What could have been the animal that {name} saw?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Kangaroo", "Cheetah", "Panther", "Tasmanian Wolf"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def physical_quantity(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "physical_quantity"
    knowledge = "Ratio attributes have a true zero and are always positive."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} recently went to a fair and measured a physical quantity on a scale and noticed that the value was always greater than zero.",
            "{name} saw a machine which was used to measure a physical quantity, he notices that the value was always greater than zero."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have measured weight.",
        ]

        false_hypotheses = [
            "He could have measured temperature.",
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
            "What could have been measured by him?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Weight", "Temperature", "Latitude", "Height"],
            answers_list=[0, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def giraffe_and_height(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "giraffe_and_height"
    knowledge = "Giraffe is the tallest animal among all the animals."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to a national park and was amazed to see an animal. This animal was taller than every other animal that was moving around in the wild.",
            "{name} saw pictures of different animals and saw picture of an animal whos was taller than any other animal which moved in nature."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been a Giraffe.",
        ]

        false_hypotheses = [
            "The animal could have been a Kangaroo.",
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
            "What could have been the animal?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Dog", "Lion", "Giraffe", "Zebra"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def no_of_hands(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "no_of_hands"
    knowledge = "All primates have two hands."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to an animal museum and saw several exhibits. One of the exhibit was very interesting since it had two hands",
            "{name} saw a two hand exhibit in an animal museum."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The exhibit could have been of an ape.",
        ]

        false_hypotheses = [
            "The exhibit could have been of an elephant.",
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
            "What could have been the animal?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Ape", "Gorilla", "Dog", "Elephant"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def worm(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "worm"
    knowledge = "Every worm has two sperm receptacles."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} in a science class was taught about the reproduction process of different species. His professor told the class that a species has two sperm receptacles.",
            "{name} was looking general facts about different things on internet, he came to know about a type of species that has two sperm receptacles."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The species could have been a worm.",
        ]

        false_hypotheses = [
            "The species could have been a pigeon.",
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
            "What could be the species that the professor is talking about?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Pigeon", "Dog", "Worm", "Eagle"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def tin_isotopes(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "tin_isotopes"
    knowledge = "Tin has the maximum number of stable isotopes."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was working on radioactive decay. He observed that an element was being formed out of different decay operations. The element that was being formed, had many isotopes.",
            "{name} works in a lab on radioactive decomposition. He observed that an element was being formed from different decadence operations and that had many isotopes."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The element could have been Tin.",
        ]

        false_hypotheses = [
            "The element could have been Copper.",
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
            "What could have been the element?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Tin", "Copper", "Boron", "Carbon"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def no_of_heart(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "No_of_heart"
    knowledge = "Some fishes like Octopus and Squids have three hearts whereas other fishes have only one heart"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went deep sea hunting and captured different animals for eating them. While dissecting them, he noticed that an animal had multiple hearts",
            "{name} had knowledge about different animals which can be found in animal. He was studying about a water animal who has multiple hearts"
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been Octopus.",
        ]

        false_hypotheses = [
            "The animal could have been Shark.",
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
            "What could have been the animal",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Whale", "Shark", "Tuna", "Squid"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def oxygen_lives(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "oxygen_lives"
    knowledge = "Animals require oxygen for survival."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a 3rd grader. His teacher told that all animals require an essential item for their survival.",
            "{name} was told taht all living beings use an essential item in order to live."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The essential item could be oxygen.",
        ]

        false_hypotheses = [
            "The essential item could be a laptop.",
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
            "What is that essential item?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Laptop", "Curtain", "Water", "Oxygen"],
            answers_list=[2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def alphabets(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "alphabets"
    knowledge = "English has total 26 alphabets."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a small kid and had just started to learn. In his test he was told to write all the 26 characters of the language.",
            "{name} is a kid who just started to go to school. In his first class he was taught to write the 26 alphabets of a language."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The language could have been English.",
        ]

        false_hypotheses = [
            "The language could have been Hindi.",
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
            "What could the language be that {name} was told to write?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["English", "Hindi", "Mandarin", "Hebrew"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def photosynthesis(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "photo"
    knowledge = "Photosynthesis is the process of converting light energy into chemical energy."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to a botanical garden and saw a graphic explaining photosynthesis in plants. It was displayed that the light energy is converted to another form of energy that plants can consume.",
            "{name} knows that in the process of photosynthesis the light energy gets converted into some other type of energy."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The other form of energy could be chemical energy.",
        ]

        false_hypotheses = [
            "The other form of energy could be mechanical energy.",
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
            "What could be the other form of energy?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Chemical Energy",
                          "Electrical Energy", "Thermal Energy", "None"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def first_day(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "first_day"
    knowledge = "Monday is first day of the week."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} received a mail to come and meet his professor for discussion on the paper on the first day of the coming week.",
            "{name} had a meeting on first day of the week."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The day could have been Monday.",
        ]

        false_hypotheses = [
            "The day could have been Tuesday.",
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
            "What could have been the day?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Sunday", "Monday", "Tuesday", "None"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def last_day(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "Last_day"
    knowledge = "Sunday is last day of the week."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s friends invited him to a party which was happening on the last day of the coming week.",
            "{name} went to a party on last day of the week."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The party could be on Sunday.",
        ]

        false_hypotheses = [
            "The party could be on Friday.",
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
            "What could be the day on which the party is happening?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Sunday", "Saturday", "Tuesday", "None"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def first_month(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "First_month"
    knowledge = "January is the first month of the year."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} asked his friend about his birthday and he replied that his birthday comes in the first month of the year.",
            "{name}'s friend's birthday comes in first month of the year."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "His friend's birthday could have been in January.",
        ]

        false_hypotheses = [
            "His friend's birthday could have been in March.",
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
            "What could have been the month?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["January", "February", "December", "July"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def last_month(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "Last_month"
    knowledge = "December is the last month of the year."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s teacher asks in class, in which month does christmas comes? and gives a hint that christmas comes in last month of the year.",
            "{name} was asked about the name of last month in which Christmas is celebrated."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have replied that the festival is on the month of December.",
        ]

        false_hypotheses = [
            "He could have replied that the festival is on the month of January.",
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
            "What could be the month that the teacher was talking about?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["January", "February", "December", "July"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def closest(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "closest"
    knowledge = "Mercury is the closest planet to the sun"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was given a question in his science exam to write the planet which is nearest to the sun.",
            "{name} studied on internet about a planet that is closer to the sun."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The planet could be Mercury.",
        ]

        false_hypotheses = [
            "The planet could be Venus.",
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
            "What could be the planet",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Earth", "Venus", "Mars", "Uranus"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def rainbow_colours(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "rainbow_colours"
    knowledge = "There are a total of seven colours in a rainbow"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was asked in a test to write the total number of colours in a rainbow, his answer was right and got full marks for that question",
            "{name} saw a rainbow, he counted the total number of colours in the rainbow and wrote the number in his diary so that he will not forget."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have written seven as the answer",
        ]

        false_hypotheses = [
            "He could have written eight as the answer",
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
            "What could be the answer given by him?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["five", "six", "seven", "eight"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def sport(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "sport"
    knowledge = "Baseball is the national sport of USA"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is fond of sports, and being a citizen of USA, he loves to play the national sport of USA.",
            "{name} is a national level champion of national sport of USA"
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The sport could be baseball",
        ]

        false_hypotheses = [
            "The sport could be cricket.",
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
            "What could be the sport that he loves?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Cricket", "Volley Ball", "Golf", "Baseball"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def dollar_cent(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "dollar_cent"
    knowledge = "one dollar is equal to 100 cents"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} makes a purchase of 3 dollars, and pays all the amount in denomination of one cent.",
            "{name} went to a supermarket and purchased something worth 3 dollars, he paid the full amount in denomenation of one cent "
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have given at most 300 coins of 1 cent.",
        ]

        false_hypotheses = [
            "He could have given at most 500 coins of 1 cent.",
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
            "How many cents could he give?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["200", "300", "400", "500"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def sfo(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "sfo"
    knowledge = "Golden Gate Bridge is located in San Fransisco, California"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} in his vacations went to visit the city in which GOlden Gate Bridge is located along with his parents.",
            "{name} has a conference in the city where which Golden Gate Bridge is located."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have gone to San Fransisco, California.",
        ]

        false_hypotheses = [
            "He could have gone to Phoenix, Arizona.",
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
            "He could have gone to which state?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["California", "Arizona", "Texas", "FLorida"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def dice(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numericalSG", "dice"
    knowledge = "A dice has distinct numbers from 1 to 6"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} and his friends were playing a game in which they had to get the number more than each other in order to win. His friend got 5 on the dice, but still {name} won.",
            "{name}'s friend rolls a dice and got 5, now {name} has to get a number more than 5 in order to win the game. After {name} rolls the dice, he winds the game."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have got 6 in the dice",
        ]

        false_hypotheses = [
            "He could have got 9 in the dice",
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
            "What could be the number?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["4", "5", "3", "6"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def norway(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numericalSG", "norway"
    knowledge = "In Norway, there is daylight for approximately 6 months"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} lives in a place, where the day does not goes dark for approx six months.",
            "{name} goes to a place for his vacation to a place where there is daylight for approx 6 months"
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The place could be Norway",
        ]

        false_hypotheses = [
            "The place could be USA",
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
            "What could be the place?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Mexico", "Norway", "USA", "India"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def chair_balance(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numericalSG", "chair_balance"
    knowledge = "A chair balances on at least 3 legs."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was standing in a queue since morning and got tired of standing. He saw a chair and decided to sit on it, but as soon as he sat on the char, he fell down",
            "{name} goes to a bank, but he had to wait because there were many people ahead of him, so decided to sit on the cair, but unfortunately he falls down as soon as he sits on the chair."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "It could have two legs.",
        ]

        false_hypotheses = [
            "It could have three legs.",
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
            "What could be the number of legs in it",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["4", "5", "1", "6"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def brain(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numericalSG", "brain"
    knowledge = "Among all the parts of brain, cerebrum is the largest part of the brain"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was curious to know the different parts of the brain, so he decided to learn about the part which consumes maximum volume of the brain.",
            "{name} is in a medical school and studies different parts of brain, he learns about that part which takes the major volume of the brain."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The part could be cerebrum.",
        ]

        false_hypotheses = [
            "The part could be cerebellum.",
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
            "What could be the part?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Cerebellum", "Cerebrum", "Brainstem", "None"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def airplane_speed(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numericalSG", "airplane_speed"
    knowledge = "An airplane runs at approx 200 mils per hour before take off"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was working on airplane design, and realized that plane was unable to take off as it's speed could have been low",
            "{name} is an airplane design engineer, and is working on a design of new model of airplane, he was not able to make the airplane fly into the air because of the less speed."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The speed could be less than 200 miles per hour.",
        ]

        false_hypotheses = [
            "The speed could be less than 400 miles per hour.",
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
            "What could be the speed of plane?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["190", "250", "500", "400"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def airplane_eng(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "airplane_eng"
    knowledge = "An airplane with multiple engines can even run on 1 engine"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "An airplane started it's journey, in between the journey, there was some technical default in the airplane and multiple engines of the plane failed, but still airplane was able to land safely.",
            "A plane began it's journey, there was some technical isuue on the plane because of which except one engine, all the other engines failed, still plane landed safely."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The plane could have at least 1 working engine.",
        ]

        false_hypotheses = [
            "The plane could have 0 working engine.",
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
            "What could be the number of working engines in the plane?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["0", "1", "2", "3"],
            answers_list=[1, 2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def alcohol(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "airplane_eng"
    knowledge = "Consuming too much alcohol may lead to liver disease."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} used to consume a lot of alcohol, because of which he faced a diseases and then, he had to stop drinking, otherwise he would have died.",
            "{name} is addicted to alcohol, but he had to stop the alcohol consumption because he was facing some disease, he would have dies if he had not stopped the alcohol consumption"

        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "It could have been a liver disease.",
        ]

        false_hypotheses = [
            "It could have been a knee injury.",
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
            "What could have been the disease?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Liver disease",
                          "Knee injury", "hand injury", "none"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def tailor(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "tailor"
    knowledge = "Job of a tailor is to stitch clothes"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to get some clothes stitched, so he went to a shop and got a suit.",
            "{name} had a family function for which he wanted some get some new clothes. So he decided to get them stitched. He went to a shop for this work."

        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have gone to a tailor.",
        ]

        false_hypotheses = [
            "He could have gone to a cobbler.",
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
            "He could have gone to who's shop",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Tailor", "Cobbler", "Mechanic", "None"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def fast_food(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "fast_food"
    knowledge = "Excessive fast food is injurious to health and can cause obesity."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went for a blood test,and got high cholesterol results.",
            "{name} has high cholestrol."

        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "It could have been because of eating excessive fast food.",
        ]

        false_hypotheses = [
            "It could have been because of doing excessive exercises.",
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
            "What could have been the reason?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["fast food", "exercise", "over speeding", "None"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def travel_air(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "travel_air"
    knowledge = "Air travel is faster than road travel"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to travel from Arizona to California in the shortest time possible. He decided to go by car, but he got late.",
            "{name} lives in arizona and had a conference in New York. He had to reach there in the shortest time possible so he decided to go on foot, but it was late."

        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have reached early if he would have traveled by flight.",
        ]

        false_hypotheses = [
            "He could have reached early if he would have traveled by bicycle.",
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
            "What could be the preferred mode of transportation?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Car", "Bus", "Bike", "Airplane"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cobbler(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "cobbler"
    knowledge = "Job of cobbler is to fix the shoes"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was going to a party, where he saw that his shoes were torn. He tried to fix them on his own but failed",
            "{name} went to a club, where his shoe got torn. Then he had to go to get his shoe fixed"

        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have gone to cobbler.",
        ]

        false_hypotheses = [
            "He could have gone to a tailor",
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
            "Whose shop he could go to fix the problem?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Cobbler", "Tailor", "Mechanic", "Driver"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def hearing(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "hearing"
    knowledge = "Hearing songs on loud volume may lead to hearing disabilities."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is fond of listening to music. He listens to music all the time. Over time he observed that because of some reason he has started to hear less from one of his ear.",
            "{name} likes to listen to music. He observed that he has begun to listen fewer than one of his ears."

        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The reason could be consistent hearing of loud music.",
        ]

        false_hypotheses = [
            "The reason could be eating too much.",
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
            "What could have been the reason?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Eating too much", "Sleeping too much",
                          "Snoring too much", "Listening to loud music"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def visual(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical_sg", "visual"
    knowledge = "More screen timing leads to eye sight problems"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is an engineer. He has to sit in front of computer the whole day in order to get the work done. His eyesight got decreased over time.",
            "{name} uses mobile phone too much. He realized one day that he was not able to see clearly and had weak eyes."

        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "It could be because of more screen time.",
        ]

        false_hypotheses = [
            "It could be because of drinking too much.",
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
            "What could have been the reason?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Eating too much", "Sleeping too much",
                          "Snoring too much", "More screen timing"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cube_side(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numericalSG", "cube_side"
    knowledge = "All the sides of a cube are equal."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} works in a toy shop. He is pasting 6 equal square shaped stickers on each face of the toy. Each side of this toy is now completely covered by this sticker.",
            "{name} is owner of a toy shop. He has a toy which has 6 equal square shaped walls."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The shape of the toy could be cube.",
        ]

        false_hypotheses = [
            "The shape of the toy could be cuboid.",
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
            "What could be the shape of the toy?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Cube", "Cylinder", "Cuboid", "Cone"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def fire_alarms(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numericalSG", "fire_alarms"
    knowledge = "Fire Alarms helps in alerting the people about fire."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was sleeping after coming from work, suddenly he heard a sound and saw a fire in his house.",
            "{name} heard a loud noice from neighbour's house and realized that there was a fire at his neighbours house."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The sound could have been of fire alarm.",
        ]

        false_hypotheses = [
            "The sound could have been his neighbour shouting.",
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
            "What could be the reason for sound?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Fire alarm", "Car alarm", "Door Ring", "None"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances
