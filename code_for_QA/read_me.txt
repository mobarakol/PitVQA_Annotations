You should have a folder structure like this:
PitVis-VQA/
    |-- images/
    |   |-- video_1
    |   |-- video_2
    |   |-- ...
    |-- QA/
All the frames are stored in the images folder.

Now do the following steps:
1. run create_txt_files.py to create txt file for each frame
2. run labeling.py to create QA pairs and write them into those txt files
    utils.py contains all the mappings for labeling



