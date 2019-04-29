import webbrowser
import replit

print("French Impressionism")
print()
print("1. Auguste Renoir")
print("2. Claude Monet")
print("3. Vincent Van Gogh")
print("4. Georges Seurat")
print("5. Paul Cezanne")
print("6. Exit")
print()
  
iArtistInput = input("Make A Selection: ")
  
if iArtistInput == '1':
  replit.clear()
  print("Renoir")
  print("----")
  print("a. Luncheon of the Boating Party")
  print("b. The Great Boulevards")
  print("c. Picking Flowers")
  print("d. Exit")
  iPaintInput = input("Select a Painting: ")
   
  if iPaintInput == 'a':
    webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/8/8d/Pierre-Auguste_Renoir_-_Luncheon_of_the_Boating_Party_-_Google_Art_Project.jpg')
  elif iPaintInput == 'b':
    webbrowser.open('https://uploads0.wikiart.org/images/pierre-auguste-renoir/the-great-boulevards-1875.jpg!Large.jpg')
  elif iPaintInput == 'c':
    webbrowser.open('https://www.pierre-auguste-renoir.org/thumbnail/79000/79190/mini_normal/Picking-Flowers-Aka-In-The-Field.jpg?ts=1459229076')
  elif iPaintInput == 'd':
    replit.clear()
  else:
    print("Error")
  
elif iArtistInput == '2':
  replit.clear()
  print("Monet")
  print("----")
  print("a. The Artist's Garden at Giverny")
  print("b. San Giorgio Maggiore at Dusk")
  print("c. Cliff Walk at Pourville")
  print("d. Exit")
  iPaintInput = input("Select a Painting: ")
  
  if iPaintInput == 'a':
    webbrowser.open('https://www.libertypuzzles.com/userfiles/media/images/5501/artist-garden-giverny-image-1700.jpg')
  elif iPaintInput == 'b':
    webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/d/da/Claude_Monet%2C_Saint-Georges_majeur_au_cr%C3%A9puscule.jpg')
  elif iPaintInput == 'c':
    webbrowser.open('https://www.artic.edu/iiif/2/8025c072-f5bc-4384-4e0e-ed5d768eb704/full/1200,/0/default.jpg?w=1200&h=800&fit=crop')
  elif iPaintInput == 'd':
    replit.clear()
  else:
    print("Error")
  
elif iArtistInput == '3':
  replit.clear()
  print("Van Gogh")
  print("----")
  print("a. The Church at Auvers")
  print("b. The Langlois Bridge at Arles")
  print("c. Irises")
  print("d. Exit")
  iPaintInput = input("Select a Painting: ")
    
  if iPaintInput == 'a':
    webbrowser.open('http://everypainterpaintshimself.com/article_images_new/VanGChurchAuversx1.jpg')
  elif iPaintInput == 'b':
    webbrowser.open('https://www.vincentvangogh.org/images/paintings/langlois-bridge-at-arles.jpg')
  elif iPaintInput == 'c':
    webbrowser.open('https://www.vincentvangogh.org/images/paintings/irises.jpg')
  elif iPaintInput == 'd':
    replit.clear()
  else:
    print("Error")
  
elif iArtistInput == '4':
  replit.clear()
  print("Seurat")
  print("----")
  print("a. Sunday Afternoon on the Island of la Grande Jatte")
  print("b. Rue Saint Vincent Montmarte in Spring")
  print("c. La Seine a la Grande Jatte ")
  print("d. Exit")
  iPaintInput = input("Select a Painting: ")
    
  if iPaintInput == 'a':
    webbrowser.open('https://images-na.ssl-images-amazon.com/images/I/81sDkEPsNXL._SX425_.jpg')
  elif iPaintInput == 'b':
    webbrowser.open('https://www.fitzmuseum.cam.ac.uk/sites/default/files/Seurat---PD.1-1948_LRG_0.jpg')
  elif iPaintInput == 'c':
    webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/9/96/Georges_Seurat_026.jpg')
  elif iPaintInput == 'd':
    replit.clear()
  else:
    print("Error")
      
elif iArtistInput == '5':
  replit.clear()
  print("Cezanne")
  print("----")
  print("a. The Card Players")
  print("b. Chrysanthemums")
  print("c. Landscape with Mill")
  print("d. Exit")
  
  iPaintInput = input("Select a Painting: ")
  
  if iPaintInput == 'a':
    webbrowser.open('https://media.vanityfair.com/photos/54ca91e2b624d6910574e3a4/master/w_768,c_limit/image.jpg')
  elif iPaintInput == 'b':
    webbrowser.open('https://images-na.ssl-images-amazon.com/images/I/61q3wENk0yL._SX425_.jpg')
  elif iPaintInput == 'c':
    webbrowser.open('https://uploads8.wikiart.org/images/paul-cezanne/landscape-with-mill-1860.jpg!Large.jpg')
  elif iPaintInput == 'd':
    replit.clear()
  else:
    print("Error")
      
else:
  print("Error")
