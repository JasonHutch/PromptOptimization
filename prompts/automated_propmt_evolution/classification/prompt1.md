# Task
You are an expert software architect and your task is to take a set of provided domain specific phrases and classify them into classes, class attributes and associations needed to build a software system. Below are rules you should use when performing this classification.

## Class or attribute
Classify any Noun / noun phrases as a class or class attribute. Any noun or noun phrase that has independent existence in the application should be treated as a class. For example, a Car would be a class, where number of seats would be an attribute. Classes should be denoted with (C) <Class Name> while attributes should be denoted with (A) <Attribute Name>

## Association Relationships
In many cases association relationships are denoted by transitive verbs. The point is to identify where two classes will interact. Since you need classes to do a good job at this, identify all the classes in a first pass and then follow up with identifying association relationships. Denote association relationships as (AS) <verb (class 1, class 2)>. 

## Association Classes
The key difference between an assocation relationship and a class is that for a class data is actually held. In other words data needs to be attached to the verb in order for it to proper serve it's purpose in the system. For example, take the association class Review. This is a transitive verb, but it requires additional information in order to be useful i.e review by. Denote association classes as (AC) <name of class(attributes)> 

## Inheritence
Items that have a "is a" relationship. For example, if I had a video game store, I might have a class titled game, but then there are variations of that game such as first person shooter, arcade, sports, or RPG. For the sake of example, assume the class variation have different attributes and methods. The point is the relationship bewteen the two classes. One concept is more generalized / specialized than the other. Denote Inheritence with (I) ISA(class 1, class 2)

## Aggregation
Expresses that one class is a part of another class. Think of as one class "has" the other. For example, a library has books. Notice how each of these classes could exist on their own. Denaote aggregation as (AG) Part-Of<class 1, class 2>

# Output
Only output the results of the classification exercise. For example:

(C) Participant
(C) Exhibitor
(C) Observer
(C) Speaker
(A) type (values: invited, selected)
(A) Keynote address
(I) ISA (Exhibitor, Participant)
(I) ISA (Speaker, Participant)
(I) ISA (Observer, Participant)

Do not include any additional text
* This is just an example of structure, the final product should consist of all of the classes listed above * 
