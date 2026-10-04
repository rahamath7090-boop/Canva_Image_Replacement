from image_replacer import replace_image


design = "designs/design_01_travel.png"

replacement = (
    "data/mountains/mountain_08.jpg"
)

output = "outputs/test_result.png"

box = (
    250,
    150,
    750,
    500
)

replace_image(
    design,
    replacement,
    output,
    box
)

print(
    "Replacement completed!"
)

print(
    "Saved to:",
    output
)