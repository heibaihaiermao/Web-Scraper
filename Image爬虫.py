import requests
for i in range(1,83):
    imgURL = 'https://image.slidesharecdn.com/tacticalcomms-220127150015/75/tactical-comms-' + str(
        i) + '-2048.jpg?cb=1668057261'
    filename = "D:/Users/ycmiao/NAVY/2023-2024 RTR/Fleet Maneuver/Tactical Comm" + str(i) + ".jpg"
    img_data = requests.get(imgURL).content
    with open(filename, 'wb') as handler:
        handler.write(img_data)
