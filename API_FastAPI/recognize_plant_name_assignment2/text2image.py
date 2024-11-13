import json
import requests


class Illusion_diffusion():
    def __init__(self, illusion_API_KEY, prompt):
        self.illusion_url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
        self.payload = {
            "image_url": "https://storage.googleapis.com/falserverless/illusion-examples/cubes.jpeg",
            "prompt": f"(masterpiece:1.4), (best quality), (detailed), {prompt}",
            "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
        }

        self.headers = {
            "Authorization": illusion_API_KEY,
            "Content-Type": "application/json"
        }

        self.response = requests.post(self.illusion_url, json=self.payload, headers=self.headers)

    def get_responseStatus(self):
        return self.response.status_code
    
    def get_imgLink(self):
        return self.response.json()['image']['url']


# An emotional portrait of a kind grandmother with white hair, a calm smile and deep wrinkles on her face. 
# She holds a bright red carnation in her hand and looks at it kindly. 
# Natural light shines through the window and shines on the carnation petals. 
# The background of the room is simple and bright with pastel colors
        