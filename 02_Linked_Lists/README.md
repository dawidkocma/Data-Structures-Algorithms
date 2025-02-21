# Singly Linked List Implementation in Python

## 📌 Overview
This repository contains an implementation of a **Singly Linked List** in Python. The implementation covers various essential operations such as insertion, deletion, searching, and reversal of the linked list.

## 🚀 Features
- Append (O(1))
- Prepend (O(1))
- Pop Last (O(n))
- Pop First (O(1))
- Get Element by Index (O(n))
- Set Value by Index (O(n))
- Insert at Index (O(n))
- Remove by Index (O(n))
- Reverse (O(n))

## 📂 Repository Structure
```
📦 LinkedList
├── 📜 linked_list.py  # Implementation of Linked List
├── 📜 README.md       # Documentation
```

## 🛠 Implementation
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
```

## ⚡ Getting Started
### Prerequisites
Ensure you have Python installed:
```sh
python --version
```

### Clone the Repository
```sh
git clone https://github.com/dawidkocma/DSA/02_Linked_Lists.git
cd LinkedList
```

### Running the Code
You can run and test the linked list implementation:
```sh
python linked_list.py
```

## 📜 License
This project is open-source and available under the MIT License.

## 📬 Contact
For any questions or suggestions, feel free to reach out:
- GitHub: [dawidkocma](https://github.com/dawidkocma)
