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


![ISO 29119 - Class Diagram](/iso29119/docs/class_diagram.png)
