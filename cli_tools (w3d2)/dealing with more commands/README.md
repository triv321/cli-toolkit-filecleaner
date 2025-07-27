
-----

````markdown
# Project 1.2: Command-Line Log File Analyzer

## Project Overview

This project is a command-line tool, written as a simple Bash script, designed to quickly parse and extract meaningful insights from raw web server access logs.

## The Core Tools Used

This script is built on the Unix philosophy of combining small, single-purpose tools to accomplish a complex task. The primary tools used are:

* **`grep` (The Searchlight):** `grep` scans the file for lines that match a specific pattern. It acts as our first filter, allowing us to narrow down millions of log entries to only the ones that are relevant to our query (e.g., only lines containing an error).

* **`awk` (The Column Extractor):** Once we have the relevant rows, `awk` carves up each line into distinct columns based on spaces. This allows us to isolate specific pieces of information, like an IP address or a URL, from the rest of the line's noise.

* **`sort` (The Organizer):** A simple but powerful utility to sort lines of text alphabetically or numerically. This is a critical preparatory step for counting unique entries.

* **`uniq` (The Counter):** After sorting, `uniq` can easily identify and count adjacent, duplicate lines. This is the core of our "Top 10" analysis.

* **`|` (The Pipe):** The pipe is the conveyor belt of our data factory. It connects each tool, sending the processed output of one command directly as the input to the next, creating a seamless and efficient pipeline.

## My Solution: The Command Pipeline

The core of the `log_analyzer.sh` script is a single, elegant command pipeline that processes the data in stages.

```bash
# Inside log_analyzer.sh

cat sample_log.log | grep " 404 " | awk '{print $1}' | sort | uniq -c | sort -nr | head -n 10
````

Here is a step-by-step breakdown of how this pipeline works:

1.  **`cat sample_log.log`**: First, we read the entire contents of the log file.
2.  **`| grep " 404 "`**: The output is piped to `grep`, which filters the stream, keeping only the lines that contain the " 404 " status code.
3.  **`| awk '{print $1}'`**: The remaining lines (only the error lines) are piped to `awk`, which extracts only the first column—the IP address—from each line.
4.  **`| sort`**: The list of IP addresses is then sorted alphabetically. This places all identical IPs next to each other, which is required for `uniq` to work correctly.
5.  **`| uniq -c`**: The sorted list is piped to `uniq -c`, which counts the occurrences of each unique IP address and prepends the count to the line.
6.  **`| sort -nr`**: The output of counts and IPs is piped to `sort -nr` for a final sorting. `-n` sorts numerically, and `-r` sorts in reverse (descending) order, placing the highest counts at the top.
7.  **`| head -n 10`**: Finally, the fully sorted list is piped to `head -n 10`, which gives us only the top 10 lines of the output.

## How to Use This Script

1.  Ensure the script `log_analyzer.sh` and the data file `sample_log.log` are in the same directory.
2.  Give the script execute permissions from the terminal:
    ```bash
    chmod +x log_analyzer.sh
    ```
3.  Run the script:
    ```bash
    ./log_analyzer.sh
    ```

## Key Takeaways

This project was a practical lesson in the power of the command line for data processing. The key takeaways were:

  * **The Unix Philosophy:** Small, single-purpose tools can be chained together to create incredibly powerful and efficient solutions.
  * **Data Streams:** A deeper understanding of how data flows through `stdin` and `stdout` and how the pipe (`|`) operator redirects these streams.
  * **Declarative Processing:** The pipeline is a declaration of what to do with the data, step-by-step, which can often be clearer and more concise than writing an equivalent script in a language like Python.

<!-- end list -->

```
```