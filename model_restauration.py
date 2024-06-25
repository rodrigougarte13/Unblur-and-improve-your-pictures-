import tensorflow as tf
import cv2
import numpy as np
import os

def load_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (256, 256))
    image = image / 255.0
    return image

def save_image(image, output_path):
    image = (image * 255).astype(np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, image)

def restore_images(input_dir, output_dir, model_path):
    try:
        # Load the model
        print(f"Loading model from: {model_path}")
        model = tf.keras.models.load_model(model_path)
        print(f"Model loaded successfully from {model_path}")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Process each image
        for filename in os.listdir(input_dir):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)

                # Load and prepare the image
                image = load_image(input_path)
                restored_image = model.predict(np.expand_dims(image, axis=0))[0]

                # Save the restored image
                save_image(restored_image, output_path)
    except Exception as e:
        print(f"Error loading model: {e}")

if __name__ == "__main__":
    input_dir = "TEST_INPUT"
    output_dir = "TEST_OUTPUT"
    model_path = "C:/Users/rodri/OneDrive/Documents/Personal Projects/Unblur-and-improve-your-pictures-/models/unet_model.keras"

    print("Starting restoration process...")
    restore_images(input_dir, output_dir, model_path)
    print("Restoration process finished.")
