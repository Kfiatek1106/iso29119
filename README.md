# ISO 29119 - Software and systems engineering - Software testing
Itg is a set of documents that define an internationally agreed set of standards for software testing that can be used by any organization when performing any form of software testing [source] 

The standard with its latest and historical versions is available on the IEEE website.

The standard contains the following parts:

ISO 29119-1: Software and systems engineering - Software testing - Part 1: Concepts and definitions
ISO 29119-2: Software and systems engineering - Software testing - Part 2: Test processes
ISO 29119-3: Software and systems engineering - Software testing - Part 3: Test documentation
ISO 29119-3: Software and systems engineering - Software testing - Part 4: Test techniques
ISO 29119-3: Software and systems engineering - Software testing - Part 5: Keyword-Driven Testing
The ISO 29119-3 inspired the development of the ISO 29119 python package. Some of the aspects from the standard have been adapted to the package, and others have been created as a result of the need to make the package functional.


# Benefits of the ISO29119 module:
- data for analysis unified to one common format (an abstract class: Metadata)
- title, final result, status, and state as one set of common attributes of the unified data, preconditions, test conditions including their attributes, postconditions, individual test cases, and their collections (an abstract class: Item)
- data collections equipped with the passes, fails and attentions iterators to express the success or failure of the collection (an abstract class Items)
- clearly distinguish between the test aspects helping to organize the test documentation such as:
  - test cases
    - test case
    - precondition
    - test condition,
      - test attribute
    - postcondition
- ready-to-use function to print
  - tests status report
  - test case report


## Items inspired by the ISO 29119
### Test Case
A set of test case preconditions, inputs (including actions, where applicable), and expected results, developed to drive the execution of a test item to meet test objectives, including correct implementation, error identification, checking quality, and other valued information. Test case groups the following information:
- unique identifier
- title
- priority
- description
- final result
- status
- state
- requirement identifier
- set of preconditions
- set of test conditions
- set of post-conditions
### Precondition
A testable aspect has to be true before the test conditions
- execution
- title
- final result
- status
- state
- additional information
### Test Condition
A testable aspect of a structural element is identified as a basis for testing. It contains:
- title
- final result
- status
- state
- set of test attributes
- an expected element
- an actual element
- additional information
### Test Attribute
A testable aspect of a characteristic of the structural element (test condition).
- title
- final result
- status
- state
- an expected value
- an actual value
### Post condition
A testable aspect has to be true after execution of the test conditions. It contains:
- title
- final result
- status
- state
- additional information
### Priority
The importance of an item. It contains:
- High
- Medium
- Low
- None
### Final Result
The validation outcome of an item. It can take one of the following:
- Pass
- Fail
- '-' (no issue)
- Attention
- Warning
### Status
An item condition at the test execution time.
- execute
- omit
- executed
- omitted
- not executed '-'
### State
An item condition at the test validation time.
- present (exists)
- not present (does not exists)
- not applicable
- not available
- missing
- redundant'-'
### Test Cases
Collection of the individual Test Cases. It contains:
- title
- final result
- status
- state
- total of passed Test Cases
- total of failed Test Cases
- total of Test Cases that need attention
### Preconditions
Collection of the individual Preconditions. It contains:
- title
- final result
- status
- state
- total of passed Preconditions
- total of failed Preconditions
- total of Preconditions that need attention
### Post Conditions
Collection of the individual Post Conditions. It contains: 
- title
- final result
- status
- state
- total of passed Post Conditions
- total of failed Post Conditions
- total of Post Conditions that need attention
### Test Conditions
Collection of the individual Test Conditions. It contains:
- title
- final result
- status
- state
- total of passed Test Conditions
- total of failed Test Conditions
- total of Test Conditions that need attention
### Test Attributes
Collection of the individual Test Attributes. It contains:
- title
- final result
- status
- state
- total of passed Test Attributes
- total of failed Test Attributes
- total of Test Attributes that need attention


## Items increase functionality
### Item
An abstract description of common characteristics of all elements of the items inspired by ISO 29119 and not inspired by the ISO. It stores:
- final result
- status
- state
- title
### Items
An abstract description of common characteristics of all collections of the inspired by ISO 29119. It stores:
- collection of items
### Condition
An abstract description of common characteristics of conditions of the inspired by ISO 29119. It stores:
- type of the condition
- additional information
### Condition Type
Sort of the condition. Its elements are:
- precondition
- post condition
- test condition
- attribute'-'
- metadata
### Metadata
An abstract description of information that is given to describe the structural elements or its attributes. 
### Metadata Collection
An abstract description of the collection of individual metadata.

## UML Class Diagram

![ISO 29119 - Class Diagram](/iso29119/docs/class_diagram.png)
