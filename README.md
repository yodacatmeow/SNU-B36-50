# SNU-B36-50
- This dataset was gathered for evaluation of models for noise type / position classification of floor impact noise in a building
- The dataset was generated and gathered in Building 36 at Seoul National University (SNU)
- Floor impact noises are recorded with a single built-in microphone of a smartphone (Samsung Galaxy S6) with sampling frequency of 44,100 *Hz*
- There are 50 audio clips per category
- This dataset was used for the following projects
  - [VGG16-SNU-B36-50 (project repository)](https://github.com/yodacatmeow/VGG16-SNU-B36-50) submitted for *IWAENC 2018*



## Category

- SNU-B36-50 includes 39 categories of floor impact noises
- The categories can be divided into five noise types
  - MB: a hammer dropped from 1.2 *m* of height hitting the floor
  - HD: a hammer dropped from 1.2 *m* of height hitting the floor
  - HH: hitting the floor with a hammer
  - CD: dragging a chair on the floor
  - VC: vacuum cleaner
- They are subset of noise types which can annoy a resident in an apartment complex (reported in the  [reference](http://www.noiseinfo.or.kr/about/data_view.jsp?boardNo=199&keyfield=whole&keyword=&pg=1))
- MB, HD, HH, CD were generated at the 9 different positions (source position) as indicated in the building section and floor plan


![](https://github.com/yodacatmeow/SNU-B36-50/blob/master/figure/bldg-sec-floorplan.png)

- Since VC is not audible to a person at the receiver position when it is generated on the first and the third floor, it was generated only on the second floor
- The following figure shows log-scaled Mel-spectrogram of all categories of the dataset. The vertical label and horizontal label indicate noise type and position, respectively

![](https://github.com/yodacatmeow/SNU-B36-50/blob/master/figure/log-scaled-mel-spec.png)



## Contents

- "audio": This folder includes audio clips. Each folder contains fifty audio clips ([see folder-category mapping](https://github.com/yodacatmeow/SNU-B36-50/blob/master/folder-category-mapping.txt))

```
audio
   |-- 000
   |-- 001
     ...
   |-- 038 
```

- "metadata": This folder includes meta-data (.csv format) including *event_start* (ES, described in the reference)
- "plot_melspec.py": You can draw a log-scaled Mel-spectrogram using this code
  - Set ```path = "audio/FOLDER_NAME"```, where FOLDER_NAME indicates name of the folder in "audio"




## Quick start

- Clone this project:  ```git clone https://github.com/yodacatmeow/SNU-B36-50.git ```  and use it for your project
- (**Optional*) Requirements (for drawing log scaled Mel-spectrogram)
  - Numpy, librosa, and Matplotlib



## Citing

```
@inproceedings{choi2018floornoise,
  title={Classification of noise between floors in a building using pre-trained deep convolutional neural networks},
  author={Choi, Hwiyong and Lee, Seungjun and Yang, Haesang and Seong, Woojae},
  booktitle={2018 16th International Workshop on Acoustic Signal Enhancement (IWAENC)},
  pages={535--539},
  year={2018},
  organization={IEEE}
}
```


## License

[License](https://github.com/yodacatmeow/SNU-B36-50/blob/master/LICENSE)
