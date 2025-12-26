> [!NOTE]
> This project has been created as part of the [__42 Warsaw__](https://42warsaw.pl/pl/) curriculum by [_okruhlia_](https://www.linkedin.com/in/oleksij-kruhlianytsia-1844a8286?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BUAE5tKFeTtCh4licBCi%2BjA%3D%3D).

> [!WARNING]
> *The accuracy of the information or implementation may not correspond to reality.*
> ___USE AT YOUR OWN RISK!___

# Garden Guardian
## Data Engineering for Smart Agriculture

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

>Build resilient data pipelines for your smart garden! Learn to handle sensor
failures, process agricultural data streams, and create robust monitoring systems that
keep your digital greenhouse thriving.
---
## Table of Contents
1. [Description](#description)
2. [Project Structure](#project-structure)
3. [Instructions](#instructions)
4. [Resources & AI](#resources--ai)
---
## Description
**Goal:**
The project aims to master Python's Exception Handling mechanisms.
Moving beyond simple logic, we focus on creating resilient code that can handle invalid inputs,
missing files, and logical paradoxes without crashing. The module covers standard exceptions,
resource cleanup, and the creation of custom error hierarchies.

**Overview:**
The module consists of several progressive exercises:
* **Level 0-1:** Catching standard errors (`ValueError`, `KeyError`, etc.) and validating inputs using `raise`.
* **Level 2-3:** Ensuring system integrity with `finally` blocks (cleanup) and combined logic checks.
* **Level 4-5:** Creating Custom Exceptions (`GardenError`), inheritance, and complex management systems (`GardenManager`).
---
## Project Structure
```text
CodeCultivation_Exceptions/
├── ex00/
│   └── ft_first_exception.py     # Catching multiple standard Python errors
├── ex01/
│   └── ft_different_errors.py    # Input validation logic using 'raise' & 'else'
├── ex02/
│   └── ft_custom_errors.py       # Guaranteed cleanup/resource management
├── ex03/
│   └── ft_finally_block.py       # Custom Exception Classes & Inheritance
├── ex04/
│   └── ft_raise_errors.py        # Combining Type checks and Logic checks
└── ex05/
    └── ft_garden_management.py   # Final Boss: Class integration with full error handling
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
1. **Concept Clarification:** Understanding the difference between raise, try/except.
2. **Code Structure:** Learning how to inherit from the base Exception class to create GardenError.
3. **Documentation:** Assistance in generating docstrings according to Google Style Guide to ensure code readability
and maintainability.