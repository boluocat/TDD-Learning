# Bad Practices with Unit Tests

- include another unit test
- test for multiple features
- not test for an actual feature within the code
- require external dependencies


# What makes a good unit test

- adds value to the codebase
- is concise, easy to understand, and complements documentation
- Isolated, tests in isolation (or one feature at a time)
- Fast, it isn't uncommon for mature projects to have thousands of unit tests. Unit tests should take little time to run.
- Self-checking, the test should be able to automatically detect if it passed or failed without any human interaction.
- Timely, a unit test shouldn't take a disproportionately long time to write compared to the code being tested. 


# Examples of best Practices
- One of several unit test scripts from the horovod open source project:  https://github.com/horovod/horovod/tree/master/test/integration
- The Diagram open source project unit tests: https://github.com/mingrammer/diagrams/blob/master/tests/test_diagram.py
- Unit tests scripts for jina-ai: https://github.com/jina-ai/jina/tree/master/tests/unit. There's also integration tests here if curious https://github.com/jina-ai/jina/tree/master/tests/integration
 