import util
import random
import pprint
import numpy as np


def teeth_cleaner(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "teeth_cleaner"
    knowledge = "A human can brush their teeth with toothpaste but not with face or body cream."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was ready to start his day and used an item to brush his teeth.",
            "{name} used an item to wash his teeth."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The item could have been a toothpaste.",
        ]

        false_hypotheses = [
            "The item could have been a face cream.",
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
            "What could be the item used?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Face cream", "Body cream",
                          "Shaving cream", "Toothpaste"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def game_object(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "game_object"
    knowledge = "The game cricket can be played using the cricket ball but not with baseball, football, or volley ball."
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} planned to play cricket and took his bat, ball.",
            "{name} planned to take his bat, ball to play cricket."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The ball could have been a cricket ball.",
        ]

        false_hypotheses = [
            "The ball could have been a football.",
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
            "What could be the ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Baseball", "Football",
                          "Volleyball", "Cricket ball"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def purchase_tennisball(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "purchase_tennisball"
    knowledge = "The sport tennis can be played using the tennis ball but not with baseball, football, or volley ball."
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} visited a shop to purchase a ball for playing tennis.",
            "{name} visited a store to buy a ball to play tennis."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The ball could have been a tennis ball.",
        ]

        false_hypotheses = [
            "The ball could have been a volleyball.",
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
            "What could be the ball that they could not prefer to play the game tennis?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Baseball", "Football", "Volleyball", "Tennis ball"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def drinking_liquid(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "drinking_liquid"
    knowledge = "A human can drink water or juices but not oil, kerosene."
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} walked for a long time under the sun and became thirsty. To quench his thirst, he drank a liquid.",
            "{name} walked for a long time in the sun and drank a liquid to quench his thirst."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The liquid could have been water.",
        ]

        false_hypotheses = [
            "The liquid could have been kerosene or oil.",
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
            "What could be the liquid?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Oil", "Kerosene", "Juice", "Water"],
            answers_list=[2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def purchase_football(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "purchase_football"
    knowledge = "The sport soccer can be played using the football but not with baseball, or volley ball."
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} visited a shop to purchase a ball for playing the soccer sport.",
            "{name} visited a store to buy a ball to play soccer."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The ball could have been the football.",
        ]

        false_hypotheses = [
            "The ball could have been a baseball.",
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
            "What could be the ball?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Baseball", "Football", "Volleyball", "Tennisball"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def measure_meter(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "measure_meter"
    knowledge = "Atmospheric pressure can be measured through Barometer but not through any other meter like hygrometer, multimeter. "
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was observing the climatic changes for which he needs a device to calculate the atmospheric pressure.",
            "{name} was watching climate changes for which a device needs to calculate atmospheric pressure."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The device could have been a Barometer.",
        ]

        false_hypotheses = [
            "The device could have been a Hygrometer.",
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
            "What could the device be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Hygrometer", "Water level meter",
                          "Galvanometer", "Barometer"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def wood_and_termites(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "wood_and_termites"
    knowledge = "Termites can chew the wood and destroy anything that is made of wood."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has a beautiful wooden house but it was damaged due to insects.",
            "{name}'s wooden house was damaged due to insects.",
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The insects could have been termites.",
        ]

        false_hypotheses = [
            "The insects could have been ants.",
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
            "What could be the insect?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Ants", "Bed Bugs", "Lice", "Termites"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def clouds_and_matter(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "clouds_and_matter"
    knowledge = "The water that makes up clouds is in liquid or ice form."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} kept a bucket of water outside the house and the water level decreased due to evaporation.",
            "{name} kept a bucket of water out of the house and the water in the bucket decreased due to evaporation."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The water could have been evaporated to form clouds.",
        ]

        false_hypotheses = [
            "The water could have been evaporated to form ice cream.",
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
            "What could have happened to the evaporated water?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Form into clouds", "Form into cool drinks",
                          "Form into juice", "Form into ice-cream"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def distance_measure(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "distance_measure"
    knowledge = "An odometer is used to measure the distance traveled by car."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} headed to office from home in his car, he wanted to know the distance between his home and office, and he used a device to calculate it.",
            "{name} went to the office from home in his car, and used a device to calculate the distance between his home and office."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The device could have been an odometer.",
        ]

        false_hypotheses = [
            "The device could have been a multimeter.",
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
            "What could be the device used ?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["odometer", "multimeter", "ammeter", "galvanometer"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def heat_flow(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "heat_flow"
    knowledge = "Heat always flows from high temperature body to low temperature body."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} purchased snacks for the picnic, which includes hot chocolate, hot pasta, ice cream, and cool drinks. {name} carried all the snacks together in a single bag.",
            "{name} bought snacks for the picnic, which includes hot chocolate, hot pizza, ice cream and cold drinks and took all of them together in a single bag."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The temperature of the ice cream could have increased.",
        ]

        false_hypotheses = [
            "The temperature of the ice cream could have decreased.",
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
            "What could be the items whose temperature could have increased?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["ice-cream", "cool drinks",
                          "hot chocolate", "hot pasta"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def current_flow(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "current_flow"
    knowledge = "Metals are good conductors of electricity whereas insulators are bad conductors of electricity."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} switched on a short-circuited switch using an object instead of his bare hands. {name} got a shock.",
            "{name} got a shock when he switched on a short-circuited switch using an object instead of his bare hands."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could be a copper stick.",
        ]

        false_hypotheses = [
            "The object could be a Rubber stick.",
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
            "What could be the object used?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Copper stick", "Rubber stick",
                          "Steel holder", "Glass rod"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def fire_proof(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "fire_proof"
    knowledge = "Fire-retardants like concrete can withstand extremely high temperatures and help to slow the spread of a fire whereas cotton cannot."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s house caught fire, and a fire engine arrived late. Some objects in the house reduced the flow of heat in the meantime.",
            "{name}'s house caught fire, and some objects in the house reduced the flow of heat in the meantime."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could be a concrete wall.",
        ]

        false_hypotheses = [
            "The object could be a cotton curtains.",
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
            "What could be the objects?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["concrete", "Fire-Bricks",
                          "Fire-Rate Doors", "Cotton curtains"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def acids_blue_to_red(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "acids_blue_to_red"
    knowledge = "Acids turn blue litmus paper to red."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is performing experiments in a chemistry lab where he is given some substances that turn blue litmus paper to red.",
            "{name} is given some substances which turn litmus paper from blue litmus to red."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The substances could have been Hydrochloric acid or Sulphuric acid.",
        ]

        false_hypotheses = [
            "The substances could have been Calcium Hydroxide or Ammonia.",
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
            "What could the substances be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["HCl", "H2SO4", "Ammonia", "Calcium Hydroxide"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def bases_red_to_blue(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "bases_red_to_blue"
    knowledge = "Bases turn red litmus paper to blue."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was working in a science fair and suddenly spilled the liquid in his hand onto the red litmus papers placed beside him, which changed the color to blue.",
            "{name} is given some substances which turn litmus paper from red litmus to blue."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The liquid could  have been  Lithium Hydroxide, Potassium Hydroxide.",
        ]

        false_hypotheses = [
            "The liquid could have been HCl, H2SO4.",
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
            "What could be the liquid ?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["HCl", "H2SO4",
                          "Lithium Hydroxide", "Potassium Hydroxide"],
            answers_list=[2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def stomach_pain_test(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "stomach_pain_test"
    knowledge = "Endoscopy is a nonsurgical procedure used to examine a person's digestive tract."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was suffering from stomach pain and so visited a doctor and he asked {name} to undertake a test which showed ulcers in the stomach.",
            "{name} was suffering from stomach pain, and took a test that showed ulcers in his stomach."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The test could have been endoscopy.",
        ]

        false_hypotheses = [
            "The test could have been colonoscopy.",
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
            "What could be the test undertaken?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Endoscopy", "Colonoscopy", "XRay", "MRI Scan"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def honey_stays_fresh(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "honey_stays_fresh"
    knowledge = "The only food that doesn't spoil is honey."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} found some food items in his kitchen rack unused for a long time where all of them got spoiled.",
            "{name} found some food on his kitchen shelf unused for a long time, where they all spoiled."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The items could have been eggs or fruits.",
        ]

        false_hypotheses = [
            "The item could have been honey.",
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
            "What could be the items?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["fruits", "vegetables", "milk", "honey"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def corn_farm(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "corn_farm"
    knowledge = "Corn is grown on every continent except antarctica."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} started traveling to different countries and planted the corn seeds wherever he went. All the planted seeds were harvested after some days.",
            "{name} began traveling to different countries and planted corn seeds wherever he went. All planted seeds were harvested after a few days."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The places could have been US or India.",
        ]

        false_hypotheses = [
            "The place could have been Antarctica.",
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
            "What could the places be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["India", "Antarctica", "US", "Australia"],
            answers_list=[0, 2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def blood_color(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "blood_color"
    knowledge = "The blood of mammals is red, the blood of insects is yellow in color, and the blood of lobster is blue."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was a reporter and went to cover the news related to natural disaster incidents that occurred on the beach nearby. {name} found some dead bodies where the area is completely covered with the blood of red and blue color.",
            "{name} was a reporter and went to cover the news related to the natural incidents of disasters that occurred on the nearby beach. {name} found some corpses where the area is completely covered with red and blue blood."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The dead bodies could be of dolphins.",
        ]

        false_hypotheses = [
            "The dead bodies could be of insects.",
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
            "What could the dead bodies be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Dolphins", "insects", "Lobster", "dog"],
            answers_list=[0, 2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def water_and_plants(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "water_and_plants"
    knowledge = "Desert plants like wildflowers and succulents need not require to water them daily."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} have many plants at his home. {name} had to leave for an educational trip for a week where no one was there to take care of the plants at his home. After the return from a trip, all the plants died except a few.",
            "{name} had to go to an educational trip for a week, where no one was there to take care of the plants at home. After the return of a trip, all the plants died except some."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The plants that were alive could have been cactus or Aloe.",
        ]

        false_hypotheses = [
            "The plants that were alive could have been rose or hibiscus.",
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
            "What could be the plants that were alive?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Rose", "Hibiscus", "Cactus", "Aloevera"],
            answers_list=[2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def surface_tension_and_insects(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "surface_tension_and_insects"
    knowledge = "Force exerted by any object like an ant on the water less than the surface tension of water makes that object float on the surface of the water whereas elephants can not."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was sitting near a riverbank and able to see some objects floating on the surface of the water.",
            "{name} saw some objects floating on the surface of the water while sitting near a river bank."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The object could have been an ant.",
        ]

        false_hypotheses = [
            "The object could have been an elephant.",
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
            "What could be the floating object?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["ant", "flies", "plastic spoon", "Iron rod"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def waves_and_wavelengths(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "waves_and_wavelengths"
    knowledge = "Human eye can detect wavelengths from 380 to 700 nanometers that are visible region waves but can not detect Gamma or Cosmic rays."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was working in the lab for his experiments where he could not see any of the EM waves he used for the testing.",
            "{name} was working in the laboratory of his experiments where he could not see any of the waves of EM that he used for the tests."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The EM waves could have been Gamma rays or Radio rays.",
        ]

        false_hypotheses = [
            "The  EM waves could have been the visible region rays.",
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
            "What could be the EM waves ?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Gamma rays", "Cosmic rays",
                          "Radio waves", "visible waves"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def cannibalism_animals(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "cannibalism_animals"
    knowledge = "Animals like a polar bear that eat their kind is an example of cannibalism."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} maintains a zoo where he did not feed the animals for some days and figured out that the parent animal ate some.",
            "{name} works in a zoo where he did not feed animals for a few days and discovered that an animal ate some animals of his species."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been a polar bear.",
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
            "What could be the animals?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["polar bears", "chickens", "dogs", "horse"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def summer_and_cotton(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "summer_and_cotton"
    knowledge = "Cotton is a soft, lightweight, breathable fabric that soaks up sweat, allowing heat to escape the body and for you to stay cool."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} got a job for the summer holidays where he needs to travel daily to and fro from his home to office. {name} planning to purchase new clothes to stay cool in the hot summer.",
            "{name} got a job for summer vacations where he needs to travel daily from one side of his home from his home to the office. {name} plans to buy new clothes to stay fresh in hot summer."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The type of clothes could have been cotton shirts and pants.",
        ]

        false_hypotheses = [
            "The type of clothes could have been Nylon shirts.",
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
            "What could be the cloth type to choose?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["cotton", "woolen", "silk", "Nylon"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def diwali_and_crackers(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "diwali_and_crackers"
    knowledge = "When subjected to fire aluminum powder, sulphur and potassium nitrate produce sound, while barium nitrate (green) and strontium nitrate (red) emit light. The aluminum powder will sparkle."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is planning to make crackers for the Diwali Festival. {name} wants only light but not noise as his dog is afraid of the cracker sounds.",
            "{name} plans to make crackers and wants light but no noise on the crackers."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The composition of crackers could have been barium nitrate.",
        ]

        false_hypotheses = [
            "The composition of crackers could have been potassium nitrate.",
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
            "What could not be the composition of the crackers?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Potassium nitrate", "Barium nitrate",
                          "Strontium nitrate", "Aluminium powder"],
            answers_list=[0, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def repitiles_and_family(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "repitiles_and_family"
    knowledge = "Reptiles like snakes, lizards are a group of air-breathing vertebrates that have internal fertilization, amniotic development, and epidermal scales covering part or all of their body."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was playing in the ground, and he saw an animal moving over the eggs laid which have the skin covered with small, hard plates called scales.",
            "{name} was playing on the floor, and saw an animal moving that have the skin covered with hard scales."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The animal could have been a snake.",
        ]

        false_hypotheses = [
            "The animal could have been a dog.",
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
            options_list=["snake", "lizard", "dog", "cat"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def storage_device(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "storage_device"
    knowledge = "A storage device like Pen drive, sd card refers to a computing hardware used to store information permanently or temporarily."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to free his laptop with all the used memory, so he planned to purchase a storage device to transfer all the data and free his laptop memory.",
            "{name} wanted to release his laptop with all the memory used, so he planned to buy a storage device to transfer all the data."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The device could have been Pen drive.",
        ]

        false_hypotheses = [
            "The device could have been a keyboard.",
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
            "What could be the storage device?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["pen drive", "sd card",
                          "hard drive disks", "Joystick"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def root_vegetables(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "root_vegetables"
    knowledge = "Root vegetables like carrot are the fleshy enlarged root of a plant that is used as a vegetable."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was interested in growing vegetables in his garden, particularly the one that grows under the soil.",
            "{name} was interested in growing vegetables that grow under the ground."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The vegetables could have been carrots or beetroots.",
        ]

        false_hypotheses = [
            "The vegetables could have been Ladies finger or Brinjal.",
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
            "What could be the vegetables?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["potato", "raddish", "carrot", "Ladies Finger"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def microwave_and_heat(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "microwave_and_heat"
    knowledge = "Materials like metals which reflect microwaves should never be used in a microwave cooking whereas the glass containers can be used."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} need to heat his food in microwave oven before eating. {name} planned to buy some containers so that he could use to heat.",
            "{name} needs to heat his meal in the microwave oven before eating and had planned to buy some containers that he could use to heat."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The containers could have been made of glass.",
        ]

        false_hypotheses = [
            "The containers could have been made of steel.",
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
            "What could be the containers made of?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["paper cups",
                          "glass container", "steel cup", "foil"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def aircraft_and_paint(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "aircraft_and_paint"
    knowledge = "Aeroplanes need to use polyurethane paint-like epoxy that adheres well to airplane surfaces, and it does not chip or become brittle over time."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to paint his aircraft, so he needs the best type of paint that can be used to fulfill his requirement.",
            "{name} wanted to paint his plane, so he needs the best suited paint that can be used to meet his requirement."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The paint could have been an epoxy paint.",
        ]

        false_hypotheses = [
            "The paint could have been an oil paint.",
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
            "What could be the type of the paint?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["epoxy", "oil paint", "enamel", "distemper"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def pecking_bird(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "pecking_bird"
    knowledge = "Only the woodpecker's family birds peck into trees in search of food or to create a nesting site. They also drum or peck in rapid rhythmic succession to establish their territory and attract mates."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} found some bird in the forest near his guest house that kept pecking the trees.",
            "{name} found a bird in the woods near his guest house that pecked trees."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The bird could have been a woodpecker.",
        ]

        false_hypotheses = [
            "The bird could have been a crow.",
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
            "What could the bird be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["woodpecker", "downy woodpecker", "crow", "pigeon"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def output_device(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "output_device"
    knowledge = "An output device like monitor printer is any hardware device used to send data from a computer to another device or user."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was asked by the teacher to identify the output devices in the computer setup provided.",
            "The teacher asked {name} to identify the output devices in the configuration of the computer provided."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The output devices could have been a monitor or a printer.",
        ]

        false_hypotheses = [
            "The output devices could have been a keyboard or mouse.",
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
            "What could be the output devices?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Monitor", "Printer", "Speakers", "Keyboard"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def input_device(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "input_device"
    knowledge = "An input device like keyboard, the mouse is any hardware device that connects to a computer which sends information into the computer."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was trying to input some data from his end. {name} was able to use some devices to send the information to the computer.",
            "{name} used a device to input some information to the computer."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The devices could have been keyboard or mouse.",
        ]

        false_hypotheses = [
            "The devices could have been a printer or monitor.",
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
            "What could be the devices?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["keyboard", "mouse", "microphone", "monitor"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def sensor_and_temperature(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "sensor_and_temperature"
    knowledge = "Sensor is a device which detects or measures a physical property and records, indicates, or otherwise responds to it. A temperature sensor is a device used to measure temperature."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}' wanted to note the temperature readings of the room three times a day at some particular timings. {name} was able to use some sensor and collected the data.",
            "{name} 'wanted to get the temperature of the room three times a day. he could use some sensor and picked up the data."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The sensor could have been temperature sensor.",
        ]

        false_hypotheses = [
            "The sensor could have been proximity sensor.",
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
            "What could be the sensor used?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["temperature sensor",
                          "proximity sensor", "accelerometer", "IR sensor"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def ultrasonic_sensor_and_distance(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "ultrasonic_sensor_and_distance"
    knowledge = "Ultrasonic sensors can measure the distance to a wide range of objects regardless of shape, color or surface texture."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s experiment was to note the level of water boiling in a container for one hour. {name} was able to note five readings with the help of some sensor.",
            "{name} was observing the level of boiling water in a container for one hour. {name} was able to observe five readings with the help of a sensor."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The sensor could have been an ultrasonic sensor.",
        ]

        false_hypotheses = [
            "The sensor could have been a light sensor.",
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
            "What could be the sensor used?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["pressure sensors", "temperature sensors",
                          "ultrasonic sensors", "proximity sensor"],
            answers_list=[2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def smoke_sensor(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "smoke_sensor"
    knowledge = "A smoke sensor is a device fitted to smoke alarms. A smoke alarm is designed to detect the presence of smoke."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s house caught fire due to a gas leak. {name} was able to identify with the help of an alarm sound generated by a sensor.",
            "{name}'s house burned down due to a gas leak and he was able to identify its cause with the help of an alarm sound generated by a sensor."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The sensor could have been a smoke sensor.",
        ]

        false_hypotheses = [
            "The sensor could have been an accelerometer sensor.",
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
            "What could be the sensor used?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["ultrasonic sensor", "smoke sensor",
                          "accelerometer", "temperature sensor"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def pressure_sensor(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "pressure_sensor"
    knowledge = "A pressure sensor is a device or instrument which can measure the pressure in gases or liquids."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} is working with steam systems, where he needs a device to calculate the pressure for controlling the valve to keep the pressure and steam flow regulated.",
            "{name} is working with steam systems, where he needs a device for calculating the pressure."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The device could have been a pressure sensor.",
        ]

        false_hypotheses = [
            "The device could have been a temperature sensor.",
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
            "What could be the device?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["pressure sensor", "proximity sensor",
                          "temperature sensor", "ultrasonic sensor"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def regular_polygon(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "regular_polygon"
    knowledge = "A polygon like square, a pentagon is regular when all angles are equal, and all sides are equal."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was asked by the instructor to draw regular polygons.",
            "The instructor asked {name} to draw regular polygons."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The polygons could have been a square or a pentagon.",
        ]

        false_hypotheses = [
            "The polygons could have been a rectangle or an isosceles triangle.",
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
            "What could be the polygons?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["equilateral triangle",
                          "pentagon", "square", "rectangle"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def citrus_fruits(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "citrus_fruits"
    knowledge = "Raw citrus fruits like oranges, lime are very high in vitamin C."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was deficient with vitamin C, so his doctor suggested him to eat fruits.",
            "{name}'s doctor suggested him to eat fruits as he had a deficiency of Vitamin C."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The fruit could have been an orange.",
        ]

        false_hypotheses = [
            "The fruit could have been an apple.",
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
            options_list=["watermelon", "bananas", "grapefruits", "oranges"],
            answers_list=[2, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def touch_me_not_plant(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "touch_me_not_plant"
    knowledge = "Mimosa pudica, also called sensitive plant, sleepy plant, action plant, touch-me-not, shame plant is a creeping annual or perennial flowering plant of the pea/legume family Fabaceae. It responds to touch and other stimulation by rapidly closing its leaves and drooping."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} visited a garden where he touched every plant and one plant rapidly closed its leaves.",
            "{name} visited a garden where he touched a plant and it quickly closed his leaves."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The plant could have been a mimosa pudica.",
        ]

        false_hypotheses = [
            "The plant could have been a rose.",
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
            options_list=["mimosa pudica", "rose", "jasmine", "Hibiscus"],
            answers_list=[0],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def curd_maker(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "curd_maker"
    knowledge = "Curd can be prepared by using Lactobacillus bacteria but not with any other like Bifidobacterium, Bacillus Coagulans."
    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to prepare curd. So she took a spoon of the old curd and mixed it with milk. A bacteria present in the old curd was important in converting the fresh milk to curd.",
            "{name} wanted to prepare curd and he took a spoon from the old curd and mixed it with milk. A bacterium present in the old curd converted fresh milk to the curd."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The bacteria could have been Lactobacillus.",
        ]

        false_hypotheses = [
            "The bacteria could have been Bifidobacterium.",
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
            "What could be the bacteria?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Bacillus Coagulans", "LactoBacillus",
                          "Bifidobacterium", "Escherichia Coli"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def protein_diet(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "protein_diet"
    knowledge = "Non vegetarian foods are rich in protein."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} planned to take a protein-rich diet in his daily routine.",
            "{name} planned to take a diet rich in protein in his daily routine."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The food items to involve in the diet could be fish or meat.",
        ]

        false_hypotheses = [
            "The food items to involve in the diet could have been carrots or tomatoes.",
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
            "What could be the food items to involve in the diet?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Milk products", "Carrots", "Broccoli", "Meat"],
            answers_list=[0, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def carbohydrates_diet(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "carbohydrates_diet"
    knowledge = "Food item like rice, wheat are rich in carbohydrates."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s sugar levels increased so high that his doctor suggested decreasing the amount of carbohydrates intake in his diet. {name} reduced the intake of an item.",
            "{name}'s doctor suggested reducing the amount of carbohydrate intake in his diet as his sugar levels increased. {name} reduced the intake of an item."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The item could have been rice.",
        ]

        false_hypotheses = [
            "The item could have been fruits.",
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
            options_list=["Rice", "Fruits", "Vegetables", "Sweets"],
            answers_list=[0, 3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances
