# :sparkles: HackYourCity 2015 - Dortmund :sparkles:
## :house: RevealYourCity :house_with_garden:
This is our project for HackYourCity. The application contains a backend service, a file served by a webserver and a mapping application integrated in the backend service.

## :information_desk_person: Introduction
### Frontend
At the moment the user is able to choose a color by flinging the smartphone. We are using the fling function provided by sense.js to choose a predifened colour. After accepting the color, the user will be able to reveal a cities map layer by doing funny moves with their device.

### Backend
The backend coordinates the many device accelerometer data send by smartphones of different users and keeping state of the id and data in Redis.
The backend processes the data and sends it on to the presentation layer, which will probably a WebGL app showing an OpenStreetMap layer of the users location.

# License
Probably MIT
