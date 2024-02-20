import yaml

yaml_file = open('startrek.yml', 'r')

dict = yaml.safe_load(yaml_file)

print(dict['ships']['1701-D']['Captain'])