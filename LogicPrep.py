
import Util

class LogicPreps:

    def __init__(self):
        self.ext_tmp = ""

    def get_target_readlines_by_fn(self, sources, delimiter, trgt_line):
        util = Util.Utils()
        strt_line = trgt_line[0]
        end_line = trgt_line[1]

        result_dict = {}
        for file_path in sources:
            read_list = util.read_txt(file_path)
            fn_key = file_path[file_path.index(delimiter) + len(delimiter) + 1:]
            result_dict.update({fn_key: read_list[strt_line: end_line]})

        return result_dict
