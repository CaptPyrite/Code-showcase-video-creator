import cv2
import os
from carbonAPI import Carbon
from PIL import Image, ImageOps

def frames2vid(frames:str,folder:str, filename:str):
    frame = cv2.imread(os.path.join(folder, "1.png"))
    height, width, layers = frame.shape
    
    video = cv2.VideoWriter(filename, 0, 11, (width,height))
    
    for image in frames:
        video.write(cv2.imread(os.path.join(folder, image)))
    
    cv2.destroyAllWindows()
    video.release()
    
    return True

def code2frames(folder:str, code:str):
    carbon = Carbon.sh("Z:/Coding/Video-creator/chromedriver.exe") # Change to the folder of your chrome driver
    urls = [carbon.code2url(code[:i+1]) for i in range(len(code))]
    for index, link in enumerate(urls):
        carbon.url2img(link, f"{folder}/{index+1}.png")
    return folder
    

def resize_frames(frames:list, folder:str):
    desired_size = Image.open(f"{folder}/" + frames[-1]).size
    color = (176, 188, 196)

    for frame in frames[:-1]:
        img = Image.open(f"{folder}/" + frame)
        delta_width = desired_size[0] - img.size[0]
        delta_height = desired_size[1] - img.size[1]
        pad_width = delta_width // 2
        pad_height = delta_height // 2
        padding = (pad_width, pad_height, delta_width - pad_width, delta_height - pad_height)
        img = ImageOps.expand(img, padding)
    
        width, height = img.size
        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                if len(pixel) == 4 and pixel[3] == 0:
                    img.putpixel((x, y), color)
        img.save(f"{folder}/" + frame)
    
code = """
print("Hello, World")

"""[1:]


if len(os.listdir("output")) <= 0:
    code2frames("output", code)

frames = sorted(os.listdir("output"), key=len)

resize_frames(frames, "output")
frames2vid(frames, "output", "otuput.avi")

