from time import clock
import os

import Util
import LogicPrep
############### start to set env ################
WORK_DIR = os.getcwd() + "/"

INPUT = "input"
OUTPUT = "output"

# [start line, right after end line]
TARGET_LINES = [0, 1]  # line 0 ~ line 0 (line 1 is right after the end line)
############### end setting env #################

def get_file_name_and_first_line_of_the_file():
    util = Util.Utils()
    logic_prep = LogicPrep.LogicPreps()

    txt_sources = util.get_files_from_dir(WORK_DIR + INPUT + '/*.txt')
    result_dict = logic_prep.get_target_readlines_by_fn(txt_sources, INPUT, TARGET_LINES)

    util.make_excel(WORK_DIR + OUTPUT + '/result', result_dict)



start_time = clock()
print("start >>>>>>>>>>>>>>>>>>")
get_file_name_and_first_line_of_the_file()
print("::::::::::: %.2f seconds ::::::::::::::" % (clock() - start_time))