import cv2
import os
import tempfile
import pytesseract
from pdf2image import convert_from_path
import time


"""extract text from images"""


def extract_text_from_image(image_path, language):
    extracted_text = pytesseract.image_to_string(
        image_path,
        lang=language,
    )
    return extracted_text


"""split image into 2 coloumns"""


def DATA_EXTRACTION_2_Columns(
    pdf_path, left_partition, right_partition, lang_part_first, lang_part_second
):
    images = convert_from_path(pdf_path)

    left_folder = "left"
    right_folder = "right"
    os.makedirs(left_folder, exist_ok=True)
    os.makedirs(right_folder, exist_ok=True)
    first_part_text = ""
    second_part_text = ""

    for page_num, image in enumerate(images):
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            image_path = temp_file.name
            image.save(image_path, "JPEG")

            img = cv2.imread(image_path)

            h, w, channels = img.shape

            left_cut = int(w * 0.01 * float(left_partition))
            right_cut = int(w * 0.01 * float(right_partition))

            left_part = img[:, :left_cut]
            right_part = img[:, -right_cut:]

            left_image_path = os.path.join(left_folder, f"left_{page_num + 1}.jpg")
            right_image_path = os.path.join(right_folder, f"right_{page_num + 1}.jpg")

            cv2.imwrite(left_image_path, left_part)
            cv2.imwrite(right_image_path, right_part)

            extracted_text_part_first = extract_text_from_image(
                left_image_path, lang_part_first
            )
            first_part_text += extracted_text_part_first

            extracted_text_part_second = extract_text_from_image(
                right_image_path, lang_part_second
            )
            second_part_text += extracted_text_part_second

            temp_file.close()
            os.remove(image_path)

    return first_part_text, second_part_text


"""split image into 2 rows"""


def DATA_EXTRACTION_2_Rows(
    pdf_path, top_partition, bottom_partition, lang_part_first, lang_part_second
):
    images = convert_from_path(pdf_path)

    top_folder = "top"
    bottom_folder = "bottom"
    os.makedirs(top_folder, exist_ok=True)
    os.makedirs(bottom_folder, exist_ok=True)
    top_part_text = ""
    bottom_part_text = ""

    for page_num, image in enumerate(images):
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            image_path = temp_file.name
            image.save(image_path, "JPEG")

            img = cv2.imread(image_path)

            h, w, channels = img.shape

            top_cut = int(h * 0.01 * float(top_partition))
            bottom_cut = int(h * 0.01 * float(bottom_partition))

            top_part = img[:, :top_cut]
            bottom_part = img[:, -bottom_cut:]

            top_image_path = os.path.join(top_folder, f"left_{page_num + 1}.jpg")
            bottom_image_path = os.path.join(bottom_folder, f"right_{page_num + 1}.jpg")

            cv2.imwrite(top_image_path, top_part)
            cv2.imwrite(top_image_path, bottom_part)

            extracted_text_part_first = extract_text_from_image(
                top_image_path, lang_part_first
            )
            top_part_text += extracted_text_part_first

            extracted_text_part_second = extract_text_from_image(
                bottom_image_path, lang_part_second
            )
            bottom_part_text += extracted_text_part_second

            temp_file.close()
            os.remove(image_path)

    return top_part_text, bottom_part_text


""" split images into multiparts"""


def split_pdfimage_into_folders(pdf_path, w_size, h_size, output_folder):
    images = convert_from_path(pdf_path)

    for page_num, image in enumerate(images):
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
            image_path = temp_file.name
            image.save(image_path, "JPEG")

            img = cv2.imread(image_path)

            height, width, channels = img.shape

            os.makedirs(output_folder, exist_ok=True)

            for ih in range(h_size):
                for iw in range(w_size):
                    x = width / w_size * iw
                    y = height / h_size * ih
                    h = height / h_size
                    w = width / w_size

                    img_part = img[int(y) : int(y + h), int(x) : int(x + w)]

                    part_folder = os.path.join(output_folder, f"Part_{ih}_{iw}")
                    os.makedirs(part_folder, exist_ok=True)

                    part_filename = os.path.join(part_folder, f"{int(time.time())}.png")
                    cv2.imwrite(part_filename, img_part)

    return img
