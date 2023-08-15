#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install moviepy


# In[2]:


from moviepy.editor import VideoFileClip

# Replace 'input_video.mp4' with the path to your video file
input_video_file = (r'C:\Users\ankit\Desktop\Technical round\ef3e_elem_r&c1&2_short film.mp4')

# Replace 'output_audio.wav' with the desired output audio file name
output_audio_file = 'output_audio.wav'

# Load the video clip
video_clip = VideoFileClip(input_video_file)

# Extract the audio from the video
audio_clip = video_clip.audio

# Save the audio to a file
audio_clip.write_audiofile(output_audio_file)

print(f"Audio extracted and saved to '{output_audio_file}'")


# In[5]:


pip install opencv-python-headless numpy


# In[6]:


pip install pyAudioAnalysis


# In[7]:


pip install hmmlearn


# In[8]:


pip install eyed3


# In[9]:


pip install pydub


# In[10]:


pip install imbalanced-learn


# In[ ]:


from pyAudioAnalysis import audioSegmentation as aS

# Replace 'output_audio.wav' with the path to your audio file
input_audio_file = 'output_audio.wav'

# Specify the expected number of speakers (this is just an example, adjust it accordingly)
n_speakers = 2

# Perform speaker diarization
segmentation = aS.speaker_diarization(input_audio_file, n_speakers)

# Print the structure of the segmentation results
print(segmentation)

# Extract speaker labels from the segmentation
speaker_labels = [segment[2] for segment in segmentation]

# Count the number of distinct speakers
total_speakers = len(set(speaker_labels))

print(f"Total number of speakers estimated: {total_speakers}")


# In[ ]:




