import yaml

#函数功能：读取整个yaml文件，并返回
def yaml_data_with_file(file_name, key):
    with open("./data/" + file_name + ".yaml", "r") as f:
        data = yaml.load(f)[key]
        case_data_list = list()
        for case_data in data.values():
            #print(case_data)
            case_data_list.append(case_data)
        return case_data_list
