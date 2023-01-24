import random
import pprint
import pandas as pd
import attribute_comparison
import attribute_comparison_hg
import attribute_comparison_KS
import attribute_comparison_ss
import attribute_comparison_sg
import attribute_comparison_sp
import attribute_comparison_yn
import change_with_time
import change_with_time_ss
import change_with_action
import implicit_numerical_knowledge
import non_numerical
import non_numerical_KS
import non_numerical_hg
import non_numerical_sp
import non_numerical_yn
import non_numerical_ss
import non_numerical_sg
import non_numerical_math_hg
import non_numerical_math_sg
import implicit_numerical_knowledge_KS
import implicit_numerical_knowledge_ss
import transaction
import half_double
import quarter_quadruple_ss

if __name__ == "__main__":
    repetition_count = 2
    binary_instances = []
    mcq_instances = []
    author_list = []
    extra_val_methods = []
    extra_val_filters = []
    directory_list = []

    # directory_names = [attribute_comparison, change_with_time, change_with_action]
    directory_names = {
        "attribute_comparison": attribute_comparison,
        "attribute_comparison_KS": attribute_comparison_KS,
        "attribute_comparison_hg": attribute_comparison_hg,
        "attribute_comparison_ss": attribute_comparison_ss,
        "attribute_comparison_yn": attribute_comparison_yn,
        "attribute_comparison_sg": attribute_comparison_sg,
        "attribute_comparison_sp": attribute_comparison_sp,
        "change_with_time": change_with_time,
        "change_with_time_ss": change_with_time_ss,
        "change_with_action": change_with_action,
        "implicit_numerical_knowledge": implicit_numerical_knowledge,
        "implicit_numerical_knowledge_ss": implicit_numerical_knowledge_ss,
        "implicit_numerical_knowledge_KS": implicit_numerical_knowledge_KS,
        "non_numerical": non_numerical,
        "non_numerical_hg": non_numerical_hg,
        "non_numerical_KS": non_numerical_KS,
        "non_numerical_yn": non_numerical_yn,
        "non_numerical_sg": non_numerical_sg,
        "non_numerical_ss": non_numerical_ss,
        "non_numerical_sp": non_numerical_sp,
        "non_numerical_math_hg": non_numerical_math_hg,
        "non_numerical_math_sg": non_numerical_math_sg,
        "transaction": transaction,
        "half_double": half_double,
        "quarter_quadruple_ss": quarter_quadruple_ss
    }

    for directory_str, directory in directory_names.items():
        if '_hg' in directory_str:
            author = 'Himanshu'
        elif '_KS' in directory_str:
            author = 'Kevin'
        elif '_ss' in directory_str:
            author = 'Saurabh'
        elif '_sp' in directory_str:
            author = 'Sivapriya'
        elif '_yn' in directory_str:
            author = 'Yamini'
        elif '_sg' in directory_str:
            author = 'Sidharth'
        else:
            author = 'Neeraj'

        question_counter = 0
        methods = dir(directory)

        for method in methods:
            if(method[0] == "_" or method in ["util", "random", "pprint", "np"]):
                continue

            method = directory_str + "." + method + \
                "(" + str(repetition_count) + ")"
            template_binary_instances, template_mcq_instances = eval(method)
            binary_instances += template_binary_instances
            if len(template_binary_instances) > 2:
                extra_val_methods.append(method)
                extra_val_filters.append(
                    template_binary_instances[0]['subcategory'])
            author_list_temp = [author] * len(template_binary_instances)
            mcq_instances += template_mcq_instances
            directory_list.append(directory_str)
            question_counter += 1
            author_list.extend(author_list_temp)

    print('\n**** STATS ****\n')
    print('Methods having multiple outputs (paraphrased): ', extra_val_methods)
    print('Directory Length: ', len(directory_list))
    print('Binary Type: ', len(binary_instances))
    print('MCQ Type: ', len(mcq_instances))
    print('Total: ', len(binary_instances) + len(mcq_instances))
    df = pd.DataFrame(binary_instances)
    # df.to_csv("./sample.csv", index=False)

    # Creating knowledge base
    knowledge_df = df.loc[:, [
        'category', 'subcategory', 'knowledge', 'premise', 'hypothesis', 'binary_classification_label']]
    knowledge_df['author'] = author_list

    # Separate treatment for methods that generate extra values
    filters = list(set(extra_val_filters))
    extra_count_df = knowledge_df[knowledge_df['subcategory'].isin(filters)]
    extra_count_df = extra_count_df[extra_count_df['binary_classification_label'] == True]
    knowledge_df = knowledge_df[~knowledge_df['subcategory'].isin(filters)].drop_duplicates(
        subset=['knowledge', 'premise'])
    knowledge_df = knowledge_df.append(extra_count_df)

    author_stats = pd.DataFrame(
        knowledge_df['author'].value_counts()).reset_index().rename(columns={'index': 'Author', 'author': 'Count'})
    tot = author_stats['Count'].sum()
    totals = pd.DataFrame({'Author': 'Total', 'Count': [tot]})
    author_stats = author_stats.append(totals, ignore_index=True)
    print(author_stats)
    print('**** ****')

    write = False

    if write:
        writer = pd.ExcelWriter('knowledge_base_df.xlsx',
                                engine='xlsxwriter',
                                engine_kwargs={'options': {'strings_to_formulas': False, 'strings_to_urls': False}})

        knowledge_df.to_excel(writer, sheet_name='Knowledge Base', index=False)
        author_stats.to_excel(writer, sheet_name='Stats', index=False)
        writer.save()
