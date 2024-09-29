# RNDJ

## Inspiration
We know that there are many in the community that have input to give, but need a way for their voices to be heard more efficiently and without bias. Our inspiration is to make sure all voices are heard.
## What it does
The main system takes in a dataset of community input. Each individual input could be in any language or dialect. The first step in the system is to create a separate database modeled off of the original input that standardizes it to a single language and style to reduce bias. Sets of 15 of these inputs will then be summarized. Each two of these summaries will then be summarized, and this will repeat until only a single summary of the whole database of community input is left. This would create a traversable tree of summaries to access both more particular input and a general overview.

## How we built it
We built a demo for this in python. We made a sample csv dataset. The generative model used was Google's Gemini 1.5 Flash 002 model, which is both cheap and accurate. 

## Challenges we ran into
One of the challenges we ran into was how we determine how successful the program is in capturing all voices. We found that the best way to do this would be to randomly sample a certain number of community inputs and make sure they are reflected in the summaries. An internal benchmark could be created and further work could be done to ensure all voices are heard.

## Accomplishments that we're proud of
We are proud to have worked together and brainstormed to come up with a product we consider will create a meaningful difference in the community.

## What we learned
We learned that there are many solutions to a given problem and brainstorming a solution is often harder than initially seems. We learned to work together and be constructive and to develop a system to make change.

## What's next for RNDJ
In the future we could refine the project and add on to it. We could add a voting system where generative AI will be used to create a list of topics and each community input will be analyzed and tallied as a vote for a certain topic to better understand where the highest need is.
