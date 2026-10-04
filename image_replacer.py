from PIL import Image, ImageOps
import os


def replace_image(
    design_path,
    replacement_path,
    output_path
):

    # ==========================================
    # OPEN SELECTED DESIGN
    # ==========================================

    design = Image.open(
        design_path
    ).convert("RGB")


    # ==========================================
    # OPEN TOP SIMILAR IMAGE
    # ==========================================

    replacement = Image.open(
        replacement_path
    ).convert("RGB")


    # ==========================================
    # GET COMPLETE DESIGN SIZE
    # ==========================================

    design_width, design_height = design.size


    # ==========================================
    # FIT SIMILAR IMAGE TO ENTIRE BACKGROUND
    # ==========================================

    fitted_image = ImageOps.fit(
        replacement,
        (design_width, design_height),
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5)
    )


    # ==========================================
    # REPLACE ENTIRE BACKGROUND
    # ==========================================

    design = fitted_image


    # ==========================================
    # CREATE OUTPUT FOLDER
    # ==========================================

    output_folder = os.path.dirname(
        output_path
    )

    if output_folder:
        os.makedirs(
            output_folder,
            exist_ok=True
        )


    # ==========================================
    # SAVE FINAL DESIGN
    # ==========================================

    design.save(
        output_path,
        quality=95
    )


    return output_path