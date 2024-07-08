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


# Items inspired by the ISO 29119
## Test Case
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
# Precondition
A testable aspect has to be true before the test conditions
- execution
- title
- final result
- status
- state
- additional information
# Test Condition
A testable aspect of a structural element is identified as a basis for testing. It contains:
- title
- final result
- status
- state
- set of test attributes
- an expected element
- an actual element
- additional information
# Test Attribute
A testable aspect of a characteristic of the structural element (test condition).
- title
- final result
- status
- state
- an expected value
- an actual value
# Post condition
A testable aspect has to be true after execution of the test conditions. It contains:
- title
- final result
- status
- state
- additional information
# Priority
The importance of an item. It contains:
- High
- Medium
- Low
- None
# Final Result
The validation outcome of an item. It can take one of the following:
- Pass
- Fail
- '-' (no issue)
- Attention
- Warning
# Status
An item condition at the test execution time.
- execute
- omit
- executed
- omitted
- not executed '-'
# State
An item condition at the test validation time.
- present (exists)
- not present (does not exists)
- not applicable
- not available
- missing
- redundant'-'
# Test Cases
Collection of the individual Test Cases. It contains:
- title
- final result
- status
- state
- total of passed
 Test Casestotal of failed Test Casestotal of Test Cases that need attentionPreconditionsCollection of the individual Preconditions.It contains:titlefinal resultstatusstatetotal of passed Preconditionstotal of failed Preconditionstotal of Preconditions that need attentionPost ConditionsCollection of the individual Post Conditions. It contains:titlefinal resultstatusstatetotal of passed Post Conditionstotal of failed Post Conditionstotal of Post Conditions that need attentionTest ConditionsCollection of the individual Test Conditions.It contains:titlefinal resultstatusstatetotal of passed Test Conditionstotal of failed Test Conditionstotal of Test Conditions that need attentionTest AttributesCollection of the individual Test Attributes.It contains:titlefinal resultstatusstatetotal of passed Test Attributestotal of failed Test Attributestotal of Test Attributes that need attention


Items increase functionalityItemAn abstract description of common characteristics of all elements of the items inspired by ISO 29119 and not inspired by the ISO.It stores:final resultstatusstatetitleItemsAn abstract description of common characteristics of all collections of the inspired by ISO 29119.It stores:collection of itemsConditionAn abstract description of common characteristics of conditions of the inspired by ISO 29119.It stores:type of the conditionadditional informationCondition TypeSort of the condition. Its elements are:preconditionpost conditiontest conditionattribute'-'metadataMetadataAn abstract description of information that is given to describe the structural elements or its attributes.Metadata CollectionAn abstract description of the collection of individual metadata.
















![ISO 29119 - Class Diagram](/iso29119/docs/class_diagram.png)
