# AudioCaptchaDecoder

## Workflow

1. Generate audio captchas using audio_captcha_generator.py (uses gTTS (Google Text-to-Speech))
2. Convert .mp3 audio captcha files to .wav format using mp3towav.py
3. Generate spectrograms of the corresponding .wav files using spectrogram_generator
4. Train the model on generated spectrograms using train.py
5. Follow steps 1-3 on test data and classify it using classify.py

This project can also be used to classify text captchas. 
