> [!NOTE]
> This project has been created as part of the [__42 Warsaw__](https://42warsaw.pl/pl/) curriculum by [_okruhlia_](https://www.linkedin.com/in/oleksij-kruhlianytsia-1844a8286?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BUAE5tKFeTtCh4licBCi%2BjA%3D%3D).

> [!WARNING]
> *The accuracy of the information or implementation may not correspond to reality.*
> ___USE AT YOUR OWN RISK!___

# Data Quest
## Mastering Python Collections for Data Engineering

**Filmed on location at:**

![42 Warsaw](https://img.shields.io/badge/-Warsaw-blue?style=for-the-badge&logo=42&logoColor=black&labelColor=white)

**Starring:**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![PyCharm on Mac](https://img.shields.io/badge/-PyCharm-blue?style=for-the-badge&logo=apple&logoColor=white&labelColor=gray)

**Powered by:**

![Bucket of Coffee](https://img.shields.io/badge/Bucket_of-Coffee-6F4E37?style=for-the-badge&logo=coffeescript&logoColor=white)
![&](https://img.shields.io/badge/-%26-gray?style=for-the-badge)
![Prayers to Machine Spirit](https://img.shields.io/badge/Prayers_to-Machine_Spirit-8B0000?style=for-the-badge&logo=warhammer&logoColor=white)

**QA Department:**

![Works on My Machine](https://img.shields.io/badge/Works_on-My_Machine-success?style=for-the-badge)

>Journey through the digital realm as a data engineer! Master Python’s
powerful data structures while building game analytics systems, processing player
statistics, and creating streaming data pipelines in the Pixel Dimension.
---
## Table of Contents
1. [Description](#description)
2. [Project Structure](#project-structure)
3. [Instructions](#instructions)
4. [Resources & AI](#resources--ai)
---
## Description
**Goal:**
The project focuses on mastering Python's core Data Structures and efficient data processing patterns.
We move away from basic loops to more "Pythonic" approaches, implementing systems typical for Game Development backend:
inventory management, achievement tracking, and real-time event processing.

**Overview:**
The module covers progressive levels of data handling:
* **Basic Structures:** Using `sys.argv` for inputs, `lists` for scores, and `tuples` for immutable 3D coordinates.
* **Collections:** implementing `sets` for unique achievement tracking and `dictionaries` for complex inventory systems.
* **Advanced Processing:**
    * **Generators (`yield`):** Creating memory-efficient data streams that process events one by one (Lazy Evaluation).
    * **Comprehensions:** Using List/Dict/Set comprehensions for elegant and fast data filtering and transformation.
---
## Project Structure
```text
Structures/
├── ex00/
│   └── ft_command_quest.py       # CLI arguments & basic input handling
├── ex01/
│   └── ft_score_analytics.py     # List processing & error handling (try/except)
├── ex02/
│   └── ft_coordinate_system.py   # Tuples & 3D Math (Euclidean distance)
├── ex03/
│   └── ft_achievement_tracker.py # Sets logic (Union, Intersection, Difference)
├── ex04/
│   └── ft_inventory_system.py    # Nested Dictionaries & Inventory logic
├── ex05/
│   └── ft_data_stream.py         # Generators & Yield (Memory efficiency)
└── ex06/
    └── ft_analytics_dashboard.py # Final Boss: List/Dict/Set Comprehensions
```
---
## Instructions
### Installation
1. Clone the repository:
2. Navigate to the specific exercise folder to run individual simulations.
> [!NOTE]
> Ensure you have Python 3.10 installed.

## Resources & AI
### Resources
1. [Google](https://www.google.com/)
2. [Python 3 Documentation](https://docs.python.org/3/)
3. [CS50](https://www.youtube.com/@cs50)
4. [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
5. [JetBrains PyCharm IDE](https://www.jetbrains.com)

### AI usage
1. **Concept Clarification:** Understanding the difference between return and yield for memory management.
2. **Syntax Help:** Learning the syntax for Dictionary Comprehensions vs Set Comprehensions.
3. **Refactoring:** Optimizing loop-based logic into declarative comprehensions.
4. **Logic Verification:** Checking set operations (union vs intersection) for achievement tracking logic.