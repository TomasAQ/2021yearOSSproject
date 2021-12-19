import os
from flask import Flask, request , render_template
from werkzeug.utils import secure_filename

import torch
import torch.nn as nn
import torch.optim as optim

import torchvision
from torchvision import datasets, models, transforms

import numpy as np
import copy
from PIL import Image



application = Flask(__name__)


def spotfind(filename):
    spotfind = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    image = Image.open('./upImg/'+filename).convert('RGB')
    image = spotfind(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = myModel(image)
        _, preds = torch.max(outputs, 1)
        print('예측 결과 : ' + MyClass_Names[preds[0]])
        return galTitle_list[preds[0]] + "&#&" + galPhotographyLocation_list[preds[0]] + "&#&" + galWebImageUrl_list[preds[0]]



@application.route("/")
def hello() :
    return "<h1>Hello!</h1>"

@application.route('/testupimg')
def hellohtml() :
    return render_template('testupimg.html')


# 파일 업로드 처리
@application.route('/fileUpload' , methods=['GET','POST'])
def upload_file():

    if request.method == 'POST':
        f = request.files['img']
        filenames = secure_filename(f.filename)
        f.save("./upImg/"+filenames)
        result = spotfind(filenames)

    return result






if __name__ == "__main__":
    global myModel
    global MyClass_Names

    data = open('./sportinfo.txt',encoding='UTF8')
    MyClass_Names = [str(sport) for sport in data.read().split('\n')]

    galTitle_list = []
    galPhotographyLocation_list = []
    galWebImageUrl_list = []
    for i in range(len(MyClass_Names)):
        galTitle, galPhotographyLocation, galWebImageUrl = MyClass_Names[i].split('\\')
        galTitle_list.append(galTitle)
        galPhotographyLocation_list.append(galPhotographyLocation)
        galWebImageUrl_list.append(galWebImageUrl)
    MyClass_Names = galTitle_list
    print("get MyClass")

    device = torch.device('cpu')
    myModel = models.resnet34(pretrained=True)
    num_features = myModel.fc.in_features
    myModel.fc = nn.Linear(num_features, out_features=41)
    myModel.load_state_dict(copy.deepcopy(torch.load("./model_state.pth", device)))
    myModel.eval()
    print("get MyModel")

    application.run(host='0.0.0.0', port='80')