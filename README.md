<h1 align="center">
  <img src="https://github.com/CG1507/style-transfer/blob/master/images/logo.png"/>
</h1>

Artify is Neural Style Transfer playground for creating art, coloring the sketches, and transfering the styles to content image. It is implemented to faster experimentation with different images and settings.

## Requirements
* PyQt5
* Keras
* numpy
* scipy
* h5py
* scikit-image

## Run

Following code-snippet opens window to select content and style images. It gives you flexibility to change the hyperparameter of the learning process.
```
python3 gui.py
```

<h1 align="center">
  <img src="https://github.com/CG1507/style-transfer/blob/master/images/demo.gif" width="900" height="500" />
</h1>

After generation of style transfered images, if you want to preserve the original color of the content image then:
```
python3 color_transform.py <path-to-content-image> <path-to-generated image>
```

## Results

| Content | Style | Art | color preserved |
| :---: | :---: | :---: | :---: |
| <img src="https://github.com/CG1507/style-transfer/blob/master/images/1/content.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/1/style.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/1/art.png" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/1/art_original_color.png" width="250" height="250" /> |
| <img src="https://github.com/CG1507/style-transfer/blob/master/images/2/content.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/2/style.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/2/art.png" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/2/art_original_color.png" width="250" height="250" /> |
| <img src="https://github.com/CG1507/style-transfer/blob/master/images/3/content.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/3/style.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/3/art.png" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/3/art_original_color.png" width="250" height="250" /> |
| <img src="https://github.com/CG1507/style-transfer/blob/master/images/4/content.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/4/style.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/4/art.png" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/4/art_original_color.png" width="250" height="250" /> |
| <img src="https://github.com/CG1507/style-transfer/blob/master/images/5/content.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/5/style.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/5/art.png" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/5/art_original_color.png" width="250" height="250" /> |
| <img src="https://github.com/CG1507/style-transfer/blob/master/images/7/content.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/7/style.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/7/art.png" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/7/art_original_color.png" width="250" height="250" /> |
| <img src="https://github.com/CG1507/style-transfer/blob/master/images/8/content.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/8/style.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/8/art.png" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/8/art_original_color.png" width="250" height="250" /> |
| <img src="https://github.com/CG1507/style-transfer/blob/master/images/9/content.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/9/style.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/9/art.png" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/9/art_original_color.png" width="250" height="250" /> |
| <img src="https://github.com/CG1507/style-transfer/blob/master/images/10/content.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/10/style.jpg" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/10/art.png" width="250" height="250" /> | <img src="https://github.com/CG1507/style-transfer/blob/master/images/10/art_original_color.png" width="250" height="250" /> |

> NOTE: All results will be added soon! Above are initial results.

## Todo

- [ ] Colab support
- [ ] custom model support for finding better settings
- [ ] preserve color in GUI

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author

[<img src="https://avatars3.githubusercontent.com/u/24426731?s=460&v=4" width="70" height="70" alt="Ghanshyam_Chodavadiya">](https://github.com/CG1507)

## Acknowledgement

:green_heart: [ozamanan](https://github.com/ozamanan/Neural-Style-Transfer)
