import subprocess


def deploy_if_better():

    print("\nStarting automated deployment...")

    try:

        subprocess.run(["git", "add", "."], check=True)

        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"]
        )

        if result.returncode == 0:
            print("No changes detected.")
            return

        subprocess.run(
            ["git", "commit", "-m", "Auto retrained model"],
            check=True
        )

        subprocess.run(
            ["git", "push", "origin", "main"],
            check=True
        )

        print("\nGitHub updated successfully.")
        print("GitHub Actions pipeline has been triggered.")

    except subprocess.CalledProcessError as e:

        print(f"\nDeployment failed: {e}")