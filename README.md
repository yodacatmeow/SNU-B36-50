# SNU-B36-50
- This dataset was gathered for evaluation of models for source location and source type classification of noise between floors (NBF)
- The dataset was generated and acquired in Building 36 at Seoul National University (SNU)
- A single built-in microphone of smartphone (Samsung Galaxy S6) records the NBF with sample frequency of 44,100 Hz




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

- "audio": This folder includes audio clips. Each folder contains fifty audio clips

```
audio
   |-- 000
   |-- 001
     ...
   |-- 038
```

- "metadata": This folder includes meta-data (.csv format)




## Quick start

- Clone this project:  ```git clone https://github.com/yodacatmeow/SNU-B36-50.git ``` 





## Citing

Hwiyong Choi, Seungjun Lee, Haesang Yang, and Woojae Seong. (2018, September). Classification of Noise between Floors in a Building Using Pre-trained Deep Convolutional Neural Networks. In *Acoustic Signal Enhancement (IWAENC), 2016 IEEE International Workshop on* (pp. 1-5). IEEE.



## License

[License](https://github.com/yodacatmeow/SNU-B36-50/blob/master/LICENSE)
