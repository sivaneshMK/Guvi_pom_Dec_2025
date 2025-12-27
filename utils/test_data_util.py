import csv
import os
import pandas as pd
import yaml


def read_csv(env_config):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    filepath = os.path.join(root, env_config['test_data_path'])
    value =pd.read_csv(filepath).to_dict(orient="records")
    print(value)
    ##[{'Test_name': 'test_search_content_is_displayed', 'search_string': 'new movie', 'result': nan}]
    '''[{'Test_name': 'test_search_content_is_displayed', 'search_string': 'new movie', 'result': nan},
     {'Test_name': 'test_somthing', 'search_string': 'New Songs', 'result': 'Song'}]
        '''
    return value


def get_test_data(env_config, field):
    data= read_csv(env_config)
    return data[0][field]

def get_data(env_config, test_name, column_name):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    filepath = os.path.join(root, env_config['test_data_path'])

    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"reader{reader}")
        for row in reader:
            if row['Test_name'] == test_name:
                value = row.get(column_name)
                return value

    raise ValueError(f"No data found for test{test_name}, and column{column_name}")

def write_data_into_csv(env_config, test_name, column_name, value):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    filepath = os.path.join(root, env_config['test_data_path'])

    df = pd.read_csv(filepath)
    df.loc[df["Test_name"] == test_name, column_name] = value
    df.to_csv(filepath, index=False)