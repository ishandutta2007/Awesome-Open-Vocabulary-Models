import os
import re

readme_path = "README.md"
pages_dir = "pages"
os.makedirs(pages_dir, exist_ok=True)

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

pages_data = [
    ("Closed-Vocabulary Era", "closed_vocabulary_era.md", "Details about the Closed-Vocabulary Era.", "graph TD\nA[Image] --> B[CNN]\nB --> C[Fixed Classes]"),
    ("Traditional Zero-Shot Era", "traditional_zero_shot_era.md", "Details about the Traditional Zero-Shot Era.", "graph TD\nA[Image] --> B[Visual Features]\nB --> C[Attribute Space]\nC --> D[Novel Classes]"),
    ("Modern Open-Vocabulary Era", "modern_open_vocabulary_era.md", "Details about the Modern Open-Vocabulary Era.", "graph TD\nA[Image] --> B[Image Encoder]\nC[Text] --> D[Text Encoder]\nB --> E[Similarity]\nD --> E"),
    ("Visual-Semantic Space Mapping (Dual-Tower Matching)", "visual_semantic_space_mapping.md", "Details about Visual-Semantic Space Mapping.", "graph TD\nA[Image] --> B[Vision Model]\nC[Text] --> D[Language Model]\nB --> E[Joint Space]\nD --> E"),
    ("Knowledge Distillation (Teacher-Student Training)", "knowledge_distillation.md", "Details about Knowledge Distillation.", "graph TD\nA[Teacher VLM] --> B[Distillation]\nB --> C[Student Detector]"),
    ("Pseudo-Labeling & Generation", "pseudo_labeling_generation.md", "Details about Pseudo-Labeling & Generation.", "graph TD\nA[Unlabeled Image] --> B[Generator/Captioner]\nB --> C[Pseudo Labels]\nC --> D[Training]"),
    ("Open-Vocabulary Detection (OVD)", "open_vocabulary_detection.md", "Details about Open-Vocabulary Detection.", "graph TD\nA[Image + Text] --> B[OVD Model]\nB --> C[Bounding Boxes]"),
    ("Open-Vocabulary Segmentation (OVS)", "open_vocabulary_segmentation.md", "Details about Open-Vocabulary Segmentation.", "graph TD\nA[Image + Text] --> B[OVS Model]\nB --> C[Segmentation Masks]"),
    ("Open-Vocabulary 3D Scene Understanding", "open_vocabulary_3d.md", "Details about Open-Vocabulary 3D Scene Understanding.", "graph TD\nA[3D Point Cloud + Text] --> B[3D OVM Model]\nB --> C[3D Segmentation]"),
    ("Zero-Shot Defect Detection in Manufacturing", "zero_shot_defect_detection.md", "Details about Zero-Shot Defect Detection.", "graph TD\nA[Product Image + Defect Text] --> B[OVM]\nB --> C[Defect Localization]"),
    ("Autonomous Robotic Manipulation & Navigation", "autonomous_robotic_manipulation.md", "Details about Autonomous Robotic Manipulation.", "graph TD\nA[Camera + Instruction] --> B[OVM]\nB --> C[Robot Action]"),
    ("E-Commerce Search-to-Image Mapping", "ecommerce_search.md", "Details about E-Commerce Search.", "graph TD\nA[Search Query + Product Catalog] --> B[OVM]\nB --> C[Ranked Products]"),
]

for title, filename, desc, diagram in pages_data:
    filepath = os.path.join(pages_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{desc}\n\n## Diagram\n\n```mermaid\n{diagram}\n```\n\n[Back to README](../README.md)\n")

# Update README to link to these pages.
# Replace occurrences of the titles in the tables with links to the pages.
for title, filename, _, _ in pages_data:
    # Use regex to find the title in the table column and replace it with a markdown link.
    # The title in the table has ** around it or may not. Let's just find the exact text and replace if not already linked.
    pattern = re.compile(rf"(\*\*?){re.escape(title)}(\*\*?)")
    content = pattern.sub(rf"\1[{title}](pages/{filename})\2", content)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
