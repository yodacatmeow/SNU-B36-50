# SNU-B36-50
- This dataset was gathered for evaluation of models for source location and source type classification of noise between floors (NBF) in a building
- The dataset was generated and acquired in Building 36 at Seoul National University (SNU)
- A single built-in microphone of a smartphone (Samsung Galaxy S6) recorded the NBF with sample frequency of 44,100 *Hz*
- This dataset was used for the following projects
  - [VGG16-SNU-B36-50 (project repository)](https://github.com/yodacatmeow/VGG16-SNU-B36-50) submitted for *IWAENC 2018*




## Category

- SNU-B36-50 includes thirty-nine cateogories of NBF
- The categories can be divided into  five source types
  - MB: a hammer dropped from 1.2 *m* hitting the floor
  - HD: a hammer dropped from 1.2 *m* hitting the floor
  - HH: hitting the floor with a hammer
  - CD: dragging a chair on the floor
  - VC: vacuum cleaner
- They are subset of source types which could annoy residents in an apartment complex reported in the  [reference.](http://www.noiseinfo.or.kr/about/data_view.jsp?boardNo=199&keyfield=whole&keyword=&pg=1)
- MB, HD, HH, CD were generated at the nine different locations (source locations) as indicated in the building section and floor plan


![](https://github.com/yodacatmeow/SNU-B36-50/blob/master/figure/bldg-sec-floorplan.png)

- Since VC is not audible to a person at the receiver position when it is generated on the first and the third floor, it was generated only on the second floor
- The following figure shows log-scaled Mel-spectrogram of all categories of the dataset. The vertical label and horizontal label indicate source type and source location, respectively

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

Hwiyong Choi, Seungjun Lee, Haesang Yang, and Woojae Seong (2018). *Classification of Noise between Floors in a Building Using Pre-trained Deep Convolutional Neural Networks*.  Submitted for *Acoustic Signal Enhancement (IWAENC), 2018 IEEE International Workshop on*. IEEE.



## License

[License](https://github.com/yodacatmeow/SNU-B36-50/blob/master/LICENSE)



