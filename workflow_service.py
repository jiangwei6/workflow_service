{
  "10": {
    "inputs": {
      "precision": "quant8"
    },
    "class_type": "DownloadAndLoadChatGLM3",
    "_meta": {
      "title": "(Down)load ChatGLM3 Model"
    }
  },
  "11": {
    "inputs": {
      "prompt": "cinematic photograph of an astronaut riding a horse in space",
      "negative_prompt": "text",
      "num_images_per_prompt": 1,
      "speak_and_recognation": true,
      "chatglm3_model": [
        "10",
        0
      ]
    },
    "class_type": "KolorsTextEncode",
    "_meta": {
      "title": "Kolors Text Encode"
    }
  },
  "12": {
    "inputs": {
      "model": "Kwai-Kolors/Kolors",
      "precision": "fp16"
    },
    "class_type": "DownloadAndLoadKolorsModel",
    "_meta": {
      "title": "(Down)load Kolors Model"
    }
  },
  "13": {
    "inputs": {
      "width": 1088,
      "height": 1024,
      "seed": 152342295013028,
      "steps": 25,
      "cfg": 5,
      "scheduler": "EulerDiscreteScheduler",
      "denoise_strength": 1
    },
    "class_type": "KolorsSampler",
    "_meta": {
      "title": "Kolors Sampler"
    }
  }
}
