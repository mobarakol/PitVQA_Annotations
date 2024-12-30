
import os
import pandas as pd

from utils import (step_phase_mapping, next_step_mapping, next_phase_mapping,
                   step_operation_mapping, number_location_mapping)

count_dict = {}
frames = 0
questions = 0


def prepare_what_phase_qa(step_name):
    question = 'What is the surgical phase shown in the image?'
    answer = step_phase_mapping[step_name]
    qa = question + '|' + answer
    if answer not in count_dict.keys():
        count_dict[answer] = 1
    else:
        count_dict[answer] += 1
    return qa, answer


def prepare_what_step_qa(step_name):
    question = 'What is the surgical step shown in this frame?'
    answer = step_name
    qa = question + '|' + answer
    if answer not in count_dict.keys():
        count_dict[answer] = 1
    else:
        count_dict[answer] += 1
    return qa


def prepare_next_phase_qa(current_phase):
    question = 'What is the next surgical phase?'
    answer = next_phase_mapping[current_phase]
    qa = question + '|' + answer
    if answer not in count_dict.keys():
        count_dict[answer] = 1
    else:
        count_dict[answer] += 1
    return qa


def prepare_next_step_qa(current_step):
    question = 'What is the next surgical step?'
    answer = next_step_mapping[current_step]
    qa = question + '|' + answer
    if answer not in count_dict.keys():
        count_dict[answer] = 1
    else:
        count_dict[answer] += 1
    return qa


def prepare_how_many_tool_qa(num_of_tool):
    question = 'How many instruments are present in the image?'
    answer = num_of_tool
    if num_of_tool == 0:
        answer = 'zero'
    elif num_of_tool == 1:
        answer = 'one'
    elif num_of_tool == 2:
        answer = 'two'
    qa = question + '|' + answer
    if answer not in count_dict.keys():
        count_dict[answer] = 1
    else:
        count_dict[answer] += 1
    return qa


def prepare_what_operation_qa(step_name):
    question = 'What is the surgical operation performed in the image?'
    answer = step_operation_mapping[step_name]
    qa = question + '|' + answer
    if answer not in count_dict.keys():
        count_dict[answer] = 1
    else:
        count_dict[answer] += 1
    return qa, answer


def prepare_what_tool_qa_one(row_content):
    # What instrument is used in the bottom-mid of the image? | 1 of 18 instruments
    qa = 0
    if pd.notna(row_content['pos_instrument1']):
        if str(row_content['pos_instrument1']) == '3.0':
            question = 'What instrument is used at the centre of the image?'
            answer = row_content['str_instrument1']
            qa = question + '|' + answer
            if answer not in count_dict.keys():
                count_dict[answer] = 1
            else:
                count_dict[answer] += 1
        else:
            position = number_location_mapping[str(row_content['pos_instrument1'])]
            question = f'What instrument is used in the {position} of the image?'
            answer = row_content['str_instrument1']
            qa = question + '|' + answer
            if answer not in count_dict.keys():
                count_dict[answer] = 1
            else:
                count_dict[answer] += 1
    elif pd.notna(row_content['pos_instrument2']):
        if str(row_content['pos_instrument2']) == '3.0':
            question = 'What instrument is used at the centre of the image?'
            answer = row_content['str_instrument2']
            qa = question + '|' + answer
            if answer not in count_dict.keys():
                count_dict[answer] = 1
            else:
                count_dict[answer] += 1
        else:
            position = number_location_mapping[str(row_content['pos_instrument2'])]
            question = f'What instrument is used in the {position} of the image?'
            answer = row_content['str_instrument2']
            qa = question + '|' + answer
            if answer not in count_dict.keys():
                count_dict[answer] = 1
            else:
                count_dict[answer] += 1
    return qa


def prepare_tool_operation_qa(row_content, operation):
    # What surgical activity is performing by the instrument kerrisons? | 1 of 14 operations
    qa = 0
    if pd.notna(row_content['pos_instrument1']):
        tool = row_content['str_instrument1']
        question = f'What surgical activity is performing by the instrument {tool}?'
        answer = operation
        qa = question + '|' + answer
        if answer not in count_dict.keys():
            count_dict[answer] = 1
        else:
            count_dict[answer] += 1
    elif pd.notna(row_content['pos_instrument2']):
        tool = row_content['str_instrument2']
        question = f'What surgical activity is performing by the instrument {tool}?'
        answer = operation
        qa = question + '|' + answer
        if answer not in count_dict.keys():
            count_dict[answer] = 1
        else:
            count_dict[answer] += 1
    return qa


def prepare_where_tool_qa(row_content):
    # Where is the surgical instrument kerrisons tip located in the image? | 1 of 5 locations
    qa = 0
    if pd.notna(row_content['pos_instrument1']):
        tool = row_content['str_instrument1']
        question = f'Where is the surgical instrument {tool} tip located in the image?'
        answer = number_location_mapping[str(row_content['pos_instrument1'])]
        qa = question + '|' + answer
        if answer not in count_dict.keys():
            count_dict[answer] = 1
        else:
            count_dict[answer] += 1
    elif pd.notna(row_content['pos_instrument2']):
        tool = row_content['str_instrument2']
        question = f'Where is the surgical instrument {tool} tip located in the image?'
        answer = number_location_mapping[str(row_content['pos_instrument2'])]
        qa = question + '|' + answer
        if answer not in count_dict.keys():
            count_dict[answer] = 1
        else:
            count_dict[answer] += 1
    return qa


def prepare_what_tool_qa_two(row_content, col_num):
    # What instrument is used in the bottom-mid of the image? | 1 of 18 instruments
    qa = 0
    if col_num == 1:  # tool 1
        if pd.notna(row_content['pos_instrument1']):
            if str(row_content['pos_instrument1']) == '3.0':
                question = 'What instrument is used at the centre of the image?'
                answer = row_content['str_instrument1']
                qa = question + '|' + answer
                if answer not in count_dict.keys():
                    count_dict[answer] = 1
                else:
                    count_dict[answer] += 1
            else:
                position = number_location_mapping[str(row_content['pos_instrument1'])]
                question = f'What instrument is used in the {position} of the image?'
                answer = row_content['str_instrument1']
                qa = question + '|' + answer
                if answer not in count_dict.keys():
                    count_dict[answer] = 1
                else:
                    count_dict[answer] += 1
    elif col_num == 2:
        if pd.notna(row_content['pos_instrument2']):
            if str(row_content['pos_instrument2']) == '3.0':
                question = 'What instrument is used at the centre of the image?'
                answer = row_content['str_instrument2']
                qa = question + '|' + answer
                if answer not in count_dict.keys():
                    count_dict[answer] = 1
                else:
                    count_dict[answer] += 1
            else:
                position = number_location_mapping[str(row_content['pos_instrument2'])]
                question = f'What instrument is used in the {position} of the image?'
                answer = row_content['str_instrument2']
                qa = question + '|' + answer
                if answer not in count_dict.keys():
                    count_dict[answer] = 1
                else:
                    count_dict[answer] += 1
    return qa


def prepare_tool_operation_qa_two(row_content, operation, col_num):
    # What surgical activity is performing by the instrument kerrisons? | 1 of 14 operations
    qa = 0
    if col_num == 1:
        if pd.notna(row_content['pos_instrument1']):
            tool = row_content['str_instrument1']
            question = f'What surgical activity is performing by the instrument {tool}?'
            answer = operation
            qa = question + '|' + answer
            if answer not in count_dict.keys():
                count_dict[answer] = 1
            else:
                count_dict[answer] += 1
    elif col_num == 2:
        if pd.notna(row_content['pos_instrument2']):
            tool = row_content['str_instrument2']
            question = f'What surgical activity is performing by the instrument {tool}?'
            answer = operation
            qa = question + '|' + answer
            if answer not in count_dict.keys():
                count_dict[answer] = 1
            else:
                count_dict[answer] += 1
    return qa


def prepare_where_tool_qa_two(row_content, col_num):
    # Where is the surgical instrument kerrisons tip located in the image? | 1 of 5 locations
    qa = 0
    if col_num == 1:
        if pd.notna(row_content['pos_instrument1']):
            tool = row_content['str_instrument1']
            question = f'Where is the surgical instrument {tool} tip located in the image?'
            answer = number_location_mapping[str(row_content['pos_instrument1'])]
            qa = question + '|' + answer
            if answer not in count_dict.keys():
                count_dict[answer] = 1
            else:
                count_dict[answer] += 1
    elif col_num == 2:
        if pd.notna(row_content['pos_instrument2']):
            tool = row_content['str_instrument2']
            question = f'Where is the surgical instrument {tool} tip located in the image?'
            answer = number_location_mapping[str(row_content['pos_instrument2'])]
            qa = question + '|' + answer
            if answer not in count_dict.keys():
                count_dict[answer] = 1
            else:
                count_dict[answer] += 1
    return qa


def get_num_of_tool(row_content):  # row_content is the content for that row
    if pd.isna(row_content['pos_instrument1']) and pd.isna(row_content['pos_instrument2']):
        number_of_tool = 0
    elif pd.notna(row_content['pos_instrument1']) and pd.notna(row_content['pos_instrument2']):
        number_of_tool = 2
    else:
        number_of_tool = 1
    return number_of_tool


def get_current_step_name(step_df, time_list, index):
    row_idx = 0
    for time in time_list:
        if index < time:
            row_idx = time_list.index(time)-1
            break
    step_name = step_df.iloc[row_idx]['str_step']
    return step_name


def write_file(video_folder, file_name, qa_list):
    file = os.path.join(video_folder, file_name)
    with open(file, 'w', encoding='utf-8') as f:
        for qa in qa_list:
            f.write(qa + '\n')


if __name__ == "__main__":

    tool_num = {}
    for i in range(1, 26):
        print(f'processing file {i}')
        QA_folder = r'D:\1-硕士研究项目\1-数据集\PitVis-VQA\QA'
        video_num = 'video_' + f"{i:02d}"
        video_folder = os.path.join(QA_folder, video_num)

        instrument_folder = r'D:\1-硕士研究项目\1-数据集\PitVis-VQA\labeling\Instruments-done'
        instrument_num = 'instruments_' + f"{i:02d}" + '.csv'
        instrument_file = os.path.join(instrument_folder, instrument_num)

        step_folder = r'D:\1-硕士研究项目\1-数据集\PitVis-VQA\Steps'
        step_num = 'steps_' + f"{i:02d}" + '.csv'
        step_file = os.path.join(step_folder, step_num)

        # open instrument file
        instrument_df = pd.read_csv(instrument_file)
        # open step file
        step_df = pd.read_csv(step_file)
        int_time_list = list(step_df['int_time'])

        # go through video folder
        for idx, file_name in enumerate(os.listdir(video_folder)):  # 遍历video_01下的所有txt文件; 0, 00000.txt; 自动忽略第一行
            # instrument csv file
            instrument_row = instrument_df.iloc[idx]  # 第idx+1行
            num_of_tool = get_num_of_tool(instrument_row)

            if (instrument_row['str_instrument1'] == 'out_of_patient' or
                    instrument_row['str_instrument2'] == 'out_of_patient'):
                continue

            # step csv file
            step_name = get_current_step_name(step_df, int_time_list, idx)
            if step_name in ['out_of_patient', 'operation_not_started', 'operation_ended']:
                continue

            # print(f'index: {idx}')
            if num_of_tool == 0:

                if num_of_tool not in tool_num:
                    tool_num[num_of_tool] = 1
                else:
                    tool_num[num_of_tool] += 1

                phase_qa_str, current_phase = prepare_what_phase_qa(step_name)  # 3
                step_qa_str = prepare_what_step_qa(step_name)  # 14

                next_phase_qa_str = prepare_next_phase_qa(current_phase)
                next_step_qa_str = prepare_next_step_qa(step_name)

                how_many_tool_qa_str = prepare_how_many_tool_qa(num_of_tool)

                qa_list = [phase_qa_str, step_qa_str, next_phase_qa_str, next_step_qa_str, how_many_tool_qa_str]
                write_file(video_folder, file_name, qa_list)
                questions += 5
                frames += 1

            if num_of_tool == 1:

                if num_of_tool not in tool_num:
                    tool_num[num_of_tool] = 1
                else:
                    tool_num[num_of_tool] += 1

                phase_qa_str, current_phase = prepare_what_phase_qa(step_name)
                step_qa_str = prepare_what_step_qa(step_name)
                operation_qa_str, operation = prepare_what_operation_qa(step_name)  # 0没有的

                next_phase_qa_str = prepare_next_phase_qa(current_phase)
                next_step_qa_str = prepare_next_step_qa(step_name)

                what_tool_qa_str = prepare_what_tool_qa_one(instrument_row)  # 0没有的
                tool_operation_qa_str = prepare_tool_operation_qa(instrument_row, operation)
                where_tool_qa_str = prepare_where_tool_qa(instrument_row)

                how_many_tool_qa_str = prepare_how_many_tool_qa(num_of_tool)

                qa_list = [phase_qa_str, step_qa_str, operation_qa_str, next_phase_qa_str, next_step_qa_str,
                           what_tool_qa_str, tool_operation_qa_str, where_tool_qa_str, how_many_tool_qa_str]
                write_file(video_folder, file_name, qa_list)
                questions += 9
                frames += 1

            if num_of_tool == 2:

                if num_of_tool not in tool_num:
                    tool_num[num_of_tool] = 1
                else:
                    tool_num[num_of_tool] += 1

                phase_qa_str, current_phase = prepare_what_phase_qa(step_name)
                step_qa_str = prepare_what_step_qa(step_name)
                operation_qa_str, operation = prepare_what_operation_qa(step_name)

                next_phase_qa_str = prepare_next_phase_qa(current_phase)
                next_step_qa_str = prepare_next_step_qa(step_name)

                what_tool_qa_str_1 = prepare_what_tool_qa_two(instrument_row, col_num=1)
                what_tool_qa_str_2 = prepare_what_tool_qa_two(instrument_row, col_num=2)

                tool_operation_qa_str_1 = prepare_tool_operation_qa_two(instrument_row, operation, col_num=1)
                tool_operation_qa_str_2 = prepare_tool_operation_qa_two(instrument_row, operation, col_num=2)

                where_tool_qa_str_1 = prepare_where_tool_qa_two(instrument_row, col_num=1)
                where_tool_qa_str_2 = prepare_where_tool_qa_two(instrument_row, col_num=2)

                how_many_tool_qa_str = prepare_how_many_tool_qa(num_of_tool)

                qa_list = [phase_qa_str, step_qa_str, operation_qa_str, next_phase_qa_str, next_step_qa_str,
                           what_tool_qa_str_1, what_tool_qa_str_2, tool_operation_qa_str_1, tool_operation_qa_str_2,
                           where_tool_qa_str_1, where_tool_qa_str_2, how_many_tool_qa_str]
                write_file(video_folder, file_name, qa_list)
                questions += 12
                frames += 1

        print(count_dict)
        print(f'video_{i} finished.')

    print(tool_num)

    print(f'number of frames: {frames}')
    print(f'number of questions: {questions}')
    print(f'sum of dict: {sum(count_dict.values())}')
