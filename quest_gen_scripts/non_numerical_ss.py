import util
import random
import pprint
import numpy as np


def mechanic(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "mechanic"
    knowledge = "A mechanic is a person who repairs faulty vehicles."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to repair an item and called a mechanic.",
            "{name} called a mechanic repair an item, because he was getting late to reach his office."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The item could be a car.",
        ]

        false_hypotheses = [
            "The item could be a table.",
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
            "What could be the item that {name} wanted to repair?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["car", "sofa", "blender", "cloth"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def dentist(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "dentist"
    knowledge = "A job of a dentist is to diagnose & fix problems in the mouth."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to dental clinic to get treatment for a problem in his body.",
            "{name} was not able to properly. He went to the dental clinic to get treatment."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He went to get treatment for his cavities.",
        ]

        false_hypotheses = [
            "He went to get treatment for hair fall.",
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
            "What could be the problem {name} went to dental clinic for?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["tooth ache", "cavities",
                          "acidity", "blood pressure"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cook(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "cook"
    knowledge = "A cook is a person who prepares food in the restaurant."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A restaurant recently hired few cooks for preparing an item.",
            "{name} is opening a restaurant near his home. He hired few cooks to prepare an item."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The item could have been pasta.",
        ]

        false_hypotheses = [
            "The item could have been a pot.",
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
            "What item could have been prepared by the cook?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["pasta", "noodles", "pot", "lock"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def composer(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "composer"
    knowledge = "A composer is a person who writes music."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A theatre recently invited a world famous composer for their final act.",
            "A popular theater in New York city is planning for their final act. They invited a world famous composer for this act."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have made a background score for the act."
        ]

        false_hypotheses = [
            "He could have painted the theatre for the act.",
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
            "What activity could have been performed by him?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cleaning", "making music", "marketing", "painting"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def plumber(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "plumber"
    knowledge = "A plumber is a person who fixes drainage and water related problems."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is having a major problem in his house and he hired a plumber to fix it",
            "A restaurant is having a problem they hired a plumber to fix it."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The problem could be leakage in the restrooms.",
        ]

        false_hypotheses = [
            "The problem could have been related to termites.",
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
            "What could be the problem faced by {name}?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["termite infestation",
                          "water leak", "internet down", "fuse blown"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def photographer(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "photographer"
    knowledge = "A photographer is a person who works with cameras."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is going to marry his fiance next month and he hires a photographer.",
            "{name}'s is marrying Janice next month. {name} hired a photographer for the wedding."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have been hired to click pictures.",
        ]

        false_hypotheses = [
            "He could have been hired to serve food.",
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
            "What could have been the job for which he was hired?"
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["take photos", "officiate the wedding",
                          "flower girl", "ring bearer"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def architect(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "architect"
    knowledge = "An architect is involved in the construction of buildings."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "An IT company wants to design their headquarters at Texas state and hired an architect.",
            "CEO of company ABC decided to expand their services. He decided to open a new office building in Tempe. The CEO of the company hired an architect and explained him the agenda."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have designed the building.",
        ]

        false_hypotheses = [
            "He could have planted trees.",
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
            "What could have been done by him as a part of his job?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["designing building", "cleaning",
                          "watering plants", "repairing vehicles"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def painter(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "painter"
    knowledge = "A painter is a person who paints."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A {name} wants to renovate his house and hired a painter. The painter used certain objects to finish the job.",
            "A shopkeeper hired a painter to renovate his shop. To paint the shop the paint used some tool to finish the job."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have used a paint brush for his job.",
        ]

        false_hypotheses = [
            "He could have used a vacuum cleaner.",
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
            "What could have been the item that he used to do the job?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["paint brush", "scissors", "knife", "hammer"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def pilot(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "pilot"
    knowledge = "A pilot is a person who flies the airplane."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "An airplane is about to take off, and a person entered in the cockpit of the plane.",
            "{name} saw a person entering the cockpit of the plane."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The person entered could be pilot.",
        ]

        false_hypotheses = [
            "The person entered could be a waiter.",
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
            "Whom could have been the person entered in the cockpit?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["gardener", "pilot", "architect", "photographer"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def electrician(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "electrician"
    knowledge = "An electrician is a person who fixes problems related to electrical devices."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} hired an electrician to fix an item in his home.",
            "A shopkeeper hired an electrician to fix some item in his shop."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The item could be an electrical socket.",
        ]

        false_hypotheses = [
            "The item could be table.",
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
            "What could be the item that he came to fix?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["garden", "table", "kitchen", "fan"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def lawyer(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "lawyer"
    knowledge = "A lawyer is a person who practices law and advises clients on aspects of all law."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is starting his new company and he hired Lawyer to advise on certain laws for the company.",
            "{name} hired lawyer to advise certain laws for his company."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The person could have been hired to counsel on tax regulations of the company.",
        ]

        false_hypotheses = [
            "The person could have been hired to counsel on mental illness.",
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
            "What could be the reason he was hired?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["programming", "cooking",
                          "tax laws", "taking photograph"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def dietitian(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "dietitian"
    knowledge = "A dietitian is an expert who counsels clients on nutrition issues and healthy eating habits."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is obese and wants to lose weight. He goes to a person to seek advise on eating habits.",
            "After hearing some health hazards of being overweight, {name} decided to lose weight starting consulting a person."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have taken counsel from a dietitian.",
        ]

        false_hypotheses = [
            "He could have taken counsel from a psychiatrist.",
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
            "Whom did {name} called to counsel for his goal?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["mechanic", "gardener", "electrician", "dietitian"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def population_growth(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "population_growth"
    knowledge = "A region's population grows either by birth or immigration."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "It is observed that there has been an increase in people at Tempe recently.",
            "In a conversation with his friend, {name} said that he observed that there has been an increase in people at Phoenix recently."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "It could be because of immigration.",
        ]

        false_hypotheses = [
            "It could be because of many people are eating more than usual.",
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
            "Wha could be reason for increase in population?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["divorce", "consumption of food",
                          "death", "immigration"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def starch(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "starch"
    knowledge = "Foods like potatoes, corn and oat are rich in starch, whereas foods like carrots, cabbage and cucumber doesn't contain starch."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has a chemistry practical session, and learned that drops of iodine solution turn blue-black if it is in contact with starch. He accidentally spills some solution on an object that turned blue-black.",
            "{name} learned that the drops of iodine solution become black blue if it is in contact with a starch substance. To understand this chemical reaction, his professor conducted a practical session. The professor asked all students to put a few drops of iodine solution on an object which turned into blue-black color."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could be potato.",
        ]

        false_hypotheses = [
            "The object could be mango.",
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
            options_list=["cabbage", "potatoes", "corn", "oat"],
            answers_list=[1, 2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def spider(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "spider"
    knowledge = "Animals like spider, scorpion and tick have 8 legs."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw an animal crawling on his arm. He got scared and threw the animal away and noticed that it has more than 6 legs.",
            "{name} saw an animal in a cage. The animal was moving around in the cage using its 8 legs."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be a spider.",
        ]

        false_hypotheses = [
            "The animal could be a dog.",
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
            "What could the animal be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["spider", "dog", "scorpion", "cat"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def tusk(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "tusk"
    knowledge = "Animals like elephant, walrus and wild boar have tusks."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A multinational team led by the University of Oxford’s Pitt Rivers Museum recently found a ancient cargo. The cargo was mostly consisting of ivory that is obtained from an animal.",
            "An archaeology team recently found a fossil. The fossil was remains of animals that had tusks."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be an elephant.",
        ]

        false_hypotheses = [
            "The animal could be a spider.",
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
            "What could the animal be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["elephant", "walrus", "scorpion", "dog"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def sleep_standing(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "sleep_standing"
    knowledge = "Animal like horse can sleep while standing up."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A zoologist was studying the sleeping habits of various animals. While researching about this he came across an animal that could sleep while standing up.",
            "In a research study on sleeping habits of animals, {name} came to know that there is an animal that could sleep while standing up."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be a horse.",
        ]

        false_hypotheses = [
            "The animal could be a cat.",
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
            "What could the animal be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cat", "dog", "scorpion", "horse"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def elephant_jump(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "elephant_jump"
    knowledge = "An adult elephant can not jump."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw various animals in circus and he saw only one animal which couldn't jump.",
            "Once {name} visited circus. He observed that only one animal was not jumpings."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be elephant.",
        ]

        false_hypotheses = [
            "The animal could be dog.",
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
            "What could the animal be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["elephant", "lion", "cat", "dog"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def seed_out(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "seed_out"
    knowledge = "Strawberries are the only fruit that grows seeds on the exterior portion of the fruit."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to supermarket to buy some fruits. He liked one fruit that have seeds attached to the outside of the fruit.",
            "{name} was fascinated by reading about a fruit which has seeds attached to the exterior of the fruit."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The fruit could be strawberries.",
        ]

        false_hypotheses = [
            "The fruit could be orange.",
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
            options_list=["apple", "orange", "mango", "strawberry"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def tomatoes(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "tomatoes"
    knowledge = "Tomatoes are fruits, not vegetables."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A lab is researching about how a fruit is grown. They want different types of fruits for their research.",
            "Dr.{name} is researching about fruits and time to cultivate them. His lab wants various fruits in his research study."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The lab could have included tomatoes in their research.",
        ]

        false_hypotheses = [
            "The lab could have included potatoes, onion or cabbage.",
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
            "Which fruit among these the lab could include for their research?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["tomatoes", "potatoes", "onion", "cabbage"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def animal_stripes(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "tomatoes"
    knowledge = "Animals like tiger and zebra have stripes on their body."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "On a visit to national park, {name} and his brother saw an animal that had stripes like shape on its body.",
            "{name} and his brother were watching a movie in which they saw an animal with stripes hunting other animals."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be a tiger.",
        ]

        false_hypotheses = [
            "The animal could be a donkey.",
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
            "What could the animal be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["donkey", "lion", "tiger", "zebra"],
            answers_list=[2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def owl_rotate(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "owl_rotate"
    knowledge = "Bird like owl can rotate its head upto 270 degrees."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a wildlife photographer. Today he clicked a picture of a bird which could rotate its neck backwards.",
            "{name} got scared when he saw a bird that turned its neck backwards."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The bird could have been an owl.",
        ]

        false_hypotheses = [
            "The bird could have been a pigeon.",
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
            "What could be the bird?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["pigeon", "lion", "owl", "zebra"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bat_sleep(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "bat_sleep"
    knowledge = "Animals like bats sleep while hanging on trees upside down."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "On his way back home, {name} saw an animal sleeping in an upside down position.",
            "{name} read about an animal which can fly and sleep while hanging on the tree in upside down manner in an encyclopedia."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been a bat.",
        ]

        false_hypotheses = [
            "The animal could have been a parrot.",
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
            "What could the animal be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["pigeon", "bat", "owl", "zebra"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def electric_eel(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "electric_eel"
    knowledge = "Animal like electric eel can give an electric shock of roughly 400 volts that knock down a human body."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was watching a show on television and learnt that there is a fish hunts its prey by giving them an electric shock.",
            "{name} was seeing a show on wildlife channel on television. He saw a fish that hunts its prey by giving them an electric shock."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The fish could be an electric eel.",
        ]

        false_hypotheses = [
            "The fish could be a goldfish.",
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
            "What could be the fish?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["goldfish", "octopus", "electric eel", "zebra"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def hammer_fish(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "hammer_fish"
    knowledge = "Animal like hammerhead fish have a head shaped similar to hammer."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A marine biologist is studying different shapes of fish. He found a peculiar fish whose head resembles a tool.",
            "During researching about different types of fish. Marine biologist found a peculiar fish whose head resembles a tool."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The fish could be hammerhead fish.",
        ]

        false_hypotheses = [
            "The fish could be jellyfish.",
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
            "What could be the fish?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["hammerhead", "octopus", "goldfish", "whale"],
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

    category, subcategory = "non_numerical", "kangaroo"
    knowledge = "Kangaroo mostly hops for their movement"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} went to a safari on his school trip to Australia. He was an peculiar animal that was jumping a lot to move around.",
            "In a movie, {name} saw a peculiar animal that was jumping a lot to move."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be kangaroo.",
        ]

        false_hypotheses = [
            "The animal could be camel.",
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
            "What could the animal be?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["elephant", "octopus", "bat", "kangaroo"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def snake_move(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "snake_move"
    knowledge = "Animals like snake doesn't have legs or hands."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw an animal crawling in the forest. The animal had no legs and was moving on the ground.",
            "{name} got scared by seeing an animal crawling on the ground. The animal did not have any legs to move"
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be a snake.",
        ]

        false_hypotheses = [
            "The animal could be a kangaroo.",
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
            "What could the animal be?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["tiger", "lion", "snake", "giraffe"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def hot_cold_air(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "hot_cold_air"
    knowledge = "Hot air is lighter than cold air."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is decorating the room for his brother's birthday and filling one balloon with hot air and the other with cold air. One of the ballon is floated to the top of the room.",
            "{name} has organized a welcome party for his friend. He was filling a balloon with hot air and the other with cold air. He noticed that one of the balloons was floating at the top of the room."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The balloon could be filled with hot air.",
        ]

        false_hypotheses = [
            "The balloon could be filled with cold air.",
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
            "The balloon could be filled with?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["water", "gasoline", "cold air", "hot air"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def soccer_basketball(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "soccer_basketball"
    knowledge = "Sports like soccer is played with legs whereas sports like basketball is played using arms."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to join a team in his school. He saw some students playing a sport which was played using legs or kicking the ball.",
            "{name} was fascinated by a sport played on a school playground. He observed that the students were using their legs to pass the ball and score a goal."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "Students could be playing soccer.",
        ]

        false_hypotheses = [
            "Students could be playing basketball.",
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
            "What sport could students be playing?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["soccer", "badminton", "basketball", "running"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def badminton_tennis(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "badminton_tennis"
    knowledge = "Sports like badminton and tennis is played using rackets."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wants to join a team in his school. He saw some students playing a sport which was played using rackets.",
            "A sports complex organized a competition for students. {name} went to support his friend and saw many students playing a sport with rackets."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "Students could be playing tennis.",
        ]

        false_hypotheses = [
            "Students could be playing soccer.",
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
            "What sport could students be playing?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cricket", "badminton", "baseball", "tennis"],
            answers_list=[1, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def fertilizer(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "fertilizer"
    knowledge = "Soil becomes fertile with manure and fertilizer."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A farmer is not able to earn enough to support his family. He wants to make his agricultural land more fertile by adding an item to increase the production of crops.",
            "{name} added an item to his flower plants, since they were not blooming."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have added fertilizer.",
        ]

        false_hypotheses = [
            "He could have added gasoline.",
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
            "What could be added by him?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["manure", "gasoline", "plastic", "fertilizer"],
            answers_list=[0, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def thorn_flower(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "thorn_flower"
    knowledge = "Flowering plants like roses and firethorn have thorns whereas daisy and lily don't have thorns."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "While plucking flowers from the garden {name} got pricked.",
            "{name} is the owner of a flower shop. In the morning, he went to his garden to pluck some flowers, during which he got pricked by one of the plants."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The plant could be of rose.",
        ]

        false_hypotheses = [
            "The plant could be of daisy.",
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
            "What could be the plant?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["rose", "firethorn", "lily", "daisy"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def spider_web(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "spider_web"
    knowledge = "Animals like spider make webs to trap insects."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} just moved to an old house. He saw some insects stuck on webs.",
            "{name} was researching on how an animal hunts its prey. He read about one animal that builds a web to trap insects."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The webs could be made by a spider.",
        ]

        false_hypotheses = [
            "The webs could be made by a cow.",
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
            "What could the animal be?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cow", "spider", "mosquito", "daisy"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def birds_fly(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "birds_fly"
    knowledge = "Birds like ostrich and penguin can't fly whereas crow, parrots, and kingfisher can fly."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw an bird that couldn't fly,and it was running around in the national park.",
            "{name} was roaming around in the national park. He saw a bird that couldn't fly."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The bird could be an ostrich.",
        ]

        false_hypotheses = [
            "The bird could be a pigeon.",
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
            "What could be the bird?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["ostrich", "crow", "woodpecker", "lion"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def birds_fly2(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "birds_fly2"
    knowledge = "Birds like penguin can't fly and live in colder regions whereas crow, parrots, and kingfisher can fly."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} visited Antarctica and saw a bird that couldn't fly and was walking on the ice.",
            "{name} was sailing on a boat near Antarctica. He saw a bird that could not fly and was walking on the ice."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The bird could be a penguin.",
        ]

        false_hypotheses = [
            "The bird could be a woodpecker.",
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
            "What could be the bird?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cheetah", "crow", "woodpecker", "penguin"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def vegetables_soil(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "vegetables_soil"
    knowledge = "Vegetables like cabbage, cauliflower and broccoli grow above soil whereas carrot, onion and potatoes grow under soil."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is teaching his son how to collect the vegetables. His son picked some vegetables from the farm, which were grown above the soil.",
            "A farmer is collecting some vegetables from his farm. He picked all the vegetables which were grown above the soil."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The vegetable could be a cabbage.",
        ]

        false_hypotheses = [
            "The vegetable could be a carrot.",
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
            "What could be the vegetable?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cabbage", "carrot", "cauliflower", "apple"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def pincer(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "pincer"
    knowledge = "Animals like crabs and lobsters have pincers at the front of their body to grab things."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} saw an interesting animal at the food shop. He asked the shopkeeper to remove the pincers of the animal as he doesn't like that part.",
            "{name} went shopping to buy some food. Since he did not like to eat the pincers, he asked the shopkeeper to remove this part from the animal."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be crab.",
        ]

        false_hypotheses = [
            "The animal could be salmon.",
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
            "Which could be the animal?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["lobster", "jellyfish", "goldfish", "crab"],
            answers_list=[0, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def crab_walk(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "crab_walk"
    knowledge = "Animals like crab walk sideways."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "On a trip to beach, {name} saw an animal that was walking in sideways direction.",
            "{name} saw an animal on a beach when he went to travel with his friends to Goa. "
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could be a crab.",
        ]

        false_hypotheses = [
            "The animal could be a snail.",
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
            "Which could be the animal?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["shark", "jellyfish", "goldfish", "crab"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def helicopter(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "helicopter"
    knowledge = "A helicopter is a vehicle that can fly by rotating its blades at very high speed."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A minister is travelling from his office to a place to attend a rally and he used a vehicle that uses rotor blades to fly.",
            "A businessman was traveling via a vehicle that uses rotating blades to fly."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The vehicle could be a helicopter.",
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
            "Which could be the vehicle?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["car", "bike", "helicopter", "train"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def pearl(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "pearl"
    knowledge = "Oyster make pearls inside their shell."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "A shop sells  pearls. The shop owner asked {name} to collect more pearls for the shop.",
            "Due to recent popularity of pearl, the shopkeeper want to restock the items. The shopkeeper hired a Tom to collect more pearls for the store."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could be collecting oysters.",
        ]

        false_hypotheses = [
            "He could be collecting reefs.",
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
            "What he could be collecting?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["car", "sharks", "oyster", "crab"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def anglerfish(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "anglerfish"
    knowledge = "Anglerfish has a filament protruding from its head that illuminates."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "During a deep diving class, {name} saw a fish with an illuminating object attached to its head which attracts other small fishes.",
            "{name} is sharing his travel experience with his friends. He was telling about his diving experience in which he saw a fish with an illuminating object attached to his head that attracts other small fish."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The fish could be an anglerfish.",
        ]

        false_hypotheses = [
            "The fish could be a whale.",
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
            "What could the animal be?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["anglerfish", "sharks", "oyster", "crab"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def kingfisher(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "kingfisher"
    knowledge = "Birds like kingfisher and albatross hunt fishes whereas birds like woodpecker, parrot and sparrow don't eat fish."

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is a photographer. He clicked many photographs of a bird hunting a fish.",
            "{name} liked a photograph in which a bird was hunting a fish. Inspired by this photograph he clicked some photographs of the same bird."

        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have taken photographs of kingfisher.",
        ]

        false_hypotheses = [
            "He could have taken photographs of sparrow.",
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
            "What could the animal be photographed by him?",
        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["kingfisher", "sharks", "oyster", "crab"],
            answers_list=[0],
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
#     template_binary_instances, template_mcq_instances = dietitian(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
