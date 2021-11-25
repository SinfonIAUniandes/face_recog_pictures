import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('images/juanjo.jpeg','Juanjo'),
      ('images/juanjo2.jpeg','Juanjo'),
      ('images/daniel.jpeg','Daniel'),
      ('images/daniel2.jpeg','Daniel'),
      ('images/susana.jpeg','Susana'),
      ('images/susana2.jpeg','Susana'),
      ('images/susana3.jpeg','Susana'),
      ('images/susana4.jpeg','Susana'),
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('imagenes-sinfonia-2021-nov','input/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )