# Manual vs. Automated testing

- Manual testing is done in person, by clicking through the application or interacting with the software and APIs wit the appropriate tooling.
- Automated testing is performed by a machine that executes a test script that was written in advance.

There are some automated testing tools introduction: [DevOps Software Testing Tutorials | Atlassian](https://www.atlassian.com/devops/testing-tutorials)



# The different types of tests

1. Unit tests

   Unit tests are very low level and close to the source of an application. They consist in testing **individual methods and functions of the classes, components, or modules** used by your software. It can run very quickly by a continuous integration server.

2. Integration tests

   Integration tests verify that **different modules or services** used by your application **work well together**.

3. Functional tests

   Functional tests **focus on the business requirements of an application**. They **only verify the output of an action** and do not check the intermediates states of the system when performing that action.

   The difference between integration tests and functional tests:

   - An integration test may simply verify that you can query the database.
   - A functional test would expect to get a specific value from the database as defined by the product requirements.

4. End -to-end tests

   End-to-end testing **replicates a user behavior with the software in a complete application environment**. **It verifies that various user flows work as expected** and can be as simple as loading a web page or logging in or much more complex scenarios verifying email notifications, online payments, etc...

   End-to-end tests are very useful, but they're expensive to perform and can be hard to maintain when they're automated. It is recommended to have a few key end-to-end tests rely more on lower level types of testing (unit and integration tests) to be able to quickly identify breaking changes.

5. Acceptance testing

   Acceptance tests are formal tests that **verify if a system satisfies business requirements.** They require then entire application to be running while testing and **focus on replicating user behaviors**. But they can also go further and **measure the performance of the system** and reject changes if certain goals are not met.

6. Performance testing

   Performance tests evaluate how a **system performs under a particular workload**. These tests help to measure the **reliability, speed, scalability, and responsiveness of an application**. For instance, a performance test can observe response times when executing a high number of requests, or determine how a system behaves with a significant amount of data. It can determine if an application meets performance requirements, locate bottlenecks, measure stability during peak traffic, and more.

7. Smoke testing

   Smoke tests are basic tests that check the basic functionality of an application. They are meant to quick to execute, and their goal is to give you the assurance that the major features of your system are working as expected.

   Smoke tests can be useful right after a new build is made to decide whether or not you can run more expensive tests, or right after a deployment to make sure that they application is running properly in the newly deployed environment.

# How to automate your tests

To automate your tests, you will first need to write them programmatically using a testing framework that suits your application.

When your tests can be executed via script from your terminal, you can have them be automatically executed by a continuous integration server like Bamboo or use a cloud service like Bitbucket Pipelines. These tools will monitor your repositories and execute your test suite whenever new changes are pushed to the main repository.





Additional link: [Types of Software Testing (100 Examples) (guru99.com)](https://www.guru99.com/types-of-software-testing.html)