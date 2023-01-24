import util
import random
import pprint
import numpy as np


def polygon_side(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "poly_Side"
    knowledge = "A polygon has more than two sides."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was given a question in math test to draw different mathematical figures. One of the figure had more than two sides.",
            "{name} received a question in his class of mathematics to draw different mathematical figures. Among all the figures one figure had  more than two sides."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The figure could be a polygon",
        ]

        false_hypotheses = [
            "The figure could be a line.",
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
            "What could be the figure?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["triangle", "line", "square", "circle"],
            answers_list=[0, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def polygon_angle(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "polygon_angle"
    knowledge = "A polygon encloses more than two angles."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} has blocks of different shapes. He noticed that a set of blocks encloses more than two angles.",
            "In a school there are blocks of different shapes to teach student's about different shapes and the angles in that particular shape. {name} found out that a some of blocks have more than two angles."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The set of blocks could be a polygon.",
        ]

        false_hypotheses = [
            "The set of blocks could be a circle.",
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
            "What could be the shape of the blocks?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["triangle", "pentagon", "square", "round"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def triangle_sides(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "triangle_sides"
    knowledge = "A triangle has three sides."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "In a maths competition {name} was told to identify all triangles from a group of shapes.",
            "In an inter school mathematical competition, {name} was given many shapes and was asked to identify all the triangles among those shaps."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "He could have selected the shapes with three sides.",
        ]

        false_hypotheses = [
            "He could have selected the shapes with five sides.",
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
            "What could be the number of sides of the selected shape?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["zero", "five", "two", "three"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def square_angle(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "square_angle"
    knowledge = "Angles enclosed in a regular polygon are equal."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was taught in maths class about the figures which have all enclosed angles equal.",
            "{name} studies about the angles and shapes from internet. He studies about a figure which has all the equal angles enclosed in that figure."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "Figure could be a square.",
        ]

        false_hypotheses = [
            "Figure could be a isosceles triangle.",
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
            "What could the figures be?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["square", "rectangle",
                          "equilateral triangle", "scalene triangle"],
            answers_list=[0, 1, 2],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def square_side(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "square_side"
    knowledge = "A square has all sides equal in length."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} wanted to fit a picture in a frame of all equal sides.",
            "{name} has a picture which has all the four sides equal and he wants to frame for that picture which can have all the sides equal so that the picture fits properly in that frame."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The frame could be of square shape.",
        ]

        false_hypotheses = [
            "The frame could be of rectangle shape.",
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
            "What could be the shape of the selected frame?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Square", "Circle", "Rectangle", "Rhombus"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def equilateral_triangle_sides(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "equilateral_triangle_sides"
    knowledge = "The sides of equilateral triangles are equal."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was solving a question on equilateral triangle. It was given that the length of two sides of the triangle are same.",
            "{name} was given a question about the equilateral triangle in his examination. It was stated in the question that any two sides of the triangle have same length."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The third side could be same as the other two sides.",
        ]

        false_hypotheses = [
            "The third side could be more than the other two sides.",
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
            "What could be the length of the third side in comparison to the other two sides?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Greater", "Lesser", "None", "Equal"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def rectangle_parallelogram(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "rectangle_parallelogram"
    knowledge = "All rectangles are parallelogram but all parallelograms are not rectangles."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was asked about the shape that can always be a parallelogram but is not possible the other way around",
            "{name} figures out about a shape that can always be a prallelogram but parallelogram can always be that shape is not possible."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "Ths shape could be a rectangle",
        ]

        false_hypotheses = [
            "Ths shape could be a pentagon.",
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
            "What could be the shape?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Square", "Circle", "Rectangle", "triangle"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def square_diagonal(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "square_diagonal"
    knowledge = "A square has only two diagonals."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was given a figure of four sides which are equal in length.",
            "{name} in his exam received a figure which has four sides and length of all the sides are equal."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The figure could have two diagonals.",
        ]

        false_hypotheses = [
            "The figure could have eight diagonals.",
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
            "What could be the number of diagonals in the figure?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["one", "two", "three", "four"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def right_angle(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "right_angle"
    knowledge = "A right angle is of exactly 90 degrees."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} attended the maths class where his teacher drew a line that is right-angled to the base.",
            "{name} was going through his mathematics school book in which he saw a line that is at right angle to the base"
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The angle enclosed could be of 90 degrees.",
        ]

        false_hypotheses = [
            "The angle enclosed could be of 190 degrees.",
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
            "What could be the angle enclosed in between the line and the base?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["180", "90", "70", "360"],
            answers_list=[1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def rectangle_sides(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "rectangle_Sides"
    knowledge = "Opposite sides of a rectangle are equal in length."

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name}'s teacher tells the students about a figure which has opposite sides equal.",
            "{name} draws a figure ona paper. That figure has equal opposite sides."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The figure could be a rectangle.",
        ]

        false_hypotheses = [
            "The figure could be a circle.",
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
            "What could be the shape of the figure?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Square", "Rectangle", "Triangle", "Circle"],
            answers_list=[0, 1],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances


def pentagon_diagonal(repetition_count):
    binary_instances = []
    mcq_instances = []

    category, subcategory = "non_numerical", "pentagon_diagonal"
    knowledge = "A pentagon has five diagonals"

    for i in range(repetition_count):
        premise_template = np.random.choice(size=repetition_count, replace=False, a=[
            "{name} was given a figure with five diagonals and was asked to name that figure.",
            "{name} in his class was asked a question about the name of figure which has a total of five diagonals."
        ])

        premise_template = premise_template[i % len(premise_template)]

        name = random.choice(util.male_names)
        premise = premise_template.format(name=name)

        true_hypotheses = [
            "The figure could be a pentagon.",
        ]

        false_hypotheses = [
            "The figure could be a square.",
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
            "What could be the figure?",

        ])
        question_text = question_template.format(name=name)
        question = util.direct_generate_question(
            question_text=question_text,
            options_list=["Circle", "Square", "Triangle", "Pentagon"],
            answers_list=[3],
        )
        mcq_instances.append(util.create_data_for_mcq(
            category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
        )
        )

    return binary_instances, mcq_instances
