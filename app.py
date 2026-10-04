import streamlit as st
from PIL import Image
import os

from similarity_search import search_similar_images
from image_replacer import replace_image


# ============================================================
# PROJECT PATH
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

QUERIES_DIR = os.path.join(
    BASE_DIR,
    "queries"
)

OUTPUTS_DIR = os.path.join(
    BASE_DIR,
    "outputs"
)

DESIGNS_DIR = os.path.join(
    BASE_DIR,
    "designs"
)


# ============================================================
# CREATE REQUIRED FOLDERS
# ============================================================

os.makedirs(QUERIES_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)
os.makedirs(DESIGNS_DIR, exist_ok=True)


# ============================================================
# STREAMLIT PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Canva Image Replacement",
    page_icon="🖼️",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🖼️ Canva Image Replacement")

st.write(
    "Select a design and a query image. "
    "The query image is used only to find visually similar images. "
    "The Top 5 similar images are then used for replacement."
)


# ============================================================
# STEP 1 - SELECT DESIGN
# ============================================================

st.header("1. Select Design")

design_file = st.file_uploader(
    "Upload the Canva design",
    type=["jpg", "jpeg", "png"],
    key="design"
)


# ============================================================
# STEP 2 - SELECT QUERY IMAGE
# ============================================================

st.header("2. Select Query Image")

query_file = st.file_uploader(
    "Upload the query image",
    type=["jpg", "jpeg", "png"],
    key="query"
)


# ============================================================
# SHOW DESIGN
# ============================================================

design_path = None

if design_file is not None:

    design_path = os.path.join(
        DESIGNS_DIR,
        "selected_design.png"
    )

    with open(
        design_path,
        "wb"
    ) as f:

        f.write(
            design_file.getbuffer()
        )

    st.subheader("Selected Design")

    st.image(
        design_file,
        width=650
    )


# ============================================================
# SHOW QUERY IMAGE
# ============================================================

query_path = None

if query_file is not None:

    query_path = os.path.join(
        QUERIES_DIR,
        "uploaded_query.jpg"
    )

    with open(
        query_path,
        "wb"
    ) as f:

        f.write(
            query_file.getbuffer()
        )

    st.subheader("Query Image")

    st.image(
        query_file,
        width=350
    )


# ============================================================
# START BUTTON
# ============================================================

if design_file is not None and query_file is not None:

    st.divider()

    start = st.button(
        "🔍 Find Similar Images and Replace",
        type="primary"
    )


    # ========================================================
    # RUN PROCESS
    # ========================================================

    if start:

        # ----------------------------------------------------
        # STEP 3 - SIMILARITY SEARCH
        # ----------------------------------------------------

        with st.spinner(
            "Finding the Top 5 similar images..."
        ):

            results = search_similar_images(
                query_path,
                top_k=5
            )


        # ----------------------------------------------------
        # CHECK RESULTS
        # ----------------------------------------------------

        if not results:

            st.error(
                "No similar images were found."
            )

            st.stop()


        # ----------------------------------------------------
        # TOP 5 SIMILAR IMAGES
        # ----------------------------------------------------

        st.header("3. Top 5 Similar Images")

        cols = st.columns(5)

        for i, result in enumerate(results):

            with cols[i]:

                st.image(
                    result["path"],
                    use_container_width=True
                )

                st.write(
                    f"**Rank {i + 1}**"
                )

                st.write(
                    f"Similarity: "
                    f"{result['score']:.2%}"
                )


        # ====================================================
        # IMAGE REPLACEMENT
        # ====================================================

        st.header("4. Final Designs")

        st.write(
            "Each Top 5 similar image is fitted into "
            "the selected design separately."
        )


        # ----------------------------------------------------
        # GENERATE 5 DESIGNS
        # ----------------------------------------------------

        for i, result in enumerate(results):

            # IMPORTANT:
            # This is the similar image returned by
            # similarity search.
            #
            # The query image is NOT used here.

            replacement_path = result["path"]


            # Output filename

            output_path = os.path.join(
                OUTPUTS_DIR,
                f"final_design_{i + 1}.png"
            )


            # ------------------------------------------------
            # REPLACE IMAGE
            # ------------------------------------------------

            try:

                replace_image(
                    design_path=design_path,
                    replacement_path=replacement_path,
                    output_path=output_path
                )

            except Exception as e:

                st.error(
                    f"Error creating Design {i + 1}: {e}"
                )

                continue


            # ------------------------------------------------
            # DISPLAY FINAL DESIGN
            # ------------------------------------------------

            st.subheader(
                f"Final Design {i + 1}"
            )

            st.image(
                output_path,
                width=650
            )


            st.write(
                f"Replacement image: "
                f"{os.path.basename(replacement_path)}"
            )

            st.write(
                f"Similarity score: "
                f"{result['score']:.2%}"
            )


            # ------------------------------------------------
            # DOWNLOAD BUTTON
            # ------------------------------------------------

            with open(
                output_path,
                "rb"
            ) as file:

                st.download_button(
                    label=f"⬇️ Download Final Design {i + 1}",
                    data=file,
                    file_name=f"final_design_{i + 1}.png",
                    mime="image/png",
                    key=f"download_{i}"
                )


        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        st.success(
            "✅ Top 5 similar images have been "
            "processed successfully!"
        )


# ============================================================
# INFORMATION WHEN FILES ARE NOT SELECTED
# ============================================================

else:

    st.info(
        "Please select both a design and a query image "
        "to start the image replacement process."
    )