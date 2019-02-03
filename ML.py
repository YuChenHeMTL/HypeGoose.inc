import json
from watson_developer_cloud import VisualRecognitionV3
from watson_developer_cloud import WatsonApiException


visual_recognition = VisualRecognitionV3 (
    '2018-03-19',
    iam_apikey = 'X_euWqW0sHEleKL5MkNdFFVwidBozz05MY_KPE9Rz-An')


try:
    # Invoke a Visual Recognition method
    classifiers = visual_recognition.list_classifiers(verbose=True).get_result()
    print (json.dumps(classifiers, indent=2))
    print ((classifiers))
    for i in classifiers ['classifiers']:
        x = i ['classifier_id']
        visual_recognition.delete_classifier(x)
except WatsonApiException as ex:
    print "Method failed with status code " + str(ex.code) + ": " + ex.message



with open('./testingData/beagle.zip', 'rb') as beagle, open(
        './testingData/golden-retriever.zip', 'rb') as goldenretriever, open(
            './testingData/husky.zip', 'rb') as husky, open(
                './testingData/cats.zip', 'rb') as cats:
    model = visual_recognition.create_classifier(
        'dogs',
        beagle_positive_examples=beagle,
        goldenretriever_positive_examples=goldenretriever,
        husky_positive_examples=husky,
        negative_examples=cats).get_result()
print(json.dumps(model, indent=2))
modelID = ""

modelID = model ['classifier_id']

with open ('./first.jpg','rb') as image_file:
    classes = visual_recognition.classify(
        image_file,
        threshold= '0.5',
        owners= ["me"],classifier_ids=modelID).get_result()
    print (json.dumps(classes,indent =2))