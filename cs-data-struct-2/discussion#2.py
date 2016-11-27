"""

Part 1: Discussion Questions

*********
Recursion
*********

1. In your own words, what is recursion?

    Recursion is to repeat a recursive procedure by definition. It happens when
    a function calls itself. Recursive function will keep going until it reaches
    a break point (the base case) or it shall repeats forever.


2. Why is it necessary to have a base case?

    The whole point of having a base case is to prevent endless recursion happens.
    A base case is setting up some conditions for breaking out the recursive procedure.

*********
Graphs
*********


1. What is a graph?

    A graph is a type of data structure that is similar to a tree, but it contains
    more flexible strucuture than trees in terms of the relationship between nodes.
    Graphs can be directed or non-directed. A graph is composed of nodes and edges
    and there is a cycle among some nodes.

2. How is a graph different from a tree?

    A tree cannot have loops but a graph can. A graph can have mutilple parents
    to one child whereas a tree can only have one parent for many children. Also
    the data flow of a tree can only go from paren to children (arrows pointing down)
    and they cannot go back up. On the other hand, a graph can have a flow going back
    and forth between "parent" and "children" nodes.

3. Give an example of something that would be good to model with a graph.

    LinkedIn is a good model of a graph implementation. The connection between different
    people is the edges of the graph and each individual is a node inside the graph. The
    relationship can be directed or non-directed because someone can change the state of this
    by simply connect with the other person.


"""
