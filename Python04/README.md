> [!NOTE]
> This project has been created as part of the [__42 Warsaw__](https://42warsaw.pl/pl/) curriculum by [_okruhlia_](https://www.linkedin.com/in/oleksij-kruhlianytsia-1844a8286?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BUAE5tKFeTtCh4licBCi%2BjA%3D%3D).

> [!WARNING]
> *The accuracy of the information or implementation may not correspond to reality.*
> ___USE AT YOUR OWN RISK!___

# Cyber Archives
## Mastering Python File I/O & Stream Management

**Fabricated within the Data-Forges of:**

![Forge World Warsaw](https://img.shields.io/badge/Sector-42_Warsaw-b71c1c?style=for-the-badge&logo=42&logoColor=white)

**Sacred Tech-Stack (Lingua Technis):**

![Python](https://img.shields.io/badge/Lingua_Technis-Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyCharm](https://img.shields.io/badge/Cogitator_Interface-PyCharm-000000?style=for-the-badge&logo=jetbrains&logoColor=white)

**Sustained by:**

![Recaf](https://img.shields.io/badge/Coffee_Stimulants-High_Grade-6F4E37?style=for-the-badge&logo=coffeescript&logoColor=white)
![&](https://img.shields.io/badge/-%26-gray?style=for-the-badge)
![Machine Spirit](https://img.shields.io/badge/Praise_the-Omnissiah-8B0000?style=for-the-badge&logo=warhammer&logoColor=white)

**Verification Rites:**

![Machine Spirit](https://img.shields.io/badge/Machine_Spirit-Appeased-success?style=for-the-badge&logo=robot-framework&logoColor=white)
> *"From the weakness of the mind, Omnissiah save us."*

>Step into the role of a Cyber Archivist! Your mission: recover ancient data fragments, manage
sacred communication channels, and secure the vault against digital entropy using Python's 
powerful I/O capabilities.
---
## Table of Contents
1. [Description](#description)
2. [Project Structure](#project-structure)
3. [Instructions](#instructions)
4. [Resources & AI](#resources--ai)
---
## Description
**Goal:**
This module focuses on mastering File Input/Output (I/O) operations, stream management, and secure resource handling in Python.
We transition from basic console interactions to professional-grade data persistence and error management patterns.

**Overview:**
The journey progresses through the layers of the Cyber Archives:
* **Basic I/O:** Reading and writing files using `open()`, `read()`, and `close()` to recover ancient text fragments.
* **Stream Management:** Direct manipulation of `sys.stdin`, `sys.stdout`, and `sys.stderr` to separate standard data from critical alerts.
* **Resource Safety:** Implementing the **Context Manager** protocol (`with` statement) to ensure fail-safe file handling and automatic cleanup.
* **Crisis Management:** Building robust error handling systems using `try-except` blocks to survive missing files, permission denials, and unexpected system anomalies.
---
## Project Structure
```text
File_IO/
├── data-generator-tools/
│   ├── data_generator.py         # Utility to generate test artifacts
│   └── ...                       # Generated files (ancient_fragment.txt, etc.)
├── ex00/
│   └── ft_ancient_text.py        # Basic File Reading (open/read/close)
├── ex01/
│   └── ft_stream_management.py   # Standard Streams (stdout vs stderr)
├── ex02/
│   └── ft_vault_security.py      # Context Managers ('with' statement) & Writing
└── ex03/
    └── ft_crisis_response.p
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
1. **Concept Clarification:** Understanding the difference between sys.stdout buffering and unbuffered stderr.
2. **Syntax Help:** Correct usage of the with statement for automatic resource closing.
3. **Debugging:** Troubleshooting PermissionError handling and Git file access issues.
4. **Best Practices:** Transitioning from C-style logic to **Pythonic** conventions (improving variable naming, ensuring readability, and structuring logical flow).