# internet-speed-tests
## Description
A Python script that uses the speedtest-cli library to conduct internet speed tests at regular intervals for a specified duration. The frequency of the tests and duration are specified by the user. The download and upload speed test results are written to a CSV file in the working directory which can be used for reference and further analysis. After all the tests are run, the statistics: minimum, maximum, and average speeds are printed to the console.

## Packages required
Please install the following packages before running the script:
* speedtest-cli

## Use cases
The script can be used to check the internet speeds of your network for long periods of time. It can help to understand the speed fluctuations of your network and get realistic estimates of your download and upload speeds.

*Note: The speedtest-cli library is not always accurate, and the results can vary depending on various factors such as server location, network congestion, etc. Therefore, the results obtained using this script should be taken as approximate values only.*
