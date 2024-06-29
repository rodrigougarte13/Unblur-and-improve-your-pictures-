# Unblur-and-improve-your-pictures

This project was born out of my passion for restoring old family photos and processing analog images, a hobby of mine. It utilizes advanced image processing techniques and a UNet architecture implemented in Python with TensorFlow to enhance image clarity and detail. Currently a work in progress, the algorithm aims to significantly improve image quality, particularly in correcting blur, taking inspiration from ESRGAN (Enhanced Super-Resolution Generative Adversarial Networks). Version 1 of the model tackled initial computational limitations by resizing images for processing, showing promising improvements in image sharpness and detail. Looking ahead, ongoing efforts focus on expanding the model's capability to handle images of various resolutions seamlessly. Additionally, this software can serve as a preprocessing tool for ESRGAN, preparing images for further enhancement with super-resolution techniques, resulting in enhanced detail and clarity.

The 3 projected improvements are: increasing the size of the training images, making the blurr function harsher, so the model can correct even blurrier photos and finally make the model accept any resolution. 

Ths is the best result, we we can see there is evident correction of the blurriness of the fish:.

![IMG_9210](https://github.com/rodrigougarte13/Unblur-and-improve-your-pictures-/assets/142838779/f01b232e-6b14-4ef2-b86f-186b6190e957)

This video was really helpful in understaing the UNet: https://www.youtube.com/watch?v=NhdzGfB1q74
