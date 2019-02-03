import json
from watson_developer_cloud import VisualRecognitionV3
from watson_developer_cloud import WatsonApiException
import numpy

visual_recognition = VisualRecognitionV3 (
    '2018-03-19',
    iam_apikey = 'X_euWqW0sHEleKL5MkNdFFVwidBozz05MY_KPE9Rz-An')


try:
    # Invoke a Visual Recognition method
    classifiers = visual_recognition.list_classifiers(verbose=True).get_result()
    #print (json.dumps(classifiers, indent=2))
    #print ((classifiers))
    for i in classifiers ['classifiers']:
        x = i ['classifier_id']
        with open ('./first.jpg','rb') as image_file:
            classes = visual_recognition.classify(
                image_file,
                threshold= '0.0',
                owners= ["me"],classifier_ids=x).get_result()
            print (json.dumps(classes,indent =2))
except WatsonApiException as ex:
    print "Method failed with status code " + str(ex.code) + ": " + ex.message

wearDesign = {}
for i in classes ['images']:
    for x in i ['classifiers']:
        for y in x ['classes']:
            wearDesign [y['class']] = y['score']

specialSelection = [];
with open ('./first.jpg', 'rb') as image_file:
    classes_result = visual_recognition.classify(image_file).get_result()
    for i in classes_result ['images']:
        for x in i ['classifiers']:
            for y in x ['classes']:
                #print (y)
                if y['score']>=0.6:
                    specialSelection.append(y['class'])
#print(json.dumps(classes_result, indent=2))


print (specialSelection)
print (wearDesign)