import argparse
import os
import requests
import dotenv
from text2image import Illusion_diffusion
from plantNet import PlantNet


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('prompt', help='prompt to generate image', type=str)
    parser.add_argument('--imgName', help='Name of image', type=str, default='generated_image')
    args = parser.parse_args()


    dotenv = dotenv.load_dotenv()
    PlantNet_API_KEY = os.getenv("PlantNet_API_KEY")
    illusion_API_KEY = os.getenv("illusion_API_KEY")

    try:
        text2img_obj = Illusion_diffusion(PlantNet_API_KEY=PlantNet_API_KEY, prompt=args.prompt)
        if text2img_obj.get_responseStatus != 200:
            raise Exception(f"There is a problem in generating image.")
        
        res = requests.get(text2img_obj.get_imgLink(), allow_redirects=True)
        open(f'{args.imgName}.png', 'wb').write(res.content)

        plantNet_obj = PlantNet(PlantNet_API_KEY=PlantNet_API_KEY, imgPath=f'{args.imgName}.png')
        if plantNet_obj.get_responseStatus != 200:
            raise Exception(f"There is a problem in identifying plant.")
        
        
    except Exception as e:
        print(e)
    else:
        print(PlantNet.get_plantName())

    
if __name__ == "__main__":
    main()