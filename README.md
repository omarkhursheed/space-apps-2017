# LandWatch

Being informed is being safe. Predictions based on weather and historical data sourced from the finest agencies in the world, combined with real-time information sourced from you, our users, lets us help keep you in the know about landslide-prone areas, and connect you to the services you need.

We aim to provide a tool that uses an algorithm to predict landslides and a platform for individuals to discuss and contribute to the management and prediction of such disasters.

The algorithm works as follows:

* Comb through datasets on rainfall and other factors that cause landslides.
* Use data about landslides that have previously occured in order to gauge threshold values for these factors.
* Get real-time (or near real-time data) to check against threshold values, and calculate chances of landslides happening based on the probability of these factors and display to the user whether they are in a high-risk, medium-risk, or low-risk area.

The platform also provides capabilities to work with first responders, for users to trigger emergency alerts, and a forum for members of the scientific community and the general public to interact with each other as well as help improve the tool.

The following branches are present in the repository:
* **LANDWATCH_PWA**: Contains the progressive web app for the project.
* **UI_DEV**: Contains the UI elements for the web app.
* **algo**: Contains the predictive algorithm for anticipating landslides.
