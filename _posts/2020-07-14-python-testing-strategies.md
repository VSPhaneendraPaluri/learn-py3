---
layout: post
title: Python Testing Strategies
date: 2020-07-14 17:48 +0530
---

## Testing Strategies

Hi folks,
The posts tha at you have seen it so far, already start dealing with few of the various available testing framworks in Python.  The objective of this post is to understand better ways to test our code using some in-built features built into unittest framwork (Python > 3.3).

### Unit Testing in Python
When it comes to unit testing, I'm a lot amazed with the configuration and easyness that one could start writing unittests for the Object Under Test (OUT).  This is an attempt from me showcasing the various possibilities available as part of the unittest framework in Python.

### Mocking in Python
This, in my mind, one the most versatile, easy to use features in Python for testing your Object Under Test (OUT) in an isolated way, removing out all the external/internal dependencies.  The following slide-deck should present the basic principles of testing in Python along with principles of mocking, patching, spec'ing and auto-spec'ing.

Here are the links:
- Link to the slide-deck is [here]({{ site.repository-path }}{{ site.baseurl }}/blob/{{ site.branch }}/slide-deck/Python-Testing-Strategies.pptx?raw=true)
- Link to few hands-on session is available [here]({{ site.repository-path }}{{ site.baseurl }}/tree/{{ site.branch }}/hands-on/mocking).

Enjoy Mock'ing !

Just that don't end up mocking the mocks :)
