# GitHub Activity Generator

## Gitter build: Adds commits on the dates you choose in an existing file

A script that helps you instantly generate a beautiful GitHub Contributions Graph for the last year.

⚠ **Disclaimer**  
This script is for educational purposes and demonstrating GitHub mechanics. It should not be used to misrepresent professional contributions or coding activity.

---

## How to Use

### Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
- **Git**: Ensure you have Git installed on your system. You can download it from [git-scm.com](https://git-scm.com/).

### Steps

1. **Add `git.py` in an Initialized Git Repo**  
   Place the `git.py` script in an existing Git repository.

2. **Add the File to the Same Directory**  
   Ensure the file you want to add commits to is in the same directory as the script.

3. **Run and Follow the Prompts**  
   Execute the script and follow the on-screen prompts to specify the dates, times, and commit messages.
   ```bash
   python git.py
   ```

4. **Push Changes to GitHub**  
   After running the script, you need to push the changes to your GitHub repository.
Example: To push your changes to the `main` branch:
   ```bash
   git push origin main
   ```

---

## System Requirements

To be able to execute the script, you need to have Python and Git installed.

---

## Troubleshooting

### I performed the script, but my GitHub activity is still the same.

- It might take several minutes for GitHub to reindex your activity. Check if the repository has new commits and wait a couple of minutes.

### The changes are still not reflected after some time.

- Are you using a private repository? If so, enable showing private contributions following this guide: [GitHub Help - Viewing contributions](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/viewing-contributions).

### Still no luck

- Make sure the email address you have in GitHub is the same as you have in your local settings. GitHub counts contributions only when they are made using the corresponding email.

  Check your local email settings with:
  ```bash
  git config --get user.email
  ```

  If it doesn't match with the one from GitHub, reset it with:
  ```bash
  git config --global user.email "user@example.com"
  ```

- Create a new repository and rerun the script.

### There are errors in the logs of the script.

- Maybe you tried to use an existing repository. If so, make sure you are using a new one which is not initialized.

- If none of the options helped, open an issue and I will fix it as soon as possible.

---

## Additional Information

### Script Functionality

- **Commit on Specific Day**: Generate commits on a specific day with a specified number of commits.
- **Commit on Range of Dates**: Generate commits over a range of dates with a specified maximum number of commits per day.
- **Randomize Commit Times**: Randomize commit times within a specified start and end time interval for each day.
- **Custom Commit Messages**: Use one commit message for all commits or different commit messages for each day.

### Example Usage

1. **Specific Day**:
   ```bash
   python git.py
   ```
   - Enter the path to the file.
   - Choose option `1` for a specific day.
   - Enter the date and time.
   - Enter the number of commits to make on that day.
   - Enter the commit message.

2. **Range of Dates**:
   ```bash
   python git.py
   ```
   - Enter the path to the file.
   - Choose option `2` for a range of dates.
   - Enter the start and end dates.
   - Enter the start and end times for commits.
   - Enter the maximum number of commits per day.
   - Enter the commit message(s).

### After the Script Has Run

- **Push Changes to GitHub**:
  After running the script, you need to push the changes to your GitHub repository. Make sure you are on the `main` branch and then push the changes:
  ```bash
  git push origin main
  ```

### Important Notes

- **Initialized Repository**: This script only works on an initialized Git repository. Make sure your repository is initialized before running the script.
- **Historical Commits**: You can go back as far as you want in history to add commits.
- **Commit Customization**: You can add commits to a specific day, choose commit messages, use one message for all commits, or randomize multiple messages.

Sure! Here’s an additional line you can add to the README to encourage contributions:

---

## Contributing

 Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

---