<!-- doc: https://stackoverflow.blog/2020/04/06/a-practical-guide-to-writing-technical-specs/ -->

# Technical Specification

- 2022 Project Artificial Intelligence Group D
- Written by: Paul, Remy
- Team:
    - [Karine Vinette](https://github.com/KarineVinette)
    - [Malo Archimbaud](https://github.com/Malo-Archimbaud)
    - [Paul Maris](https://github.com/PaulMarisOUMary) 
    - [Pierre Gorin](https://github.com/Pierre2103)
    - [Remy Charles](https://github.com/RemyCHARLES)
    - [Romain Nicolaon](https://github.com/RomainNicolaon)
- Created on: 2020-04-01
- Last updated on: 2020-04-01

## 1. Introduction

### a. Overview

In the school, during project time when the students work in autonomy, they are expected to speak english, but they are often speaking french.</br>We are building an intelligent device that can recognize if the people are speaking french or english.</br>
It will turn on a red Led when people are speaking french.

Summary of the problem (from the perspective of the user), the context, suggested solution, and the stakeholders. 

### b. Glossary

| Terms | Definitions |
| ----- | ----------- |
| AI    | Artificial Intelligence : the theory and development of computer systems able to perform tasks normally requiring human intelligence, such as visual perception, speech recognition, decision-making, and translation between languages |
| DL | Deep Learning : It was created by drawing inspiration from the neural networks found in the human brain, which means that deep learning is made up of a large number of layers of interconnected artificial neurons, hence the name "deep learning". |

### c. Context
<!-- ! TODO -->

Reasons why the problem is worth solving
Origin of the problem
How the problem affects users and company goals
Past efforts made to solve the solution and why they were not effective
How the product relates to team goals, OKRs
How the solution fits into the overall product roadmap and strategy
How the solution fits into the technical strategy

### d. Goals
<!-- ! TODO -->

Product requirements in the form of user stories 
Technical requirements

### e. Out of Scope
The device will not speak.
The device will not translate french to english.

Product and technical requirements that will be disregarded

### f. Assumptions
<!-- ! TODO -->

Conditions and resources that need to be present and accessible for the solution to work as described. 

## 2. Solutions

### a. Current or Existing Solution / Design
<!-- ! TODO -->

Current solution description
Pros and cons of the current solution

### b. Suggested or Proposed Solution / Design 
<!-- ! TODO -->

External components that the solution will interact with and that it will alter
Dependencies of the current solution
Pros and cons of the proposed  solution 
Data Model / Schema Changes
Schema definitions
New data models
Modified data models
Data validation methods
Business Logic
API changes
Pseudocode
Flowcharts
Error states
Failure scenarios
Conditions that lead to errors and failures
Limitations
Presentation Layer
User requirements
UX changes
UI changes
Wireframes with descriptions
Links to UI/UX designer’s work
Mobile concerns
Web concerns
UI states
Error handling
Other questions to answer
How will the solution scale?
What are the limitations of the solution?
How will it recover in the event of a failure?
How will it cope with future requirements?

### c. Technical Requirements

- Python
    - Version `3.9.X`
    - Why ?
    Python is an interpreted and dynamic programming language which is ideal to work AI.
- Tensorflow
    - Version `2.8.X`
    - Why ?
    Tensorflow is a library for machine learning.
- NumPy
    - Version `1.22.X`
    - Why ?
    NumPy is a library written in `C` with the purpose of better efficiency, rather than using python default list-type we'll use `numpy.array`.
- Matplotlib
    - Version `3.5.X`
    - Why ?
    Matplotlib is a library for plotting graphs, we'll use this library especialy for rendering spectrograms of the sound.


### d. Test Plan
<!-- ! TODO -->

Explanations of how the tests will make sure user requirements are met
Unit tests
Integrations tests
QA

### e. Release / Roll-out and Deployment Plan
<!-- ! TODO -->

Deployment architecture 
Deployment environments
Phased roll-out plan e.g. using feature flags
Plan outlining how to communicate changes to the users, for example, with release notes

### f. Alternate Solutions / Designs
<!-- ! TODO -->

Short summary statement for each alternative solution
Pros and cons for each alternative
Reasons why each solution couldn’t work 
Ways in which alternatives were inferior to the proposed solution
Migration plan to next best alternative in case the proposed solution falls through

-> Speetch to text

## 3. Further Considerations

### a. Cost analysis
<!-- ! TODO -->

What is the cost to run the solution per day?
What does it cost to roll it out? 

### b. Security considerations
<!-- ! TODO -->

What are the potential threats?
How will they be mitigated?
How will the solution affect the security of other components, services, and systems?

### c. Privacy considerations
<!-- ! TODO -->

Does the solution follow local laws and legal policies on data privacy?
How does the solution protect users’ data privacy?
What are some of the tradeoffs between personalization and privacy in the solution? 

### d. Accessibility considerations
<!-- ! TODO -->

How accessible is the solution?
What tools will you use to evaluate its accessibility? 

### e. Risks
The model can't recognize the language speaking because of the accent, the noise or multiple speakers.

What risks are being undertaken with this solution?
Are there risks that once taken can’t be walked back?
What is the cost-benefit analysis of taking these risks? 

## 4. Success Evaluation

### a. Impact
<!-- ! TODO -->

-> Security impact
-> Performance impact
Cost impact
Impact on other components and services

### b. Metrics
<!-- ! TODO -->

List of metrics to capture
Tools to capture and measure metrics
Tests to verify metrics

## 5. Work

### a. Work estimates and timelines
<!-- ! TODO -->

List of specific, measurable, and time-bound tasks
Resources needed to finish each task
Time estimates for how long each task needs to be completed

-> Link to the github project

### b. Prioritization
Build a dataset of english and french speaking. </br>

Categorization of tasks by urgency and impact

### c. Milestones
Make a dataset </br>
Train the machine learning model </br>
Deploy it to the Microcontroller </br>
Control it with a webpage.</br>

Dated checkpoints when significant chunks of work will have been completed
Metrics to indicate the passing of the milestone
d. Future work
Build an English speaker accent recognition </br>

List of tasks that will be completed in the future
