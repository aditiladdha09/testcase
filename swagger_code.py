# Script to parse swagger and generate Karate test cases

import yaml
import json

def parse_swagger(swagger_path):
    with open(swagger_path, 'r') as file:
        return yaml.safe_load(file)

def generate_feature_file(swagger):
    feature_file_content = ""
    base_path = swagger.get('basePath', '')

    for path, methods in swagger['paths'].items():
        for method, details in methods.items():
            feature_file_content += f"Scenario: {method.upper()} {base_path}{path}\n"
            feature_file_content += f"  Given url baseUrl + '{base_path}{path}'\n"
            if 'parameters' in details:
                for param in details['parameters']:
                    if param['in'] == 'body':
                        feature_file_content += f"  And request {param['name']}\n"
            feature_file_content += f"  When method {method}\n"
            feature_file_content += f"  Then status 200\n"
            feature_file_content += f"  And match response == expectedResponse\n\n"
    
    return feature_file_content

def write_feature_file(content, output_path):
    with open(output_path, 'w') as file:
        file.write(content)

def main():
    swagger = parse_swagger('swagger.yaml')
    feature_content = generate_feature_file(swagger)
    write_feature_file(feature_content, 'features/generated.feature')

if __name__ == "__main__":
    main()
