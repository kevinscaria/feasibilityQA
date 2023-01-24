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
    author_listb = []
    author_listm = []

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

        methods = dir(directory)
        for method in methods:
            if (method[0] == "_" or method in ["util", "random", "pprint", "np"]):
                continue
            method = directory_str + "." + method + \
                "(" + str(repetition_count) + ")"
            template_binary_instances, template_mcq_instances = eval(method)
            author_list_binary = [author] * len(template_binary_instances)
            author_list_mcq = [author] * len(template_mcq_instances)
            binary_instances += template_binary_instances
            mcq_instances += template_mcq_instances
            author_listb.extend(author_list_binary)
            author_listm.extend(author_list_mcq)

    # print('Binary: ', len(binary_instances))
    bdf = pd.DataFrame(binary_instances)
    bdf['author'] = author_listb
    mdf = pd.DataFrame(mcq_instances)
    mdf['question_text'] = mdf['question'].apply(lambda x: x['question_text'])
    mdf['options'] = mdf['question'].apply(lambda x: x['options'])
    mdf['value_answer'] = mdf['question'].apply(lambda x: x['value_answer'])
    mdf['option_answer'] = mdf['question'].apply(lambda x: x['option_answer'])
    mdf['author'] = author_listm

    print('***** STATS BINARY*****')
    author_stats_bin = pd.DataFrame(
        bdf['author'].value_counts()).reset_index().rename(columns={'index': 'Author', 'author': 'Count'})
    tot = author_stats_bin['Count'].sum()
    totals = pd.DataFrame({'Author': 'Total', 'Count': [tot]})
    author_stats = author_stats_bin.append(totals, ignore_index=True)
    print(author_stats)
    print('********\n')

    # print('MCQ: ', len(mcq_instances))
    print('***** STATS MCQ*****')
    author_stats_mc1 = pd.DataFrame(
        mdf['author'].value_counts()).reset_index().rename(columns={'index': 'Author', 'author': 'Count'})
    tot = author_stats_mc1['Count'].sum()
    totals = pd.DataFrame({'Author': 'Total', 'Count': [tot]})
    author_stats = author_stats_mc1.append(totals, ignore_index=True)
    print(author_stats)
    print('********')

    print('Grand Total: ', len(binary_instances) + len(mcq_instances))

    write = True
    if write:
        writer = pd.ExcelWriter('knowledge_base_df.xlsx',
                                engine='xlsxwriter',
                                engine_kwargs={'options': {'strings_to_formulas': False, 'strings_to_urls': False}})

        bdf.to_excel(writer, sheet_name='Binary Questions', index=False)
        mdf.to_excel(
            writer, sheet_name='Multiple Choice Questions', index=False)
        writer.save()
