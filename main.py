from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

image_photo = None
watermark_photo = None
image_uploaded = False

def upload_image():
    global image_photo, image_uploaded
    image_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    if image_path:
        img = Image.open(image_path)
        img.thumbnail((280, 400))
        image_photo = ImageTk.PhotoImage(img)

        image_canvas.delete("all")
        image_canvas.create_image(140, 200, image=image_photo)

        image_uploaded = True
        convert.pack(pady=20)
    else:
        print("No image selected")

def upload_watermark():
    global watermark_photo
    watermark_path = filedialog.askopenfilename(
        title="Select a watermark",
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    if watermark_path:
        watermark = Image.open(watermark_path)
        watermark.thumbnail((280, 400))
        watermark_photo = ImageTk.PhotoImage(watermark)

        watermark_canvas.delete("all")
        watermark_canvas.create_image(140, 200, image=watermark_photo)
    else:
        print("No watermark selected")

def add_watermark():
    main_frame.pack(fill="both", expand=False, pady=20)

window = tk.Tk()
window.title("Image Watermark Generator")
window.minsize(600,600)
window.resizable(False, False)

frames_container = tk.Frame(window)
frames_container.pack(fill="both", expand=False)

left_frame = tk.Frame(frames_container)
left_frame.pack(side="left", fill="both", expand=True, padx=10)

right_frame = tk.Frame(frames_container)
right_frame.pack(side="right", fill="both", expand=True, padx=10)

main_frame = tk.Frame(window)


uploaded_image = tk.Button(left_frame, text="Upload Image", command=upload_image)
uploaded_image.pack(pady=10)
image_canvas = tk.Canvas(left_frame, width=280, height=400, bg="lightgray")
image_canvas.pack(pady=10)

uploaded_watermark = tk.Button(right_frame, text="Upload Watermark", command=upload_watermark)
uploaded_watermark.pack(pady=10)
watermark_canvas = tk.Canvas(right_frame, width=280, height=400, bg="lightgray")
watermark_canvas.pack(pady=10)

convert = tk.Button(window, text="Apply Watermark", command=add_watermark)

window.mainloop()
