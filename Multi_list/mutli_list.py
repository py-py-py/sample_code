def create_num_list(target_list):
    tmp_num_list = []
    for num in target_list:
        tmp_num_list.append(int(num.split("-")[0]))
    num_list = list(set(tmp_num_list))
    return num_list


def create_multi_list(target_list, num_list):
    results = []
    tmp_result = []
    for num in num_list:
        for content in target_list:
            if content.split("-")[0] == str(num):
                tmp_result.append(content)
        results.append(tmp_result)
        tmp_result = []
    return results


if __name__ == '__main__':
    target_list = [
        "1-1", "1-2", "1-3", "2-1", "2-2", "2-3", "2-4"
    ]
    num_list = create_num_list(target_list)
    results = create_multi_list(target_list, num_list)
    for result in results:
        print(",".join(result))


