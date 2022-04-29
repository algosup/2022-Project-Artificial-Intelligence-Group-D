# Functional Specification

### Stakeolders

| Person/Organization | Role            |
| ------------------- | --------------- |
| ALGOSUP             | Customers       |
| Jackie   BOSCHER    | Tech consultant |
| Karine   VINETTE    | Team member     |
| Malo     ARCHIMBAUD | Team member     |
| Paul     MARIS      | Team member     |
| Pierre   GORIN      | Team member     |
| Remy     CHARLES    | Team member     |
| Romain    NICOLAON  | Team member     |

### Overview

Our goal for this project is to create a device which will be able to listen to conversations and
detect the language which is spoken between French and English. 
If this is not the right
language which is spoken, then the device will emit a sound or display a color to tell people
who are speaking to switch language. This will be used to check if people are speaking

English during class or project time. In this scenario, the device would emit a signal when a
person switches from English to French to ensure that everyone is speaking English in order
to practice.

### Project Target

Using an AI, this AI should be able to detect which language is spoken in a room, emit a sound when the
wrong language is spoken and display a light depending on the language you use when you
speak.

- Deliverable deadline: June 27th 2022

### Risks and Assumptions

One of the major risks is about recognition and there are several cases we’re afraid of;
- Irregular accent
- Noise interference
- Two people speaking at the same time

Since data is a major corner-stone, the problem may cause either a lot of delay in the final delivery or reduce the quality of the product.
We will have to be careful to keep control of our AI and make sure it is going in the right direction in order to avoid going in circles and getting stuck. 

The compute power needed to keep the IA alive is also something we should be worried about.

The Covid or disease may have an impact on the capacity of the team project and causing, absences and delays on the project. 

### Project and Scopes:

• IA needs datas to be trained.
And there are several ways to collect these datas (we can use several of them), such as 
datas collected during project time/class
open datas from the web

•As mentioned in the project target, a device should be able to listen to conversations.
We’re gonna need a hardware device with at least a microphone.

•Ensure privacy is respected is a major scope of the project too. The team should proove that the device is not recording conversations.

•Balancing between computer power and quality/quantity of data that can be processed will  be a thing to take in consideration all along the project.


### Requirement Specifications

##### Device Overview

As written in the project target, the IA should be able to run on a device, so at a specific stage of the project some investment will be needed, for a microphone and probably a device like a raspberry pi, or pi zero, the cost and which device we'll need will depend of our evaluation during the project.

The device will have a microphone to capture the sound in a room. It will also have a son
emitter or a display to indicate if the right language is spoken.

### Development Environement and Requirements

- Python3
    - Tensorflow
- MacOSx/Windows on development
- Unix/Linux on production environment

### Glosary
AI: Artificial Intelligence.

Deep Learning: It was created by drawing inspiration from the neural networks found in the human brain, which means that deep learning is made up of a large number of layers of interconnected artificial neurons, hence the name "deep learning". 