import sklearn.datasets

# load the datasets
faces = sklearn.datasets.fetch_olivetti_faces()

# prove that dataset was loaded
print(faces.data.shape)
