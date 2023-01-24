import random
import operator

male_names = "Aaron,Abraham,Adam,Adriel,Alan,Alex,Alexander,Andrew,Anthony,Antonio,Arthur,Ashton,Atlas,Barrett,Benjamin,Bennett,Bentley,Brandon,Calvin,Cameron,Carlos,Carson,Charles,Charlie,Christian,Christopher,Cole,Connor,Cooper,Daniel,David,Dawson,Dylan,Edward,Eric,Evan,Finn,Gabriel,George,Graham,Greyson,Hayden,Henry,Hudson,Ian,Isaac,Ivan,Jace,Jack,Jackson,Jacob,James,Jameson,Jason,Jaxon,Jayden,Jesse,Joel,John,Jonah,Jonathan,Jordan,Jose,Joseph,Joshua,Judah,Jude,Julian,Justin,Kayden,Kevin,Leo,Leon,Leonardo,Liam,Lincoln,Logan,Lucas,Luke,Mateo,Matthew,Maxwell,Michael,Miles,Nathan,Nicolas,Noah,Nolan,Oliver,Parker,Patrick,Richard,Robert,Ryan,Samuel,Sebastian,Thomas,Tyler,Victor,William".split(
    ",")
female_names = "Abigail,Addison,Adeline,Alana,Alexandra,Alice,Alina,Alyssa,Amelia,Andrea,Anna,Arabella,Aria,Arianna,Arya,Ashley,Athena,Ava,Avery,Bailey,Bella,Brielle,Camila,Caroline,Catalina,Chloe,Claire,Clara,Daisy,Elena,Eliana,Eliza,Elizabeth,Elliana,Ellie,Emery,Emilia,Emily,Emma,Eva,Evelyn,Everleigh,Gabriella,Gemma,Genesis,Gracie,Hadley,Hailey,Hannah,Harper,Isabel,Isabella,Jasmine,Josephine,Josie,Julia,Juliana,Juliette,Katherine,Kaylee,Khloe,Kylie,Leila,Leilani,Lily,Lucy,Margaret,Maria,Mary,Maya,Mia,Mila,Millie,Naomi,Natalia,Natalie,Nevaeh,Nora,Olivia,Riley,Ruby,Samantha,Sara,Savannah,Scarlett,Sofia,Sophie,Stella,Valentina,Victoria,Vivian".split(
    ",")
countries = "USA,China,Japan,Germany,United,France,India,Italy,Brazil,Canada,Australia,Russia,Spain,Mexico,Indonesia,Turkey,Netherlands,Switzerland,Argentina,Sweden,Poland,Belgium,Iran,Thailand,Nigeria,Austria,Norway,Israel,Denmark,Philippines,Ireland,Singapore,Malaysia,Venezuela,Pakistan,Colombia,Egypt,Chile,Finland,Bangladesh,Vietnam,Portugal,Czech,Greece,Peru".split(
    ",")
colors = "White,Yellow,Orange,Red,Pink,Purple,Blue,Green,Black".split(",")
animals = "Cat,Dog,Deer,Bear,Wolf,Rabbit,Fox,Lion,Horse,Monkey,Donkey,Elephant,Tiger,Sheep,Goat,Cow,Buffalo,Hound".split(
    ",")
birds = "Owl,Parrot,Woodpecker,Falcon,Hummingbird,Eagle,Kingfisher,Sparrow,Bat,Crow,Pigeon,Turkey,Hawk".split(
    ",")


def create_all_scenarios_for_binary_classification_task(category,
                                                        subcategory,
                                                        knowledge,
                                                        premise,
                                                        hypothesis_template,
                                                        name,
                                                        given_value,
                                                        diff,
                                                        more_is_correct_flag,
                                                        equal_is_correct_flag,
                                                        negative_options_possible,
                                                        round_to=1,
                                                        scale=1
                                                        ):
    binary_instances = []
    lowest_possible_answer = given_value - diff
    highest_possible_answer = given_value + diff
    if (negative_options_possible is False):
        lowest_possible_answer = max(0, lowest_possible_answer)

    possible_answers = set([])
    for i in range(lowest_possible_answer, highest_possible_answer, scale):
        possible_answers.add(round(i/round_to) * round_to)
    # possible_answers = random.sample(possible_answers, 2)

    correct_answers = set([])
    incorrect_answers = set([])
    for i in range(lowest_possible_answer, highest_possible_answer, scale):
        binary_classification_label = False
        possible_answer = round(i / round_to) * round_to
        if (equal_is_correct_flag == False):
            if (more_is_correct_flag == True and possible_answer > given_value):
                binary_classification_label = True

            elif (more_is_correct_flag == False and possible_answer < given_value):
                binary_classification_label = True

        elif (equal_is_correct_flag == True):
            if (more_is_correct_flag == True and possible_answer >= given_value):
                binary_classification_label = True
            elif (more_is_correct_flag == False and possible_answer <= given_value):
                binary_classification_label = True

        if(binary_classification_label == True):
            correct_answers.add(possible_answer)
        else:
            incorrect_answers.add(possible_answer)

    possible_answers = random.sample(
        correct_answers, 1) + random.sample(incorrect_answers, 1)

    for idx, possible_answer in enumerate(possible_answers):
        binary_classification_label = False
        hypothesis = hypothesis_template.format(
            name=name, hyp_value=possible_answer)
        if (equal_is_correct_flag == False):
            if (more_is_correct_flag == True and possible_answer > given_value):
                binary_classification_label = True

            elif (more_is_correct_flag == False and possible_answer < given_value):
                binary_classification_label = True

        elif (equal_is_correct_flag == True):
            if (more_is_correct_flag == True and possible_answer >= given_value):
                binary_classification_label = True
            elif (more_is_correct_flag == False and possible_answer <= given_value):
                binary_classification_label = True

        binary_instances.append(
            create_data_for_binary_classification_task(
                category=category, subcategory=subcategory, knowledge=knowledge,
                premise=premise, hypothesis=hypothesis, binary_classification_label=binary_classification_label,
            )
        )
    return binary_instances


def for_transaction_create_all_scenarios_for_binary_classification_task(category,
                                                                        subcategory,
                                                                        knowledge,
                                                                        premise,
                                                                        hypothesis_template,
                                                                        name,
                                                                        given_value,
                                                                        diff,
                                                                        from_name1_to_name2,
                                                                        equal_is_correct_flag,
                                                                        negative_options_possible,
                                                                        round_to=1,
                                                                        scale=1
                                                                        ):
    binary_instances = []
    binary_instances += create_all_scenarios_for_binary_classification_task(
        category,
        subcategory,
        knowledge,
        premise,
        hypothesis_template,
        name["name1"],
        given_value["given_value1"],
        diff=diff,
        more_is_correct_flag=operator.not_(from_name1_to_name2),
        equal_is_correct_flag=equal_is_correct_flag,
        negative_options_possible=negative_options_possible,
        round_to=round_to,
        scale=scale
    )

    binary_instances += create_all_scenarios_for_binary_classification_task(
        category,
        subcategory,
        knowledge,
        premise,
        hypothesis_template,
        name["name2"],
        given_value["given_value2"],
        diff=diff,
        more_is_correct_flag=from_name1_to_name2,
        equal_is_correct_flag=equal_is_correct_flag,
        negative_options_possible=negative_options_possible,
        round_to=round_to,
        scale=scale
    )

    return binary_instances


def create_data_for_binary_classification_task(category,
                                               subcategory,
                                               knowledge,
                                               premise,
                                               hypothesis,
                                               binary_classification_label,
                                               ):

    return {
        "category": category,
        "subcategory": subcategory,
        "knowledge": knowledge,
        "premise": premise,
        "hypothesis": hypothesis,
        "binary_classification_label": binary_classification_label,
    }


def direct_create_data_for_binary_classification_task(category,
                                                      subcategory,
                                                      knowledge,
                                                      premise,
                                                      true_hypotheses,
                                                      false_hypotheses,
                                                      ):

    binary_instances = []
    if(true_hypotheses != []):
        binary_instances.append({
            "category": category,
            "subcategory": subcategory,
            "knowledge": knowledge,
            "premise": premise,
            "hypothesis": random.choice(true_hypotheses),
            "binary_classification_label": True,
        })

    if (false_hypotheses != []):
        binary_instances.append({
            "category": category,
            "subcategory": subcategory,
            "knowledge": knowledge,
            "premise": premise,
            "hypothesis": random.choice(false_hypotheses),
            "binary_classification_label": False,
        })
    return binary_instances


def create_data_for_mcq(category,
                        subcategory,
                        premise,
                        knowledge,
                        question,
                        ):

    return {
        "category": category,
        "subcategory": subcategory,
        "premise": premise,
        "knowledge": knowledge,
        "question": question
    }


def generate_question(question_text, given_value, diff=10, more_is_correct_flag=False, equal_is_correct_flag=False, negative_options_possible=False, round_to=None, scale=1):
    all_options = []
    value_answer = []
    option_answer = []
    mapping = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
    }
    number_of_options = 4
    correct_flag = False
    idx = -1

    possible_answers = set([])
    lowest_possible_answer = given_value - diff
    highest_possible_answer = given_value + diff

    if(negative_options_possible is False):
        lowest_possible_answer = max(0, lowest_possible_answer)

    for i in range(lowest_possible_answer, highest_possible_answer, scale):
        possible_answers.add(round(i/round_to) * round_to)

    keys = random.sample(possible_answers, number_of_options)

    for idx, key in enumerate(keys):
        all_options.append({mapping[idx]: key})

        if (equal_is_correct_flag == False):
            if (more_is_correct_flag == True and key > given_value):
                correct_flag = True
                option_answer.append(mapping[idx])
                value_answer.append(key)
            elif (more_is_correct_flag == False and key < given_value):
                correct_flag = True
                option_answer.append(mapping[idx])
                value_answer.append(key)

        elif (equal_is_correct_flag == True):
            if (more_is_correct_flag == True and key >= given_value):
                correct_flag = True
                option_answer.append(mapping[idx])
                value_answer.append(key)
            elif (more_is_correct_flag == False and key <= given_value):
                correct_flag = True
                option_answer.append(mapping[idx])
                value_answer.append(key)

    if (random.choice([0, 1]) == 0 or correct_flag == False):
        key = "None"
        idx += 1
        all_options.append({mapping[idx]: key})
        if (correct_flag == False):
            option_answer.append(mapping[idx])
            value_answer.append(key)

    return {"question_text": question_text,
            "options": all_options,
            "value_answer": value_answer,
            "option_answer": option_answer,
            "other": {
                "given_value": given_value,
                "more_is_correct_flag": more_is_correct_flag,
                "equal_is_correct_flag": equal_is_correct_flag,
            }
            }


def direct_generate_question(question_text, options_list, answers_list):
    all_options = []
    value_answer = []
    option_answer = []
    mapping = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
    }
    for idx, key in enumerate(options_list):
        all_options.append({mapping[idx]: key})

        if (idx in answers_list):
            correct_flag = True
            option_answer.append(mapping[idx])
            value_answer.append(key)

    return {"question_text": question_text,
            "options": all_options,
            "value_answer": value_answer,
            "option_answer": option_answer,
            "other": {}
            }


def for_transaction_generate_question(category,
                                      subcategory,
                                      knowledge,
                                      premise,
                                      question_text,
                                      name,
                                      given_value,
                                      diff=10,
                                      from_name1_to_name2=False,
                                      equal_is_correct_flag=False,
                                      negative_options_possible=False,
                                      round_to=None,
                                      scale=1):
    mcq_instances = []
    question = generate_question(question_text=question_text.format(name=name["name1"]),
                                 given_value=given_value["given_value1"],
                                 diff=diff,
                                 more_is_correct_flag=operator.not_(
                                     from_name1_to_name2),
                                 equal_is_correct_flag=equal_is_correct_flag,
                                 negative_options_possible=negative_options_possible,
                                 round_to=round_to,
                                 scale=scale)

    mcq_instances.append(create_data_for_mcq(
        category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
    )
    )

    question = generate_question(question_text=question_text.format(name=name["name2"]),
                                 given_value=given_value["given_value2"],
                                 diff=diff,
                                 more_is_correct_flag=from_name1_to_name2,
                                 equal_is_correct_flag=equal_is_correct_flag,
                                 negative_options_possible=negative_options_possible,
                                 round_to=round_to,
                                 scale=scale)

    mcq_instances.append(create_data_for_mcq(
        category=category, subcategory=subcategory, knowledge=knowledge, premise=premise, question=question,
    )
    )
    return mcq_instances


def generate_question_indirect(question_text, given_value, diff=10, more_is_correct_flag=False, equal_is_correct_flag=False, negative_options_possible=False, round_to=None, scale=1):
    all_options = []
    value_answer = []
    option_answer = []
    mapping = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
    }
    number_of_options = 4
    correct_flag = False
    idx = -1

    possible_answers = set([])
    lowest_possible_answer = given_value - diff
    highest_possible_answer = given_value + diff

    if(negative_options_possible is False):
        lowest_possible_answer = max(0, lowest_possible_answer)

    for i in range(lowest_possible_answer, highest_possible_answer, scale):
        possible_answers.add(round(i/round_to) * round_to)

    keys = random.sample(possible_answers, number_of_options)

    for idx, key in enumerate(keys):
        quantifier = random.choice(["more than", "less than"])
        all_options.append({mapping[idx]: quantifier + " " + str(key)})

        if (equal_is_correct_flag == False):
            if (more_is_correct_flag == True and
                    (
                        (key > given_value and quantifier in ["less than"])
                        or
                                (key < given_value and quantifier in ["more than"])
                        )
                    ):
                correct_flag = True
                option_answer.append(mapping[idx])
                value_answer.append(key)
            elif (more_is_correct_flag == False and
                  (
                      (key > given_value and quantifier in ["less than"])
                      or
                      (key < given_value and quantifier in ["more than"])
                  )
                  ):
                correct_flag = True
                option_answer.append(mapping[idx])
                value_answer.append(key)

        elif (equal_is_correct_flag == True):
            pass

    if (random.choice([0, 1]) == 0 or correct_flag == False):
        key = "None"
        idx += 1
        all_options.append({mapping[idx]: key})
        if (correct_flag == False):
            option_answer.append(mapping[idx])
            value_answer.append(key)

    return {"question_text": question_text,
            "options": all_options,
            "value_answer": value_answer,
            "option_answer": option_answer,
            "other": {
                "given_value": given_value,
                "more_is_correct_flag": more_is_correct_flag,
                "equal_is_correct_flag": equal_is_correct_flag,
            }
            }
