# DigitalHuman
Meta human powered by a large language model

<b><u>Baseline Architecture</u></b>
<img align="center" src="https://github.com/deepakpillai/DigitalHuman/blob/main/DifitalHuman.jpg" />

<b><u>Demo</u></b>
[Project Demo](https://github.com/deepakpillai/DigitalHuman/blob/main/video.mp4)
<video width="640" height="360" controls>
  <source src="https://github.com/deepakpillai/DigitalHuman/blob/main/video.mp4" type="video/mp4">
  <img align="center" src="https://github.com/deepakpillai/DigitalHuman/blob/main/screenshot.png" />
  
</video>

<b><u>How it works!</u></b><br/>
1. The Python code uses speech_recognition lib to convert audio to text and the text is passed to LLM for inferencing. <br/>
2. Once we get the response from LLM, we pass it to NVIDIA OMNIVERSE AUDIO2FACE to calculate the face expressions through REST API <br/>
3. Once the facial expression is calculated, we pass the values to unreal via UDP protocol. <br/>
4. The Unreal Metahuman blueprint is listening to a specific port, as as soon as it gets the data, we animate the Metahuman avatar <br/>
