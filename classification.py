from keras.models import load_model
import rasterio
import numpy as np



def predicted_image(filename):
  src = rasterio.open('botPWP/Images_test/' + filename)
  list_class = ['asia_argento',
 'arcueid_brunestud',
 'aisaka_taiga',
 'abigail_williams_(fate)',
 'aqua_(konosuba)',
 'anastasia_(idolmaster)',
 'aegis_(persona)',
 'albedo']

  model = load_model('botPWP/trained_anime_classifier.h5')
  
  # Pré-processamento da imagem
  im = src.read()
  im = im.transpose([1, 2, 0])
  im1 = im[:, :, 0:3]  
  
  test_image_processed = np.dstack((im1, im1, im1)) 
  test_image_processed = test_image_processed/10000.0 
  
  result = model.predict(test_image_processed[np.newaxis, ...])
  predicted_class = np.argmax(result, axis=-1)
  return f"Pela minha experiência que não é tão boa mas também não tão ruim, esse(a) personagem é o(a): ", list_class[predicted_class[0]]