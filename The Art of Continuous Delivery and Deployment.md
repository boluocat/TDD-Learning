Continuous Deployment and Delivery are two terms that are sometimes confused with each other. Both terms have a relationship with each other in the evolution of a software development project. 

### Difference of continuous delivery and continuous deployment

- Continuous Delivery is having software in the state in which it can be manually deployed. 
- Continuous Deployment is the process of automatically deploying software into a production environment.

- With continuous delivery the software does't have to be put into production, but it must be in a state in which it could which means no hugs, proper configuration, automated tests passing, etc.
- With continuous deployment after each build is successfully executed the software is automatically deployed.

Some software practitioners say that you can’t have continuous deployment without continuous delivery. 

- With continuous delivery there’s human intervention because after the software has made its way through several stages it’s a business decision to manually deploy the software or not. 
- With continuous deployment there’s no human intervention as the entire process is automated. 

### Benefits of continuous delivery and deployment

- Shorter release cycles
- Integrate new software feature quicker
- Less chances of integration hell
- Discover when code breaks quickly
- Make customers happy by continuous providing valuable software

Continuous Integration is the first step in the process which means that you can't have continuous delivery or deployment without continuous integration. **With CI the goal is that when a new commit is added to the main repository, the CI serve is triggered, automated tests are run, and contingent on the tests passing the build is produced**.

Now, does software automatically get shipped after the build is produced? Absolutely not, as there are a plethora of things that could go wrong once the software is released into the wild. One thing that many software companies have is a QA environment so that once the build is created it’s tested many different ways.

This is important because it’s common for something to work on our machine yet when it’s shipped to a customer mysterious bugs manifest which are difficult and stressful to fix. However, by conducting many different types of tests on the build then this will help minimize those issues from happening giving the software team greater confidence on the quality of their software. 

### Deployment pipeline

It takes discipline to implement continuous delivery and deployment into your pipeline but it’s worth it. Different companies have different ways of managing their deployment pipeline but here’s a general scenario of how it works:

Developers commit code -> 
CI server runs automated tests -> 
If process is successful a build is created -> 
Build is shipped to QA environment for additional testing -> 
Build can be released manually (continuous delivery), or automatically released via continuous deployment

Automation plays a key component in this process for speeding things up. The tests are automated along with the build. This allows teams to efficiently work together towards a common goal. 

Travis CI supports deployment with a variety of providers such as AWS Lambda, Azure, Heroku, and GitHub Pages: https://docs.travis-ci.com/user/deployment

To get more familiar with the continuous delivery and deployment process, work through the accompanying lab for this module. 