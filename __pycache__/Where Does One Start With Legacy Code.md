When you join a software team there’s a high probability that you have to work with a pre-existing code base.You most likely won’t be building the code from the ground-up which means that you inherited the code. However, not all things you inherit in life are gold!

Let's assume that you get a codebase that contains 100s of directories which in turn contains 100s of files that collectively exceeds 500,000 lines of code. Working in a codebase that’s been passed down to you is known as legacy code. Legacy code is often a mystery box, it holds great powers but it’s understood by few. A characteristic that’s generally associated with legacy code is that it’s old and needs to be maintained.

However, legacy code could be as young as 3 months if the core maintainer of the software leaves the company and didn’t leave behind any documentation or tests. So, the main thing to remember is that legacy code will have complexity to it that needs to be untangled. If done correctly, refactoring legacy code will reduce technical debt which means the price that software companies pay for having software that’s difficult to maintain. By constantly refactoring legacy code you can reduce the technical debt and make it easier and cheaper to add functionality to it in the future. 

# Where to Start

From my experience refactoring legacy code for the sake of doing so without a clear strategy is not a good investment. There needs to be a vision with measurable outcomes. Otherwise, a software team could work weeks refactoring legacy code to only end up with something that's marginally better. Since many software teams will have varying reasons and goals for improving their legacy code I will provide some general tips to consider. The good thing about these tips is that they can be mixed-and-matched to suit your needs.

# Taking A Measured Approach
Writing software is complex and debugging software can be even more so. Making changes can lead to bugs, broken dependencies which are difficult to untangle, and the software no longer working. Therefore, when you make a modification to some existing codebase it's generally **a good idea to start small and then test the results** . It's easier to detect how your change broke the system when you ade one modificationvs when you made 8 of them. As the old idiom goes, slow and steady wins the race.

# Breaking Down Complex Methods
If you have large methods in your codebase then it may be a good idea to extract some of their functionality into separate methods. There's a couple of benefits for doing so.
- One, by including them in smaller methods it makes it easier for you to write unit tests
- Two, by breaking down the large complex method into smaller ones it helps make your code more self-documenting or easier to understand
- Three, by breaking down the large complex method into separate chunks it makes the problem more manageable
- Lastly, breaking the code up into smaller methods tends to make the code easier to read and maintain

# Adding Unit Tests
A great technique to use when working with legacy code is to a**dd unit tests to cover the core functionality**. The reason why I said core is because it's impractical to try and add unit tests for every sigle method in a large codebase. However, by applying unit tests to the critical functionality of the software, this will serve as a safety net when you refator the legacy code because if something breaks then you will be notified wit the failed unit test. T**his is why using a continuous integration server like Travis CI or Jenkins is invaluable when working on legacy code for large software projects** because once you have your unit tests in place the CI server will automatically run them once updates are made to the repository. If a unit test now fails then the team will be notified so that they can quickly correct this issue. If you need to add new functionality to legacy code then the TDD approach is a solid one to use. Remember, the red-green-refactor principle will still apply in this case. Create a unit test that fails(red), andd JUST enough functionality to get it to pass(green), and the refactor.

# Adding Docstrings / Comments / Annotation
If you're working with legacy code that contains sparse documentation then it's a good idea to add documentation to add more clarity to it. When looking over legacy code I typically don't like to trace the code line-by-line on the first ren-through. Instead, I like to get a rough idea of it by quickly skimming the code, and then forming relationships between the functionality by looking at the naming conventions. For example, if I'm looking at some code that has a class of Centroid and a method of sine_distance() then I will assume that this is some type of scientific application. Once you have a better understanding you can start adding your comments. Docstrings are great for classes and methods as they helo explain the bigger picture, comments are great for adding clarity to some otherwise ambiguous code snippet, and annotations are a great way to add additional clarity to your python programs.


# Tools for Refactoring Legacy Code in Python:
If you have a sophisticated IDE then it will come equipped with various tools that will assist you with the refactoring process. Below is an example of some of these tools:

- PyCharm Refactoring Tools: https://blog.jetbrains.com/pycharm/2015/02/feature-spotlight-refactoring-python-code/
- VSCode Refactoring Tools for Python: https://docs.microsoft.com/en-us/visualstudio/python/refactoring-python-code?view=vs-2019
- Atom Tools for Python: https://atom.io/packages/python-tools
- PyRefactor tools for Sublime: https://github.com/dnatag/PyRefactor
- PEP 526 (Syntax for Variable Annotations): https://www.python.org/dev/peps/pep-0526/#rationale