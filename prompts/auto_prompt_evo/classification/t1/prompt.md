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
Output **one markdown table** with exactly these columns and nothing else after it.

| label | element | arg1 | arg2 |
|---|---|---|---|

Use one row per element. Leave a cell empty when it does not apply.

## Labels

| label | meaning | element | arg1 | arg2 |
|---|---|---|---|---|
| `C` | class | class name | | |
| `A` | attribute | attribute name | owning class | |
| `V` | attribute value | the literal value | owning attribute | |
| `AS` | association | association / verb name | participating class | participating class |
| `AC` | association class | class name | participating class | participating class |
| `AG` | aggregation | `Part-of` | part | whole |
| `I` | inheritance | `ISA` | child class | parent class |

## Rules

- One row per element. Do not merge several elements into one row.
- `element` is a noun phrase for `C`/`A`/`AC`, a verb phrase for `AS`.
- For `AG` and `I` the `element` cell is always the literal `Part-of` or `ISA`.
- Do not invent elements that are not supported by the text.
- No prose, no explanation, no code fences around the table.

## Example

| label | element | arg1 | arg2 |
|---|---|---|---|
| C | Customer | | |
| C | Invoice | | |
| A | name | Customer | |
| A | status | Invoice | |
| V | paid | status | |
| AS | pay | Customer | Invoice |
| AC | Payment | Customer | Invoice |
| AG | Part-of | Line Item | Invoice |
| I | ISA | Corporate Customer | Customer |
