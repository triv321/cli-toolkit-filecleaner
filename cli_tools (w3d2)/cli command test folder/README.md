
-----

````markdown
# Segment 1: Command-Line Navigation and Filesystem Operations

## Overview

This repository contains the output of my practice for linux scripting. The objective of this segment was to build foundational muscle memory and fluency with the Linux command line, focusing on filesystem navigation and essential file/directory management commands.

## Core Commands Mastered

The following commands were practiced and mastered during this segment.

### `pwd` (Print Working Directory)
- **Description:** Displays the full path of the current working directory.
- **Usage:**
  ```bash
  pwd
````

### `ls` (List)

  - **Description:** Lists the contents (files and directories) of the current directory.
  - **Usage:**
    ```bash
    # List contents
    ls

    # List all contents (including hidden files) in a detailed format
    ls -la
    ```

### `cd` (Change Directory)

  - **Description:** Navigates from the current directory into a different one.
  - **Usage:**
    ```bash
    # Navigate into a sub-folder
    cd my_project_folder

    # Navigate up to the parent directory
    cd ..
    ```

### `mkdir` (Make Directory)

  - **Description:** Creates a new, empty directory.
  - **Usage:**
    ```bash
    mkdir new_directory
    ```

### `touch` (Create Empty File)

  - **Description:** Creates a new, blank file.
  - **Usage:**
    ```bash
    touch new_file.txt
    ```

### `cp` (Copy)

  - **Description:** Copies a file or directory from a source to a destination.
  - **Usage:**
    ```bash
    # Copy a file in the same directory
    cp source_file.txt destination_file.txt

    # Copy a file into another directory
    cp source_file.txt ./another_directory/
    ```

### `mv` (Move / Rename)

  - **Description:** Moves a file or directory. This command is also used to rename files and directories.
  - **Usage:**
    ```bash
    # Move a file to a new directory
    mv my_file.txt ./new_location/

    # Rename a file
    mv old_filename.txt new_filename.txt
    ```

### `rm` (Remove)

  - **Description:** Deletes a file or directory.
  - **Usage:**
    ```bash
    # Delete a file
    rm file_to_delete.txt

    # Delete an empty directory
    rmdir empty_directory

    # Delete a directory and all its contents (use with caution)
    rm -r directory_to_delete
    ```

## Key Concepts

  - **Tab Completion:** Using the `Tab` key to auto-complete commands, filenames, and directory paths is essential for speed and accuracy.
  - **Absolute vs. Relative Paths:** Understood the difference between a full path starting from the root (`/`) and a relative path starting from the current directory (`.` or `..`).
  - **Special Directories:** Learned the meaning and usage of `.` (current directory), `..` (parent directory), and `~` (home directory) as critical navigation shortcuts.

## Commands Practice Log

1.  Navigating to my home directory (`cd ~`).
2.  Creating a folder (`mkdir folder`).
3.  Navigating into the folder (`cd folder`).
4.  Creating a structure of files and sub-directories using `touch` and `mkdir`.
5.  Practicing `cp` and `mv` to copy and reorganize the files and directories.
6.  Navigating up and down the directory tree using `cd ..` and `cd subfolder`.
7.  Cleaning up the environment using `rm` and `rm -r` to complete the practice session.

<!-- end list -->

```
```