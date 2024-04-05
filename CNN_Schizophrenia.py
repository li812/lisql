#CNN_Schizophrenia.py

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
#from dPred import CNN_Schizophrenia

# Define Architecture For CNN_Schizophrenia
class CNN_Schizophrenia(nn.Module):
    
    # Network Initialisation
    def __init__(self, params):
        super(CNN_Schizophrenia, self).__init__()
        Cin, Hin, Win = params["shape_in"]
        init_f = params["initial_filters"] 
        num_fc1 = params["num_fc1"]  
        num_classes = params["num_classes"] 
        self.dropout_rate = params["dropout_rate"] 
        
        # Convolution Layers
        self.conv1 = nn.Conv2d(Cin, init_f, kernel_size=3)
        h, w = findConv2dOutShape(Hin, Win, self.conv1)
        self.conv2 = nn.Conv2d(init_f, 2*init_f, kernel_size=3)
        h, w = findConv2dOutShape(h, w, self.conv2)
        self.conv3 = nn.Conv2d(2*init_f, 4*init_f, kernel_size=3)
        h, w = findConv2dOutShape(h, w, self.conv3)
        self.conv4 = nn.Conv2d(4*init_f, 8*init_f, kernel_size=3)
        h, w = findConv2dOutShape(h, w, self.conv4)
        
        # compute the flatten size
        self.num_flatten = h * w * 8 * init_f
        self.fc1 = nn.Linear(self.num_flatten, num_fc1)
        self.fc2 = nn.Linear(num_fc1, num_classes)

    def forward(self, X):
        # Convolution & Pool Layers
        X = F.relu(self.conv1(X))
        X = F.max_pool2d(X, 2, 2)
        X = F.relu(self.conv2(X))
        X = F.max_pool2d(X, 2, 2)
        X = F.relu(self.conv3(X))
        X = F.max_pool2d(X, 2, 2)
        X = F.relu(self.conv4(X))
        X = F.max_pool2d(X, 2, 2)
        X = X.view(-1, self.num_flatten)
        X = F.relu(self.fc1(X))
        X = F.dropout(X, self.dropout_rate)
        X = self.fc2(X)
        return F.log_softmax(X, dim=1)

def findConv2dOutShape(Hin, Win, conv, pool=2):
    kernel_size = conv.kernel_size
    padding = conv.padding
    stride = conv.stride
    dilation = conv.dilation
    out_height = ((Hin + 2 * padding[0] - dilation[0] * (kernel_size[0] - 1) - 1) / stride[0]) + 1
    out_width = ((Win + 2 * padding[1] - dilation[1] * (kernel_size[1] - 1) - 1) / stride[1]) + 1
    return int(out_height), int(out_width)

def predict(image_path):
    # Define the transformation for preprocessing the image
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])

    # Load the saved model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = torch.load("Schizophrenia_Model.pt", map_location=device)  # Load the model
    model.eval()

    # Load and preprocess the new image
    image = Image.open(image_path)
    image = transform(image)  # Apply the transformation

    if image.shape[0] == 1:
        image = torch.cat([image] * 3)

    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    image = normalize(image)

    image = image.unsqueeze(0)

    with torch.no_grad():
        output = model(image)

    predicted_probabilities = torch.exp(output)
    predicted_class = torch.argmax(predicted_probabilities, dim=1).item()

    class_labels = {
        0: 'Negative',
        1: 'Positive'
    }

    return class_labels[predicted_class]



