import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image


class FeatureExtractor:

    def __init__(self):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        weights = models.ResNet50_Weights.DEFAULT

        model = models.resnet50(weights=weights)

        self.model = torch.nn.Sequential(
            *list(model.children())[:-1]
        )

        self.model = self.model.to(self.device)
        self.model.eval()

        self.transform = weights.transforms()

    def extract(self, image_path):

        image = Image.open(image_path).convert("RGB")

        image = self.transform(image)

        image = image.unsqueeze(0).to(self.device)

        with torch.no_grad():

            features = self.model(image)

        features = features.squeeze()

        features = features.cpu().numpy()

        return features