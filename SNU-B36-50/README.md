# SNU-B36-50
- Inter-floor noises in the dataset were generated and gathered in Building 36 (**B36**) at Seoul National University (**SNU**)
- The noises were recorded with a single built-in microphone of a smartphone (Samsung Galaxy S6)
- Sampling frequency is 44,100 Hz
- Each folders in [audio](https://github.com/yodacatmeow/SNU-B36-50/tree/master/SNU-B36-50/audio) contains **50** noises
- This dataset was used in the following projects
  - [VGG16-SNU-B36-50](https://github.com/yodacatmeow/VGG16-SNU-B36-50) (accepted for *IWAENC 2018*)



## Category

- Each audio clip (inter-floor noise) has two labels: **noise type** and **noise source position**
- Noise type (annoying noise types reported in the  [reference](http://www.noiseinfo.or.kr/about/data_view.jsp?boardNo=199&keyfield=whole&keyword=&pg=1))
  - MB: a medicine ball at height 1.2 m above the floor falls and hits the floor
  - HD: a hammer at height 1.2 m above the floor falls and hits the floor
  - HH: hammering
  - CD: chair dragging
  - VC: vacuum cleaner
- Noise source position: 9 positions in Building 36 as illustrated in the following image


![](https://github.com/yodacatmeow/SNU-B36-50/blob/master/SNU-B36-50/figure/bldg-sec-floorplan.png)

- Since VC is not audible to a person at the receiver position when VC is generated on the first and the third floor, it was generated only on the second floor
- The following figure shows log-scaled Mel-spectrograms of the dataset. The vertical label and horizontal label indicate noise type and noise source position, respectively

![](https://github.com/yodacatmeow/SNU-B36-50/blob/master/SNU-B36-50/figure/log-scaled-mel-spec.png)



## Contents

- [audio](https://github.com/yodacatmeow/SNU-B36-50/tree/master/SNU-B36-50/audio) includes audio clips ([see folder-category mapping](https://github.com/yodacatmeow/SNU-B36-50/blob/master/folder-category-mapping.txt))
- [metadata](https://github.com/yodacatmeow/SNU-B36-50/tree/master/SNU-B36-50/metadata) includes metadata (csv format) including *event_start* 



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


