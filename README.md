# LogicMonitor API Client

The LogicMonitor API Client is a Python application that interacts with the LogicMonitor REST API to retrieve and manage alert rules and related data.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Description

The LogicMonitor API Client is a tool designed to work with the LogicMonitor platform, allowing users to:

- Fetch alert rules by ID
- Fetch a paginated list of all alert rules
- Save retrieved data to JSON files for analysis or backup

## Installation

To use the LogicMonitor API Client, follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/haianhltr/logicmonitor-api-client.git
   ```

2. Install the required Python packages using pip:

   ```
   cd logicmonitor-api-client
   pip install logicmonitor-sdk
   ```
   
## Usage
To use the LogicMonitor API Client, you need to modify a configuration file named config.py in the root directory of the project. Define your LogicMonitor account details in this file:
   ```
    # config.py
    class AppConfig:
        def __init__(self, company, access_id, access_key):
            self.company = company
            self.access_id = access_id
            self.access_key = access_key
    
    app_config = AppConfig(
        company="your_company",
        access_id="your_access_id",
        access_key="your_access_key"
    )
   ```
    
After configuring your account details, you can navigate to api/ and run your desired API calls.

## Configuration
The config.py file contains your LogicMonitor account configuration, including your company name, access ID, and access key. Ensure that this file is securely stored and protected.


## Contributing
We welcome contributions to this project. If you'd like to contribute, please follow these guidelines:

Fork the repository.
1. Create a feature branch: git checkout -b feature-name.
2. Commit your changes: git commit -m 'Add new feature'.
3. Push to the branch: git push origin feature-name.
4. Create a pull request.

Please make sure to follow the Code of Conduct and adhere to best practices when contributing.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Note: This project is not officially affiliated with LogicMonitor, Inc.

