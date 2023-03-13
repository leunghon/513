# MoveSync

MoveSync is an innovative game that promotes physical activity and mindfulness through Yoga movements. The game is designed to be an interactive way to get people moving and practicing yoga in a fun and engaging way. The game uses OpenPose to detect the user's key points and then uses an algorithm to score their performance. The game has a user-friendly interface and provides visualizations of the user's movements to help them improve their performance.

## Prerequisites

Before running MoveSync, you need to install the OpenPose package. You can find installation instructions for OpenPose on their GitHub page.

## Code Files

- `ui.py`: This file contains the code for the user interface of the game. It links all the other files together and is the main file to run the program.

- `main.py`: This file contains the code for key point detection using OpenPose. It takes a video file as input and outputs the key points for each frame.

- `plot.py`: This file contains the code for visualizing the user's movement patterns. It takes the key points from the `main.py` file as input and outputs a visualization of the user's movement pattern.

- `scoring.py`: This file contains the code for the scoring system. It uses an algorithm to score the user's performance based on the accuracy of their movements.

## Usage

To run the program, simply run the `ui.py` file. This will start the user interface and allow you to start playing the game. The game will guide you through the movements and provide feedback on your performance. You can use the visualizations provided by the `plot.py` file to improve your performance and get a higher score.

## Conclusion

Overall, MoveSync is a fun and engaging way to practice yoga and promote physical activity and mindfulness. It provides a user-friendly interface and visualizations to help you improve your performance and get the most out of your yoga practice.
