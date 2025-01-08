Quality documentation is something that many software companies are investing heavily into. With cleaner and more comprehensive  documentation it makes the company's software more accessible to a wide audience. In most large companies quality documentation is a must as without it only those specialized knowledge will be able to make use of it.

Let's get a more real-world perspective on how unit tests can assist documentation. Let's take a peek at the docs for some popular python repositories on GitHub:
- Optuna (A hyper parameter optimization framework): https://github.com/optuna/optuna/blob/master/docs/source/index.rst
- pwndbg (A GDB plugin for debugging):  https://github.com/pwndbg/pwndbg/blob/dev/docs/index.md
- Bottle (A Python Web Framework): https://github.com/bottlepy/bottle/tree/master/docs
 
The docs describe these projects along with giving potential contributors tips on how to get involved, which is critical for the growth of an open source community. However, the docs are great but sometimes it's nice to look at some production code that's understandable because this can help reinforce the information in the documentation. That’s another benefit for unit tests -  not only does it help ensure the quality of code in a software project, but they're a neat way to gain a deeper understanding of the functionality of software. That’s another benefit for unit tests -  not only does it help ensure the quality of code in a software project, but they're a neat way to gain a deeper understanding of the functionality of software. 

For example, let’s assume that you’ve read the documentation for Bottle and you now want to gain a better understanding of the source code. One suggestion is to next look at the unit tests and understand what they're testing. Remember, a unit test is supposed to test a unit of software functionality, so if done according to these principles the gist of them should be straightforward to understand. Here's a more concrete example of how to use unit tests to supplement documentation. 

More specifically you’re interested in building plugins with the web framework so you read the appropriate section of the docs here: 
https://github.com/bottlepy/bottle/blob/master/docs/plugins/dev.rst

Let's say that after reading the documentation everything doesn’t quite click so you want some additional reinforcement. Therefore, one approach is to dig into the unit tests to gain a better understanding. 

For example, there’s specific unit tests to test plugins which we can check out here: 
https://github.com/bottlepy/bottle/blob/master/test/test_plugins.py

We can take a look at one of the unit tests from test_plugins.py here:
```python
def test_install_plugin(self):
    plugin = MyPlugin()
    installed = self.app.install(plugin)
    self.assertEqual(plugin, installed)
    self.assertTrue(plugin in self.app.plugins)
```
This unit test is named test_install so even if you can’t code a single line of python you will have a good understanding that this plugin is designed to test to see if a plugin was installed. Now, let’s step into the logic of this code, the first line is:
```python
plugin = MyPlugin()
```

What's happening here? We can use our knowledge about python to reverse engineer this. We know that this is creating an instance of a class called MyPlugin. We don’t have to know the inner workings of MyPlugin, we just need to be aware that this simply represents an instance of a plugin that the user created. Let's take a look at the the next line: 
```python
installed = self.app.install(plugin)
```

Again, we don’t have to fully understand what self.app.install() does, but due to the clean naming convention we can deduce that this is the method which installs the plugin. The next two code snippets are assert statements from the unittest module: 
```python
self.assertEqual(plugin, installed)
self.assertTrue(plugin in self.app.plugins)
```

These simple assert statements are useful. We know that the value returned from plugin and self.app.install() must be identical or less or this test will fail. We also know that once a plugin is created it must be in self.app.plugins otherwise again, an error will occur. This gives us clues to how the components in the class all work together. The issue with unit tests is that since they’re isolated they don't give you a clear view of how the whole entire system works. However, look at enough unit tests combined with thoroughly covering the docs and perhaps integration tests if they exist, and your vision of the entire software project should become a lot more clear. 