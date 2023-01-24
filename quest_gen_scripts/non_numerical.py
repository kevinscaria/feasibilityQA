import util
import random
import pprint
import numpy as np


def ball_throw(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "ball_throw"
    knowledge = "A human can throw a ball to a limited distance"

    for i in range(repetition_count):

        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} threw a ball from his terrace.",
            "{name} a small boy was playing with a ball along with his friend on his terrace. He threw the ball towards his friend."
        ])

        premise_template = premise_template[i % len(premise_template)]
        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The ball can reach his neighbor's house.",
        ]

        false_hypotheses = [
            "The ball can reach the moon.",
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
            "Till where can the ball reach?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["moon", "sun", "neighbor's home", "another planet"],
            answers_list=[2],
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
#     template_binary_instances, template_mcq_instances = ball_throw(repetition_count)
#     binary_instances += template_binary_instances
#     mcq_instances += template_mcq_instances
#
#     pprint.pprint(binary_instances)
#     print("---------------")
#     pprint.pprint(mcq_instances)
