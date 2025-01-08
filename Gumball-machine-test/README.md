# Instructions

Epic Gum Balls is a company that creates an assortment of gum balls using exotic fusions like lemongrass and paprika. They have their gum ball machines in various supermarkets and malls across the world. However, they want to integrate their physical machines with software, and did a quick Google search and decided to use python due to all of the good things they heard about it. They also heard about TDD and how it’s a good strategy for building software. They ship you the following requirements and ask you to design tests for them first before developing the business logic. 

# Here's a list of the requirements
- Include functionality to give the remaining amount of gumballs in machine. The machine can fit a maximum of 1000 gumballs in them
- The software needs to be able to keep track of how many gumballs were dispensed during each transaction. A gumball can be dispensed the proper amount of .75 and 3 gumballs will be given (each gumball worth 0.75, and each transaction give 3 gumballs)
- If there are less than 100 gumballs, then the machine needs to return a message of low that indicates that it needs to be replaced