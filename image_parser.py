from PIL import Image

class ImageParser(object):
    def size(self, image_path):
        return Image.open(image_path).size
