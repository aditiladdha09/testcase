import yaml
import json

def generate_karate_feature_from_swagger(swagger_path):
    with open(swagger_path, 'r') as file:
        swagger = yaml.safe_load(file)

    feature_content = "Feature: API Testing with Swagger Document\n\n"
    feature_content += "Background:\n"
    feature_content += "  * def constants = read('datafiles/petstore/constants.json')\n"
    feature_content += "  * def expectedRequest = read('datafiles/petstore/expectedRequest.json')\n"
    feature_content += "  * def expectedResponse = read('datafiles/petstore/expectedResponse.json')\n\n"

    for path, methods in swagger['paths'].items():
        for method, details in methods.items():
            scenario = f"Scenario: Test API endpoint {path} ({method.upper()})\n"
            scenario += f"  Given url constants.basePath + '{path}'\n"
            if method in ['post', 'put', 'patch']:
                scenario += f"  And request expectedRequest.{details['operationId']}\n"
            scenario += f"  When method {method}\n"
            scenario += "  Then status 200\n"
            scenario += f"  And match response == expectedResponse.{details['operationId']}\n"
            scenario += f"  And schema validation 'schemas/{details['operationId']}Schema.json'\n\n"
            feature_content += scenario

    with open('features/swagger_features.feature', 'w') as file:
        file.write(feature_content)

# Example usage
generate_karate_feature_from_swagger('swagger.yaml')
