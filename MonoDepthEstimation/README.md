
# :sparkles: 실행 방법
```
!git clone https://github.com/ialhashim/DenseDepth.git
```

## :dizzy: 사진 촬영 및 저장
```
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.png', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename
  ```
  위의 코드를 실행하여 노트북에 장착된 카메라로 사진 촬영을 합니다   
     
  ```
  from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))
  ```
  해당 코드를 실행하여 촬영한 사진을 확인 및 저장합니다   
  촬영한 사진 또는 원하는 사진을 examples 파일에 넣어줍니다   
  파일 형식은 640X480 사이즈의 png 파일만 가능합니다   
     
  
  ## :dizzy: 학습된 모델 불러오기
  ```
  !wget https://s3-eu-west-1.amazonaws.com/densedepth/nyu.h5 -O ./DenseDepth/nyu.h5
  ```
  nyu로 학습된 모델을 불러옵니다   
     
  ## :dizzy: 깊이 추정 적용
  ```
  !cd DenseDepth; python test.py
  ```
     
  ## :dizzy: 적용한 결과 확인
  ```
  from matplotlib import pyplot as plt
from skimage import io

plt.figure(figsize=(20,20))
plt.imshow( io.imread('./DenseDepth/test.png') )
  ```
  깊이 추정을 적용한 사진은 './DenseDepth/test.png'로 저장됩니다   
  해당 사진 파일을 불러와서 결과를 확인할 수 있습니다   
       
  ![image](https://user-images.githubusercontent.com/112617546/206852786-527e9af6-2b66-4782-9a86-1e282465e840.png)
